import pandas as pd

data = pd.DataFrame({'A': ['X', 'Y'],
  'B': 1,
  'C': [2, 3]}, index=[])
print data
data['D'] = [10, 9]
print data




#    A  B  C
# 0  X  1  2
# 1  Y  1  3
#    A  B  C   D
# 0  X  1  2  10
# 1  Y  1  3   9
