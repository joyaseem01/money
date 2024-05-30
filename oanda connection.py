import pandas as pd
import tpqoa
import matplotlib.pyplot as plt
from Supertrend import Supertrend
import pandas_ta as pdta

api = tpqoa.tpqoa("oanda.cfg")

print(api.get_account_summary())

df = api.get_history(instrument = "EUR_USD", start = "2024-02-01", end = "2024-02-02",
                granularity = "M1", price = "B")

# df.info()

# df.to_csv('output.csv', index=True)

# print(df.count())

# print(df.c)

# print(df.index)

df.c.shift(1)

print(df.iloc[5])

# df["upperband"] = Supertrend().calculate_supertrend(df)[0]
# df["lowerband"] = Supertrend().calculate_supertrend(df)[1]

# plt.plot(df.index, df.c, label='close')
# plt.plot(df.index, df.upperband, label='upper')
# plt.plot(df.index, df.lowerband, label='lower')

# for current in range(1,len(df.index)):
#     previous = df.iloc[current] - 1
#     if df.iloc[current].c > df.iloc[previous].upperband:

lenght = 3
# for current in range(0,len(df.index)):
#     df["supertrend"] = pdta.supertrend(high=df.iloc[current-lenght:current].h,low=df.iloc[current-lenght:current].l,close=df.iloc[current-lenght:current].c,length=lenght,multiplier=3)

st = pdta.supertrend(high=df["h"],low=df["l"],close=df["c"],length=7,multiplier=3)

plt.plot(df.index, df.c, label='close')
plt.plot(df.index,st["SUPERT_7_3.0"], label='upper')



print(df)



