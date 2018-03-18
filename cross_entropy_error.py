import numpy as np

def cross_entropy_error(pred_y, target_y):
	delta = 1e-7
	return -np.sum(target_y * np.log(pred_y + delta))

#Correct Value is "2", target_y[2]
pred_y = np.array([0,0,0.9,0.025,0.025,0.025,0.025,0,0,0])
target_y = np.array([0,0,1,0,0,0,0,0,0,0])
result = cross_entropy_error(pred_y, target_y)
print("cross_entropy_error is {}".format(result))
