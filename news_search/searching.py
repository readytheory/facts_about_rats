from config import Config
import requests
import json


def search(searchstring):
    c = Config()
    apikey = c.app_settings["api_key"]
    apiurl = c.app_settings["query_url"]

    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': apikey
    }

    querystring = {"autoCorrect":"false",
                   "pageNumber":"1",
                   "pageSize":"25",
                   "q": searchstring,
                   "safeSearch": "false",
    }


    try:
        response = requests.request("GET", apiurl, headers=headers, params=querystring)
        return json.loads(response.text)['value']
    except:
        return [{'There was a failure'}]

#--------- 


# querystring = {"autoCorrect":"false",
#               "pageNumber":"1",
#               "pageSize":"25",
#               "q":"'long ball' -homer -run -bases",
#               "safeSearch":"false",
#               "fromPublishedDate": '2000-01-01',
#               "toPublishedDate": '2015-12-31',}


# response = requests.request("GET", url, headers=headers, params=querystring)
# news_dict = json.loads(response.text)
