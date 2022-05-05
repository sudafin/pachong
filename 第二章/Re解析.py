import re

# findall：匹配字符串中所有的符合正则的内容
lst = re.findall(r"\d+", "my telephone is 10086 and 10001")
print(lst)
# ['10086', '10001']

# finditer：匹配字符串中是所有的内容{返回的是迭代器}，从迭代器中拿内容需要.group()
it = re.finditer(r"\d+", "my telephone is 10086 and 10001")
for ret in it:
    print(ret.group())
# 10086
# 10001

# search，找到一个结果就返回，返回的结果是match对象,拿数据用.group，匹配一个
s = re.search(r"\d+", "my telephone is 10086 and 10001")
print(s.group())
# 10086

# match 从头可以匹配，匹配一个
t = re.match(r"\d+", "my telephone is 10086 and 10001")
# 执行错误
newt = re.match(r"\d+", "10086 and 10001 is my telephone")
print(newt.group())
# 10086

print("------------------")

# 预加载正则表达式
obj = re.compile(r"\d+")  # 写一个正则表达式
yet = obj.findall("my telephone is 10086 and 10001")  # 输入的内容
print(yet)
# ['10086', '10001']
iet = obj.finditer("my telephone is 10086 and 10001")
for i in iet:
    print(i.group())
# 10086
# 10001

s = """""
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>周杰伦</span></div>
<div class='jolin'><span id='3'>蔡依林</span></div>
<div class='loken'><span id='4'>林俊杰</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>", re.S)
# re.S让.能匹配到换行符,使用"" 不要使用'',原文中已经有''了
role = obj.finditer(s)
for k in role:
    print(k.group())
print("--------------------")

# <div class='jay'><span id='1'>郭麒麟</span></div>
# <div class='jj'><span id='2'>周杰伦</span></div>
# <div class='jolin'><span id='3'>蔡依林</span></div>
# <div class='loken'><span id='4'>林俊杰</span></div>

# (?P<名字>正则) 可以单纯从正则匹配的内容中进一步提取内容
newObj = re.compile(r"<div class=(?P<wahhh>'.*?')><span id='\d+'>(?P<wahh>.*?)</span></div>", re.S)
newRole = newObj.finditer(s)
for k1 in newRole:
    print(k1.group("wahhh"))
    print(k1.group("wahh"))
# 'jay'
# 郭麒麟
# 'jj'
# 周杰伦
# 'jolin'
# 蔡依林
# 'loken'
# 林俊杰
