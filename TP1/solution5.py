def letter_grade(score):
    if score>=97 and score <100:
        return "A+"
    elif score<97 and score >=90:
        return "A"
    elif score <90 and score >=80:
        return "B"
    elif score <80 and score >=70:
        return "C"
    elif score < 70 and score >=60:
        return "D"
    elif score < 60 and score >=0:
        return "F"
    else:
        return "INVALID"

for i in [99, 90, 85, 72, 60, 59.9, -5, 101]:
    print(i,"->", letter_grade(i))