def average(x):
	averageValue = sum(x)/len(x)
	return averageValue

#print average([0,87,75,22])
def getAverage(d):
	averageHomework = average(d["homework"])*.1
	avergeQuizzes = average(d["quizzes"])*.3
	averageTests = average(d["tests"])*.6
	weightedAverage = 0
	weightedAverage += averageHomework
	weightedAverage += avergeQuizzes
	weightedAverage += averageTests
	return weightedAverage

	
Tyler = {
        "name":"Tyler",
        "homework": [0,87,75,22],
        "quizzes": [0,75,78],
        "tests": [100,100]
        }
Lloyd = {
    "name":"Lloyd",
    "homework": [90,97,75,92],
    "quizzes": [ 88,40,94],
    "tests": [ 75,90]
    }
Alice = {
    "name":"Alice",
    "homework": [100,92,98,100],
    "quizzes": [82,83,91],
    "tests": [89,97]
    }

print getAverage(Tyler)

def getLetterGrade(score):
	score = round(score)
	if score >= 90:
		return 'A'
	if score >= 80:
		return 'B'
	if score >= 70:
		return 'C'
	if score >= 60:
		return 'D'
	if score < 60:
		return 'F'
	
print getLetterGrade(getAverage(Tyler))

students = [Lloyd,Alice,Tyler]

def getClassAverage(cl):
	totalScore = 0
	for student in cl:
		totalScore += getAverage(student)
	return totalScore/len(cl)
	
   



print getClassAverage(students)
		