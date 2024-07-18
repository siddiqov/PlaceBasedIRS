# query_processor.py

import re

def process_query(user_query, dataset_file):
    with open(dataset_file, 'r', encoding='utf-8') as f:
        dataset = f.read()

    # Split the dataset into individual hotel entries
    hotel_entries = dataset.split("\n\n")

    results = []

    # Iterate through each hotel entry to find relevant details
    for entry in hotel_entries:
        if contains_keywords(entry, user_query):
            # Extract only relevant information about dinner times
            dinner_info = extract_dinner_info(entry)
            if dinner_info:
                results.append(dinner_info)

    # Format and return the response
    if results:
        return "\n\n".join(results)
    else:
        return "No relevant information found."

def contains_keywords(entry, user_query):
    keywords = ['radisson', 'dinner', 'time', 'served']  # Adjust as necessary
    for keyword in keywords:
        if re.search(r'\b{}\b'.format(re.escape(keyword)), entry, re.IGNORECASE):
            return True
    return False

def extract_dinner_info(entry):
    # Use regex or simple string parsing to extract dinner time information
    dinner_pattern = r'Dinner.*?(\d{1,2}(:\d{2})?\s?(AM|PM))'
    match = re.search(dinner_pattern, entry, re.IGNORECASE)
    if match:
        return match.group(0)
    return None
