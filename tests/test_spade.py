import pytest
import numpy as np
import pandas as pd
from SPADE.spade import read_dataset, find_F1


@pytest.fixture()
def df_expected() -> pd.DataFrame:
    return pd.DataFrame([[0, 0, "{'C'}"], [0, 0, "{'D'}"], [0, 1, "{'A'}"], [0, 1, "{'B'}"], [0, 1, "{'C'}"], [0, 2, "{'A'}"], [0, 2, "{'B'}"], [0, 2, "{'F'}"], [0, 3, "{'A'}"], [0, 3, "{'C'}"],
                         [0, 3, "{'D'}"], [0, 3, "{'F'}"], [1, 0, "{'A'}"], [1, 0, "{'B'}"], [1, 0, "{'F'}"], [1, 1, "{'E'}"], [2, 0, "{'A'}"], [2, 0, "{'B'}"], [2, 0, "{'F'}"], [3, 0, "{'D'}"],
                         [3, 0, "{'G'}"], [3, 0, "{'H'}"], [3, 1, "{'B'}"], [3, 1, "{'F'}"], [3, 2, "{'A'}"], [3, 2, "{'G'}"], [3, 2, "{'H'}"]], columns=['SID', 'EID', 'Items'])


@pytest.fixture()
def atoms_expected() -> pd.DataFrame:
    return pd.DataFrame([["{'A'}", 4], ["{'B'}", 4], ["{'D'}", 2], ["{'F'}", 4]])


def test_read_dataset(df_expected):
    df_returned = read_dataset('tests/test_data.txt')
    pd.testing.assert_frame_equal(df_returned, df_expected)


def test_find_F1(atoms_expected, df_expected):
    np.array_equal(find_F1(df_expected, 2), atoms_expected)
