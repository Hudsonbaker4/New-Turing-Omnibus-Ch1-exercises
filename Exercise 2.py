import matplotlib.pyplot as plt

side = int(input("Enter a value for the side: "))
corna = int(input("Enter a value for corner a: "))
cornb = int(input("Enter a value for corner b: "))

redX = []
redY = []
greenX = []
greenY = []

for i in range(100):
    for j in range(100):
        x = corna + i*side/100
        y = cornb + j*side/100
        c = int(x**2 + y**2)
        if c % 3 == 0:
            redX.append(x)
            redY.append(y)
        elif c % 3 == 2:
            greenX.append(x)
            greenY.append(y)

plt.plot(redX, redY, 'r+', marker = 'o', markersize = 1)
plt.plot(greenX, greenY, 'g+', marker = 'o', markersize = 1)
plt.show()
