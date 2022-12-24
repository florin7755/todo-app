def get_todos(filepath="todos.txt"):   #file path is the argument for get_todos function
    #filepath="todos1.txt"
    with open(filepath, 'r') as file_local:
         todos_local=file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):   #filepath and todos are local variables
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action=input("Type add, show, edit,complete or exit: ")  #for input function the argument is what is into parantheses
    user_action=user_action.strip()

    if user_action.startswith("add"):
       todo=user_action[4:]

       todos=get_todos()  #filepath =argument and todos.txt=value of argument

       todos.append(todo + '\n')

       #write_todos(filepath="todos.txt", todos_arg=todos)
       write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):  #print(index, item)
             item=item.strip('\n') #delete empty rows beetwin lines
             row=f"{index +1}-{item}"
             print(row)

    elif user_action.startswith('edit'):
        try:
           number=int(user_action[5:])
           print(number)

           number=number-1

           todos=get_todos()

           new_todo=input("Enter a new todo: ")
           todos[number]=new_todo + '\n'

           write_todos("todos.txt", todos)
        except ValueError:
           print("Your command is not valid.")
           continue
    elif user_action.startswith('complete'):
        try:
            number=int(user_action[9:])
            todos=get_todos()
            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt" ,todos)

            message=f"Todo {todo_to_remove} was remove from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
         print("command is not valid.")

print("Bye!")