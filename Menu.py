import types

class Menu:
    def __init__(self, prompt: str = "Make a selection.", options: dict = None) -> None:
        '''
        A menu object facilitates allowing a user to select an option from a provided list.
        
        Parameters
        ----------
        prompt : str
            a string explaining the purpose of the input request
        
        options: dict
            the keys  in this dict are the items the user can enter as input to select
            the corresponding value.
        '''
        self.__prompt = prompt
        self.__options = dict()
        for key, value in options.items():
            self.__options[str(key)] = value
        
    def select(self):
        '''
        This method prompts the user to make a selection from the associated menu.
        If the menu's options are function references, then the function will be run
        as a result of the selection, otherwise, the value associated with the key
        selected by the user will be returned.
        The method detects incorrect input and reintroduces the prompt until valid
        input is provided
        '''

        # this constant is used to extract content from view type objects after converting them to a list
        EXTRACT_CONTENT = 0

        # this loop runs until a valid selection is made or until an exception is raised
        while True:
            # Display the prompt
            print(self.__prompt)

            # Make sure the Menu object has options
            if self.__options:
                # display the list of options to assist the user
                print(f'Options: {[option for option in self.__options.keys()]}\n')

                # the 'selection' to be returned is stored as the value of the option key the user enters
                selection = self.__options.get(input('Your selection: ').lower(), None)

                # if the value of the option key selected is a function, run the function
                if isinstance(selection, types.FunctionType): 
                    return selection()

                # otherwise, if it is valid, return the corresponding value as a variable
                elif isinstance(selection, type(list(self.__options.values())[EXTRACT_CONTENT])): 
                    return selection
                
                # otherwise, explain the error and allow the user to try again
                else: print(f'\nERROR: Your input was not recoginzed, please review the listed options and try again.\nValid selections are {tuple(self.__options.keys())}.')
            
            # if the menu object has no options, raise a Syntax error explaining the problem
            else:
                raise SyntaxError('ERROR: The Menu.select() method can only be run on a Menu with options')
    
    def collect_int(prompt) -> int:
        '''
        This method validates the user input to make sure that the value returned is an integer.

        Parameter
        ---------
        prompt : str
            A prompt explaining the use of the input to the user
        
        Returns
        -------
        int
            The integer entered by the user
        '''

        # this loop will run until an integer is collected
        while True:
            
            # collect the user input
            collected = input(f'{prompt}\nEnter an integer: ')
            
            # only return the input if it is an integer
            if collected.isdecimal():
                
                # return the input as an integer rather than a string
                return int(collected)
            
            # if the input is not an integer, explain the issue and allow the user to try again
            else:
                print(f'\nERROR: Only integers are accepted as valid input!\n')
    
    def collect_number(prompt) -> float:
        '''
        This method allows the user to enter a number with up to a single decimal point.  Otherwise,
        it functions similarly to collect_int.
        Using a comma separator is not supported.

        Parameter:
        ----------
        prompt : str
            A prompt explaining the use of the input to the user
        
        Returns
        -------
        int or float
            The number the user entered
        '''

        # this loop will continue until a valid number is collected
        while True:

            # collect the input from the user
            collected = input(f'{prompt}\nEnter a number: ')

            # if the input is a valid integer, return as an integer
            if collected.isdecimal():
                return int(collected)

            # if the input is a valid float, return as a float
            elif collected.count('.') == 1 and all(substring.isdecimal() for substring in collected.split('.')):
                return float(collected)
            
            # if it is neither, explain the issue and allow the user to try again
            else:
                print(f'\nERROR: Only numbers are accepted as valid input!  Note: comas are not supported.\n')


#######################################################
#Testing code:
#######################################################
if __name__ == '__main__':

    '''
    # Testing Menu().collect_number
    user_number = Menu('Some prompt.').collect_number()
    print(f'\nYou entered a {user_number}, which is a {type(user_number)}.')

    '''
    # Testing Menu().select()
    def choice_1():
        print('(((1)))')

    def choice_2():
        print('<<<2>>>')
    
    #test_1 = lambda: choice_1()
    
    prompt = 'Make a selection:'
    choices = {1: choice_1, 2: choice_2}
    Menu(prompt, choices).select()

    choice_menu = Menu('choose an option: ', {1: 'first one', 2: 'second one'})
    print(f'You picked the {choice_menu.select()}')
    ''' #'''