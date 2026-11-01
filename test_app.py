from pathlib import Path

import pytest

from app import DEFAULT_MESSAGE, MOCKED_RESPONSES, NOT_FOUND_MESSAGE, app

STATIC_DIR = Path(app.static_folder)
FRAGMENTS = [fragment for fragment, _ in MOCKED_RESPONSES]


@pytest.fixture
def client():
    return app.test_client()


def test_default_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == DEFAULT_MESSAGE


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
    assert response.data == (STATIC_DIR / filename).read_bytes()


@pytest.mark.parametrize("filename", [filename for _, filename in MOCKED_RESPONSES])
def test_mocked_file_exists(filename):
    assert (STATIC_DIR / filename).is_file()


def test_specific_fragments_come_first():
    # A fragment contained in a later one would shadow it, making it unreachable.
    for index, fragment in enumerate(FRAGMENTS):
        shadowed = [later for later in FRAGMENTS[index + 1 :] if fragment in later]
        assert not shadowed, f"{fragment!r} shadows {shadowed}"


@pytest.mark.parametrize("method", ["GET", "POST"])
def test_unknown_route(client, method):
    response = client.open("/unknown", method=method)
    assert response.text == NOT_FOUND_MESSAGE
