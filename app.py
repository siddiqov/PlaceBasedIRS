# app.py

from flask import Flask, request, render_template
import os
from src.query_processor import process_query  # Import process_query from query_processor.py

app = Flask(__name__)

# Path to dataset (assuming it's in the artifacts folder)
dataset_path = os.path.join('PlacedBasedIRS', 'artifacts', 'dataset.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query']
    result = process_query(user_query, dataset_path)  # Use process_query from query_processor.py
    return render_template('query_result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
