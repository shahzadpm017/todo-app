#from functions import get_todos,write_todos
from time import strftime

import functions

new = strftime("%b %d,%Y %H:%M:%S")
print("it is",new)
while True:
    user_input=input("Type add , edit , show ,complete or exit : ")
    user_input=user_input.strip()

    if user_input.startswith("add"):
        todo=user_input[4:]

        todos=functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)



    elif user_input.startswith("show"):

        with open('todos.txt','r') as file:
           todos = file.readlines()

        #new_todos = [item.strip('\n') for item in todos]


        for index,item in enumerate(todos):
            item = item.strip('\n')
            item=item.capitalize()
            row=f"{index+1}-{item}"
            print(row)

    elif user_input.startswith("edit"):
        try:
            number=int(user_input[5:])
            number=number-1

            todos=functions.get_todos()

            new_todo=input("Enter new todo : ")
            todos[number]=new_todo + '\n'

            functions.write_todos( todos)
        except ValueError:
            print("Command not valid")
            continue

    elif user_input.startswith("complete"):
        try:
            number=int(user_input[9:])

            todos=functions.get_todos()

            todo_to_remove=todos[number-1].strip('\n')
            todos.pop(number-1)

            functions.write_todos(todos)


            message=f"todo {todo_to_remove} is completed"
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue

    elif user_input.startswith("exit"):
        break
    else:
        print("command not valid")

print("bye!")