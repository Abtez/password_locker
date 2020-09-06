class User:
    
    user_list = []
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def save_user(self):
        User.user_list.append(self)
        
class Credentials:
    
    credentials_list = []
    
    def __init__(self,account_name,username, password):
        self.account_name = account_name
        self.username = username
        self.password = password
    
    
    def save_credentials(self):
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        Credentials.credentials_list.remove(self)
        
    @classmethod
    
    def find_account_name(cls,account_name):
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials
            
    @classmethod
    
    def credentials_exist(cls, account_name):
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True
        return False
    
    @classmethod
    
    def display_credentials(cls):
        return cls.credentials_list