#!usr/bin/env python
# encoding: utf-8

import sys

from tqdm import tqdm

sys.path.append("..")
from paths import weibo_ner_path
import os

def deseg_weibo(weibopath):
    train_path = os.path.join(weibopath, 'weiboNER_2nd_conll.train')
    dev_path = os.path.join(weibopath, 'weiboNER_2nd_conll.dev')
    test_path = os.path.join(weibopath, 'weiboNER_2nd_conll.test')

    for data_file in [train_path, dev_path, test_path]:
        output_file = data_file + "_deseg"
        f_out = open(output_file, "w", encoding='utf8')
        with open(data_file, "r", encoding='utf8') as f:
            for line in f.readlines():
                line = line.strip()
                if line != "":
                    span_list = line.split('\t')
                    raw_char = ''.join(list(span_list[0])[:-1])
                    tag = span_list[-1]
                    f_out.write(' '.join([raw_char, tag]) + '\n')
                else:
                    f_out.write('\n')


def convert_format(data_file):
    output_file = data_file.split('.')[0] + "_format." + data_file.split('.')[1]
    f_out = open(output_file, "w", encoding='utf8')
    with open(data_file, "r", encoding='utf8') as f:
        for line in tqdm(f.readlines()):
            line = line.strip()
            if line != "":
                span_list = line.split('\t')
                text = ''.join(list(span_list[0])).split(' ')
                labels = ''.join(list(span_list[1])).split(' ')
                text_process = []
                print(text[0])
                for char in text[0]:
                    text_process.append(char)
                print("text_process:",text_process, len(text_process))
                print("labels:",labels, len(labels))
                if len(text_process) == len(labels):
                    for index in range(len(text_process)):
                        f_out.write(' '.join([text_process[index], labels[index]]) + '\n')
                    f_out.write('\n')
            else:
                f_out.write('\n')


if __name__ == '__main__':
    # deseg_weibo(weibo_ner_path)
    convert_format("/home/lab/shenyaodi/Flat-Lattice-Transformer-master/data/Address/train.txt")
    convert_format("/home/lab/shenyaodi/Flat-Lattice-Transformer-master/data/Address/dev.txt")
    convert_format("/home/lab/shenyaodi/Flat-Lattice-Transformer-master/data/Address/test.txt")
    print('- Done!')