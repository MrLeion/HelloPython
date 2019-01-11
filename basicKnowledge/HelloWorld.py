
print('Hello python')
print('你好，世界')


name = input('Please enter your name:')

print('hello',name)
print(name)




# Ex1
width = input('Please input width:')
height = input('Please input height:')
print(int(width)*int(height))




# 总结：input(提示信息)
# 输出中文的时候要在字符串前面加u。
# 因为python中字符串默认采用ASCII，要声明为unicode就要加u(linux环境下不需要加u)