# -*- coding:utf-8 -*-

"""
example.py -- builder in action
"""
import argparse
import builder

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']
__email__ = __credits__[0]

IPV4 = '127.0.0.0/8'
OS = 'RHEL8.3'
CPU = '2'
MEM = '8'

def get_arguments():
    """
    get_arguments for cli

    :returns: parser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', help=IPV4)
    parser.add_argument('-o', '--os', help=OS)
    parser.add_argument('-c', '--cpu', help=CPU)
    parser.add_argument('-m', '--mem', help=MEM)
    return parser.parse_args()


def run():
    """
    run
    """
    # what do you want to do?
    resp = {}
    resp['ip'] = IPV4
    resp['os'] = OS
    resp['cpu'] = CPU
    resp['mem'] = MEM

    # cli
    args = get_arguments()
    resp['ip'] = args.ip or resp['ip']
    resp['os'] = args.os or resp['os']
    resp['cpu'] = args.cpu or resp['cpu']
    resp['mem'] = args.mem or resp['mem']

    print('Running builder...')
    build = builder.Builder(resp['ip'],
                            resp['os'],
                            resp['cpu'],
                            resp['mem'],
                            )
    print(build.to_yaml())

if __name__ == '__main__':
    run()
