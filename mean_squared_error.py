import numpy as np

def mean_squared_error(pred_y, target_y):
	return 0.5 * np.sum((pred_y - target_y) ** 2)

pred_y = np.array([0,0,0.9,0.025,0.025,0.025,0.025,0,0,0])
target_y = np.array([0,0,1,0,0,0,0,0,0,0])
result = mean_squared_error(pred_y, target_y)
print("Mean Squared Error is {}".format(result))
