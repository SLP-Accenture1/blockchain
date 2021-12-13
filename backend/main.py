from blockchain import Blockchain, load_blockchain
from flask import Flask
from flask_cors import CORS

details1 = {
    'Manufacturer' : 'Airbus',
    'Parts' : '221839y3192',
    'Description' : 'd',
    'Serial Number' : '9e2h92hf3r0u0',
    'Date of Manufacture' : '21-12-2004',
    'Cycles since last check' : 299,
}

details2 = {
    'Manufacturer' : 'Boeing',
    'Parts' : '221839y3192',
    'Description' : 'd',
    'Serial Number' : '9e2h92hf3r0u0',
    'Date of Manufacture' : '21-12-2005',
    'Cycles since last check' : 299,
}

NAME = 'Aircraft Maintainance'


try:
    block1 = load_blockchain('logs/' + NAME + '.bc')
    print('Loading Blockchain: ', NAME)
    # block1.verify()
except FileNotFoundError:
    print('Creating Blockchain: ', NAME)
    block1 = Blockchain(NAME)

print(block1)

# ==============================================================
'''
def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)

@APP.route('/auth/login/v2', methods=['POST'])
def login():
    data = request.get_json()
    auth_user_id = auth_login_v1(
        data['email'],
        data['password'],
        )
    return dumps({
        'token' : new_token(auth_user_id),
        'auth_user_id' : auth_user_id,
    })
'''

# ==============================================================
# Edit blockchain
block1.add_cache(details2)
block1.create_block()

print(block1)

block1.save_blockchain()