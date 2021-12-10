import hashlib
import datetime
import pickle
import json

class Blockchain:
    def __init__(self, name : str, genesis_data : dict):
        self.name = name
        self.chain = []
        self.create_block(genesis_data)

    def __repr__(self) -> str:
        return 'Blockchain Object'

    def __str__(self) -> str:
        return str(self.chain)

    def create_block(self, data : dict):
        data['timestamp'] = str(datetime.datetime.now())
        data['previous_hash'] = self.hash_previous()
        data['proof'] = proof(self)
        self.chain.append(data)

    def hash_previous(self):
        prev_block = {} if len(self.chain) == 0 else self.chain[-1]
        encoded_block = json.dumps(prev_block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def save_block(self):
        with open('logs/' + self.name + '.bc', 'wb') as f:
            pickle.dump(self, f)

    def verify():
        pass

def proof(block):
    return 0