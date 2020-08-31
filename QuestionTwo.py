print("**Question no. 2 solution***")
print("by Abhinav Kumar Singh")
def eliminateDuplicates(lst): 
    newlist = []
    for number in lst:
        if number not in newlist:
            newlist.append(number)
    return newlist

def main():
    numbers =(input("Enter numbers separated by space: "))
    x = ((numbers.split()))
    print("The distinct numbers are: ", (eliminateDuplicates(x))) 

main()