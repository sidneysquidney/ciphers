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

    