try:
    import cPickle as pickle
except:
    import pickle

# 1.3.4
import pandas as pd
import numpy as np
import pyscf

df = pd.read_pickle("./water-x6.pkl")
df
