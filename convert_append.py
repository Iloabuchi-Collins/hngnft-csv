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
                        "hair": '',
                        "eyes": '',
                        "teeth": '',
                        "clothing": '',
                        "accessories": '',
                        "expression": '',
                        "strength": '',
                        "weakness": ''

                    }
                ]
            },
        }
    hash = []


    with open(csvfilepath, 'r') as csvf:
        csvReader = csv.DictReader(csvf)
        
        for rows in csvReader:
                     
            nft['collection']['id'] = rows['UUID']
            nft["series_number"] = rows['Series Number']
            nft["description"] = rows['Description']
            nft["name"] = rows['Name']
            nft["attributes"][0]['value'] = rows['Gender']

            # i joined the whole 'attributes' to one string and split the single string so that i can get the value for each attribute
            new_attrib = ''.join(rows['Attributes'])
            result1 = new_attrib.replace(":", " ")
            result2 = result1.replace(";", " ")
            result = [result1.split(" ")]
            print(result)
            nft['collection']['attributes'][0]['hair'] = result[0][1]
            nft['collection']['attributes'][0]['eyes'] = result[0][3]
            nft['collection']['attributes'][0]['teeth'] = result[0][5]
            nft['collection']['attributes'][0]['clothing'] = result[0][7]
            nft['collection']['attributes'][0]['accessories'] = result[0][9]
            nft['collection']['attributes'][0]['expression'] = result[0][11]
            nft['collection']['attributes'][0]['strength'] = result[0][13]
            nft['collection']['attributes'][0]['weakness'] = result[0][15]
            


            #get name of nft to save as output name
            name = rows['Filename']
            jsonFilePath= 'output/{}.json'.format(name)

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
    with open(file, 'r') as csvf:
        csvReader = csv.reader(csvf)
        csv_input = pd.read_csv(file)
        csv_input['Hash'] = hash
        
        csv_input.to_csv('file1.output.csv', index=False)