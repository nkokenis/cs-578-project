import json

"""
->Function: update_cache
    Updates the users local cache
->Parameters:
key: String
    json key
val: T
    json value
->Returns:
N/A
"""
def update_cahce(key,val):
    with open('cache.json') as infile:
            data = json.load(infile)
            data[key][val]
    with open('cache.json', 'w') as outfile:
        json.dump(data, outfile)