from flask import Flask, request, render_template, send_file
import os
from dotenv import load_dotenv
from src.web_scraping import scrape_and_save_to_pdf  # Correct import statement
from src.bert_model import bert_process_query
from src.gpt_model import gpt_process_query
# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

# Path to dataset (assuming it's in the artifacts folder)
dataset_path = os.path.join('PlaceBasedIRS', 'artifacts', 'dataset.txt')

# Accessing OpenAI API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query']
    model_choice = request.form['model_choice']
    
    if model_choice == 'bert':
        result = bert_process_query(user_query, dataset_path, model_choice='bert')
    elif model_choice == 'gpt':
        result = gpt_process_query(user_query)  # Use OpenAI GPT model
        # Example usage of OpenAI GPT model API
        # Uncomment and adjust as needed
        # result = process_openai_gpt(user_query)
    
    return render_template('query_result.html', result=result)

@app.route('/scrape_and_download', methods=['GET'])
def scrape_and_download():
    url = "https://www.ihg.com/intercontinental/hotels/us/en/reservation"
    output_file = "hotel_info.pdf"
    if scrape_and_save_to_pdf(url, output_file):
        return send_file(output_file, as_attachment=True)
    else:
        return "Failed to scrape data and create PDF."

if __name__ == '__main__':
    app.run(debug=True)
