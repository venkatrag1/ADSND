import hashlib
from datetime import datetime
import unittest

class Block:
    """
    Description: Represents a Block stored in Block chain, consisting of data, previous hash, current hash and time
    """

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        Calculate block hash

        Args:
          None

        Returns:
           Hash of a string composed of timestamp, new block data, and previous block hash
        """
        sha = hashlib.sha256()

        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return """
        Timestamp: {timestamp}
        Data: {data}
        Previous Hash: {previous_hash}
        Current Hash: {hash}
        """.format(timestamp=self.timestamp,
                   data=self.data,
                   previous_hash=self.previous_hash,
                   hash=self.hash)

class BlockChain(object):
    """
    Description: Block chain object that adds new blocks to ledger
    """
    def __init__(self):
        self.ledger = [self._get_genesis_block()]

    def _get_genesis_block(self):
        """
        Seed block for Block chain

        Args:
          None

        Returns:
           Block with "0" hash
        """
        return Block(datetime.utcnow(), "Genesis Block", "0")

    def append(self, data):
        """
        Add new block to ledger

        Args:
          data: Data to be added to block chain

        Returns:
           None
        """
        prev_block = self.ledger[-1]
        new_block = Block(datetime.utcnow(), data, prev_block.hash)
        self.ledger.append(new_block)

    def __str__(self):
        out_str = ""
        for block in self.ledger:
            out_str += str(block) + "<- "
        return out_str


class TestBlockChain(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def test_case1(self):
        bc = BlockChain()
        bc.append("This is the first block")
        bc.append("This is the second block")
        print(bc)
        """
        Timestamp: 2019-07-02 15:50:59.284294
        Data: Genesis Block
        Previous Hash: 0
        Current Hash: 9f3d40a5f6495247ab21759b0eb1e105113ac52d240de50f7744ffb928f0c5c0
        <- 
        Timestamp: 2019-07-02 15:50:59.284342
        Data: This is the first block
        Previous Hash: 9f3d40a5f6495247ab21759b0eb1e105113ac52d240de50f7744ffb928f0c5c0
        Current Hash: feea1ddfca6921b65fd8c1956d44e4f7def2a4d1dd68605836b73be9139a196c
        <- 
        Timestamp: 2019-07-02 15:50:59.284349
        Data: This is the second block
        Previous Hash: feea1ddfca6921b65fd8c1956d44e4f7def2a4d1dd68605836b73be9139a196c
        Current Hash: f4eda1e15450e3cdc9f2f56b057f5635e40de7b3fb19751bb0915703c1fb7c30
        <- 

        """


    def test_case2_empty_bc(self):
        bc = BlockChain()
        print(bc)
        """
        Timestamp: 2019-07-02 15:50:59.287616
        Data: Genesis Block
        Previous Hash: 0
        Current Hash: 8a8f73f2594a63d225a8f937920c2fabf1e18dbab54c6c0969ae348381f71b6c
        <-         
        """

    def test_case3_same_block_add(self):
        bc = BlockChain()
        bc.append("This is the block")
        bc.append("This is the block")
        bc.append("This is the block")
        bc.append("This is the block")
        print(bc)
        """
        Timestamp: 2019-07-02 16:05:25.617251
        Data: Genesis Block
        Previous Hash: 0
        Current Hash: e6a82e4a438100ce4e1611da0597446e0457545bc283602dabf0a1a0d6fa1c1c
        <- 
        Timestamp: 2019-07-02 16:05:25.617263
        Data: This is the block
        Previous Hash: e6a82e4a438100ce4e1611da0597446e0457545bc283602dabf0a1a0d6fa1c1c
        Current Hash: fa0033f4868d293e98f85f937412c6b401437cd4d6f5f0b6ea53c79b5a41603a
        <- 
        Timestamp: 2019-07-02 16:05:25.617275
        Data: This is the block
        Previous Hash: fa0033f4868d293e98f85f937412c6b401437cd4d6f5f0b6ea53c79b5a41603a
        Current Hash: 7f267dc1f58da6d0e3670c83b147c0814ed59208002edece67eefdf35c238f17
        <- 
        Timestamp: 2019-07-02 16:05:25.617280
        Data: This is the block
        Previous Hash: 7f267dc1f58da6d0e3670c83b147c0814ed59208002edece67eefdf35c238f17
        Current Hash: 333a831a71cd010867433fc667fba6cfe3219e32b574fb94d995a26357d79ab1
        <- 
        Timestamp: 2019-07-02 16:05:25.617284
        Data: This is the block
        Previous Hash: 333a831a71cd010867433fc667fba6cfe3219e32b574fb94d995a26357d79ab1
        Current Hash: a7bcd27432e2c72e349de52089f0e7eae0b6088516fd83f7084b1a844a429a7b
        <- 

        """
if __name__ == '__main__':
    unittest.main()






