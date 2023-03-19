import math
while 1:
	try:
		r,d,n=input().split()
		r=int(r)+6440
		d=int(d)
		if n=='min':
			d=d/60
		ans1=r*2*math.pi*(d/360)
		ans2=2*(math.sin((d*math.pi/180)/2)*r)
		print('{:.6f} {:.6f}'.format(ans1,ans2))
		
	except:
		break