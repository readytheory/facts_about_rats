from config import Config
import requests

def search(searchstring):
    c = Config()
    apikey = c.apikey
    apiurl = c.query_url
    results = [ {'turn': 'now', 'ear': 'o1', 'fin': 'wake', 'x': 3},
            {'ear': 'o2', 'bite' : ['dog', 'dentist', 'bee']},
            {'portly': 1, 'ear': 'o3d'},]
    return results


    
    
