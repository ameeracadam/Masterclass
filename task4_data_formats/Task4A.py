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
                
            





                # xml = dicttoxml(rows, custom_root='test', attr_type=False)
                # print(xml)
                # #save in xml
