import pandas as pd

def read_dataset(path: str) -> pd.DataFrame:
    sid = 0
    data = []
    with open(path, 'r') as file:
        for line in file:
            eid = 0
            line = line.split(' -2')
            line = line[0].split(' -1 ')
            for element in line:
                data.append((sid, eid, element))
                eid += 1
            sid += 1
    df = pd.DataFrame(data, columns=['SID', 'EID', 'Items'])
    return pd.DataFrame(data, columns=['SID', 'EID', 'Items'])