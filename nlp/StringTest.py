import operator

s = '  hello, world!'
# 用于去掉字符串的头部和尾部的特殊字符串
print(s.strip("!"))
# 截取左边的指定字符串，并生成新的字符串,如果没有则返回整个字符串
print(s.lstrip(' hello, '))
print(s.lstrip(" hello, "))
# 分隔字符串并转成数组  结果：['  hello, world', '']
print(s.rsplit('!'))

# 连接字符串


# 查找字符 查找某个字符首次出现的位置
print(s.index("o"))

# 比较字符串  False
s1 = "hello"
print(operator.eq(s1, s))

# 翻转字符串
s3 = s[::-1]
print(s3)

# 分隔字符串
sStr1 = 'ab,cde,fgh,ijk'
sStr1=sStr1[sStr1.find(",") + 1:]
#cde,fgh,ijk
print(sStr1)
#['cde', 'fgh', 'ijk']
print(sStr1.split(","))