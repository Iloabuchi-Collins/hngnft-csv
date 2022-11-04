# hngnft-csv
A cli tool that generates SHA256 of your CSV file and appends it to the CSV file.

The CSV (Comma Seperated Values) file is converted to a JSON (Javascript Object Notation) file then its hash(SHA256) is appended to each row of the file and it's reconverted back to a csv file. 

## Steps
1. In your terminal, clone this repository to your local machine: <br>
        `git clone https://github.com/Iloabuchi-Collins/hngnft-csv.git` <br>

2. Change directory to the newly cloned repository:<br>
        `cd hngnft-cvs` <br>

3. install the required dependencies for the project: <br>
        `pip install -r requirements.txt` <br>

4. Run the code: <br>
        `python3 main.py {csv name}` <br>
    Remember to replace the 'csv name'above with the name of your csv file <br>