from blockchain import Blockchain
import pickle

details = {
    'Manufacturer' : 'Airbus',
    'Part' : '221839y3192',
    'Description' : 'd',
    'Serial Number' : '9e2h92hf3r0u0',
    'Date of Manufacture' : '21-12-2004',
    'Cycles since last check' : 299,
    '' : '',
}

# block1 = Blockchain('Aircraft Maintainance log', details)
# block1.save_block()

with open('logs/Aircraft Maintainance log.bc', 'rb') as file:
    block1 = pickle.load(file)
    print(block1)