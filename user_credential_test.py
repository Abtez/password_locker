import  unittest
from  user_credential import User, Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Abzed',' Abzed1z0')
        
    def test_init(self):
        self.assertEqual(self.new_user.username,'Abzed')
        self.assertEqual(self.new_user.password,'Abzed1z0')