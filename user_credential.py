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