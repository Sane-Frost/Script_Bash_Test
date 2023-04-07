#!/usr/bin/env python3
"""
Разработаем скрипт-Bash для Unbuntu 22.04.
Будем использовать материалы:
https://pyneng.readthedocs.io/ru/latest/book/05_basic_scripts/index.html
"""

from sys import argv

interface = argv[0]
vlan = argv[0]

access_template = [
    'switchport mode access',
    'swichport access vlan {}',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable']

print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
