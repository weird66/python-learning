import numpy as np

temptures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

print('average:',np.mean(temptures))
print('lowest:', np.min(temptures))
print('highest:',np.max(temptures))
print('ftemptures', temptures * 1.8 + 32)
print('daysExcced20', np.where(temptures >= 20))
