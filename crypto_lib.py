#!/usr/bin/env python
# https://en.bitcoin.it/wiki/Protocol_documentation#Addresses

import hashlib
import base58
import struct
import ripemd

from crypto_op import *

def uint1(stream):
    return ord(stream.read(1))


def uint2(stream):
    # H represents unsigned short
    return struct.unpack('H', stream.read(2))[0]


def uint4(stream):
    # I represents unsigned int
    return struct.unpack('I', stream.read(4))[0]


def uint8(stream):
    # Q represents unsigned long long
    return struct.unpack('Q', stream.read(8))[0]


def hash4(stream):
    return stream.read(8)


def hash32(stream):
    # follow the practice in blockchain.info and blockexplorer.com
    return stream.read(32)[::-1]


def time(stream):
    time = uint4(stream)
    return time


def varint(stream):
    size = uint1(stream)

    if size < 0xfd:
        return size
    if size == 0xfd:
        return uint2(stream)
    if size == 0xfe:
        return uint4(stream)
    if size == 0xff:
        return uint8(stream)
    return -1


def hash_tx(tx_bytes):
    hash_bytes = hashlib.sha256(hashlib.sha256(tx_bytes).digest()).digest()[::-1]
    return hashStr(hash_bytes)


def hashStr(bytes):
    return ''.join(("%02x" % a) for a in bytes)


def convert_hex_to_ascii(h):
    chars_in_reverse = []
    while h != 0x0:
        chars_in_reverse.append(chr(h & 0xFF))
        h = h >> 8

    chars_in_reverse.reverse()
    return ''.join(chars_in_reverse)


def gen_addr(hash_code):
    """ 
    Generates the address by hash.
    https://en.bitcoin.it/wiki/Protocol_documentation#Addresses
    """
    key_hash = '00' + hash_code
    # Obtain signature:
    sha = hashlib.sha256()
    sha.update(bytearray.fromhex(key_hash))
    checksum = sha.digest()
    sha = hashlib.sha256()
    sha.update(checksum)
    checksum = sha.hexdigest()[0:8]
    address = (base58.b58encode(bytes(bytearray.fromhex(key_hash + checksum)))).decode('utf-8')
    return address, key_hash, checksum


def hash160(hex_str):
    """
    See 'compressed form' at https://en.bitcoin.it/wiki/Protocol_documentation#Signatures
    """
    sha = hashlib.sha256()
    rip = ripemd.RIPEMD160()
    sha.update(hex_str)
    rip.update(sha.digest())
    return rip.hexdigest()  # .hexdigest() is hex ASCII


def pubkey_to_address(pubkey):
    compress_pubkey = False
    if compress_pubkey:
        if ord(bytearray.fromhex(pubkey[-2:])) % 2 == 0:
            pubkey_compressed = '02'
        else:
            pubkey_compressed = '03'
        pubkey_compressed += pubkey[2:66]
        hex_str = bytearray.fromhex(pubkey_compressed)
    else:
        hex_str = bytearray.fromhex(pubkey)

    # Obtain key:
    return gen_addr(hash160(hex_str))


def segment(raw_script):
    """ Segments the hex script to op sequence. """
    hex_script = hashStr(raw_script)
    pos = 0
    op_list = []
    push_data_dict = {OP_PUSHDATA1:2, OP_PUSHDATA2:4, OP_PUSHDATA4:8}
    while pos < len(hex_script):
        hex_idx = hex_script[pos:pos+2]
        op_idx = int(hex_script[pos:pos+2], 16)
        pos+=2
        # reference
        # https://github.com/bitcoin-sv/bitcoin-sv/blob/v1.0.10/src/script/interpreter.cpp#L310-L337
        if op_idx in OPCODE_NAMES:
            op_list.append(OPCODE_NAMES[op_idx])
            # If the op is PUSHDATAX, read the following payload.
            if op_idx in push_data_dict:
                data_len = int(hex_script[pos:pos+push_data_dict[op_idx]], 16)
                op_list.append(bytes.fromhex(hex_script[pos:pos+data_len * 2]))
                pos += data_len * 2
            if op_idx == OP_1NEGATE:
                op_list.append("-1")
                pos += 2
        elif op_idx <= 75:  # The data should less than 150.
            op_list.append(hex_script[pos:pos+op_idx*2])
            pos+=op_idx*2
        else:
            error = "ERROR:{}-{}".format(op_idx, hex_idx)
            op_list.append(error)
    return op_list
            
