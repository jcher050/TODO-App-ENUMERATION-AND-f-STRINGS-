

while True:
    user_action = input("type add, show , edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo: ") + "\n"

            file = open('files/todo.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('files/todo.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('files/todo.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index +1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number the todo to complete"))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")