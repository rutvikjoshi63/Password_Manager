from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()                 #A function which will generate a key after being called
    with open('key.key', 'wb') as key_file :
        key_file.write(key)
'''
def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

print('Welcome to Password Manager')

key =load_key() 
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as file:        #'r' to not mistakenly add in file
        for line in file.readlines():
            data = line.rstrip()         #rstrip specifically to strip \n generated while adding
            user , passw = data.split('|')
            print('User name:', user , ', Password: ', fer.decrypt(passw.encode()).decode())
def add():
    name = input('Enter the Name: ')
    pwd = input('Enter the password: ')
    with open('passwords.txt', 'a') as file:     #with= used here so we can open a file and close at the end of program. 
        file.write(name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")             #Alternatively we can write file = open('passwords.txt', 'a')
                                                # a = append, r= read, w= overwite
while True:
    mode = input('Would you like to view or add passwords? (view/add/quit) ').lower()
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    elif mode == 'quit':
        quit()
    else:
        print('Invalid option')
        pass