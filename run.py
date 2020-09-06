#! /usr/bin/env python3
from user_credential import User, Credentials

def create_user(username, password):
    new_user = User(username, password)
    return new_user

def save_user(user):
   user.save_user()

def display_user():
    return User.display_user()

def verify_user(username, password):
     check_user = Credentials.check_user(username,password)
     return check_user
 
def create_credentials(account_name,username, password):
     new_credentials = Credentials(account_name, username, password)
     return new_credentials
 
def save_credentials(credentials):
     credentials.save_credentials()
     
def display_credentials():
    return Credentials.display_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials()
    
def check_credentials(account_name):
    return Credentials.credentials_exist()

def generate_password():
    gen_pwrd = Credentials.generate_password()
    return gen_pwrd

def main():
    print('Welcome to Accounts Management. Use the these commands to proceed: CA = create account, SI = sign in')
    short_code = input().lower()   
    if short_code == 'ca':
        print('Enter new account details')
        print('*' * 100)
        username = input('Enter Username: ')
        while True:
            print('use : GP = to auto generate password... or MP = to manually enter your own password')
            password_choice = input().lower()
            if password_choice == 'mp':
                password = input('Enter Password: ')
                break
            elif password_choice == 'gp':
                password = generate_password()
                break
            else:
                print('Invalid short code. Please try again')
                
        print('*' * 100)
        print(f'Welcome {username} to your new account your password is <--- {password} --->')
        print('*' * 100)

               
        
            
                
                
                
                


if __name__ == '__main__':
    main()