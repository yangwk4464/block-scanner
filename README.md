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
python3 scanner.py blk01234.001
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

BSD 3
