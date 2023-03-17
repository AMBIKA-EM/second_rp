"""import pandas as pd
df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)"""

import pandas as pd
df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
print(df['company'].value_counts())

"""import pandas as pd
df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company','price'].max()
print(priceDf)

import pandas as pd
carsDf = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDf.head(5))"""

"""import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)

carsDf3 = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
print(carsDf3)"""

"""import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
print(carsDf)"""

"""import pandas as pd
carsDf = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDf.head(5))"""

