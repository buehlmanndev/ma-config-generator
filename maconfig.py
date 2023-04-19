#!/usr/bin/python
import argparse
import csv
import string
import os
from pathlib import Path

__author__ = 'ChBuehlmann'


def parse_args():
    parser = argparse.ArgumentParser(
        description='This Script generates MA Scripts from a Template XML File and a normal CSV Table witch should have'
                    'at minimum a column named "FILE_NAME"')
    parser.add_argument('-i', '--input', help='Input file name, file has to include the Headers', required=True)
    parser.add_argument('-t', '--template', help='Template file name, values from CSV can be referenced as ${HEADER}',
                        required=False, default='template_colors.xml')
    return parser.parse_args()


def transform(input_file, template_file):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(Path(input_file)) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for count, row in enumerate(reader, start=1):
            with open('output/'+row['FILE_NAME'].lower()+'.xml', 'w', encoding='utf-8', newline='') as outputFile:
                template = readXmlTemplate(template_file)
                outputFile.writelines(template.safe_substitute(row))


def readXmlTemplate(template_file):
    with open(Path(template_file), 'r', encoding='utf-8-sig') as f:
        data = f.read()
    return string.Template(data)


def main():
    args = parse_args()
    transform(args.input, args.template)
    print("Done.")


if __name__ == "__main__":
    main()
