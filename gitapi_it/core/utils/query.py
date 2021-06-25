import requests
import json
def run_query(query, token):
      url = "https://api.github.com/graphql"
      headers = {"Authorization": "Bearer " + token}
      request = requests.post(url, json={'query': query}, headers=headers)
      if request.status_code == 200:
        return json.dumps(request.json(), indent=2, sort_keys=True)
      else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))