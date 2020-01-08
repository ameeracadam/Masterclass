import csv, json
from dicttoxml import dicttoxml
import sys

# python Task4.py [name_of file.csv]

if __name__ == "__main__":

    #If there is no CSV file given in in the command line, Error will be raised.
    if len(sys.argv) < 1:
        raise ValueError("invalid argument given, needs to be filename")
    else:
        with open(sys.argv[1]) as f:

            #Open CSV file
            with open('task4a.json', 'w') as outfile:
                readcsv = csv.reader(f, delimiter=',')

                #Select row to be listed
                columns = [2,0]
                row_list=[]

                #Lists out selected rows
                for row in readcsv:
                    rows = list(row[i] for i in columns)
                    row_list.append(rows)
                
                #Dump rows into JSOn
                json.dump(row_list, outfile)
                xml = dicttoxml(row_list, custom_root='test', attr_type=False)
                with open('task4a.xml', 'wb') as f:
                    f.write(xml)
                
            




                """
                Bonus: Save Data in XML
                xml = dicttoxml(rows, custom_root='test', attr_type=False)
                print(xml)
                #save in xml
                """