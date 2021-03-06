from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox();
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do',self.browser.title)
       # self.fail("Finish the test!")
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text=='1:Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        self.fail('Finish the test')
        
if __name__=='__main__':
    unittest.main(warnings='ignore')

#browser = webdriver.Firefox()
#Edith has heard about a cool new online to-do app  ,she  goes 
#to check out its homepage
#browser.get("http:://localhost:8000")

#she notices the page title and  header mention to-do lists
#assert 'To-Do' in browser.title
#she is invited to enter a to-do item straight away

#she types  "But peacock feathers" into a text box(Edith's hobby )
#is trying fly-fishing lures)

#when she hits enter,the page updates,and now the page lists
#"1:Buy peacock feathers" as an item in a to-do list

#There is still a text box inviting her to add another item ,she 
#enters "Use peacock feathers to make fly " (Edith is very methodical)

#the page updates again ,and now shows both items on her list 

#Edith wonders whether the site will remember hher list.Then she sees 
#that the site has generated a unique URL for her --there is some 
#explanatory text to that effect

#she visits that URL --her to-do list is still there 

#Satisfied, she goes back to sleep
  
#browser.quit()