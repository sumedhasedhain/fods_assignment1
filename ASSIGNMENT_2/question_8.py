''' Program that holds the average daily temperature for each day of the week
'''

def add_daily_temp(temp_dict, temperature, day):
    if day not in temp_dict:
        temp_dict[day] = temperature  
    return temp_dict

daily_temperatures = {}

daily_temperatures = add_daily_temp(daily_temperatures, 80, 'Monday')
print(daily_temperatures)  

daily_temperatures = add_daily_temp(daily_temperatures, 80, 'Monday')
print(daily_temperatures)  

daily_temperatures = add_daily_temp(daily_temperatures, 70, 'Tuesday')
print(daily_temperatures) 
