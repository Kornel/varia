
# coding: utf-8

# In[17]:

import numpy as np
import pandas as pd


# In[45]:

N = 10
p = 2

features = pd.DataFrame(np.random.randn(N, p))

b = np.random.normal(size = p)

Y = features.apply(lambda row: sum(row * b), axis = 1)

features['Y'] = Y


# In[ ]:



