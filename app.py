from flask import Flask

app = Flask(__name__)

# Matched in order against the request path: the first fragment found wins,
# so more specific fragments must come before the ones they contain.
MOCKED_RESPONSES = (
    # OPENWEATHERAPI
    ("openweatherapi/weather", "openweatherapi/weather_paris.json"),
    ("openweatherapi/forecast", "openweatherapi/forecast_paris.json"),
    # STEAM
    ("steam/ISteamUser/GetPlayerSummaries/v0002/", "steam/playerData.json"),
    ("steam/IPlayerService/GetOwnedGames/v0001/", "steam/ownedGames.json"),
    ("steam/ISteamUserStats/GetPlayerAchievements/v0001", "steam/halfLife2Episode2Stats.json"),
    # STRAVA
    ("strava/oauth/token", "strava/stravaTokenResponse.json"),
    ("strava/api/v3/athlete/activities", "strava/stravaActivitiesData.json"),
    ("strava/api/v3/athlete", "strava/stravaAthleteData.json"),
    # AIRPARIF
    ("airParif/commune", "airParif/airParifForecastResponse.json"),
    ("airParif/couleurs", "airParif/airParifColorsResponse.json"),
)


@app.get("/")
def default_route():
    return "Dash MockServer is up and running."


@app.route("/<path:path>", methods=["GET", "POST"])
def mocked_route(path):
    for fragment, filename in MOCKED_RESPONSES:
        if fragment in path:
            return app.send_static_file(filename)
    return "Not found"
