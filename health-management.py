print("******* HEALTH MANAGEMENT SYSTEM *******")

def getdate():
	"""This will give the date and time of entering"""
	import datetime
	return datetime.datetime.now()

storea = "\n"+"["+str(getdate())+"]"+"\t"


#Log
while(True):
	print("\nwhat you want to do?\nfor log(1)\nfor retrieving(2)")
	choicea = int(input("Enter from (1, 2):"))
	
	if choicea==1:
		print("\nFor whom do you want to log?\nharry(1)\nrohan(2)\nhammad(3)")
		choiceb = int(input("Enter from (1, 2, 3):"))
	
				#harry
		if choiceb==1:
			print("\nwhat do you want to log?\nfor exercise(1)\nfor diet(2)")
			choicec = input("Enter from (1, 2):")
			
			#exercise for harry
			if choicec==1:
				exharry = input("Enter it below:\n")
				f1 = open("/sdcard/python3/main/exercise/harry.exercise","a")
				f1.write(storea+exharry)
				f1.close()
				choiced  = int(input("you have successfully entered the data,do you want to continue\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
			#diet for harry
			else:
				dharry = input("Enter it below:\n")
				f2 = open("/sdcard/python3/main/diet/harry.diet","a")
				f2.write(storea+dharry)
				f2.close()
				choiced  = int(input("you have successfully entered the data,do you want to continue\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
				
		#rohan
		elif choiceb==2:
			print("\nwhat do you want to log?\nfor exercise(1)\nfor diet(2)")
			choicec = int(input("Enter from (1, 2):"))
			
			#exercise for rohan
			if choicec==1:
				exrohan = input("Enter it below:\n")
				f1 = open("/sdcard/python3/main/exercise/rohan.exercise","a")
				f1.write(storea+exrohan)
				f1.close()
				choiced  = int(input("you have successfully entered the data,do you want to continue\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
			#diet for rohan
			else:
				drohan = input("Enter it below:\n")
				f2 = open("/sdcard/python3/main/diet/rohan.diet","a")
				f2.write(storea+drohan)
				f2.close()
				choiced  = int(input("you have successfully entered the data,do you want to continue\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
	
		#hammad
		else:
			print("\nwhat do you want to log?\nfor exercise(1)\nfor diet(2)")
			choicec = int(input("Enter from (1, 2):"))
			
			#exercise for hammad
			if choicec==1:
				exhammad = input("Enter it below:\n")
				f1 = open("/sdcard/python3/main/exercise/hammad.exercise","a")
				f1.write(storea+exhammad)
				f1.close()
				choiced  = int(input("you have successfully entered the data,do you want to continue\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
			#diet for hammad
			else:
				dhammad = input("Enter it below:\n")
				f2 = open("/sdcard/python3/main/diet/hammad.diet","a")
				f2.write(storea+dhammad)
				f2.close()
				choiced  = int(input("you have successfully entered the data,do you want to continue\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
	
	#Retrieve
	else:
		print("for whom do you want to retrieve the data?\nharry(1)\nrohan(2)\nhammad(3)")
		choicef = int(input("Enter (1, 2, 3):"))
		#harry
		if choicef==1:
			print("\nDo  you want to retrieve\nfor exercise(1)\nfor diet(2)")
			choiceg = int(input("Enter from(1, 2)"))
			#exercise for harry
			if choiceg==1:
				f1 = open("/sdcard/python3/main/exercise/harry.exercise")
				print(f1.read())
				f1.close()
				choiced  = int(input("\nDo you want to rerun the program\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
			#diet for harry
			else:
				f1 = open("/sdcard/python3/main/diet/harry.diet")
				print(f1.read())
				f.close()
				choiced  = int(input("\nDo you want to rerun the program\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
		
		#rohan
		elif choicef==2:
			print("\nDo you want to retrieve\nfor exercise(1)\nfor diet(2)")
			choiceg = int(input("Enter from(1, 2)"))
			#exercise for rohan
			if choiceg==1:
				f1 = open("/sdcard/python3/main/exercise/rohan.exercise")
				print(f1.read())
				f1.close()
				choiced  = int(input("\nDo you want to rerun the program\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
			#diet for rohan
			else:
				f1 = open("/sdcard/python3/main/diet/rohan.diet")
				print(f1.read())
				f1.close()
				choiced  = int(input("\nDo you want to rerun the program\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break

		#hanmad
		else:
			print("\nDo you want to retrieve\nfor exercise(1)\nfor diet(2)")
			choiceg = int(input("Enter from(1, 2)"))
			#exercise for hammad
			if choiceg==1:
				f1 = open("/sdcard/python3/main/exercise/hammad.exercise")
				print(f1.read())
				f1.close()
				choiced  = int(input("\nDo you want to rerun the program\n continue(1)\n over(2)"))
				if choiced==1:
					continue
				else:
					break
			#diet for rohan
			else:
				f1 = open("/sdcard/python3/main/diet/hammad.diet")
				print(f1.read())
				f1.close()
				choiced  = int(input("\nDo you want to rerun the program\n continue(1)\n over(2)\n:"))
				if choiced==1:
					continue
				else:
					break
