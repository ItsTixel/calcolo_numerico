import numpy as np

# 
a: list[int] = [1, 2, 3]
a_vec_np = np.array(a)
a_vec_np2 = np.array([[5,6,7,8,9],[10,11,12,13,14]])
print(type(a_vec_np))
print(a_vec_np)
print(a_vec_np.shape)
print(a_vec_np2.shape)

a_vec_np = np.array([1.1,2.647], dtype=np.float32)
print(a_vec_np)



