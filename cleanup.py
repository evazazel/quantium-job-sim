#%% # import packages
import csv
import pandas as pd


# %% read csv
df = pd.read_csv('data\daily_sales_data_2.csv')
df.head
# %% check data types
for i in df:
    print(type(df[i][0]))

# %% filter out pink morsel
pink_df = df[df['product'].str.contains('pink morsel')]
pink_df.head
# %% get rid of dollar symbol
pink_df['price'] = pink_df['price'].str.strip('$')

pink_df.head
# %%convert price and quant into floats
pink_df = pink_df.astype({'price':float, 'quantity':float})
# %% check data types
for i in pink_df:
    print(type(pink_df[i][0]))
pink_df.head
# %% create new column sales = price x quantity 
sales = pink_df['price'] * pink_df['quantity']
pink_df['sale'] = sales
pink_df.head

# %% #drop unnecsary columns, we need just sales, date. region
final_df = pink_df.drop(columns=['product','price','quantity'])
final_df.head
# %% export csv
final_df.to_csv('daily_sales_data_2_cleaned.csv',index=False)
# %%
