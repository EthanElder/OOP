import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd (this is an option for later)


x = np.array(["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"])
y = np.array([128, 100, 85, 76, 54, 26, 98, 0, 52])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("grades")

#line chart
plt.plot(x, y)
plt.show()

#pie chart
mylabels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]
plt.pie(y, labels=mylabels)
plt.show()


x= [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y= [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

#scatter plot
plt.scatter(x, y)
plt.show()