#This code tests a person on their mathematical knowledge as well as history facts
import random
counter = 0
counter2 = 0

#Introducing User to Program
print("Welcome to the Math and History Tester! Whats your name?")
name = input("Name: ")
print("Hello " + name + ", to take the Math Quiz, type '1'. To take the History Quiz, type '2'.")
quiz = int(input("Which test do you wish to take: "))

#Lists for Math Quiz
mathTerm = []
for i in range (1, 30):
  mathTerm.append(random.randint(1,100))

#Lists for History Quiz
historyQuestions = ["What American President got Stuck in a Bathtub?", "Who is credited to be the first king of England, ruling from 802 to 839?", "What year was slavery abolished in the USA?", "Was Alexander the Great Buried Alive? (Yes or No)", "Who did England fight in the Hundred Years War?", "What year did D-Day take place in World War II?", "Who was the first explorer to circumnavigate the globe?", "Who created the printing press?", "What year did the first astronaut reach space?", "What Started World War 1?"]
historyAnswers = ["William Howard Taft", "King Egbert", "1865", "Yes", "France", "1944", "Ferdinand Magellen", "Johannes Gutenburg", "1961", "A Sandwich"]

#Math Quiz
if (quiz == 1):

  def math1(term1, term2):
    answer = term1 + term2
    return answer

  def math2(term1, term2):
    answer = term1 - term2
    return answer

  
  def mathAnswer2(mathType, term1, term2, userAnswer):
    if (mathType(term1,term2) == userAnswer): 
      responseCorrect = ["Nice!", "Amazing!", "Epic!", "Cool!", "Dope.", "Cheerio", "Fire!!", "Clip that!!"]
      responseCounter = 0
      for i in range(random.randint(1, 5), random.randint(5, 8)):
          responseCounter = responseCounter + 1
      print(responseCorrect[responseCounter] +"\n")
    else:
      print("Incorrect. The correct answer is: " + str(mathType(term1, term2)) + "\n")

  questionNumber = 0
  for o in range (1, 11):
    mathType = random.randint(1,3)

#Addition Problems
    if (mathType == 1):
      questionNumber = questionNumber + 1
      term1 = mathTerm[random.randint(0,28)] 
      term2 = mathTerm[random.randint(0,28)]
      print("Question #" + str(questionNumber) + ":\n" + str(term1) + " + " + str(term2))
      userAnswer = int(input("Answer to Question #" + str(questionNumber) + ": "))
      mathAnswer2(math1, term1, term2, userAnswer)
      if (term1+term2 == userAnswer): 
          counter = counter + 1

#Subtraction Problems
    if (mathType == 2):
      questionNumber = questionNumber + 1
      term1 = mathTerm[random.randint(0,28)] 
      term2 = mathTerm[random.randint(0,28)]
      print("Question #" + str(questionNumber) + ":\n" + str(term1) + " - " + str(term2))
      userAnswer = int(input("Answer to Question #" + str(questionNumber) + ": "))
      mathAnswer2(math2,term1,term2, userAnswer)
      if (term1-term2 == userAnswer): 
          counter = counter + 1
#Multiplication Problems
    if (mathType == 3):
      questionNumber = questionNumber + 1
      term1 = mathTerm[random.randint(0,28)] 
      term2 = mathTerm[random.randint(0,28)]
      print("Question #" + str(questionNumber) + ":\n" + str(term1) + " x " + str(term2))
      userAnswer = int(input("Answer to Question #" + str(questionNumber) + ": "))
      if (term1*term2 == userAnswer): 
          counter = counter + 1
          print(" Correct!\n")
      else:
          print("Incorrect. The correct answer is: " + str(term1*term2) + "\n")

#Score Counter
    if (questionNumber == 10):
          print("You got " + str(counter) + " out of 10 right!!")

#History Quiz
if(quiz == 2):
  questionNumber = 1
  for o in range (0,10):
    print("Question #" + str(questionNumber) + ":\n" + historyQuestions[counter2])
    userAnswered = input("Answer to Question #" + str(questionNumber) +": ")
    if (userAnswered == historyAnswers[counter2]):
      print("Correct!\n")
      counter = counter + 1
      counter2 = counter2 + 1
      questionNumber = questionNumber + 1
    else:
      print("Incorrect! The correct answer is " + historyAnswers[counter2] +".\n")
      counter2 = counter2 + 1
      questionNumber = questionNumber + 1
    if (questionNumber == 11):
       print("You got " + str(counter) + " out of 10 right!!")
