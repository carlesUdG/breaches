import json
import requests
import re
from app.views import APP

def list_routes():
    return ['%s' % rule for rule in APP.url_map.iter_rules()]

def test_index():

    response = requests.get('http://localhost:5000/api/version')
    assert response.status_code == 200

def test_content_type():

    routes = list_routes()

    for route in routes:
        response = requests.get('http://localhost:5000/%s' % route)
        assert response.headers['Content-Type'] == 'application/json'
        
        json_response = json.loads(response.content)
        assert type(json_response) == dict or type(json_response) == list

def test_version_commit():

    response = requests.get('http://localhost:5000/api/version')
    json_response = json.loads(response.content)

    contains_version = 'version' in json_response.keys()

    assert contains_version == True

    commit_sha = json_response['version']

    assert re.search(r'[a-z0-9]{40}', commit_sha)

