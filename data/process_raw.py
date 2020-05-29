import re
from tqdm import tqdm
import codecs
file = '/Users/admin/Documents/pythonFiles/punctuation_restoration/2014/2014_corpus.txt'
from sklearn.model_selection import train_test_split
with open(file,'r',encoding='utf-8') as fp:
    lines = fp.readlines()
    processed_lines = []
    for line in tqdm(lines):

        line = re.sub(r'《','',line)
        line = re.sub(r'》', '', line)
        line = re.sub(r'“', '', line)
        line = re.sub(r'”', '', line)
        line = re.sub(r'——', '', line)
        line = re.sub(r'‘', '', line)
        line = re.sub(r'：', '', line)
        line = re.sub(r'’', '', line)
        line = re.sub(r'\[', '', line)
        line = re.sub(r']', '', line)
        line = re.sub(r'{', '', line)
        line = re.sub(r'}', '', line)
        line = re.sub(r'【', '', line)
        line = re.sub(r'】', '', line)
        line = re.sub(r'（', '', line)
        line = re.sub(r'）', '', line)
        line = re.sub(r'—', '', line)
        line = re.sub(r'…', '', line)
        line = re.sub(r'/[a-z]+\d* *[\[\]]?', "", line)
        line = ''.join(char+' ' for char in line)
        line = re.sub(r'、', " ,COMMA", line)
        line = re.sub(r'！', " .PERIOD ", line)
        line = re.sub(r'；', " ,COMMA ", line)
        line = re.sub(r'，', " ,COMMA ", line)
        line = re.sub(r'。', " .PERIOD ", line)
        line = re.sub(r'？', " ?QUESTIONMARK ", line)
        line = line.replace('\n', ' ')
        processed_lines.append(line)
    train_set ,dev_test_set = train_test_split(processed_lines,shuffle=True,test_size=0.2)
    print(len(dev_test_set))
    print(len(train_set))
    dev_set , test_set = train_test_split(dev_test_set,shuffle=True,test_size=0.5)
    print(len(dev_set))
    print(len(test_set))
def write_txt(filename, dataset):
    s = ''
    for line in  tqdm(dataset):
        s = s+line+ ' '
    with open(filename, mode="w+", encoding="utf-8") as f:
        f.write(s)
write_txt('./raw/LREC/2014_train.txt',train_set)
write_txt('./raw/LREC/2014_dev.txt',dev_set)
write_txt('./raw/LREC/2014_test.txt',test_set)
print('done')