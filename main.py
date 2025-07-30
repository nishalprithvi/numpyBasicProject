import numpy as np 

# creating random data for the month 
print("Daily Temperature Analysis and Tracking")
temperatures = np.random.randint(15, 36, size=(30,))
print("\nTotal no of days : ", len(temperatures))
print("Temperature recorded in : Celsius (°C)")
print("Temperatures recorded on each day of month : \n", temperatures)

print("-"*30)
# Calculating Aggregations
avg = np.mean(temperatures)
maxTemp = np.max(temperatures)
minTemp = np.min(temperatures)
stdDev = np.std(temperatures)

print("The Average temperature for the month : ",avg)
print("Maximum Temperature for the month : ",maxTemp)
print("Minimum Temperature for the month : ", minTemp)
print("Standard Deviation of the Temperature throughout the month : ", stdDev)
print("-"*30)

# Converting Temperatures to Farenheit, Broadcasting

fah_temp = (temperatures * 1.8) + 32
print("Temperatures in Fahrenheit (°F) : \n", fah_temp)
print("-"*30)

# Hot & Cold days Analysis 

print("Hot Days (> 30°C), Cold Days (< 20°C)")
hot_days = temperatures[temperatures > 30]
cold_days = temperatures[temperatures < 20]
print("Number of Hot days : ",len(hot_days))
print("Hot Days dates : \n", (np.where(temperatures > 30)[0] + 1))
print("Temp on Hot days : ",hot_days)
print("Number of Cold days : ", len(cold_days))
print("Cold Days dates : \n", (np.where(temperatures < 20)[0] + 1))
print("Temp on Cold days : ", cold_days)

print("-"*30)

# Weekly Stats 

weeks = np.split(temperatures, [7,14,21,28])
print("\n\nWeekly Stats : - ")

print("week 1 : ", weeks[0])
print("Avg Temp : ", np.mean(weeks[0]))
print("-"*10)
print("week 2 : ", weeks[1])
print("Avg Temp : ", np.mean(weeks[1]))
print("-"*10)
print("week 3 : ", weeks[2])
print("Avg Temp : ", np.mean(weeks[2]))
print("-"*10)
print("week 4 : ", weeks[3])
print("Avg Temp : ", np.mean(weeks[3]))
print("-"*10)