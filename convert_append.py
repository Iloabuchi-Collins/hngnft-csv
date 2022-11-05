import csv
import json
import hashlib
import pandas as pd

def convert(csvfilepath):
    #convert csv to json and hashes it. Then stores the hash in a list

    nft = {
          "format": "CHIP-0007",
            "name": "",
            "description": "",
            "minting_tool": "HNG Minting Tool",
            "sensitive_content": False,
            "series_number": "",
            "series_total": 420,
            "attributes": [
                {
                    "trait_type": "gender",
                    "value": ''
                }
            ],
            "collection": {
                "name": "Zuri NFT tickets for free lunch",
                "id": "",
                "attributes": [
                    {
                        ""
                    }
                ]
            },
        }
    hash = []


    with open(csvfilepath, 'r') as csvf:
        csvReader = csv.reader(csvf)
        
        for rows in csvReader:
                     
            nft['collection']['id'] = rows[7]
            nft['collection']['attributes'][0] = rows[6]
            nft["series_number"] = rows[1]
            nft["description"] = rows[4]
            nft["name"] = rows[3]
            nft["attributes"][0]['value'] = rows[5]


            #get name of nft to save as output name
            name = rows['Filename']
            jsonFilePath= '{}.json'.format(name)

            #creates a json file with name from the nft
            with open(jsonFilePath, 'w') as jsonf:
                json.dump(nft, jsonf, indent=4, separators=(", ", ": "))
                jsonf.close()
            
            if name == "Filename":
                pass
            else:
                with open(jsonFilePath, "rb") as f:
                    bytes = f.read()
                    readable_hash = hashlib.sha256(bytes).hexdigest()
                    hash.append(readable_hash)
                    f.close()
        return hash


def append(hash,file):
    # appends hash 
    file_name = file.split('.')
    outfile = file_name[0].split('/')
    outfile = file_name[0].split('\\')
    outfile= outfile[-1] + '.output'+ '.csv'
    csv_input = pd.read_csv(file_name)
    csv_input['Hash'] = hash
    
    csv_input.to_csv('filename.output.csv', index=False)