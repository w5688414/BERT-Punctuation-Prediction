# PunctuationPrediction-BERT
Use bert to predict punctuation on IWSLT2012 and The People's Daily 2014.

+ Data preprocessing can refer to this project: https://github.com/IsaacChanghau/neural_sequence_labeling

+ codes are forked from the project: https://github.com/MenNianShi/PunctuationPrediction-BERT

+ add some additional code to make sure the code can normally run

## requirements

- python3
- tensorflow-gpu 1.14


## data process
```
python process_raw.py
python dataprocess_peopledaily.py
```
## training

```
cd bert/
sh run_train.sh
```
## inference

```
cd bert/
sh run_predict.sh
```