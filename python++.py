valid_commands = ['print', 'type', 'def', '//', '#']

while True:
    command = input("Type a command or type 'help' for help: ")
    help_topics = ['syntax', 'logical signs']
    
    if command == 'help':
        for i in help_topics:
            print(i)
        help_topic = input("Which one of those do you need help with: ")
        
        if help_topic == 'syntax':
            print("Python++ uses elements of both python and c++ syntax such as:")
            examples = ['semicolons', 'curly brackets', 'def keyword', 'comments']
            for i in examples:
                print(i)
            print('Comments use either // or #, functions use curly brackets, they also use the def keyword to define a function, python++ has lists as well, python++ uses semicolons to tell when the line of code ends!')
        
        if help_topic == 'logical signs':
            print("python++ uses both the logical and, not, and or and the python and not and or")
            examples = ['&&', '||', '!=', 'and', 'not', 'or']
            for i in examples:
                print(i)
    
    if command.startswith('print'):
        if ';' in command[-1]:
            print_value = input("What do you want to print: ")
            print(print_value)
        else:
            print(command[6:])
    
    if command.startswith('type'):
        if ';' not in command:
            print("Command does not contain semicolon. Please enter command with semicolon.")
        else:
            command_parts = command.split(';')
            if len(command_parts) != 2:
                print("Invalid command format. Please enter a command with one semicolon.")
            else:
                data_type = command_parts[0].strip().lower()
                value = command_parts[1].strip()
                if data_type == 'int':
                    if value.isdigit():
                        enter_number = int(value)
                        if enter_number in range(1, 1000000000):
                            print("The entered value is an integer.")
                        else:
                            print("The entered value is not an integer in the range of 1 to 1,000,000,000.")
                    else:
                        print("The entered value is not a valid integer.")
                elif data_type == 'bool':
                    if value.lower() == 'true' or value.lower() == 'false':
                        enter_bool = bool(value)
                        print("The entered value is a boolean.")
                    else:
                        print("The entered value is not a valid boolean.")
                elif data_type == 'str':
                    print("The entered value is a string.")
                else:
                    print("Invalid data type. Please enter 'int', 'bool', or 'str'.")
