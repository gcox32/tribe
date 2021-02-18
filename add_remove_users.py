import users_mgt as um
import sys

cmd = sys.argv[1]

if cmd == 'create':
    um.create_user_table()
elif cmd == 'add':
    name = input('Username: ')
    pw = input('Password: ')
    email = input('Email: ')
    um.add_user(name, pw, email)
elif cmd == 'show':
    um.show_users()
elif cmd == 'del':
    name = input('User to delete: ')
    print(f'Are you sure you want to delete {name}? (Y/N)')
    confirm = input('(Y/N): ')
    if confirm == 'Y':
        um.del_user(name)
        print(f'Deleted {name}')