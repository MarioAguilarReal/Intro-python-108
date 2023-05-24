from os import system


class Calculator:

    def __init__(self) -> None:
        select = 0
        while select != 5:
            select = self.print_menu()
            if select is not 5:
                self.operations(select)
            else:
                exit()
            system('pause')
            system('cls')


    def print_menu(self):

        print(f'==========' +
            '\n[1]SUM'+
            '\n[2]SUBSTRACT' +
            '\n[3]MULTIPLY' +
            '\n[4]DIVIDE'+
            '\n[5]EXIT'+
            '\n==========')
        selection = int(input('->'))

        return selection
        

    def operations(self, select):

        num1 = float(input('Type the firt number\n->'))
        num2 = float(input('Type the second number\n->'))

        match select:
            case 1:
                print(f'{num1} + {num2} = {num1 + num2}')

            case 2:
                print(f'{num1} - {num2} = {num1 - num2}')

            case 3:
                print(f'{num1} * {num2} = {num1 * num2}')

            case 4:
                if num2<=0:
                    print('Error, cannot to divide by zero')

                else:
                    print(f'{num1} / {num2} = {num1 / num2}')
            
cal = Calculator()
