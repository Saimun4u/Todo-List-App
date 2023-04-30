todolist = []
print('Enter a todo: ')

user_todo = input()
todolist.append(user_todo.capitalize())

while True:
    print('Do you want to add another todo? y-yes or n-no' )
    response = input()
    if response == 'y':
        new_todo = input('Enter another todo: ')
        todolist.append(new_todo.capitalize())
    elif response == 'n':
        break
    else:
        print('Enter a valid response y or n')
    

print('\n')
print('---------------------------')
print('\n')
print(f'Your todos are: {todolist}')
