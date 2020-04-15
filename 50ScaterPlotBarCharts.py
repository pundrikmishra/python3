from matplotlib import pyplot as plt
#style.use('ggplot')
#style.use('dark_background')
#style.use('grayscale')


# x = [5,6,7,8,0]
# x = [5,6,7,8]
x = [2,4,6,8]
y = [7,3,8,3]
x2= [5,6,7,8]
y2= [6,7,2,6]

# print(len(x))
# print(len(y))

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X  axis')

# plt.grid(True, color='g')

# plt.scatter(x,y,label='Line One')
# plt.scatter(x2,y2,label='Line Two')
# plt.scatter(x,y,color='r')
# plt.scatter(x2,y2,color='g')
# plt.bar(x,y,label='Line One', align='center')
# plt.bar(x2,y2,label='Line Two', align='center')
plt.bar(x,y,label='Line One')
plt.bar(x2,y2,label='Line Two')
# plt.bar(x,y,color='r')
# plt.bar(x2,y2,color='g')



plt.legend()
plt.show()