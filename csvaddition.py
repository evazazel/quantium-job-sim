# %%
import pandas as pd
import glob
import os
# %% combine csvs
# Path to your CSVs
path = r"D:\gradjobs\quantium\quantium-job-sim\cleaned_data\*.csv"

# Read and combine all CSVs
df = pd.concat([pd.read_csv(f) for f in glob.glob(path)], ignore_index=True)

# Save the combined file
df.to_csv(r"D:\gradjobs\quantium\quantium-job-sim\cleaned_data\combined_cleaned_sales_data.csv", index=False)


# %%
