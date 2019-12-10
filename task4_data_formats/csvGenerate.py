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
    Message = []

    # start loop
    for _ in tqdm.tqdm(range(rows)):
        msg = []
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

        msg.append(fake.text().split(" ")[0])

        value = random()
        if value > 0.5:
            msg.append(hash)
        
        msg =  ' '.join(str(v) for v in msg) 
        Message.append(msg)

    # generate dataframe and return
    return pd.DataFrame({
        'Name':fnames,
        'Index':index,
        'Location':location,
        'ID':ID,
        'Message':Message
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
    