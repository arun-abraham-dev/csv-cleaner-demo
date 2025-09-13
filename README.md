# CSV Cleaner Demo

A simple repository showcasing how to clean and analyze CSV data using **Python** and **pandas**.  
Contains two small example projects:

- **Weather Data Analyzer** → computes average & max temperatures, finds rows of interest (e.g. Monday, hottest day), and outputs summary metrics.  
- **Squirrel Fur Color Counter** → counts squirrels by primary fur color from Central Park census data and outputs a clean summary.

---

## Project Structure
csv-cleaner-demo/
├── squirrel_counter.py             - Counts squirrel fur colors from census data
├── weather_analyzer.py             - Analyzes daily weather data
├── input_samples/                  - Sample CSV files for testing
│   ├── squirrel_data_sample.csv
│   └── weather_data.csv
├── outputs/                        - Results saved here after running scripts
│   ├── squirrel_count.csv          - Squirrel Counts
│   └── new_data.csv                - Weather Metrics
└── README.md

---

## Requirements

- Python 3.8+
- [pandas](https://pandas.pydata.org/)  

Install dependencies:
```bash
pip install pandas
```

## Usage

Run each script directly from the project root:

### Weather Analyzer
```
python weather_analyzer.py
```
- Computes average & max temperature
- Finds rows where day = Monday and the hottest day
- Converts Monday’s temperature to Fahrenheit
- Saves metrics to outputs/new_data.csv


Example output (new_data.csv):
```
metric,value
avg_temp_pandas,17.43
max_temp,24.0
```

---

### Squirrel Fur Color Counter
```
python squirrel_counter.py
```
- Counts squirrels by primary fur color
- Outputs results to outputs/squirrel_count.csv


Example output (squirrel_count.csv):
```
Fur Color,Count
Gray,2473
Cinnamon,392
Black,103
```

---

## Notes

- Scripts handle invalid values (NaN) safely.
- Output files are always written to the outputs/ folder for consistency.
- This repo is introductory and focuses on clean, beginner-friendly pandas usage.



---

## License

This project is licensed under the MIT License.

---