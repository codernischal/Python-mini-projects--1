import time


#Starting
class Contestant:

  def __init__(self):
    self.name = input("Enter your name : ")
    print(f"\nWECOME TO Kaun Banega Crorepati MR.{self.name}\n")
    time.sleep(1)
    print(
      "Rules:\n Questions will be displayed one after another.\nYou have to choose and type any one option index.Such as a/a/c/d\n\n"
    )
    time.sleep(2)
    input("Press any key to start")
    time.sleep(3)
    print("********Lets Start******\n")


#Main operation
class Contest:
  #All the prizes are displayed here
  #All the available question are displayed here
  questions = [{
    "question": "What is the capital of France?",
    "answers": ["A)Paris", "B)London", "C)Berlin", "D)Rome"],
    "correct_answer": "A"
  }, {
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  }, {
    "question":
    "Who was the first person to walk on the moon?",
    "answers": ["A)Neil Armstrong", "B)Michael Collins", "C)Edwin \"Buzz\" Aldrin", "D)Mt.Alps"],
    "correct_answer":
    "A"
  }, {
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  }, 
  {
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  }, {
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  },{
    "question":
    "Which is the largest ocean in the world?",
    "answers": [
      "A)Indian Ocean", "B)Atlantic Ocean", "C)Pacific Ocean", "D)Arctic Ocean"
    ],
    "correct_answer":
    "C"
  }]
  score = 0

  #here the question displays and evaluation starts
  def __init__(self):
    #Questions display iteration
    for qn in self.questions:
      print(qn['question'])
      for i in qn['answers']:
        print(i)
      #Answer Evaluation
      self.user_answer = input("Enter your answer: ").upper()
      if self.user_answer == qn['correct_answer']:
        print('Correct Answer!!!!!\n')
        self.score += 1
      else:
        print("Incorrect\n")
        break

  def result(self):
    print(f"You scored {self.score} and earned Rs{self.score*1000}")


a = Contestant()
time.sleep(1)
b = Contest()
b.result()
