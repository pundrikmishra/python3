from matplotlib import pyplot as plt
#style.use('ggplot')
#style.use('dark_background')
#style.use('grayscale')


# x = [5,6,7,8,0]
x = [5,6,7,8]
y = [7,3,8,3]
x2= [5,6,7,8]
y2= [6,7,2,6]

# print(len(x))
# print(len(y))

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X  axis')

plt.plot(x,y,'g',linewidth=5)
plt.plot(x2,y2,'c',linewidth=10)

plt.show()