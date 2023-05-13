import unittest
import crypto_lib

class TestStringMethods(unittest.TestCase):

    def test_segment_happycase(self):
        self.assertEqual(
            crypto_lib.segment(bytes.fromhex(
                "76a9141974262d0e27ba2b49e566e6191922cba6bacd1d88ac")),
            [
                'OP_DUP', 
                'OP_HASH160',
                '1974262d0e27ba2b49e566e6191922cba6bacd1d',
                'OP_EQUALVERIFY',
                'OP_CHECKSIG'
            ]
        )
        self.assertEqual(
            crypto_lib.segment(bytes.fromhex(
                "4830450221008ecb5ab06e62a67e320880db70ee8a7020503a055d7c45b73dcc41adf01ea9f602203a0d8f4314342636a6a473fc0b4dd4e49b62be288f0a4d5a23a8f488a768fa9b012103dd8763f8c3db6b77bee743ddafd33c969a99cde9278deb441b09ad7c14cf740f")),
            [
                '30450221008ecb5ab06e62a67e320880db70ee8a7020503a055d7c45b73dcc41adf01ea9f602203a0d8f4314342636a6a473fc0b4dd4e49b62be288f0a4d5a23a8f488a768fa9b01', 
                '03dd8763f8c3db6b77bee743ddafd33c969a99cde9278deb441b09ad7c14cf740f'
            ]
        )


    def test_pubkey_to_address(self):
        # Genesis 
        # 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
        # 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
        # https://www.blockchain.com/btc/address/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
        addr, hash_key, check_sum = crypto_lib.pubkey_to_address("04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f")
        self.assertEqual(addr, "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
        self.assertEqual(hash_key.upper(), "0062E907B15CBF27D5425399EBF6F0FB50EBB88F18")
        self.assertEqual(check_sum.upper(), "C29B7D93")


if __name__ == '__main__':
    unittest.main()