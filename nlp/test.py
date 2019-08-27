b = [2, 2, 6, 3, 5]

for i in range(len(b)):
    print('i:', i)


a={'皮靴':15, '合适':1}
for k,v in a.items():
    print(k)

stop_list=set()
with open('stop_list.txt','r',encoding='utf-8') as f:
    for word_lst in f.readlines():
        word=word_lst[0]
        stop_list.add(word)
print(stop_list)