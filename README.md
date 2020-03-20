# Evaluation-of-Convolutional-Neural-Networks-models-for-pneumonia-diagnosis-master

1) Authors and collaborators
2) Abstract 
3) Requirements
4) Code structure


## 1) Authors and collaborators

Helena Liz López, Manuel Sanchez-Montañés Isla y David Camacho Fernandez

Collaborators: Ben-Gurion University (Israel) and Research Institute Hospital 12 de Octubre

## 2) Abstract

Pneumonia is a lung infection that causes 15% of childhood mortality of children under 5 years around the world. This disease could be mainly caused by bacterias and viruses. In the first case, patients need antibiotics urgently, while in the second case the patients only need supportive care. For this reason, an early diagnosis is very important, due if antibiotics are used in the case of a viral infection, it could generate antibiotic resistance in the population. X-rays imaging is one of the most used tests on pneumonia diagnosis and microorganism identification. In the last years, Artificial Intelligence and Medicine have undergone a great development, that has helped Decision Support Systems development. However, this system has the main limitation, the labeled samples available to generate the models.

A clear example is the field of Supervised Learning models for image recognition. For example, the diagnosis of pneumonia by radiography analysis, which is the objective of this work. Within the wide variety of existing algorithms to do this, convolutive neural networks (CNNs) are currently the best performers. There are considered as \textit{Black Box AI Algorithms}, that is, models where the model where the internal operations are not intuitively. For this reason, we need visualization techniques, called Explainable Artificial Intelligence, that generate an explainable output so that the medical staff can understand how the network has made the decision.

In this work, we have designed and fitted a convolutional neural network trying to maximize Area Under the Curve (AUC) and True Positive Rate (TPR), where the positive class corresponds to Consolidation cases. Finally, we generate heatmaps related to the analysis made by the model to understand how the network has made the decision.

## 3) Requirements

The software used to it was Ubuntu 18.04.2 LTS.
This project was run in Anaconda Navigator version 4.7.12, in the file requirements.txt, it includes all packages with each version and the command to install them:

conda create --name <env> --file <this file>

## 4) Code structure

.<br/>
├── general_models: different models used in the project <br/>
│   ├── model_90.ipynb <br/>
│   ├── model_102.ipynb <br/>
│   ├── model_108.ipynb <br/>
│   ├── model_121.ipynb <br/>
│   ├── model_124.ipynb	<br/>
│   ├── model_125.ipynb <br/>
│   └── model_pneumonia.ipynb <br/>
│ <br/>
├── kfold_models: models for cross-validation <br/>
│   ├── model_90_0.ipynb <br/>
│   ├── model_102_0.ipynb <br/>
│   ├── model_108_0.ipynb <br/>
│   ├── model_121_0.ipynb <br/>
│   ├── model_124_0.ipynb	 <br/>
│   ├── model_125_0.ipynb <br/>
│   └── model_pneumonia_0.ipynb <br/>
│ <br/>
├── create_kfold_datasets.ipynb: it generates different subsets from the original one. <br/>
│ <br/>
├── heatmap_byfold.ipynb: eXplainable AI technique to generate a heatmap for each class (Consolidation/ No <br/>
│   consolidation) for a model. <br/>
│ <br/>
├── heatmap_bymean_and_std.ipynb: eXplainable AI technique to generate a heatmap for each class (Consolidation/ <br/>
│   No consolidation) combining all models from k-fold cross-validation. <br/>
│ <br/>
├── statistical_test.ipynb: different statistical test to analyze the results of models <br/>
│ <br/>
└── source <br/>
│ <br/>
│   └── my_module.py <br/>

















