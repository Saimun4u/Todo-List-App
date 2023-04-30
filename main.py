todolist = []
print('Enter a todo: ')

user_todo = input()
todolist.append(user_todo.capitalize())

while True:
    print('Do you want to add another todo? yes or no' )
    response = 'yes' or 'no'
    if response == 'yes':
        user_todo = input('Enter a todo: ')
        todolist.append(user_todo.capitalize())
    break

print(f'Your todos are: {todolist}')
