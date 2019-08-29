# 主要掌握 jieba.cut   jieba.cat_for_search
import jieba

seg_list = jieba.cut("我在学习自然语言处理", cut_all=True)
print(seg_list)
print("Full Model:" + "/".join(seg_list))  # 全模式

seg_list = jieba.cut("我在学习自然语言处理", cut_all=False)
print("Default Model:" + "/".join(seg_list))  # 精确模式


seg_list = jieba.cut("他毕业于上海交通大学，在百度深度学习研究院进行研究")
print(", ".join(seg_list))
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")
print(", ".join(seg_list))

seg_list = jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")
print(", ".join(seg_list))


#用户自定义词典
print("/".join(jieba.cut("如果放到旧字典中将出错。",HMM=False)))
print(jieba.suggest_freq(('中','将'),True))
print("/".join(jieba.cut('如果放到旧字典中将出错。',HMM=False)))
