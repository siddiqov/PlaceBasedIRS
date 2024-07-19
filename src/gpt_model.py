import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')  # Adjust path as needed
load_dotenv(dotenv_path)

# Access OpenAI API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI API client
openai.api_key = openai_api_key

# Function to process user queries using OpenAI's GPT model
def process_query(user_query):
    # Example: Using OpenAI's GPT-3.5 model for completion
    response = openai.Completion.create(
        engine="davinci",  # Specify the model (e.g., davinci, curie, etc.)
        prompt=user_query,
        max_tokens=150  # Adjust as needed based on your response length requirements
    )

    return response.choices[0].text.strip() if response.choices else "No response from model."

# Example function to demonstrate usage
if __name__ == "__main__":
    query = "What time is breakfast served?"
    result = process_query(query)
    print("Response from GPT model:")
    print(result)
