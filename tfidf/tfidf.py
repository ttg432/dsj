import os

file_path = "./allfiles"
'''
word_freq:{word:count} 单篇文章的词频统计
'''
# 获取doc和对应每篇文章的词频TF
# print(os.listdir(file_path))  取出每个文章的名字
for filename in os.listdir(file_path):
    # os.path.join(file_path,filename) 等价于 file_path+'/'+filename
    with open(file_path + '/' + filename, "r", encoding="utf-8") as f:
        word_freq = dict()
        sum_cnt=0
        for line in f.readlines():
            words = line.strip().split(" ")
            for word in words:
                if len(word.strip()) < 1:
                    continue
                if word_freq.get(word, -1) == -1:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
                sum_cnt+=1
        print(word_freq)
        sort_word_freq=sorted(word_freq.items(),key=lambda word:(word[1],word[0]),reverse=True)
        print(max(sort_word_freq,key=sort_word_freq.get()))
        #占比方式处理
        for word in word_freq.keys():
            word_freq[word] /= sum_cnt  #tf/总单词数量
        #取最大值

        break
