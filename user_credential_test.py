import  unittest
from  user_credential import User, Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Abzed','Abzed1z0')
        
    def test_init(self):
        self.assertEqual(self.new_user.username,'Abzed')
        self.assertEqual(self.new_user.password,'Abzed1z0')
        
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.new_credentials = Credentials('Instagram','Abzed','Abzed1z0')
        
        
        
if __name__ == '__main__':
    unittest.main()    