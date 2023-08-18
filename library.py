import rsa


class RSA:
    # (pubkey, privkey) = rsa.newkeys(128)
    e: int
    d: int
    n: int

    def __init__(self, key_bits):
        self.key_bits = key_bits
        self.key_generate()

    def key_generate(self):
        (pubkey, privkey) = rsa.newkeys(self.key_bits)
        self.e = pubkey.e
        self.d = privkey.d
        self.n = pubkey.n

    def encrypt(self, val):
        c = pow(val, self.e, self.n)
        return c

    def decrypt(self, val):
        de = pow(val, self.d, self.n)
        return de

    @staticmethod
    def multiply(val1, val2):
        return val1 * val2


def execute():
    obj = RSA(128)  # for choosing key size
    c1 = obj.encrypt(200)  # encrypting data
    c2 = obj.encrypt(19897)

    # c3 = obj.Multiply(c1, c2)  # multiplying the data
    c3 = RSA.multiply(c1, c2)

    res = obj.decrypt(c3)  # decrypting the data

    print(res)
