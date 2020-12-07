# -*- coding: utf-8 -*-
"""
helper functions for NetworkData
"""
import os
import socket

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']
__email__ = __credits__[0]

# GLOBALS
LOOP = '127.0.0.1'
NET = '127.0.0.0'
MASK = '255.0.0.0'
LOCALHOST = 'localhost.localdomain'


def _range(*args, **kwargs):
    """
    _range helper function

    :param *args: (int)
    :param **kwargs: (int)
    :return: (list)
    """
    return list(range(*args, **kwargs))


def bytes_to_bits():
    """
    bytes_to_bits

    :return: (str)
    """
    lookup = []
    bits_per_byte = _range(7, -1, -1)
    for num in range(256):
        bits = 8 * [None]
        for i in bits_per_byte:
            bits[i] = '01'[num & 1]
            num >>= 1
        lookup.append(''.join(bits))
    return lookup


BYTES_TO_BITS = bytes_to_bits()


def cidr(netmask=MASK):
    """
    calculate cidr

    :param netmask: (str)
    :return: cidr (int)
    """
    numbits = 0
    for i in netmask.split('.'):
        part = int_to_bits(int(i), 8, 1)
        for j in list(part):
            numbits += int(j)
    return numbits


def get_domain(hostname=LOCALHOST):
    """
    get_domain

    :param hostname: (str)
    :return: domainname (str)
    """
    if hostname in ['localhost', 'localhost.localdomain']:
        return 'localdomain'
    return hostname.split('.', 1)[1]


def get_gateway(network=NET, netmask=MASK):
    """
    get_gateway

    :param network: (str)
    :param netmask: (str)
    :return: gateway (str)
    """
    gate = [0, 0, 0, 0]
    net = network.split('.')
    mask = netmask.split('.')
    for i in range(4):
        gate[i] = (int(net[i]) & int(mask[i]))
    gate[3] = gate[3] + 1
    return f'{gate[0]}.{gate[1]}.{gate[2]}.{gate[3]}'


def get_host_ip(hostname=LOCALHOST):
    """
    get_host_ip

    :param hostname: (str)
    :return: ip (str)
    """
    ip_address = LOOP
    if hostname in ['localhost', 'localhost.localdomain']:
        return ip_address
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.error as err:
        print(f'get_host_ip error: {err}')
    return ip_address


def get_netmask(lookup):
    """
    get_netmask

    :param cidr: str
    :returns: netmask
    """
    key = int(lookup)
    netmasks = {1: '128.0.0.0',
                2: '192.0.0.0',
                3: '224.0.0.0',
                4: '240.0.0.0',
                5: '248.0.0.0',
                6: '252.0.0.0',
                7: '254.0.0.0',
                8: '255.0.0.0',
                9: '255.128.0.0',
                10: '255.192.0.0',
                11: '255.224.0.0',
                12: '255.240.0.0',
                13: '255.248.0.0',
                14: '255.252.0.0',
                15: '255.254.0.0',
                16: '255.255.0.0',
                17: '255.255.128.0',
                18: '255.255.192.0',
                19: '255.255.224.0',
                20: '255.255.240.0',
                21: '255.255.248.0',
                22: '255.255.252.0',
                23: '255.255.254.0',
                24: '255.255.255.0',
                25: '255.255.255.128',
                26: '255.255.255.192',
                27: '255.255.255.224',
                28: '255.255.255.240',
                29: '255.255.255.248',
                30: '255.255.255.252',
                31: '255.255.255.254',
                32: '255.255.255.255',
                }
    return netmasks[key]


def get_network(ipaddr, netmask):
    """
    get_network

    :param ip: str
    :param netmask: str
    :returns: network
    """
    network = [0, 0, 0, 0]
    ip_parts = ipaddr.split('.')
    mask_parts = netmask.split('.')
    for i in range(4):
        network[i] = (int(ip_parts[i]) & int(mask_parts[i]))
    return f'{network[0]}.{network[1]}.{network[2]}.{network[3]}'


def get_short_name(hostname=LOCALHOST):
    """
    get_short_name

    :param hostname: (str)
    :return: short_name (str)
    """
    if hostname in ['localhost', 'localhost.localdomain']:
        return 'localhost'
    return hostname.split('.', 1)[0]


def int_to_words(int_val, word_size, num_words):
    """
    int_to_words

    :param int_val: (int)
    :param word_size: (int)
    :param num_words: (int)
    :return: words (str)
    """
    max_int = 2 ** (num_words * word_size) - 1
    max_word = 2 ** word_size - 1
    words = []
    if int_val > max_int:
        return 0
    for _ in range(num_words):
        word = int_val & max_word
        words.append(int(word))
        int_val >>= word_size
    return tuple(reversed(words))


def int_to_bits(int_val, word_size, num_words, word_sep=''):
    """
    int_to_bits

    :param int_val: (int)
    :param word_size: (int)
    :param num_words: (int)
    :param word_sep: (str)
    :return: bits (str)
    """
    bit_words = []
    for word in int_to_words(int_val, word_size, num_words):
        bits = []
        while word:
            bits.append(BYTES_TO_BITS[word & 255])
            word >>= 8
        bits.reverse()
        bit_str = ''.join(bits) or '0' * word_size
        bits = ('0' * word_size + bit_str)[-word_size:]
        bit_words.append(bits)
    return word_sep.join(bit_words)


def write_file(filename, contents):
    """
    write_file

    :param filename: str
    :param contents: [str]
    """
    with open(filename, 'w') as stream:
        stream.write(contents)
        os.chmod(filename, 0o644)
