import requests

#requests.get    # select
#requests.post   # create
#requests.put    # update
#requests.delete # delete

url = "https://www.pokeapi.co/api/v2/pokemon/25"
response = requests.get(url)
data = response.json()
data_types = data['types']
types_list = []
for type_info in data_types:
    types_list.append(type_info['type']['name'])
types = ', '.join(types_list)
print(data['name'], types)



