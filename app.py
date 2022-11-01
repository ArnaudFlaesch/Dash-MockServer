from flask import Flask, current_app

app = Flask(__name__)

@app.route("/")
def default_route():
    return "Dash MockServer is up and running."


@app.route('/<path:text>', methods=['GET'])
def all_routes(text):

    # OPENWEATHERAPI
    if 'openweatherapi/weather' in text :
       return current_app.send_static_file("openweatherapi/weather_paris.json")
    elif 'openweatherapi/forecast' in text :
        return current_app.send_static_file("openweatherapi/forecast_paris.json")

    # STEAM
    elif "steam/ISteamUser/GetPlayerSummaries/v0002/" in text :
        return current_app.send_static_file("steam/playerData.json")

    elif 'steam/IPlayerService/GetOwnedGames/v0001/' in text :
        return current_app.send_static_file("steam/ownedGames.json")

    elif 'steam/ISteamUserStats/GetPlayerAchievements/v0001' in text :
        return current_app.send_static_file("steam/halfLife2Episode2Stats.json")

    # STRAVA
    elif 'strava/oauth/token' in text :
        return current_app.send_static_file("strava/stravaTokenResponse.json")

    elif 'strava/api/v3/athlete/activities' in text :
        return current_app.send_static_file("strava/stravaAthleteData.json")

    elif 'strava/api/v3/athlete' in text :
        return current_app.send_static_file("strava/stravaActivitiesData.json")

    # AIRPARIF
    elif 'airParif/commune/<insee>' in text :
        return current_app.send_static_file("airParif/airParifForecastResponse.json")

    elif 'airParif/couleurs' in text :
        return current_app.send_static_file("airParif/airParifColorsResponse.json")

    else:
        return "Not found"