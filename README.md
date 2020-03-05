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

```
Evaluate on asr:
----------------------------------------------
PUNCTUATION      PRECISION RECALL    F-SCORE
,COMMA           83.22     83.39     83.30
.PERIOD          83.12     74.77     78.72
?QUESTIONMARK    75.67     76.26     75.96
----------------------------------------------
Overall          83.12     81.06     82.08
ERR: 2.3%
SER: 27.7%

```