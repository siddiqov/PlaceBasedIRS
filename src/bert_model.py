# src/bert_model.py (formerly hotel_query.py)

import re

# Function to process user queries and return relevant information
def process_query(user_query, dataset_file):
    with open(dataset_file, 'r', encoding='utf-8') as f:
        dataset = f.read()

    # Split the dataset into individual hotel entries
    hotel_entries = dataset.split("\n\n")

    results = []

    # Iterate through each hotel entry to find relevant details
    for entry in hotel_entries:
        if contains_keywords(entry, user_query):
            results.append(format_hotel_entry(entry))

    # Format and return the response
    if results:
        return "\n\n".join(results)
    else:
        return "No relevant information found."

# Function to check if a hotel entry contains keywords from user query
def contains_keywords(entry, user_query):
    keywords = ['hotel', 'hotels', 'Aarhus', 'city']  # Modify as necessary
    for keyword in keywords:
        if re.search(r'\b{}\b'.format(re.escape(keyword)), entry, re.IGNORECASE):
            return True
    return False

# Function to format the response with relevant hotel information
def format_hotel_entry(entry):
    # Simple formatting, you can enhance this based on actual data extraction needs
    return entry.strip()  # Basic example, adjust as per actual data extraction
