'''
@ Elena Voinu
Program that calculates calories burned in a certain amount of minutes 
that user inputs. User inputs minutes on one line sparated by spaces, the program
stores those values in a list and displays the result. For example
Input: 10 15 20 25 30
Output will be: Calories burned in 10 minutes: 39.0
                Calories burned in 15 minutes: 58.5
                Calories burned in 20 minutes: 78.0
                Calories burned in 25 minutes: 97.5
                Calories burned in 30 minutes: 117.0
'''
                
answer = 'y'
while answer == 'y':
    try:
        # Get user input for minutes
        minutes = input("Enter minutes separated by spaces: ")

        # Split minutes into separate strings
        tokens = minutes.split()

        # Convert strings to integers
        nums = []
        for t in tokens:
            nums.append(int(t))
        
        for num in nums:
            # multiply the values in the list by 3.9 and round them
            cal_burn =round(num * 3.9, 2) 
            # dislay the result
            print("Calories burned in", num, "minutes:",cal_burn)
            
    except ValueError:
        print("Invalid input. Try typing ONLY whole numbers next time...")
    
    print("Run again?")
    answer = input("Enter 'y' to run again or any key to quit: ")
    
print("________________________________________")
print("Exiting Program...")
print("Thank You For Using Our Services Today!")
        



