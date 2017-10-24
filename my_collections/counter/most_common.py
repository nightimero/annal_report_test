# -*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
"""
下面这个例子就是使用Counter模块统计一段句子里面所有字符出现次数
"""
from collections import Counter

s = '''A Counter is a dict subclass for counting hashable objects.
 It is an unordered collection where elements are stored as dictionary
  keys and their counts are stored as dictionary values.
   Counts are allowed to be any integer value including zero or negative counts. 
   The Counter class is similar to bags or multisets in other languages.'''.lower()

c = Counter(s)
# 获取出现频率最高的5个字符
print c.most_common(5)


# Result:
[(' ', 54), ('e', 32), ('s', 25), ('a', 24), ('t', 24)]

t = u"""为你我用了
半年的积蓄飘洋过海的来看你
为了这次相聚
我连见面时的呼吸都曾反复练习
言语从来没能
将我的情意表达千万分之一
为了这个遗憾
我在夜里想了又想不肯睡去
记忆它总是慢慢的累积
在我心中无法抹去
为了你的承诺
我在最绝望的时候都忍着不哭泣
陌生的城市啊 熟悉的角落里
也曾彼此安慰 也曾相拥叹息
不管将会面对什么样的结局
在漫天风沙里望着你远去
我竟悲伤得不能自己
多盼能送君千里直到山穷水尽
一生和你相依
为你我用了
半年的积蓄飘洋过海的来看你
为了这次相聚
我连见面时的呼吸都曾反复练习
言语从来没能
将我的情意表达千万分之一
为了这个遗憾
我在夜里想了又想不肯睡去
记忆它总是慢慢的累积
在我心中无法抹去
为了你的承诺
我在最绝望的时候都忍着不哭泣
陌生的城市啊 熟悉的角落里
也曾彼此安慰 也曾相拥叹息
不管将会面对什么样的结局
在漫天风沙里望着你远去
我竟悲伤得不能自己
多盼能送君千里直到山穷水尽
一生和你相依
陌生的城市啊 熟悉的角落里
也曾彼此安慰 也曾相拥叹息
不管将会面对什么样的结局
在漫天风沙里望着你远去
我竟悲伤得不能自己
多盼能送君千里直到山穷水尽
一生和你相依
多盼能送君千里直到山穷水尽
一生和你相依"""

c =Counter(t)

print c.most_common(5)

