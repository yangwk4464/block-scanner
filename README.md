This is a simple block scanner.

- Support Segwit block.
- Address has been encoded by Base58.
- Support basic payment methods.   

## block scanner

block scanner implementation written in python3.

- block.py - classes for Blocks, Transactions
- scan.py - Another example to iterate the block.
- crypto_lib.py, crypto_op.py the util and constant required.
- 5megs.dat - first 5 megs from blk00000.dat
- 1M.dat - first 1M from blk00000.dat
- blk01234.001 - first 1.4M from blk01234.dat, segwit enabled.

## Usage

```
>python3 scanner.py blk01234.001
Block:0 Tx:0 Tx_hash:886723399667ca1591161b6e355f1c7c5aada0a229bd30a02cc6269b877d68d1
input - 0000000000000000000000000000000000000000000000000000000000000000:0
0370e8072cfabe6d6d4774135ea41e120e9aac2f7182afb954dff9969862b0addbe08338db9c146cf704000000f09f909f0f4d696e6564206279206c7a783838380000000000000000000000000000000000000000000000000000000000000000000000
output - 1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY:0
['OP_DUP', 'OP_HASH160', 'c825a1ecf2a6830c4401620c3a16f1995057c2ab', 'OP_EQUALVERIFY', 'OP_CHECKSIG']
output - aa21a9ed592d57c4901c098132ac44e8152cf2b0c700dd49a2fdb51f45d91629733fe161:1
['OP_RETURN', 'aa21a9ed592d57c4901c098132ac44e8152cf2b0c700dd49a2fdb51f45d91629733fe161', '0000000000000000']
Block:0 Tx:1 Tx_hash:697af18a115485a0ca683cc2b86f42f8e764cc1e81d8fe2ce297722f332ae9ed
input - 351463c3f240c45ffb330b8185cc62bfb81e773db0060258792e4beb06a7c7aa:0
['3044022028829b175e677bde02e228ce50d41d8b8a168e9ca424d54188edc1e20134e33c022045b1229f0c751b47addde93100d9f24e61f9e97968d1b0a6bea2d1b702aa312a01', '04e7e8eeb1d060e2ae611e2e6253b7948d7c02b7ea7c2dce09d939225a5c39d86553b07acf5073b1dc1e432cdf574d587b2800e0c3d4e43fcb3a1f84bfdf602a1e']
input - f3dca8108d7b5620024df8dc097d7630b60d8877271d5cf20459995739e76d20:1
['3044022053515cf29b39db5f800ad15e8a3e3d307103b47ce9dc42637dd6d79eb7e36d4f0220139ef712cbdab987fa15a61549c4c441eab4c214b1f5df6c19dd81e8e496deb801', '04e7e8eeb1d060e2ae611e2e6253b7948d7c02b7ea7c2dce09d939225a5c39d86553b07acf5073b1dc1e432cdf574d587b2800e0c3d4e43fcb3a1f84bfdf602a1e']
...
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

BSD 3
