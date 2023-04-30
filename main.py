todolist = []
print('Enter a todo: ')

while True:
    user_todo = input()
    todolist.append(user_todo.capitalize())
    break
print(todolist)