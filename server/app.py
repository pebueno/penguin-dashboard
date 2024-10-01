from flask import Flask, jsonify, request
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the dataset
csv_file_path = os.path.join(os.path.dirname(__file__), 'penguins.csv')

# Read the CSV file and clean column names
df = pd.read_csv(csv_file_path)

# Strip whitespace from headers
df.columns = df.columns.str.strip()

# Data preprocessing: remove rows with missing or invalid values
df.dropna(subset=['species', 'island', 'sex'], inplace=True)

# Convert columns to numeric, coercing errors into NaNs
df['flipper_length_mm'] = pd.to_numeric(df['flipper_length_mm'], errors='coerce')
df['body_mass_g'] = pd.to_numeric(df['body_mass_g'], errors='coerce')
df['bill_length_mm'] = pd.to_numeric(df['bill_length_mm'], errors='coerce')
df['bill_depth_mm'] = pd.to_numeric(df['bill_depth_mm'], errors='coerce')

# Drop rows with NaN values in specific columns
df.dropna(subset=['flipper_length_mm', 'body_mass_g', 'bill_length_mm', 'bill_depth_mm'], inplace=True)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
