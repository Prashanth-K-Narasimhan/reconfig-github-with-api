import requests
import json

with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile)
    print("Read successful")
print(type(config))

with open("urls.json", "r") as jsonfile:
    url_list = json.load(jsonfile)
    print("Read successful")
print(type(url_list))

def http_requests(URL, config = config):
    r = requests.get(url = URL, params = config)
    url_response = r.json()
    owner = url_response.get("source").get("full_name")
    print("https://github.com/" + owner)
    return_str = URL + " --> " + owner
    return return_str

response = list(map(lambda x : http_requests(x), url_list))

output_file = open('forked_from.txt','w')
output_file.write('\n'.join(response) + '\n')
output_file.close()
  