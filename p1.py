x=int(input("enter number: "))
y=int(input("enter number: "))
z=int(input("enter number: "))
if x>=y and x >=z:
	largest=x
	print("largest numbet=",largest,)
elif y>=x and y>=z:
	largest=y
	print("largrst number=",largest,)
else :
	largest=z
	print("largest number=",largest,)
