import random
#hm - The value will be "how much." This is how many datapoints that we want in the set. We could choose to have 10, or 10 million, for example.
#variance - This will dictate how much each point can vary from the previous point. The more variance, the less-tight the data will be.
#step - This will be how far to step on average per point, defaulting to 2.
#correlation - This will be either False, pos, or neg to indicate that we want no correlation, positive correlation, or negative correlation.
def create_dataset(hm, variance, step=2, correlation=False):
	val = 1
	ys = []
	for i in range(hm):
		y = val + random.randrange(-variance, variance)
		ys.append(y)
		if correlation and correlation == 'pos':
			val+=step
		elif correlation and correlation == 'neg':
			val-=step
	xs = [i for i in range(len(ys))]
	return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

