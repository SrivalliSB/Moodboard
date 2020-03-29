L=int(input())
N=int(input())
for i in range(0,N+1):
	W=int(input())
	H=int(input())
	if W<L or H<L:
		print("upload another")
	elif W>L and H>L:
		if W==H:
			print("accepted")
	else:
		print("crop it")
			
		