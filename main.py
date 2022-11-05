from convert_append import convert, append
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, required=True)
args = parser.parse_args()

csvfilepath = args.f

if (csvfilepath.endswith(".csv")):
        if os.path.exists(csvfilepath) == False:
            raise Exception('File isn\'t in repository')
        hashlist = convert(csvfilepath)

        append(hashlist,csvfilepath)
else:
    raise Exception('invalid file format')        