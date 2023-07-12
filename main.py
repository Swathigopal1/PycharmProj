import numpy as np
my_arr=np.array([[1,2,3,4],[5,6,7,8]])
my_arr.resize((3,4))
print(my_arr)

my_first_arr=np.array([1,2,3,4,5,6,7,8])
print(my_first_arr)
my_new_arr=my_first_arr.reshape(2,4)
print(my_new_arr)

my_second_arr=np.array([0,1,2,3,4,5,6,7,8])
my_updated_arr=my_second_arr.reshape(-1,3)
