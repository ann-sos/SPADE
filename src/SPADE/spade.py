import pandas as pd

def read_dataset(path: str) -> pd.DataFrame:
    """
    This function reads into pandas DataFrame a dataset formatted as follows:
        -1 separates elements
        -2 separates sequences
        Item can contain one or more items"""
    sid = 0
    data = []
    with open(path, 'r') as file:
        for line in file:
            eid = 0
            line = line.split(' -2')
            line = line[0].split(' -1 ')
            for element in line:
                element = element.split()
                for item in element:
                    data.append((sid, eid, item))
                eid += 1
            sid += 1
    df = pd.DataFrame(data, columns=['SID', 'EID', 'Items'])
    return pd.DataFrame(data, columns=['SID', 'EID', 'Items'])


def spade():
    # 1 Find frequent items or 1-sequences e.g. {A}, {B} 
    #   1a find atoms
    #   1b keep only the frequent ones
    # 2 Find frequent 2-sequences (containing 2 items) e.g. {AB}, {A}->{B}, {B}->{A}
    # 3 Find equivalence classes / sequences longer than 3 items
    # 4 Calculate support for sequences from step 3
    pass