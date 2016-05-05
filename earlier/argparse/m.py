#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='argparse demo')
# parser.add_argument('arg') 
parser.add_argument('-a', dest='arg', nargs=2, type=int) 
args = parser.parse_args()
print args.arg
