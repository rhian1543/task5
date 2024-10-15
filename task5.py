def check_grade(grade):
    if grade <= 100 and grade >= 80:
        return "You did a great Job!"
    elif grade >= 70 and grade <= 79:
          return "Keep it up!"
    elif grade >= 60 and grade <= 69:
         return "You passed, but there's room for it improvement"
    elif grade >= 59:
         return "better lack next time"
    
grade = int(input("enter number"))

print(check_grade(grade))
