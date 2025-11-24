import numpy as np

a = np.loadtxt(fname='campaign_A.csv', dtype=str, unpack=True)

dates = a[0]
visits = a[1]

b = pd.DataFrame({'date': a[0], 'visit':a[1]})
print(b)