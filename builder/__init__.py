# -*- coding:utf-8 -*-

# pylint: disable=C0103
# pylint: disable=R0902
# pylint: disable=R0913
# pylint: disable=E0401

"""
:class:`Builder`
"""
import yaml
import json
from . import helpers

__author__ = 'Joel E Carlson'
__credits__ = ['joel.elmer.carlson@gmail.com']
__email__ = __credits__[0]


class Builder():
    """
    :returns: :class:`Builder`
    """

    def __init__(self, ip, os, cpu, mem):
        """
        builder environment
        """
        self.ip = ip.split('/')[0]
        self.cidr = int(ip.split('/')[1])
        self.netmask = helpers.get_netmask(self.cidr)
        self.network = helpers.get_network(self.ip, self.netmask)
        self.gateway = helpers.get_gateway(self.network, self.netmask)
        self.os = os
        self.cpu = cpu
        self.mem = mem

    def __repr__(self):
        return (f'Builder({self.ip!r}, '
                f'{self.cidr!r}, '
                f'{self.netmask!r}, '
                f'{self.network!r}, '
                f'{self.gateway!r}, '
                f'{self.os!r}, '
                f'{self.cpu!r}, '
                f'{self.mem!r}'
                ')')

    def to_yaml(self):
        """
        to_yaml
        """
        content = {'ip': self.ip,
                   'cidr': self.cidr,
                   'netmask': self.netmask,
                   'gateway': self.gateway,
                   'os': self.os,
                   'cpu': self.cpu,
                   'mem': self.mem,
                   }
        return yaml.dump(content)

    def to_json(self):
        """
        to_json
        """
        content = {'ip': self.ip,
                   'cidr': self.cidr,
                   'netmask': self.netmask,
                   'gateway': self.gateway,
                   'os': self.os,
                   'cpu': self.cpu,
                   'mem': self.mem,
                   }
        return json.dumps(content).encode('utf-8')
