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
    return pd.DataFrame(data, columns=['SID', 'EID', 'Items'])


def find_F1(df: pd.DataFrame, min_sup: int) -> pd.DataFrame:
    """
    Finds frequent (support >= min_sup) items or 1-sequences,
    e.g. {A}, {B}, returns dataframe with these items and their support.
    """
    atoms_series = df.groupby('Items')['SID'].nunique()
    atoms = pd.DataFrame({'Items': atoms_series.index, 'Support': atoms_series.values})
    return atoms.loc[atoms['Support'] >= min_sup]


def spade(df: pd.DataFrame, min_sup: int):
    # (STEP 1): Find atoms and their support
    F1 = find_F1(df, min_sup)
    # 2 Find frequent 2-sequences (containing 2 items) e.g. {AB}, {A}->{B}, {B}->{A}
    # 3 Find equivalence classes / sequences longer than 3 items
    # 4 Calculate support for sequences from step 3
    pass
