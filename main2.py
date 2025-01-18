import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig, ax=plt.subplots()
df=pd.read_excel("C:\\Users\\aishw\\OneDrive\\Desktop\\graph\\List of Audit courses ay 24-25 including ECE.xlsx",'Sheet1')
print (df)
plt.plot(df['YEAR'],df['Erosion_in_Spain'])
plt.plot(df['YEAR'],df['Deposition_in_Spain'])


plt.xlabel('Year',color='black')
plt.ylabel('Erosion and Deposition in Sq-km',color='blue')
plt.title("EROSIION AND DEPOSITION VS YEAR",color='red')
line_1,=plt.plot(df['YEAR'],df['Erosion_in_Spain'],label='EROSION',color='red',marker='.')
line_2,=plt.plot(df['YEAR'],df['Deposition_in_Spain'],label='DEPOSITION',color='blue',marker='*')
plt.legend(handles=[line_1,line_2],loc='upper left',prop={'weight':'bold','size':12,'family':'Times New Roman'})
plt.grid()
plt.show()