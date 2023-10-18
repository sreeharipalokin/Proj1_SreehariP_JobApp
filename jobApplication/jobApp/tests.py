from django.test import TestCase
import re

# Create your tests here.
class NamevalidationTest(TestCase):

    def validateNameTest(self):
        fullname = "John Snow"
        v = re.findall('/^[a-zA-Z ]+$/',fullname)
        asserIs(v,True)   
        