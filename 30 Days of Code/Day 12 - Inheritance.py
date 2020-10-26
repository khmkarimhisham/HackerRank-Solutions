class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
		
#Beginning of the answer
		
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        n=len(self.scores)
        a=0
        for i in range(n):
            a += scores[i]
        a /= n 
        if a <= 100 and a >= 90:
            return 'O'
        elif a < 90 and a >= 80:
            return 'E'
        elif a < 80 and a >= 70:
            return 'A'
        elif a < 70 and a >= 55:
            return 'P'
        elif a < 55 and a >= 40:
            return 'D'
        elif a < 40:
            return 'T'
			
#End of the answer

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())