from functions import *  
    
def main():
    continue_loop = True
    choice = str 

    print("Welcome to the Python Currency Exchange!")      
    while continue_loop: 
        print("""Please select an option (a/ b):
        a. Find Currency Code
        b. Exchange Currency""")

        user_choice = input('a/ b: ').strip().lower()
        print('')
        if user_choice == 'a':
            print(search_currency())
        elif user_choice == 'b':
            print(exchange())
        else:
            print('Please enter valid characters!')
        
        again = input("Would you like to use this program again? (y/n): ")
        continue_loop = True if again in ['y', 'yes']  else False
        
    print('\nThanks for using the Python Currency Exchange and see you next time!')

if __name__ == '__main__':
    main()
