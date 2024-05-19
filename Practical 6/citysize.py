#import the necessary libraries
#store the data in the dictionary
#plot the figure in  the dictionary
#use the subplot function to plot two bar chart in one figure
import matplotlib.pyplot as plt 

uk_cities = [0.56, 0.62, 0.04, 9.7]
uk_names = ["Edinburgh", "Glasglow", "Stirling", "London"]
china_cities = [0.58, 8.4, 29.9, 22.2]
china_names = ["Haining", "Hangzhou", "Shanghai", "Beijing"]

plt.figure()
plt.subplot(2,1,1)
plt.bar(uk_names, uk_cities)
plt.title("Population of UK cities in 2024")
plt.xlabel("Cities in UK")
plt.ylabel("Population (in million)")

plt.subplot(2,1,2)
plt.bar(china_names, china_cities)
plt.title("Population of China cities in 2024")
plt.xlabel("Cities in china")
plt.ylabel("Population (in million)")
plt.tight_layout()
plt.show()
plt.clf()

