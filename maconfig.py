#!/usr/bin/python
import argparse
import csv
import string
import os

__author__ = 'ChBuehlmann'


def parse_args():
    parser = argparse.ArgumentParser(
        description='This Script translates sage 50 beam NT CSV Files from Sophisweb to Banana CSV '
                    '(to be imported as txt file). Resort Buchungen in Banana after Import to ake them visible!')
    parser.add_argument('-i', '--input', help='Input file name, file has to include the Headers', required=True)
    return parser.parse_args()


def transform(input_file):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(input_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for count, row in enumerate(reader, start=1):
            with open('output/'+row['FILE_NAME'].lower()+'.xml', 'w', encoding='utf-8', newline='') as outputFile:
                template = readXmlTemplate()
                outputFile.writelines(template.safe_substitute(row))


def readXmlTemplate():
    # Reading data from the xml file
    with open('template.xml', 'r', encoding='utf-8-sig') as f:
        data = f.read()

    # Passing the data of the xml
    # file to the xml parser of
    # beautifulsoup
    return string.Template(data)


def main():
    args = parse_args()
    transform(args.input)
    print("Done.")


if __name__ == "__main__":
    main()
