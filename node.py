class daynames():
	
	def __init__(self, dataval = None):
		self.dataval = dataval
		self.nextval = None
		
e1 = daynames("lunes")
e2 = daynames("martes")
e3 = daynames("miercoles")
e4 = daynames("jueves")
e5 = daynames("viernes")

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

thisvalue = e1

while thisvalue:
	print(thisvalue.dataval)
	thisvalue = thisvalue.nextval