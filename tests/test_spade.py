import pytest
import pandas as pd
from SPADE.spade import read_dataset


def test_read_dataset():
    df_expected = pd.DataFrame([[0, 0, 'C D'], [0, 1, 'A B C'], [0, 2, 'A B F'], [0, 3, 'A C D F'],
                                [1, 0, 'A B F'], [1, 1, 'E'],
                                [2, 0, 'A B F'],
                                [3, 0, 'D G H'], [3, 1, 'B F'], [3, 2, 'A G H']], columns=['SID', 'EID', 'Items'])
    df_returned = read_dataset('tests/test_data.txt')
    pd.testing.assert_frame_equal(df_returned, df_expected)
