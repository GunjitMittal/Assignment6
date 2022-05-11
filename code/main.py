import numpy as np
N=36
x_i=np.array([i for i in range(2,13)])
p_i=np.array([i/N for i in range(1,7)]+([i/N for i in range(5,0,-1)]))
m=p_i@x_i
print(f"mean is {round(m)}")