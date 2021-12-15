from blockchain import Blockchain, load_blockchain

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

# Edit blockchain
block1.add_cache(details2)
block1.create_block()

print(block1)

block1.save_blockchain()