import ascii_text
import sys
import configparser
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

config = configparser.ConfigParser()

config.read('config.ini')

import api_keys

from modules import proxynova,hunter,ipqualityscore,leaklookup,breachdirectory,haveibeenpwned,snusbase,leakcheck,databreach,dehashed,emailrep

import argparse

parser = argparse.ArgumentParser(description="EmailDig — email digging tool")

parser.add_argument("-T", "--target", required=True, help="Email to search")

args = parser.parse_args()

email = args.target

if config.getboolean('SETTINGS', 'ascii_art'):
	
	print(ascii_text.art)

if config.getboolean('SETTINGS', 'version'):

	print("version 0.2")

if config.getboolean('SERVICES', 'use_proxynova'):

	print("\nProxyNova Results:")

	proxynova.proxynova(email)

if config.getboolean('SERVICES', 'use_breachdirectory'):

	print("\nBreachDirectory Results:")

	breachdirectory.breachdirectory(email)

if config.getboolean('SERVICES', 'use_hunter'):

	print("\nHunter Results:")

	hunter.hunter(email)

if config.getboolean('SERVICES', 'use_ipqualityscore'):

	print("\nIpQualityScore Results:")

	ipqualityscore.ipqualityscore(email)

if config.getboolean('SERVICES', 'use_emailrep'):

	print("\nEmailrep Results:")

	emailrep.emailrep(email)

if config.getboolean('SERVICES', 'use_haveibeenpwned'):

	print("\nHaveIBeenPwned Results:")

	haveibeenpwned.haveibeenpwned(email)

if config.getboolean('SERVICES', 'use_snusbase'):

	print("\nSnusbase Results:")

	snusbase.snusbase(email)

if config.getboolean('SERVICES', 'use_leaklookup'):

	print("\nLeaklookup Results:")

	leaklookup.leaklookup(email)

if config.getboolean('SERVICES', 'use_dehashed'):

	print("\nDeHashed Results:")

	dehashed.dehashed(email)

if config.getboolean('SERVICES', 'use_databreach'):

	print("\nDatabreach Results:")

	databreach.databreach(email)

if config.getboolean('SERVICES', 'use_leakcheck'):

	print("\nLeakcheck Results:")

	leakcheck.leakcheck(email)

if config.getboolean('SERVICES', 'use_hudsonrock'):

	print("\nHudsonrock Results:")

	hudsonrock.hudsonrock(email)





