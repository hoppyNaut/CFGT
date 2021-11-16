import os
import random

l_train = []
l_val = []
l_test = []

# 读取文件中的内容，并将其打乱写入列表
def ReadFileDatas(original_filename):
    file = open(original_filename, 'r+')
    dataList = file.readlines()
    random.shuffle(dataList)
    file.close()
    print("数据集总量：", len(dataList))
    return dataList

# 将数据集随机划分
def TrainValTestFile(dataList):
    i = 0
    j = len(dataList)
    for line in dataList:
        if i < (j * 0.6):
            i += 1
            l_train.append(line)
        elif i < (j * 0.8):
            i += 1
            l_val.append(line)
        else:
            i += 1
            l_test.append(line)

    print("总数量:%d,此时创建train,val,test数据集" % i)
    print("len(train):%d len(dev):%d len(test):%d" % (len(l_train),len(l_val),len(l_test)))
    return l_train, l_val, l_test

#将获取到的各个数据集的包含的文件名写入txt中
def WriteDatasToFile(listInfo, new_filename):
    file_handle = open(new_filename,'w')
    for str_Result in listInfo:
        file_handle.write(str_Result)
    file_handle.close()
    print('写入 %s 文件成功.' % new_filename)


if __name__ == "__main__":
      listFileInfo = ReadFileDatas('data/Address/address_info.txt') # 读取文件
      l_train,l_val,l_test=TrainValTestFile(listFileInfo)
      WriteDatasToFile(l_train, 'data/Address/train.txt')
      WriteDatasToFile(l_val, 'data/Address/val.txt')
      WriteDatasToFile(l_test, 'data/Address/test.txt')