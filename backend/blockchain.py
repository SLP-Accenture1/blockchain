import hashlib
import time
import pickle
import json

class Blockchain:
    def __init__(self, name : str):
        # Initialise blockchain with genesis data
        self.name = name
        self.chain = []
        self.cache = {
            'previous_hash' : 0,
            'data' : [],
            'proof' : 1
            }

    def __repr__(self) -> str:
        # To print class description
        return 'Blockchain Object of length ' + len(self.chain)

    def __str__(self) -> str:
        # Print contents of blockchain
        return json.dumps(self.chain, sort_keys=True, indent=2)

    def add_cache(self, data : dict):
        data['timestamp'] = str(time.time())
        self.cache['data'].append(data)

    def create_block(self):
        # Append cached block to chain
        if len(self.chain) != 0:
            self.cache['previous_hash'] = self.hash_block(self.chain[-1])
        self.mine_proof(self.cache)

        self.chain.append(self.cache.copy())
        self.broadcast()

        # Clear cache
        self.cache['data'] = []
        self.cache.clear()
        self.cache = {
            'previous_hash' : 0,
            'data' : [],
            'proof' : 1
            }

    def hash_block(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def mine_proof(self, block : dict):
        data = self.chain[-1]['proof'] if len(self.chain) > 0 else 0
        block['proof'] = 1
        check_proof = False

        while check_proof is False:
            block['proof']**2 - data**2
            hash_operation = self.hash_block(block)
            # print('Trying ', block['proof'], ': ', hash_operation)
            if hash_operation[:2] == '00':
                check_proof = True
            else:
                block['proof'] += 1
        

    def save_blockchain(self):
        with open('logs/' + self.name + '.bc', 'wb') as f:
            pickle.dump(self, f)

    # def verify(self):
    #     previous_block = self.chain[0]
    #     i = 1
		
    #     while i < len(self.chain):
    #         block = self.chain[i]
    #         if block['previous_hash'] != self.hash(previous_block):
    #             return False
			
    #         previous_proof = previous_block['proof']
    #         proof = block['proof']
    #         hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2)).encode().hexdigest()
			
    #         if hash_operation[:4] != '00000':
    #             raise Exception('Blockchain has been tampered')
    #         previous_block = block
    #         i += 1
		
    #     print('Blockchain is verified')
    #     return True

    def broadcast(self):
        pass


def load_blockchain(name: str):
    with open(name, 'rb') as f:
        return pickle.load(f)