todolist = []
print('Enter a todo: ')

user_todo = input()
todolist.append(user_todo.capitalize())

while True:
    print('Do you want to add another todo? yes or no' )
    response = input()
    if response == 'yes':
        new_todo = input('Enter another todo: ')
        todolist.append(new_todo.capitalize())
    elif response == 'no':
        break

print('\n')

print(f'Your todos are: {todolist}')
