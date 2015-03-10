#Aman Mangalore
#aamangal
#programming assignment 5
#prints out all the verses of ant.txt
def antsprinter():
	for i in range (10):
		print ("The ants go marching {} by {}, hurrah! Hurrah!".format(i+1, i+1))
		print ("The ants go marching {} by {}, hurrah! Hurrah!".format(i+1, i+1))
		print ("The ants go marching {} by {},".format(i+1, i+1))
		actions(i)
		print ("And they all go marching down...")
		print ("In the ground...")
		print ("To get out...")
		print ("Of the rain.")
		print ("Boom! Boom! Boom!")	
def actions(int):
	theactions = ['suck his thumb', 'tie his shoe', 'climb a tree', 'shut the door', 
				  'take a dive', 'pick up sticks', 'look up to heaven', 'shut the gate', 
				  'check the time', 'say the end']
	print ("The little one stops to %s," %theactions[int])
antsprinter()
