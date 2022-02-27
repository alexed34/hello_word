l = []

def get_list():
	global l
	if len(l) == 0:
		l = input().split()	
	if len(l) == 0:
		get_list()

def Int():
	global l
	get_list()
	return int(l.pop(0))
	
def Float():
	global l
	get_list()
	return float(l.pop(0))

def Char():
	global l
	get_list()
	return l.pop(0)[0]

def String():
	global l
	get_list()
	return l.pop(0)

def Line():
	return input()