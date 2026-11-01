"""Mock server returning canned JSON responses for the external APIs used by Dash."""

from flask import Flask

app = Flask(__name__)

DEFAULT_MESSAGE = "Dash MockServer is up and running."
NOT_FOUND_MESSAGE = "Not found"

# Matched in order against the request path: the first fragment found wins,
# so more specific fragments must come before the ones they contain.
MOCKED_RESPONSES: tuple[tuple[str, str], ...] = (
    # OpenWeather
    ("openweatherapi/weather", "openweatherapi/weather_paris.json"),
    ("openweatherapi/forecast", "openweatherapi/forecast_paris.json"),
    # Steam
    ("steam/ISteamUser/GetPlayerSummaries/v0002/", "steam/playerData.json"),
    ("steam/IPlayerService/GetOwnedGames/v0001/", "steam/ownedGames.json"),
    ("steam/ISteamUserStats/GetPlayerAchievements/v0001", "steam/halfLife2Episode2Stats.json"),
    # Strava
    ("strava/oauth/token", "strava/stravaTokenResponse.json"),
    ("strava/api/v3/athlete/activities", "strava/stravaActivitiesData.json"),
    ("strava/api/v3/athlete", "strava/stravaAthleteData.json"),
    # Airparif
    ("airParif/commune", "airParif/airParifForecastResponse.json"),
    ("airParif/couleurs", "airParif/airParifColorsResponse.json"),
)


def find_mocked_file(path: str) -> str | None:
    """Return the static file mocking ``path``, or None if no fragment matches."""
    return next((filename for fragment, filename in MOCKED_RESPONSES if fragment in path), None)


@app.get("/")
def default_route():
    return DEFAULT_MESSAGE


@app.route("/<path:path>", methods=["GET", "POST"])
def mocked_route(path: str):
    filename = find_mocked_file(path)
    if filename is None:
        return NOT_FOUND_MESSAGE
    return app.send_static_file(filename)
