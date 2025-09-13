import pandas as pd
import os

# === Weather Data Analyzer ===
# Script to clean and analyze weather CSV data:
# - Computes average & max temperature
# - Retrieves rows by condition (e.g. Monday, hottest day)
# - Safely handles invalid or missing values (NaN)
# - Outputs summary metrics to CSV for client consumption

print("\n=== Weather Data Analyzer ===\n")

# --- Load & preprocess dataset ---
data = pd.read_csv("input_samples/weather_data.csv")
data.columns = [c.lower() for c in data.columns]  # Normalize headers to lowercase
data["temp"] = pd.to_numeric(data["temp"], errors="coerce")  # Coerce bad values → NaN

# --- Guard: ensure we have valid numeric temperatures ---
clean = data["temp"].dropna()
if clean.empty:
    print("No valid temperatures in the dataset.")
    # Still produce an output file so the run is auditable
    os.makedirs("outputs", exist_ok=True)
    pd.DataFrame({"metric": ["avg_temp_pandas", "max_temp"], "value": ["", ""]}).to_csv(
        "outputs/new_data.csv", index=False
    )
    print("\nSummary metrics saved to ./outputs/new_data.csv")
    raise SystemExit(0)                   # Early exit: stop execution if no valid temps (output file already written)

# --- Key statistics ---
print(f"Average temperature : {clean.mean():.2f}")
print(f"Highest Temperature : {clean.max()}")

# --- Filtered rows ---
print("\nRow(s) where day=Monday:\n", data[data["day"].str.lower() == "monday"])
print("\nRow with highest temperature:\n", data[data["temp"] == clean.max()])

# --- Monday-specific conversion ---
monday = data[data["day"].str.lower() == "monday"]
# Guard: only convert if Monday exists in dataset AND its temp value is valid
if not monday.empty and pd.notna(monday["temp"].iloc[0]):
    monday_temp_f = monday["temp"].iloc[0] * 9 / 5 + 32
    print(f"\nMonday's temperature in Fahrenheit : {monday_temp_f:.2f}")
else:
    print("Monday not found in dataset or temperature missing")

# --- Output metrics to CSV ---
summary = pd.DataFrame(
    {
        "metric": ["avg_temp_pandas", "max_temp"],
        "value": [round(float(clean.mean()), 2), float(clean.max())],
    }
)
os.makedirs("outputs", exist_ok=True)  # Ensure output folder exists
summary.to_csv("outputs/new_data.csv", index=False)
print("\nSummary metrics saved to outputs/new_data.csv")