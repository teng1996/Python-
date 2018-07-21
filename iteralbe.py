from collections import Iterator
from collections import Iterable
class next1():
    def __init__(self,data):
        self.data = data
        self.count = 0
    def __next__(self):
        print('迭代器被调用了')
        if self.count < len(self.data):
            val = self.data[self.count]
            self.count+=1
            return val
        else:
            raise StopIteration
class iterable():
    def __init__(self,data):
        self.data = data
        self.count = 0
    def __iter__(self):
        print('__iter__被调用了')
        return next1(self.data)
    
        
a = iterable([3,46,74,23])
print(type(a))
print(isinstance(a,Iterable)) # 显示为True，因为iterable类实现了__iter__方法
                              # 是一个可迭代的对象
print(isinstance(a,Iterator)) # 显示为False，因为iterable类没有实现 __next__方法
                              # 故不是迭代器
aa = iter(a)
print(type(aa))
print(isinstance(aa,Iterable))# 显示为False，因为aa是通过调用iter方法来调用a对象中的
                              # __iter__方法 return了自定义的next1对象，
print(isinstance(aa,Iterator))# 显示为False ， 因为 aa对象并没有实现__iter__方法，
                              # 故aa既不是迭代器（同时实现__iter__和__next__方法），也不是可迭代对象（必须具有__iter__
                              #  方法，如果添加了__next__方法，那么它也是迭代器）
class iterable1():
    def __init__(self,data):
        self.data = data
        self.count = 0
    def __iter__(self):
        print('__iter__被调用了')
        return self
    def __next__(self):
        print('__next__被调用了')
        if self.count < len(self.data):
            val = self.data[self.count]
            self.count+=1
            return val
        else:
            raise StopIteration
b = iterable1([3,4,5,6])
print(isinstance(b,Iterable))
print(isinstance(b,Iterator))
# 以上两个都显示True，因为iterable1 类不仅实现了__iter__方法(可迭代对象)
# 也实现了__next__方法（迭代器）
# 故，iteralbe1 既是可迭代对象，又是迭代器
class iterable2():
    def __init__(self,data):
        self.data = data
        self.count = 0
    def __next__(self):
        print('__next__被调用了')
        if self.count < len(self.data):
            val = self.data[self.count]
            self.count += 1
            return val
        else:
            raise StopIteration
c = iterable2([3,2,3,5])
print(isinstance(c,Iterable)) #显示False，说明不是可迭代对象，因为没有iter方法
print(isinstance(c,Iterator))



for i in b:
    print(i)
for i in a:
    print(i)
print(next(aa))

print(next(aa))
print(isinstance(aa,Iterator))



        












