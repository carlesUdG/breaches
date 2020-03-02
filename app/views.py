from flask import Flask, Response
import json

APP = Flask(__name__, static_folder=None)

@APP.route('/api/version', methods=['GET'])
def version():
    commit_sha = open('version.txt','r').read()
    commit_sha = commit_sha.strip('\n')
    return Response(response=json.dumps({'version': commit_sha}), content_type='application/json')

def list_routes():
    return ['%s' % rule for rule in APP.url_map.iter_rules()]

@APP.route('/api/routes', methods=['GET'])
def get_routes():
    return Response(response=json.dumps(list_routes()), content_type='application/json')

APP.run(host='0.0.0.0', port=5000)