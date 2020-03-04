# PunctuationPrediction-BERT
Use bert to predict punctuation on IWSLT2012 and The People's Daily 2014.

Data preprocessing can refer to this project: https://github.com/IsaacChanghau/neural_sequence_labeling
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
python cn_punctor.py
```
