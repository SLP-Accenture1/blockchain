from ctypes import create_string_buffer
import hashlib
import datetime
import pickle

class Blockchain:
    def __init__(self, genesis_data):
        self.chain = []
        self.create_block(genesis_data)

    def __repr__(self) -> str:
        return 'Blockchain Object'

    def __str__(self) -> str:
        return self.chain

    def create_block(self, proof, data):
        block = data{'index': len(self.chain) + 1,
				'timestamp': str(datetime.datetime.now()),
				'proof': proof,
				'previous_hash': hashlib.sha256(self.chain[-1])
                }
        self.chain.append(block)

    def save_block(self):
        with open('logs/maintainance', 'wb') as f:
            pickle.dump(self, f)

    def check():
        pass