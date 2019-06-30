import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)

        sha.update(hash_str)

        return sha.hexdigest()

class BlockChain(object):
    def __init__(self):
        self.ledger = [self._get_genesis_block()]

    def _get_genesis_block(self):
        return Block(0, datetime.utcnow(), "Genesis Block", "0")

    def add_new_entry(self, data):
        prev_block = self.ledger[-1]
        new_block = Block(datetime.utcnow(), data, prev_block.hash)
        self.ledger.append(new_block)






