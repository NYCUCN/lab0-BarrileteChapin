def myFunction(opt):
    '''
    Write a Python function that return the sum of every digit of your student ID
    And print the answer before you return
    You can write in python2 or python3 :D
    '''
    id=0
    sum=0

    if(opt==1):
        id = str(108006207)
    elif (opt ==2):
        id = str(92644)
    else:
        print("please insert your ID")
        id = str(input())
    

    for i, x in enumerate(id):
	    sum+= int(x)
	   # print(x)

    #printing
    print("The sum is: ", sum)

    return sum


if __name__ == '__main__':
    print("Welcome! Please choose (number) a School to execute the program\n 1) NTHU \n 2) NYCU \n 3)Insert personal id")
    option = int(input())
    myFunction(option)
