import pandas as pd
import random

numbers=[random.randint(1,100)for i in range(10)]

series=pd.Series(numbers)

print("Pandas series with 10 random numbers : ")
print(series)