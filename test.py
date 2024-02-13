try:
    import cPickle as pickle
except:
    import pickle

# 1.3.4
import pandas as pd
import numpy as np
import pyscf

df = pd.DataFrame(np.ones((100,4)))
df.to_pickle("water-x6.pkl")
print(df.keys())
print(df)
