import sys

from tqdm import tqdm

sys.path.append("..")
from paths import ontonote4ner_cn_path
import os

def convert_ontonotes(ontonotespath):
    train_path = os.path.join(ontonotespath, 'train.char.bmes')
    dev_path = os.path.join(ontonotespath, 'dev.char.bmes')
    test_path = os.path.join(ontonotespath, 'test.char.bmes')

    for data_file in [train_path, dev_path, test_path]:
        output_file = data_file + "_clip"
        f_out = open(output_file, "w", encoding='utf8')
        with open(data_file, "r", encoding='utf8') as f:
            for line in tqdm(f.readlines()):
                line = line.strip()
                if line != "":
                    span_list = line.split('\t')
                    text = ''.join(list(span_list[0])).split(' ')
                    labels = ''.join(list(span_list[1])).split(' ')
                    print("text:",text)
                    print("labels:",labels)
                    if len(text) == len(labels):
                        for index in range(len(text)):
                            f_out.write(' '.join([text[index], labels[index]]) + '\n')
                        f_out.write('\n')
                else:
                    f_out.write('\n')

if __name__ == '__main__':
    convert_ontonotes(ontonote4ner_cn_path)
    print('- Done!')