import json
import pandas as pd
import numpy as np

# Load JSON data
file_path = "C:\\Users\\BharathwajSoundarara\\Downloads\\fir-demo-4a5b4-default-rtdb-months-export.json"
with open(file_path, 'r') as f:
    data = json.load(f)

# Extracting relevant data for each month and calculate correlation between attendance/behavior and academic performance
monthly_correlations = {}

# Process each month
for month, month_data in data.items():
    if 'result' in month_data:
        # Extract data for each student in the month
        results = month_data['result']
        month_df = pd.DataFrame(results).T
        
        # Ensure necessary columns are present and convert to numeric, handling non-numeric gracefully
        for col in ['Attendance', 'Behavior', 'AcademicOverall']:
            if col in month_df.columns:
                month_df[col] = pd.to_numeric(month_df[col], errors='coerce')
        
        # Calculate correlation, handling missing values
        attendance_correlation = month_df['Attendance'].corr(month_df['AcademicOverall'])
        behavior_correlation = month_df['Behavior'].corr(month_df['AcademicOverall'])
        
        # Store results
        monthly_correlations[month] = {
            'Attendance vs AcademicOverall': attendance_correlation,
            'Behavior vs AcademicOverall': behavior_correlation
        }

print(monthly_correlations)

