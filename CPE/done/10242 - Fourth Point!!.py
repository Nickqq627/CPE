while 1:
	try:
		arr=list(map(float, input().split()))
		if arr[2]==arr[4] and arr[3]==arr[5]:
			x=arr[0]+arr[6]-arr[2]
			y=arr[1]+arr[7]-arr[3]
		elif arr[2]==arr[6] and arr[3]==arr[7]:
			x=arr[0]+arr[4]-arr[2]
			y=arr[1]+arr[5]-arr[3]
		elif arr[0]==arr[4] and arr[1]==arr[5]:
			x=arr[2]+arr[6]-arr[0]
			y=arr[3]+arr[7]-arr[1]
		else:
			x=arr[2]+arr[4]-arr[0]
			y=arr[3]+arr[5]-arr[1]
		print('{:.3f} {:.3f}'.format(x,y))
	except:
		break