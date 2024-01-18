import rsa
from rsa.key import PublicKey, PrivateKey

from base.base_crypto import CryptoSettings


class Crypto(CryptoSettings):
    @staticmethod
    def encode(text):
        message = text.encode('utf8')
        pub_key = PublicKey()
        crypto = rsa.encrypt(message, pub_key)
        return crypto

    @staticmethod
    def decode(crypto):
        priv_key = PrivateKey(CryptoSettings.N, CryptoSettings.E, CryptoSettings.D, CryptoSettings.P, CryptoSettings.Q)
        message = rsa.decrypt(crypto, priv_key)
        return message.decode('utf8')
