import pytest

from app import MOCKED_RESPONSES, app


@pytest.fixture
def client():
    return app.test_client()


def test_default_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Dash MockServer is up and running."


@pytest.mark.parametrize(
    ("path", "filename"),
    [
        ("/openweatherapi/weather?q=Paris", "openweatherapi/weather_paris.json"),
        ("/openweatherapi/forecast?q=Paris", "openweatherapi/forecast_paris.json"),
        ("/steam/ISteamUser/GetPlayerSummaries/v0002/", "steam/playerData.json"),
        ("/steam/IPlayerService/GetOwnedGames/v0001/", "steam/ownedGames.json"),
        ("/steam/ISteamUserStats/GetPlayerAchievements/v0001/", "steam/halfLife2Episode2Stats.json"),
        ("/strava/oauth/token", "strava/stravaTokenResponse.json"),
        ("/strava/api/v3/athlete/activities?page=1", "strava/stravaActivitiesData.json"),
        ("/strava/api/v3/athlete", "strava/stravaAthleteData.json"),
        ("/airParif/commune/75056", "airParif/airParifForecastResponse.json"),
        ("/airParif/couleurs", "airParif/airParifColorsResponse.json"),
    ],
)
@pytest.mark.parametrize("method", ["GET", "POST"])
def test_mocked_routes(client, method, path, filename):
    response = client.open(path, method=method)
    assert response.status_code == 200
    assert response.mimetype == "application/json"
    with open(f"static/{filename}", "rb") as expected:
        assert response.data == expected.read()


def test_every_mocked_file_exists():
    for _, filename in MOCKED_RESPONSES:
        with open(f"static/{filename}", "rb"):
            pass


def test_unknown_route(client):
    response = client.get("/unknown")
    assert response.text == "Not found"
