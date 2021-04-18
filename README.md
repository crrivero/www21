# Revisiting the Evaluation Protocol of Knowledge Graph Completion Methods for Link Prediction
Source code of our paper published in TheWebConf'21 (https://doi.org/10.1145/3442381.3449856).

## Pre-reqs
We have adapted many of the implementations provided by the OpenKE framework (https://github.com/thunlp/OpenKE/). The generation of negative triples is part of our CIKM'20 paper (https://github.com/crrivero/ImpactNegativeTriples).

You must install PyTorch, SciPy and the Ax platform (https://ax.dev/).

## Run
Call ax_async.py to generate all the experiments. These are files located in the Ax folder. Many of the experiments involve several rounds; subsequent calls to ax_async.py will keep advancing these experiments.

Call train.py to train the models. The generated models are located in the Model folder.

Call test.py to evaluate the models (validation or test). After validation, the output contains a number of model files that should be discarded; make sure to discard those before running the test.

## Datasets
Files 'new_train.txt', 'new_valid.txt' and 'new_test.txt' contain the new splits computed using Kolmogorov-Smirnov with alpha=.05.

## Trained models
The following folder (https://drive.google.com/drive/folders/1T_YUs9posPXv1KaMiPiF9h30072Eko9z) contain all the experiments reported in our paper.
