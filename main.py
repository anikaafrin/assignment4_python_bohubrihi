def gpa(full_number, got_number):
    if got_number <= full_number:
        parsent = (got_number*100)/full_number
        if parsent>=80:
            gpa = "5.00" 
            lg = "A+"
        elif 80 > parsent >= 70:
            gpa= "4.00"
            lg="A"
        elif 70 > parsent >= 60:
            gpa= "3.50"
            lg="A-"
        elif 60 > parsent >= 50:
            gpa= "3.00"
            lg="B"
        elif 50 > parsent >= 40:
            gpa= "2.00"
            lg="C"
        elif 40 > parsent >= 33:
            gpa= "1.00"
            lg="D"
        elif  parsent<33 :
            gpa= "0.00"
            lg="F"
        return_txt = "Hi student, Your Result is: GPA " + gpa + "\nLetter Grade: " + lg
        return return_txt
    else:
        return "Error"
full_marks = int(input("Full Marks: "))
got_marks = int(input("Got Marks: "))
print(gpa(full_marks, got_marks))