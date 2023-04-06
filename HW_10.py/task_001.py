import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data = pd.get_dummies(data['whoAmI'])

print(f'one hot coding with get_dummies:\n{data}\n')

data = pd.DataFrame(0, index=np.arange(len(lst)), columns=sorted(list(set(lst))))
for i, item in enumerate(lst):
    data[item][i] = 1

print(f'one hot coding without get_dummies:\n{data}')