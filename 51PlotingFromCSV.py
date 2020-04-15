from matplotlib import pyplot as plt
import numpy as np
#style.use('ggplot')
#style.use('dark_background')
#style.use('grayscale')

x,y,x1,y1  = np.loadtxt('example2.txt', unpack= True, delimiter= ',' )


# print(x)
# print(y)

plt.plot(x,y1)
plt.plot(y,x1)
plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X  axis')
# plt.grid(True, color='g')

plt.show()