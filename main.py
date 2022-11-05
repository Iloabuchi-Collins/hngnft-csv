from . import convert_append
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, required=True)
args = parser.parse_args()

csvFilePath = args.f

if (csvFilePath.endswith(".csv")):
        if os.path.exists(csvFilePath) == False:
            raise Exception('File isn\'t in repository')
        hashlist = convert_append.convert(csvFilePath)

        convert_append.append(hashlist,csvFilePath)
else:
    raise Exception('invalid file format')        