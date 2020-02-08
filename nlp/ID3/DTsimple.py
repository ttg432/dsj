import math


def create_data_set():
    data_set = [[1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    cols = ['no surfacing', 'flippers']
    return data_set, cols


# print(create_data_set())
# 计算熵
def calc_ent(data_set):
    n = len(data_set)
    label_cnt = {}
    for featVec in data_set:
        cur_label = featVec[-1]
        if cur_label not in label_cnt.keys():
            label_cnt[cur_label] = 0
        label_cnt[cur_label] += 1

    E = 0.0
    for key in label_cnt:
        prob = float(label_cnt[key]) / n
        E -= prob * math.log(prob)
    return E


# print(calc_ent(create_data_set()))
# 划分数据集：根据特征每个值划分数据集 i:age value:青年、中年、老年
def split_data_set(data_set, i, value):
    ret_data_set = []
    for featVec in data_set:
        if featVec[i] == value:
            # 将i之前和之后的特征重新放入样本中，把i特征去掉
            reduced_feat_vec = featVec[:i]
            reduced_feat_vec.extend(featVec[i + 1:])
            ret_data_set.append(reduced_feat_vec)
    return ret_data_set


# 选择最好的特征进行分裂
def choose_best_feature_to_split(data_set):
    print('choose_data_set:'+str(data_set))
    num_features = len(data_set[0]) - 1
    base_entropy = calc_ent(data_set)  # 第一层的熵
    best_info_gain = 0.0  # 信息增益
    best_feature = -1
    print('num_features:'+str(num_features))
    # i相当于年龄
    for i in range(num_features):
        print('i:'+str(i))
        # 获取当前年龄这一列的所有制，为了下一步获取青年，中年，老年唯一值
        feat_list = [example[i] for example in data_set]
        print('choose:'+str(feat_list))
        # 获取中年、青年、老年三个不同值的唯一值
        unique_vals = set(feat_list)
        new_entropy = 0.0

        # value相当于青年，中年，老年
        for value in unique_vals:
            # 比如属于青年的数据集合
            sub_data_set = split_data_set(data_set, i, value)
            print('sub_data_set:'+str(sub_data_set))
            # 青年中年老年在总（上一次划分数据集）样本中的占比
            prob = len(sub_data_set) / float(len(data_set))
            # 划分之后的数据集的信息entropy
            new_entropy += prob * calc_ent(sub_data_set)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature


# 叶子节点返回的规则：样本中类别数量最多的一个类别
def majority_cnt(class_list):
    d = dict()
    for c in class_list:
        if d.get(c, -1) == -1:
            d[c] = 0
        d[c] += 1
    return max(d.items(), key=lambda x: x[1])[0]


# 生成决策树，递归
def create_tree(data_set, cols):
    print(data_set)
    class_list = [example[-1] for example in data_set]
    print(class_list)
    # print(class_list[0])
    # print(class_list.count('no'))
    # 判断类别列表中是不是只有一个值，如果是，表示已经是纯了
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 如果数据维度为1，要基于最后一个特征划分，相当于接下来没有特征了，特征列表为空
    # print(majority_cnt(class_list))
    print(data_set[0])
    if len(data_set[0]) == 1:
        # 返回样本类别数量最多的一个类别
        return majority_cnt(class_list)
    best_feat = choose_best_feature_to_split(data_set)
    best_feat_label = cols[best_feat]
    # 初始化树，用字典作为树
    my_tree = {best_feat_label: {}}
    del (cols[best_feat])
    feat_values = [example[best_feat] for example in data_set]
    unique_vals = set(feat_values)
    # 用特征值划分数据集
    for value in unique_vals:
        subcols = cols
        my_tree[best_feat_label][value] = create_tree(split_data_set(data_set, best_feat, value), subcols)
    return my_tree


if __name__ == '__main__':
    data_set, cols = create_data_set()
    print(create_tree(data_set, cols))
    # a = [1, 1, 'yes']
    # print(a[:2])
    # print(a[1:])
    # split_data_set(data_set,i=)
