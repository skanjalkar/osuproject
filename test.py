l = [1,2,3,4,5]

ss = [[]]

for i in range(0, len(l)):
	temp = []
	for s in ss:
		new_s = s + [l[i]]
		temp.append(new_s)
	ss += temp
ss.sort()
print(ss)


def seq(arr):
	if len(arr) == 0:
		return [[]]
	a = seq(arr[0:-1])
	import copy
	b = copy.deepcopy(a)
	for elem in a:
		elem.append(arr[-1])
	return b + a

print(seq(l))