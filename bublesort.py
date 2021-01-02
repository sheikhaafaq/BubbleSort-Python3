arr = [5,2,9,0,3,8,1,4]
for i in range(0,len(arr)-1):
	flag = 0
	for j in range(0,len(arr)-1 - i ):
		if arr[j] > arr[j+1]:
			arr[j+1], arr[j] = arr[j], arr[j+1]
			flag = 1
		else:
			pass
	if flag == 0:
		break 

print(arr)