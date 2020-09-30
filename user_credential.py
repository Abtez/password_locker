import random
import string

class User:
    """
    Create User class that generates new instances of a user.
    """
    
    user_list = []
    
    def __init__(self,username,password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password
        
    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)
        
    @classmethod
    
    def user_exist(cls, username,password):
        """
        method to verify whether the user is in our user_list or not
        """
        current_user = ''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                current_user = user.username
        return current_user
        
class Credentials:
    """
    Create credentials class to help create new objects of credentials
    """
    
    credentials_list = []
    
    def __init__(self,account_name,username, password):
        """
        method that defines user credentials to be stored
        """
        self.account_name = account_name
        self.username = username
        self.password = password
    
    
    def save_credentials(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        '''
        delete_account method deletes a  saved credential from the list
        '''
        Credentials.credentials_list.remove(self)
        
    @classmethod
    
    def find_account_name(cls,account_name):
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials
            
    @classmethod
    
    def credentials_exist(cls, account_name):
        """
        method to verify whether the credentilas are in our user_list or not
        """
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True
        return False
    
    @classmethod
    
    def display_credentials(cls):
        """
        method to display all credentials in the credentials list
        """
        return cls.credentials_list
    
    def generate_password(stringLength = 8):
        """
        method to generate random password 8 characters long
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "(|/~!.@,)#{?$[%]^}&*"
        return ''.join(random.choice(password) for i in range(stringLength))