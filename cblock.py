from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class SomeClass:
    string = None

    def __init__(self, my_string):
        self.string = my_string

    def __repr__(self):
        return self.string


class CBlock:
    data = None
    previous_block = None
    previous_hash = None

    def __init__(self, data, previous_block):
        self.data = data
        self.previous_block = previous_block
        if previous_block is not None:
            self.previous_hash = previous_block.compute_hash()

    def compute_hash(self):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(bytes(str(self.data), 'utf8'))
        digest.update(bytes(str(self.previous_hash), 'utf8'))
        return digest.finalize()

