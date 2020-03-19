from sklearn.metrics import classification_report, roc_curve, auc
from PIL import Image
from matplotlib.ticker import MaxNLocator

def report(y_num, y_pred, y_prob_pred):
    print('')
    print(classification_report(y_num, y_pred))

    fpr, tpr, thresholds = roc_curve(y_num, y_prob_pred)
    fig, ax1 = plt.subplots(1,1)
    ax1.plot(fpr, tpr, 'r-.', label = 'Simple model (%2.2f)' % auc(fpr, tpr))
    ax1.set_xlabel('False Positive Rate')
    ax1.set_ylabel('True Positive Rate')
    ax1.plot(fpr, fpr, 'b-', label = 'Random Guess')
    ax1.legend();

def my_load_img(f):
    img = Image.open(f)
    fp = img.fp
    img.load()
    fp.closed
    return img

def mi_montage2d(data):
    n = len(data)
    lado = int(np.ceil(np.sqrt(n)))
    alto1, ancho1 = data.shape[1:]
    aux = np.zeros((lado*alto1, lado*ancho1))
    for i,image in enumerate(data):
        row = i // lado
        col = i % lado
        aux[(row*alto1):((row+1)*alto1), (col*ancho1):((col+1)*ancho1)] = image
    return aux

def draw_borders(ax, ntiles, tile_width, tile_height, color='r'):
    
    aux1 = int(np.ceil(np.sqrt(ntiles)))
    
    npixels_y = tile_height*aux1
    for i in range(aux1-1):
        aux2 = (i+1)*tile_width - 0.5
        ax.plot([aux2, aux2], [0, npixels_y - 1], color, linewidth=3)
        
    npixels_x = tile_width*aux1
    for i in range(aux1-1):
        aux2 = (i+1)*tile_height - 0.5
        ax.plot([0, npixels_x - 1], [aux2, aux2], color)

def grafica_entrenamiento(tr_acc=[], val_acc=[], tr_loss=[], val_loss=[], best_epoch=0,
                          figsize=(10,4)):
    plt.figure(figsize=figsize)
    if len(val_acc)>0:
        ax = plt.subplot(1,2,1)
        plt.plot(1+np.arange(len(tr_acc)),  100*np.array(tr_acc))
        plt.plot(1+np.arange(len(val_acc)), 100*np.array(val_acc))
        plt.plot(1+best_epoch, 100*val_acc[best_epoch], 'or')
        plt.title('tasa de acierto del modelo (%)', fontsize=18)
        plt.ylabel('tasa de acierto (%)', fontsize=18)
        plt.xlabel('época', fontsize=18)
        plt.legend(['entrenamiento', 'validación'], loc='upper left')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax = plt.subplot(1,2,2)
    else:
        ax = plt.subplot(1,1,1)
    
    plt.plot(1+np.arange(len(tr_loss)), np.array(tr_loss))
    plt.plot(1+np.arange(len(val_loss)), np.array(val_loss))
    plt.plot(1+best_epoch, val_loss[best_epoch], 'or')
    plt.title('loss del modelo', fontsize=18)
    plt.ylabel('loss', fontsize=18)
    plt.xlabel('época', fontsize=18)
    plt.legend(['entrenamiento', 'validación'], loc='upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.show()

def save_result(score_tr, score_val, score_te, version_name):
    
    keys = ["Train loss", "Train accuracy", "Val loss", "Val accuracy", "Test loss", "Test accuracy"]
    values = [score_tr[0], score_tr[1], score_val[0], score_val[1], score_te[0], score_te[1]]
    
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
        
    f = open("saved_result/"+version_name+".txt","w")
    f.write( str(result_dict) )
    f.close()
