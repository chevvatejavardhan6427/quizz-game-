options=(("A)india","B)chile","C)china","D)france"),
('A)112','B)113','C)114','D)118'),
("A)Russia","B)india","C)china","D)america"))
guesses=[]
answers=["B","D","A"]
score=0
question_number=0
questions=["Longest country in the world",
"How many elements are present in modern PT",
"largest country in the world"]
for question in questions:
	print(question)
	print()
	for option in options[question_number]:
		print(option)
	guess=input("choose in A,B,C,D : ").upper()
	if guess==answers[question_number]:
		score+=1
		print("CORRECT")
		
	else:
		print("INCORRECT")
		print(f"CORRECT ANSWER IS {answers[question_number]}")
	question_number+=1
	print("---------------------------------------------------")
	
print()
percentage=score/len(questions)*100
print(f"your percentage is {round(percentage,2)}%")	
