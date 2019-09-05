import math

train_data = "./mid_data/train.txt"
sim_user_user = "./mid_data/sim_user_user.txt"

# d = generate_train_data(nrows=None)
# with open(train_data,'w') as f:
#     f.write((str(d)))
# print(d)
'''
找相似的用户
1.获得用户和用户之间的相似度
1.1正常逻辑的用户相似度计算
1.2优化计算用户与用户之间的相似度 user->item=>item=>user
'''


# 1.1正常逻辑的用户相似度计算
def user_normal_simmilarity(d):
    w = dict()
    for u in d.keys():
        if u not in w:
            w[u] = dict()
        for v in d.keys():
            if u == v: continue
            # 相似度计算，通过两个用户共同拥有的物品集合数量
            '''
            print(d[u])  {'242': 3}
            print(d[v])  {'302': 3}
            print(set(d[u]))  {'242'}
            print(set(d[v]))  {'302'}
            print(set(d[u]) & set(d[v])) set()  # 两个集合的交集  是map形式 只取了key进行比较
            print(len(set(d[u]) & set(d[v]))) 0
            '''
            sim_size = len(set(d[u]) & set(d[v]))
            if sim_size > 0:
                w[u][v] = sim_size  # jaccard distance相似度
                w[u][v] = 2 * w[u][v] / (len(d[u]) + len(d[v])) * 1.0
    # print(w['196'])
    # print(len(w['196']))


# 1.2优化计算用户与用户之间的相似度 user->item=>item=>user
# 建立item->users的倒排表
def user_sim(d):
    item_users = dict()
    for u, items in d.items():
        for i in items.keys():
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)
    # print(item_users)
    # 计算用户共同的items的数量
    C = dict()  # 存放统计用户与用户共同item数量
    N = dict()  # 存放用户对应的item数量

    for i, users in item_users.items():
        for u in users:
            if N.get(u, -1) == -1: N[u] = 0
            N[u] += 1
            if C.get(u, -1) == -1: C[u] = dict()
            for v in users:
                if u == v: continue
                if C[u].get(v, -1) == -1: C[u][v] = 0
                # C[u][v] += 1
                # 对每项的统计值 加一下权重
                C[u][v] += 1 / math.log(1 + len(item_users[i]))
    del item_users
    # print(C)
    # print(N)
    # 计算最终的相似度
    for u, sim_users in C.items():
        for v, cuv in sim_users.items():
            C[u][v] = 2 * C[u][v] / float(N[u] + N[v])
    return C


# 先将相似用户矩阵存储到磁盘里
# C=user_sim(d)
# with open(sim_user_user,'w') as fw:
#     fw.write(str(C))


def recommend(user, d, C, k):
    rank = dict()
    # 用户评论过的电影
    interacted_items = d[user].keys()
    print(interacted_items)
    print(C[user].items())
    # 取相似的top k个用户
    for v, cuv in sorted(C[user].items(), key=lambda x: x[1], reverse=True)[0:k]:
        # 取相似的K个用户的items
        for i, rating in d[v].items():
            if i in interacted_items:
                # 过滤掉已经评论过的电影（购买过的商品）
                continue
            elif rank.get(i, -1) == -1:
                rank[i] = 0
            rank[i] += cuv * rating


if __name__ == '__main__':
    d = dict()
    with open(train_data, 'r') as ft:
        d = eval(ft.read())

    C = dict()
    with open(sim_user_user, 'r') as fc:
        C = eval(fc.read())

    user = '196'
    k = 10
    rank = recommend(user, d, C, k)
    print(sorted(rank.items(), key=lambda x: x[1], reverse=True))
