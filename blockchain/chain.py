import hashlib
from block import Block

class Chain():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.pool = []

    def proof_of_work(self, block):
        h = hashlib.sha256()
        h.update(str(block).encode('uft-8'))
        return block.h.hexdigest() == h.hexdigest() and int(h.hexdigest(), 16) < 2**(256-self.difficulty) and block.previous_hash == self.blocks[-1].hash

    def add_to_chain(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)
    
    def add_to_pool(self, data):
        self.pool.append(data)
        
    def create_origin_block(self):
        h = hashlib.sha256()
        h.update('utf-8')
        origin = Block("Origin", h)
        origin.mine(self.difficulty)
        self.blocks.append(origin)

    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.add_to_chain(block)

