import json
import os
"""
->Function: update_cache
    Determines if file exists: append, if not write
    Updates the users local cache
->Parameters:
key: String
    json key
val: String
    json value
->Returns:
N/A
"""
def update_cache(key,val):
    json_file = 'cache.json'

    # Check if file exists
    # If file exists, load json as string
    # Append new key or overwrite existing key
    if os.path.exists(json_file):
        
        with open(json_file) as json_file:
            json_decoded = json.load(json_file)

        json_decoded[key] = val

        # Cannot use json_file variable, pointer issue
        with open('cache.json', 'w') as json_file:
            json.dump(json_decoded, json_file)

    # If file does not exist, (+)create and (w)rite to file
    else:
        data = {key: val}
        with open(json_file, 'w+') as outfile:
            json.dump(data, outfile)