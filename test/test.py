from prettytable import PrettyTable
student_list = []
while True:
    new_entry_list  =  []
    name = input ( "enter your name:" )
    
    Class = input ( "enter your class (cse / csbs)" )
    
    rep_before = input ( "have you ever been representative before:" )
    
    cgpa_in_previous_semester  =  float ( input ( "cgpa_in_previous_semester:" ))

    responsibilities_in_college=list(map(str, input("responsibilities in college").split()))
    
    new_entry_list.extend ( [name , Class , rep_before , cgpa_in_previous_semester , responsibilities_in_college] )

    student_list.append(new_entry_list)
    continue_registration = bool ( input ( " continue " ) )
    
    if continue_registration:
        student_registered=PrettyTable ( [ " Name " , " Class ", " Rep_Before " , " CGPA " , " Responsibilities " ])

        for student in student_list:
            student_registered.add_row(student)
        print ( student_registered )
        break

