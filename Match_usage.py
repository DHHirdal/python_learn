n = int (input("Enter the number from 1 to 7:  "))

match n:
    case 1: print("Sunday")
    case 2: print("Monday")
    case 3: print("Tuesday")
    case 4: print("Wednesday")
    case 5: print("Thursday")
    case 6: print("Friday")
    case 7: print("Saturday")
    case default:
        print("wrong entry")

#========================================================================
# This is like Switch case stament : instead of if-else  and no need to mention "break"
# Use the underscore character "_" as the last case value 
# if you want a code block to execute when there are not other matches:
