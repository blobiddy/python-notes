from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler

import pandas as pd

nRowsRead = 1587
data = pd.read_csv('./Harry Potter 1.xls', delimiter=';', nrows = nRowsRead)
data.dataframeName = 'Harry Potter 1.csv'
nRow, nCol = data.shape
print(f'There are {nRow} rows and {nCol} columns')