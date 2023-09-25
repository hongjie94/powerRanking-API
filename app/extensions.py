from flask_restx import Api
from flask_pymongo import PyMongo

api = Api()
mongo = PyMongo()

import bz2
from urllib.request import urlopen
from datetime import datetime
# import requests
import json
  

def fetch_games():
    game_id = "ESPORTSTMNT01:1121638"
    path =  f"https://power-rankings-dataset-gprhack.s3.us-west-2.amazonaws.com/athena-ready/games/{game_id}.json.bz2"

    response = requests.get(path)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Decompress the content in memory
    decompressed_data = bz2.decompress(response.content)
    game_data_list = [json.loads(line) for line in decompressed_data.decode('UTF8').split('\n') if line.strip()]

    return game_data_list
    



# @app.route('/')
# def home():
#     data = fetch_games()
 
#     game_info1 = data[0] if data else None
#     game_info2 = data[1] if data else None
#     game_start = data[2] if data else None
#     game_end = data[-2] if data else None
#     game_result = data[-1] if data else None  

#     result = {
#         "game_info1": game_info1,
#         "game_info2": game_info2,
#         "game_start": game_start,
#         "game_end": game_end,
#         "game_result": game_result
#     }
#     return jsonify(result) , 200


   
    # with open("output.json", "w") as json_file:
    #     json.dump(result, json_file, indent=2)
      
       