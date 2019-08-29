import os
import math
import cos.stop_list

file_path = "./allfiles"
'''
word_freq:{word:count} 单篇文章的词频统计
'''
# 获取doc和对应每篇文章的词频TF
# print(os.listdir(file_path))  取出每个文章的名字
doc_freq = {}
doc_num = 0
doc_words = {}
for filename in os.listdir(file_path):
    # os.path.join(file_path,filename) 等价于 file_path+'/'+filename
    stop_list = cos.stop_list.stop_list()
    # print(stop_list)
    with open(file_path + '/' + filename, "r", encoding="utf-8") as f:
        word_freq = dict()
        sum_cnt = 0
        for line in f.readlines():
            words = line.strip().split(" ")
            for word in words:
                if len(word.strip()) < 1 or word in stop_list:
                    continue
                if word_freq.get(word, -1) == -1:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
                sum_cnt += 1
        # print(word_freq)
        sort_word_freq = sorted(word_freq.values(), reverse=True)
        max_cnt = sort_word_freq[0]
        # print(max_cnt)
        # 占比方式处理
        for word in word_freq.keys():
            # word_freq[word] /= sum_cnt  # tf/总单词数量
            # 取最大值
            word_freq[word] /= max_cnt  # 最大值标准化
            if doc_freq.get(word, -1) == -1:
                doc_freq[word] = 1
            else:
                doc_freq[word] += 1
            # if word_freq[word] ==1:
            #     print('value 1:',word)
        doc_words[filename] = word_freq
        doc_num += 1
        # print(word_freq)


#套idf公式
for word in doc_freq.keys():
    doc_freq[word]=math.log10(doc_num/float(doc_freq[word]+1))
print(doc_freq)
print(sorted(doc_freq.items(),key=lambda x:x[1],reverse=False)[:10])
print(sorted(doc_freq.items(),key=lambda x:x[1],reverse=True)[:10])
#套tf-idf公式
for doc in doc_words.keys():
    for word in doc_words[doc].keys():
        doc_words[doc][word] *=doc_freq[word]
print(doc_words["3business.seg.cln.txt"]['金价'])
print(doc_words["3business.seg.cln.txt"]['重大'])

