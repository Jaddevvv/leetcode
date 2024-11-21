# https://www.deep-ml.com/problem/Matrix%20times%20Vector

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0])!= len(b):
		return -1
	list =[]
	for line in a :
		result = 0
		for valuea,valueb in zip(line,b) :
			result+= valuea*valueb
		list.append(result)
	return list