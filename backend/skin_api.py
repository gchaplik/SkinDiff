from fastapi import FastAPI, HTTPException
import requests

"""
To run server, go into terminal, and run fastapi dev skin_api.py
For endpoint requests, go the url in the terminal, i.e 127.0.0.0/8000 and add the endpoint and params such as /champions/skins/kalista
For the /champions endpoint, no data is required to be passed
"""

# Define constants
app = FastAPI()
CHAMP_URL = r'https://ddragon.leagueoflegends.com/cdn/14.10.1/data/en_US/champion.json'
SKIN_URL = r'https://ddragon.leagueoflegends.com/cdn/14.10.1/data/en_US/champion/'
IMAGE_URL = r'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/'

# Retrieve champion names
def get_league_champs():
    response_json = requests.get(CHAMP_URL).json()
    champion_names = list(response_json['data'].keys())
    return champion_names

def get_champ_skins(champion: str):
    champion_names = get_league_champs()
    # For champs like drmundo, we can pass in drmundo or Drmundo and expect to get skins
    split_name = champion.split(" ")
    champion_validated = ''.join([name.title() for name in split_name])
    # Check if champion is valid
    if champion_validated not in champion_names:
        raise HTTPException(status_code=400, detail="Invalid Champ Name Provided")

    skin_url_champ = SKIN_URL + f'{champion_validated}.json'
    request_skins_champ = requests.get(skin_url_champ).json()
    champ_skin_data = request_skins_champ['data'][champion_validated]['skins']

    skin_names = {skin['name']: {"splash": f'{IMAGE_URL + champion_validated}_{skin["num"]}.jpg', "id":skin['num']} for skin in champ_skin_data if skin['name']!='default'}

    return {'Total Skins':len(skin_names), champion_validated:skin_names}

@app.get("/champions/skins/{champ_name}")
def get_skin_data(champ_name:str):
    return get_champ_skins(champion=champ_name)

@app.get("/champions")
def get_champ_names():
    return get_league_champs()