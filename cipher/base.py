# IGNORE THIS FOR NOW, WE MAY GO ON TO TURN THE CIPHERS INTO CLASSES
# BUT IT MAY BE UNNECESSARY

from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self):
        super().__init__()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    @abstractmethod
    def encrypt(self, text, key):
        pass

    @abstractmethod
    def decrypt(self, text, key):
        pass

    