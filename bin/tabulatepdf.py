#!/usr/bin/env python

import argparse
import sys
import tabula

 # Create the parser
client_parser = argparse.ArgumentParser(prog='tabulatepdf', 
	description='extract tables from pdf', allow_abbrev=False)

# Add the arguments
client_parser.add_argument(
						  '--pdf',
						  metavar='pdf',
						  required=True,
						  help='pdf file to extract tables from',
	)

client_parser.add_argument(
						  '--output',
						  metavar='output',
						  help='output filename, default: output.csv'
	)

client_parser.add_argument(
						  '--page',
						  metavar='page',
						  help='page number of pdf to extract from, default: 1'
	)

args = client_parser.parse_args()

output = args.output or 'output.csv'
page = args.page or 1

tabula.convert_into(args.pdf, output, output_format="csv", pages=page)
print(f'table saved to {output}')