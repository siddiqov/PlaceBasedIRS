import re

def process_query(user_query, dataset_file):
    with open(dataset_file, 'r', encoding='utf-8') as f:
        dataset = f.read()

    hotel_entries = dataset.split("\n\n")
    results = []

    for entry in hotel_entries:
        if contains_keywords(entry, user_query):
            results.append(format_hotel_entry(entry))

    if results:
        return "\n\n".join(results)
    else:
        return "No relevant information found."

def contains_keywords(entry, user_query):
    keywords = user_query.split()
    for keyword in keywords:
        if re.search(r'\b{}\b'.format(re.escape(keyword)), entry, re.IGNORECASE):
            return True
    return False

def format_hotel_entry(entry):
    return entry.strip()
