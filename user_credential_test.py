import  unittest
from  user_credential import User, Credentials

class TestUser(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('Abzed','Abzed1z0')
        
    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'Abzed')
        self.assertEqual(self.new_user.password,'Abzed1z0')
        
    def test_save_user(self):
        """
        test case to check if the user has been saved
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class
    """ 
    
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credentials = Credentials('Instagram','Abzed','Abzed1z0')
        
    def  test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credentials.account_name,'Instagram')
        self.assertEqual(self.new_credentials.username,'Abzed')
        self.assertEqual(self.new_credentials.password,'Abzed1z0')
        
    def test_save_credentials(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
        
    def test_save_multiple_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Abzed','Abzedar2')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Abzed','Abzedar2')
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_credentials(self):
        """
        test to check if we can find credential using account name
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Abzed','Abzedar2')
        test_credentials.save_credentials()
        found_credentials = Credentials.find_account_name('Twitter')
        self.assertEqual(found_credentials.account_name,test_credentials.account_name)
        
    def test_credentials_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Abzed','Abzedar2')
        test_credentials.save_credentials()
        credentials_exist = Credentials.credentials_exist('Twitter')
        self.assertTrue(credentials_exist)
        
    def display_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
        
        
        
if __name__ == '__main__':
    unittest.main()    