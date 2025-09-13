import pandas as pd

# =====Squirrel Fur Color Counter=====
# Script to analyze Central Park squirrel census CSV:
# - Counts squirrels by primary fur color
# - Outputs results to a clean CSV for client consumption

data = pd.read_csv("./input_samples/squirrel_data_sample.csv")

# --- Count by fur color & clean labels ---
color_count = data["Primary Fur Color"].value_counts()
color_count_df = color_count.rename_axis("Fur Color").reset_index(name="Count")

# --- Save results ---
color_count_df.to_csv("./outputs/squirrel_count.csv", index=False)
print("Squirrel fur color counts saved to ./outputs/squirrel_count.csv")