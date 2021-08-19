# from example in Collab
# load pandas package
import matplotlib.pyplot as plt
import pandas as pd

# Part 1: read data into data frame
df = pd.read_csv("owid-covid-data.csv")

# Part 2: select only data from US
df = df[ df.location == "United States" ]


# Part 3: make a multiline plot
# df.plot.line(x="date", y="people_fully_vaccinated_per_hundred")
# # df.plot.line( y="hosp_patients_per_million")
# plt.show()

plt.plot('date',"people_fully_vaccinated_per_hundred", data=df, marker='', color='blue', linewidth=2)
plt.plot('date',"hosp_patients_per_million", data=df, marker='', color='red', linewidth=2)
plt.legend()
plt.show()
