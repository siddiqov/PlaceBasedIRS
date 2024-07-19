from src.bert_model import process_query as bert_process_query
from src.gpt_model import process_query as gpt_process_query

def process_query(user_query, dataset_path, model_choice):
    if model_choice == 'bert':
        return bert_process_query(user_query, dataset_path)
    elif model_choice == 'gpt':
        return gpt_process_query(user_query, dataset_path)
