	
#Funcion de angulo 
def angulo_sol(Hora_militar):
	horas, minutos = Hora_militar.split(':') #separar string en 2 ints 
	Horas_=int(horas) + int(minutos)/60   #Cantidad de horas
	if Horas_<= 6.00 or Horas_>=18.00:
		print("No hay sol", "A las ", Hora_militar)
	if Horas_>6.00 and Horas_<=18.00:
		print("Ángulo del sol es ", 15*(Horas_-6), "A las ", Hora_militar)
		
	
angulo_sol("12:30")
angulo_sol("07:00")
angulo_sol("05:55")


	



