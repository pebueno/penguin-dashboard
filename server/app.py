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
df = df[df['species'].str.strip() != '']
df = df[df['island'].str.strip() != '']
df = df[df['sex'].str.strip() != '']
df['flipper_length_mm'] = pd.to_numeric(df['flipper_length_mm'], errors='coerce')
df['body_mass_g'] = pd.to_numeric(df['body_mass_g'], errors='coerce')
df.dropna(subset=['flipper_length_mm', 'body_mass_g'], inplace=True)

@app.route('/api/data', methods=['GET', 'POST'])  # Allow both GET and POST
def get_data():
    if request.method == 'POST':
        filters = request.json  # Get the JSON data sent from the frontend
        # Apply filters to the DataFrame based on the request data
        filtered_data = df.copy()

        # Apply filtering based on the filters provided
        if filters.get('species'):
            filtered_data = filtered_data[filtered_data['species'] == filters['species']]
        if filters.get('island'):
            filtered_data = filtered_data[filtered_data['island'] == filters['island']]
        if filters.get('flipper_length_mm'):
            flipper_length_filter = float(filters['flipper_length_mm'])  # Ensure it's a float
            filtered_data = filtered_data[filtered_data['flipper_length_mm'] >= flipper_length_filter]
        if filters.get('body_mass_g'):
            body_mass_filter = float(filters['body_mass_g'])  # Ensure it's a float
            filtered_data = filtered_data[filtered_data['body_mass_g'] >= body_mass_filter]

        # Remove any rows with NaN values before returning
        filtered_data = filtered_data.dropna()
        
        # Convert to dictionary format and return as JSON
        return jsonify(filtered_data.to_dict(orient='records'))
    
    # For GET requests, return all data without NaN values
    valid_data = df.dropna().to_dict(orient='records')
    return jsonify(valid_data)

if __name__ == '__main__':
    app.run(debug=True)
