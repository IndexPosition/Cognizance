student_details = [["Roll No","Name","Marks"]]

def records():
    def addrecords():
        Roll_no = int(input("Enter the Roll number : "))
        Name = str(input("Enter the Name of Roll number {} : ".format(Roll_no)))
        Marks = float(input("Enter the Marks of {} : ".format(Name)))
        a=[Roll_no,Name,Marks]
        print("\nAdding the records into the list...\n")
        student_details.append(a)
        for i in range (len(student_details)):
            for j in range(0,3):
                if i == 0:
                    print(student_details[i][j], end = "\t")
                else:
                    print(student_details[i][j], end = "   \t")
            print()
        print()
    addrecords()
    x="y"
    while x=="y":
        x=str(input("Want to add more records? (y/n) : "))
        if x=="y":
            addrecords()
        elif x=="n":
            main()
        else:
            print("Invalid option. Try again...")
        


def main():
    print("\nMenu \n1. Add elements in the list.\n2. Print second record.\n")
    query = int(input("Please choose any option (1-2) : "))
    if query == 1:
        records()
    elif query == 2:
        print("{}\t{}\t{}.".format(student_details[2][0],student_details[2][1],student_details[2][2]))
    else:
        print("Invalid option. Try again...")
        main()

main()
