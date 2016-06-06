#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Data type: int\ float\ string\ bool\ None
print 'integer:', 1
print 'float  :', 3.14, 1e-5
print 'string :', 'python'
print 'string :', 'I\'m OK'			# 加\有避免转义的作用
print 'string :', '\\\n\\'
print 'string :', '\\\t\\'
print 'string :', r'\\\t\\'      	# 加r则不转义 个人认为比加/好用
print 'string :', 'doesn\'t'  		# use \' to escape the single quote...
print 'string :', '''line1
line2'''							# 多行字符串
print 'Bool   :', True, not True, True and False, True or False
print None


# Data type: string 'abc'
# + * index slice
# methods: split() join()
# immutable.
# ''和''''效果相同 '''...'''or"""..."""中间可以任意添加''或者'''' 也可以当做一种注释 通常用于doc_comment
# ' "包含对方的时候均不需要转义
# 对于较长的语句 可以用\来续行 \后不能有# 也不能有任何字符
# The only difference between the two is that within single quotes you don’t need to escape "
# (but you have to escape \') and vice versa.
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
a = 'I am OK.'
b = a.split()
print b

s = ';'
li = ['apple', 'pear', 'orange']
fruit = s.join(li)
print fruit

# Data type: List ['a', 'b', 'c'] or [1, 2, 3]
# +/index/slice/nestable/del/mutable
# methods: append(x) extend(L) insert(i, x) remove(x) pop([i]) index(x) count(x) sort() reverse()
# item的type可以不同
# 遍历list的时候可以用list[:]复制一个相同的list来遍历
classmates = ['Michael', 'Bob', 'Tracy']
print 'List:', classmates
print 'length of List:', len(classmates)
classmates.append('Adam')   	# 末尾插入
print 'List:', classmates
classmates.insert(1, 'Jack')    # 指定位置插入
print 'List:', classmates
classmates.pop()    # 删除末尾元素
print 'List:', classmates
classmates.pop(1)   # 删除指定元素
print 'List:', classmates
classmates[1] = 'Sarah'     # 直接替换指定位置元素
print 'List:', classmates
s = ['python', 'java', ['asp', 'php'], 'scheme']    # list可嵌套
print list('abc')       # 得到一个list['a', 'b', 'c']

# 用collections.deque构造双端队列来快速的从任意方向pop或append
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print queue

# Data type: Tuple: ('a', 'b', 'c')
# index/immutable
# Tuple和list非常类似，但是tuple一旦初始化就不能修改，更安全
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 如果元素是可变的 则该元素可变 相当于tuple的内容还是改变了
classmates = ('Michael', 'Bob', 'Tracy')
print 'Tuple:', classmates
print classmates[0], classmates[1]
t = (1)                 # 特例，按照数学运算定义
tt = (1,)               # 用,来消除歧义
print type(t), type(tt)

# Data type: dict 	{key: value}
# key是immutable 但是整体是mutable
# dict全称dictionary，在其他语言中也称为map，使用键-值（'key':value）存储，具有极快的查找速度
# list比较，dict有以下几个特点：
# 1.查找和插入的速度极快，不会随着key的增加而增加
# 2.需要占用大量的内存，内存浪费多
# dict是用空间来换取时间的一种方法。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print 'dict:', d
print d['Bob']
d['Adam'] = 67   # 通过key放入value值进入dict，同一个key放入多个value后面的会抵消前面的
print 'dict:', d
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print 'Thomas' in d
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print d.get('Thomas')
print d.get('Thomas', -1)
d.pop('Bob')    # 删除key 对应的value也会删除
# 使用zip来生产dict  d = dict(zip(keys, values))
keys = ['Safe', 'Bob', 'Thomas']
values = ['Hammad', 'Builder', 'Engine']
d = dict(zip(keys, values))
print d

# Data type: set{'key'}
# set和dict类似，也是一组key的集合，但不存储value, key不能重复
# 常用来清理重复元素
# s = set([1, 2, 3]) 也可以这样定义
s = {'1', '2', '3'}
print 'set:', s
s = {'1', '2', '1', '1', '2', '3', '3'}
print 'set:', s
s.add(4)            # 添加key
print 'set:', s
s.add(4)            # 重复添加无效
print 'set:', s
s.remove(4)         # 删除key
print 'set:', s
# set可以看成数学意义上的无序和无重复元素的集合
# 因此，两个set可以做数学意义上的 - 交集、并集等操作
s1 = {'1', '2', '3'}
s2 = {'2', '3', '4'}
print 'set:', s1 & s2
print 'set:', s1 | s2

# 可变对象：list/
# 不变对象：string/
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容
a = ['c', 'b', 'a']
a.sort()
print 'a =', a
a = 'abc'
b = a.replace('a', 'A')
print b
print a

# 变量可以为任意数据类型
a = 123
print 'the type of a is', type(a)
a = '123'
print 'the type of a is', type(a)
a = True
print 'the type of a is', type(a)
a = ('1', '2', '3')
print 'the type of a is', type(a)
a = ['1', '2', '3']
print 'the type of a is', type(a)
a = {'a': 1, 'b': 2, 'c': 3}
print 'the type of a is', type(a)
a = {'1', '2', '3'}
print 'the type of a is', type(a)


