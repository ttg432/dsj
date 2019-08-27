import jieba

s1 = "这只皮靴号码大了，那只号码合适"
s2 = "这只皮靴号码不小，那只更合适"

# s1_seg = "/".join([x for x in jieba.cut(s1, cut_all=True) if x != ''])
# s2_seg = "/".join([x for x in jieba.cut(s2, cut_all=True) if x != ''])
# print(s2_seg)
s1_list = [x for x in jieba.cut(s1, cut_all=True) if x != '']
s2_list = [x for x in jieba.cut(s2, cut_all=True) if x != '']
# 合并方式一
# lst合并一起再去重: {'大', '更合', '了', '皮靴', '那', '号码', '这', '合适', '只', '不小'}
print("lst合并一起再去重:", set(s1_list + s2_list))
# 合并方式二
s1_set = set(s1_list)
s2_set = set(s2_list)
s_set = s1_set.union(s2_set)
# s_set: {'那', '号码', '不小', '这', '皮靴', '只', '更合', '了', '合适', '大'}
print("s_set:", s_set)
# 对所有汉语单词进行编码，给每个汉语一个位置，对应这个位置上放入词的频率
index = 0
word_encode_dict = {}
# s_set中已经是唯一了，所以不用判断word_encode_dict中word的唯一性
for word in s_set:
    word_encode_dict[word] = index
    index += 1
print(word_encode_dict)


# word count
# s1_dict={}
# for word in s1_list:
#     if(s1_dict.get(word,-1)==-1):
#         s1_dict[word]=0
#     s1_dict[word]+=1
# print(s1_dict)
# s2_dict={}
# for word in s2_list:
#     if(s2_dict.get(word,-1)==-1):
#         s2_dict[word]=0
#     s2_dict[word]+=1
# 计算单独个体所有词组的统计
def word_cnt(lst):
    s_dict = {}
    for word in lst:
        if (s_dict.get(word, -1) == -1):
            s_dict[word] = 0
        s_dict[word] += 1
    return s_dict


s1_dict = word_cnt(s1_list)
s2_dict = word_cnt(s2_list)


# 计算单独个体向量
def word_tf(lst):
    s1_freq_lst = [0] * len(word_encode_dict)
    for word, cnt in lst.items():
        if word_encode_dict.get(word, -1) == -1:
            continue
        s1_freq_lst[word_encode_dict[word]] = cnt
    return s1_freq_lst


# [2, 0, 1, 1, 1, 1, 1, 1, 0, 2]
# [1, 1, 1, 1, 1, 0, 1, 0, 1, 2]
print(word_tf(s1_dict))
print(word_tf(s2_dict))

# 线上新来文本
c = "为什么就喜欢皮靴呢？运动鞋怎么样？"
# 1.切词
c_lst = [x for x in jieba.cut(c, cut_all=True) if x != '']
# 2.转数组(数组大小（sparse[]）就是字典大小)  文本数据向量有多大
'''
dense vector  稠密向量
sparse vector  稀疏向量 只会取不等于0的索引和值
例如
array1=[0,0,1,0]  array1_index=[2](代表index)  array1_value=[1]（代表value）  
array2=[0,1,0,1]  array2_index=[1,3](代表index) array2_value=[1,1] 代表value)
scipy.sparse
sparse vector 会以两个数组的形式保存 第一个数组保存非零值对应的索引  第二个数据保存非零值
然后遍历array1,array2中代表index的数组array1_index,array2_index如果索引没有匹配上结果直接是0
'''
'''
word_encode_dict这个数据字典是非常庞大的 8W
'''
c_dict = word_cnt(c_lst)
c_freq_lst = word_tf(c_dict)
print(c_freq_lst)
# -------------------------余弦相似度代码逻辑梳理--------------------------------------
# 1.对两个个体先进行逐个切词 例如：s1 =>（切词之后）s1_list   s2 =>（切词之后）s2_list
# 2.对两个已经切好词的集合分别去重，并 合并在一起 实现方式可以自己随意发挥
# 3.对两个集合的数据词典进行排序编号
# 4.统计单独个体词组出现的次数
# 5.分别对两组的个体计算向量(都是用离线)
