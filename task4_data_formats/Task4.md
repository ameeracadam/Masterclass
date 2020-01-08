#   Task4
****
##  Task4A
### Given the data in a CSV, write a short Python snippet to read the CSV, extract only the 3rd and 1st fields (in that order) and write the output in JSON. 
-   Create a Python file and open it in your favourite code editor
-   Enter the following in your Python file:
    ```
    #import csv, json, and sys modules
    import csv, json
    import sys 

    if __name__ == "__main__":
    #Allows any CSV file to be accepted. CSV file not hard-coded in.
        if len(sys.argv) < 1:
        #If no file given, error message will be raised
            raise ValueError("invalid argument given, needs to be filename")
        else:
            with open(sys.argv[1]) as f:
            #Creates and open a JSON file titled task4a.json
                with open('task4a.json', 'w') as outfile:
                   
                    #Reads CSV file given
                    readcsv = csv.reader(f, delimiter=',')
                    
                    #Set columns to be 3rd and 1st columns
                    columns = [2,0]
                   
                    #Create an array to list output
                    row_list=[]
                    
                    for row in readcsv:
                        rows = list(row[i] for i in columns)
                        row_list.append(rows)
                    
                    #Dumps output from row_list into JSON file
                    json.dump(row_list, outfile)
    
    ```
-   Save the file and run the file in a Terminal 
    `python [FILE_NAME].py [CSV_FILE].csv`
-   The output will be a JSON file titled **task4a.json**

### Bonus: Write in XML
-   Open the file created in a code editor
-   Edit the script to include the following lines:
    ```
    #import XML module
    from dicttoxml import dicttoxml

    #Writes row_lines into an XML file titled task4a.xml
    xml = dicttoxml(row_list, custom_root='test', attr_type=False)
    with open('task4a.xml', 'wb') as f:
    f.write(xml)
    ``` 
-   Save the file and run in Terminal
    `python [FILE_NAME].py [CSV_FILE].csv`
-   The output will be a JSON file titled **task4a.json**, and a XML file titled **task4a.xml**

-   The final code (combined JSON and XML) would look like this:
    ```
    import csv, json
    from dicttoxml import dicttoxml
    import sys
    
    if __name__ == "__main__":
        if len(sys.argv) < 1:
            raise ValueError("invalid argument given, needs to be filename")
        else:
            with open(sys.argv[1]) as f:
                with open('task4a.json', 'w') as outfile:
                    readcsv = csv.reader(f, delimiter=',')
                    columns = [2,0]
                    row_list=[]
    
                    for row in readcsv:
                        rows = list(row[i] for i in columns)
                        row_list.append(rows)
                    
                    json.dump(row_list, outfile)
                    xml = dicttoxml(row_list, custom_root='test', attr_type=False)
                    with open('task4a.xml', 'wb') as f:
                        f.write(xml)
    ```


****
##  Task4B
### Given the data in a CSV, write a bash shell script, uisng regular expressions to replace the ID with "XXXXX". You mar assume IDs have 6-7 digits with an optional letter.
-   Create a Shell Script and open it in a code editor
-   Enter the following in your script:
    ```
    #!/bin/bash
    awk '{gsub(/^([a-z0-9]{6,7})/, "xxxxx", $NF);}1' generatedData_4b.csv > replaced_4b.csv
    awk -F, '{gsub(/^([a-z0-9]{6,7})/, "xxxxx", $4);}1' replaced_4b.csv > replaced.csv
    ```
-   Save your file and run in Terminal using the following command line:
    `bash [FILE_NAME].sh [CSV_FILE].csv`
-   The output will be a CSV file titled **replaced.csv**

****

### Bonus: Populating a CSV file with fake data
You can create your own CSV file and populate it with randomly faked data in Python. 
-   Create a new Python script and open it in a code editor
-   Enter in the following code:
    ```
    import pandas as pd
    from faker import Faker
    from random import randrange
    import hashlib
    import sys
    import tqdm
    from random import seed, random
    
    SGLOCATIONS = ['Bedok', 'Punggol', 'Jurong East', 'one-north', 'Tampines']
    seed(1)
    
    def createDataFrame(rows):
        '''
        Creates a Pandas dataframe with number of rows specified.
    
        Args:
        rows = number of rows
    
        Returns:
        Pandas dataframe obj
        '''
        fake = Faker()
    
        # initialise arrays
        fnames = []
        index = []
        index_ctr = 10
        location = []
        ID = []
    
        # start loop
        for _ in tqdm.tqdm(range(rows)):
            # if _ % 100 == 0:
            #     print("Generating row {}/{}".format(_,rows))
            fnames.append(fake.name().split(" ")[0])
            index.append(index_ctr)
            location.append(SGLOCATIONS[randrange(len(SGLOCATIONS))])
            
            # generate a random integer based on number of rows and hash it
            originalID = randrange(rows*1000)
            hash = hashlib.sha256(str(originalID).encode()).hexdigest()[:7]
            ID.append(hash)
    
            index_ctr += 10
    
        # generate dataframe and return
        return pd.DataFrame({
            'Name':fnames,
            'Index':index,
            'Location':location,
            'ID':ID,
        })
    
    if __name__ == "__main__":
        if len(sys.argv) < 1:
            print("Number of rows not provided!")
        else:
            try:
                df = createDataFrame(int(sys.argv[1]))
            except:
                print("Row value is not valid!")
            df.to_csv("generatedData.csv", index=False)
            print("Data with {} rows generated!".format(sys.argv[1]))
    ```
-   Save the file and run the script in Terminal using the following command line:
    `python [FILE_NAME].py [NUMBER_OF_ROWS]`
-   The output will be a CSV file titled **generatedData.csv**. You can use this file to run Task4A.
-   The script can be edited to include faked mesages to run Task4B.