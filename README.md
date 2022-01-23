# SPADE
An implementation of the SPADE algorithm.

## Installation
To install SPADE package clone it from github repository and install with following commands:
```console
git clone https://github.com/ann-sos/SPADE.git
python3 setup.py install
```
## Installation for development
To work with the package interactively you may wish to use the following way of installation:
```
pip install -e .
```

## Usage

### read_dataset(path: str) -> pd.DataFrame
SPADE package provides a function to read txt files into dataframe. The formatting of the text file should follow the rules:

1. *'-1'* separates itemsets,
1. *'-2'* indicated the end of the sequence.

Such formatting is adjusted to formatting of datasets from http://www.philippe-fournier-viger.com/spmf/index.php?link=datasets.php as the package was prepared to process them. http://www.philippe-fournier-viger.com/spmf/SPADE.php provides more information about formatting of the input and general information about the algorithm.

Example of use:
```
df = read_dataset(r"test_data/test.txt")
```

### spade(df: pd.DataFrame, min_sup: int)
The fuction SPADE is the heart of the package. Given a dataframe with all the data (for example df returned by read_dataset) and a value of minimal support it will return a dataframe containing all sequences with support value greater than or equal to minimal support.
It will be returned in the following format:
```
                         Items  Support
0                        {'A'}        4
1                        {'B'}        4
2                        {'D'}        2
3                        {'F'}        4
4                 [{'A', 'B'}]        3
5                 [{'A', 'F'}]        3
6               [{'B'}, {'A'}]        2
7                 [{'F', 'B'}]        4
8               [{'D'}, {'A'}]        2
9               [{'D'}, {'B'}]        2
10              [{'D'}, {'F'}]        2
11              [{'F'}, {'A'}]        2
12           [{'F', 'A', 'B'}]        3
13         [{'F', 'B'}, {'A'}]        2
14       [{'D'}, {'B'}, {'A'}]        2
15       [{'D'}, {'F'}, {'A'}]        2
16         [{'D'}, {'F', 'B'}]        2
17  [{'D'}, {'F', 'B'}, {'A'}]        2
```
[{'D'}, {'F', 'B'}, {'A'}] should be read as D->FB->B and [{'B'}, {'A'}] as B->A. 
### examples
For more comprehensive example of usage covering import of SPADE and read_dataset check main.py.