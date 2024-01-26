def gpa(full_number, got_number):
    if got_number <= full_number:
        parsent = (got_number*100)/full_number
        if parsent>=91:
            gpa = "5.00" 
            lg = "A+"
        elif 91 > parsent >= 81:
            gpa= "4.00"
            lg="A"
        elif 81 > parsent >= 71:
            gpa= "3.50"
            lg="B"
        elif 71 > parsent >= 61:
            gpa= "3.00"
            lg="C"
        elif 61 > parsent >= 41:
            gpa= "2.00"
            lg="D"
        elif 41 > parsent >= 0:
            gpa= "0.00"
            lg="F"
        return_txt = "Hi student, Your Result is: GPA " + gpa + "\nLetter Grade: " + lg
        return return_txt
    else:
        return "Error"
full_marks = int(input("Full Marks: "))
got_marks = int(input("Got Marks: "))
print(gpa(full_marks, got_marks))
