# -*- coding: utf8 -*-
import nltk
import xlrd
import pandas as pd
from collections import Counter
import re

# 读取停用词表
def read_stopwords(path):
    f = open(path, 'r')
    data = [d.strip() for d in f.readlines()]
    return data

def read_excel(path):
    # 打开excel文件
    workbook = xlrd.open_workbook(path)
    # sheet文件列表
    sheet = workbook.sheets()
    # print sheet
    mysheet = sheet[0]
    # 获取行数
    nrows = mysheet.nrows
    for i in range(1, nrows):
        value = mysheet.cell_value(i, 1)
        yield value

# 去停用词
def remove_stopwords(seg_words, stop_words):    
    new_words = []
    for w in seg_words:
        w = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", w)
        if w in stop_words or w == '' or w == ' ':
            continue
        else:
            new_words.append(w)   
    return new_words

# 词频统计
def statistic_words(words):
    value = ''
    c = Counter(words)
    for w, num in c.most_common():
        value = value + w + '/' + str(num) + '#'
    return value

# 用nltk分词
def process():    
    result_dt = {'title':[], 'seg_word':[], 'remove_stopwords':[], 'statistic':[]}

    stop_words = read_stopwords('stop_words.txt')
    
    excel_path = 'data.xlsx'
    for value in read_excel(excel_path):
        value = value.lower()
        result_dt['title'].append(value)
        # print vaule
        
        seg_words = nltk.word_tokenize(value)
        seg_words_str = ' '.join(seg_words)
        result_dt['seg_word'].append(seg_words_str)
        # print seg_words_str
        
        remove_words = remove_stopwords(seg_words, stop_words)
        new_words_str = ' '.join(remove_words)
        result_dt['remove_stopwords'].append(new_words_str)
        # print new_words_str
        
        word_num_str = statistic_words(remove_words)
        result_dt['statistic'].append(word_num_str)
        # print word_num_str                

    result = pd.DataFrame(result_dt)
    result_path = 'seg_word.csv'
    result.to_csv(result_path, columns=['title', 'seg_word', 'remove_stopwords', 'statistic'])
        
if __name__ == '__main__':
    process()
