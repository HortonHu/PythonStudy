# -*- coding:utf-8 -*-

# 正则表达式

# 匹配规则如下：
#   \d      匹配一个数字
#   \w      匹配一个字母或数字或下划线或汉字
#   \s      匹配一个空白符（包括空格、制表、换行、中文全角空格等）
#   .       匹配任意字符
#   \b	    匹配单词的开始或结束
#   ^	    匹配字符串的开始
#   $	    匹配字符串的结束

#   *       任意个字符（包括0个）
#   +       至少一个字符
#   ?       0个或1个字符
#   {n}     n个字符
#   {n,}    至少n个字符
#   {n,m}   n到m个字符
#   '-'     是特殊字符，在正则表达式中，要用'\'转义
# 例如\d{3}\s+\d{3,8} 可以匹配任意3个数字、空格、8个数字的字符串

# 分支条件
# | 表示分支条件，从左往右匹配，匹配到则不再继续

# 反义
# 查找不属于某个能简单定义的字符类的字符
#   \W	        匹配任意不是字母，数字，下划线，汉字的字符
#   \S	        匹配任意不是空白符的字符
#   \D	        匹配任意非数字的字符
#   \B	        匹配不是单词开头或结束的位置
#   [^x]	    匹配除了x以外的任意字符
#   [^aeiou]	匹配除了aeiou这几个字母以外的任意字符

# 更精确地匹配，可以用字符集[]表示范围
# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
# A|B可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'。

# 转义
# 对于 . ^ $ * + ? { [ ] \ | ( ) 字符串本身，如果想匹配字符本身 需要在前面加上\转义
# 由于Python的字符串本身也用\转义，所以要特别注意：
# Python的字符串   s = 'ABC\\-001'  对应的正则表达式字符串变成： 'ABC\-001'
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题

# re模块
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
# match（）函数只检测RE是不是在string的开始位置匹配， search()会扫描整个string查找匹配
# match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象 否则返回None。
# 常见的判断方法就是：
test_str = '用户输入的字符串'
print 'ok' if re.match(r'正则表达式', test_str) else 'failed'

# 切分字符串
# 用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
print 'a b   c'.split(' ')                      # 只能识别一个空格
print re.split(r'\s+', 'a b   c')               # 识别任意个空格
print re.split(r'[\s\,]+', 'a,b, c  d')         # 识别任意个空格和','
print re.split(r'[\s\,\;]+', 'a,b;; c  d')      # 识别任意个空格和';'

# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能
# 用()表示的就是要提取的分组（Group）
# 分组后可以加上数量来匹配重复字符 如(\d{1,3}\.){3}
# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m
print m.group(0)
print m.group(1)
print m.group(2)
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串
# group(0)是原始字符串，group(1)、group(2)……表示第1、2、……个子串

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]'
             r'|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
m.groups()
# 这个正则表达式可以直接识别合法的时间。但是有些时候，用正则表达式也无法做到完全验证，比如识别日期：
# '^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
# 对于'2-30'，'4-31'这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了


# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print re.match(r'^(\d+)(0*)$', '102300').groups()       # 匹配出数字后面的0
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
print re.match(r'^(\d+?)(0*)$', '102300').groups()


# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤
import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()
# 匹配模式 比如忽略大小写、多行匹配
# re.compile(pattern[, flags])
# re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
# M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
# S(DOTALL): 点任意匹配模式，改变'.'的行为
# L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
# U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
# X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的：

# 练习
# 尝试写一个验证Email地址的正则表达式。
# 版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com
# re_rule_str = r'([a-zA-Z\.]*@[a-z]*.com)'

# 版本二可以验证并提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org
# re_rule_str = r'<([a-zA-Z]*\s[a-zA-Z]*)>\s[a-zA-Z\.]*@[a-z]*.org'


# 用正则表达式匹配网页中的中文内容
# Python 2.x版本，需要用unicode来匹配。正则表达式的字符串前要加上u，待匹配的文本要decode()。例如：
import re
text = "你好吗？我很好！"
m = re.findall(ur"你好", text.decode("utf8"))
if m:
    print m[0].encode('utf8')
else:
    print 'not match'







