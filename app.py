from flask import Flask, current_app

app = Flask(__name__)

@app.route("/")
def default_route():
    return "Dash MockServer is up and running."

@app.route('/openweatherapi/weather/<city>')
def get_weather(city):
   return current_app.send_static_file("openweatherapi/weather_"+city+".json")

@app.route('/openweatherapi/forecast/<city>')
def get_forecast(city):
   return current_app.send_static_file("openweatherapi/forecast_"+city+".json")


@app.route('/steam/playerData')
def get_steam_player_data():
   return current_app.send_static_file("steam/playerData.json")

@app.route('/steam/ownedGames')
def get_steam_owned_games():
   return current_app.send_static_file("steam/ownedGames.json")

@app.route('/steam/achievementsData')
def get_hl2ep2_stats():
   return current_app.send_static_file("steam/halfLife2Episode2Stats.json")


@app.route('/strava/token')
def get_strava_token_reponse():
   return current_app.send_static_file("strava/stravaTokenResponse.json")

@app.route('/strava/athleteData')
def get_strava_athlete_data():
   return current_app.send_static_file("strava/stravaAthleteData.json")

@app.route('/strava/activitiesData')
def get_strava_activities_data():
   return current_app.send_static_file("strava/stravaActivitiesData.json")


@app.route('/airParif/forecast')
def get_airparif_forecast():
   return current_app.send_static_file("airParif/airParifForecastResponse.json")

@app.route('/airParif/colors')
def get_airparif_colors():
   return current_app.send_static_file("airParif/airParifColorsResponse.json")