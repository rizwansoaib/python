def bubble_sort(l):
	for j in range(len(l)):

		for i in range(len(l)-1):
			if l[i]>l[i+1]:
				temp=l[i]
				l[i]=l[i+1]
				l[i+1]=temp

				
		
	print("sorted list: ",l) 
	
l=list(map(int,input("Enter element separted by space: ").split()))
bubble_sort(l)