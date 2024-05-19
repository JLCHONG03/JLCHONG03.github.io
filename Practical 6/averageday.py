#use matplotlib to plot graphs in python
#store the data in dictionary
#plot the figure in the dictionary

import matplotlib.pyplot as plt 

Time_spent_during_an_average_day = [8,6,3.5,2,1,3.5]
Activity = ['Sleeping','Classes','Studying','TV','Music','Others'] 

plt.figure() 
plt.pie(Time_spent_during_an_average_day, labels = Activity, startangle = 90)
plt.show()
plt.clf()


