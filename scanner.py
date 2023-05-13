#!/usr/bin/python
import sys
from block import BlockFile

def main():
  """Print all detail of a specific block file, such as block00000.dat """
  if len(sys.argv) < 2:
    print('Usage: scan.py filename')
  else:
    block_file = BlockFile(sys.argv[1])
    block_counter = 0
    for block in block_file.get_next_block():
      tx_counter = 0
      for tx in block.txs:
        print("Block:%d Tx:%d Tx_hash:%s" % (block_counter, tx_counter, tx.tx_hash))
        for input in tx.inputs:
          print("input - %s:%d" % (input.prev_hash, input.idx))
          print(input.segments)
        output_idx = 0
        for output in tx.outputs:
          print("output - %s:%d" % (output.addr, output_idx))
          print(output.segments)
          output_idx += 1
        tx_counter = tx_counter + 1
      block_counter = block_counter + 1


if __name__ == '__main__':
  main()
