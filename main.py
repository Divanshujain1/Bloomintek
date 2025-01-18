import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

df = pd.read_excel('List of Audit courses ay 24-25 including ECE.xlsx')

data_array= df.to_numpy()
#print(data_array)
transposed_array= data_array.transpose()
#print(transposed_array)
sorted_array = transposed_array[:, np.argsort( transposed_array[2] ) ]
#print(sorted_array)
x=np.array(transposed_array[2])
y=np.array(transposed_array[1])
z=np.array(transposed_array[0])

fig=plt.figure()
ax= fig.add_subplot(111, projection='3d')
ax.plot(x,y,z, color='green',marker='o')

ax.set_xlabel("Deposition In Spain")
ax.set_ylabel("Erosion in Spain")
ax.set_zlabel("Year")
plt.show()