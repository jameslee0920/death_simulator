import unittest
import pytest
from os import path
class UnitTests(unittest.TestCase):

    
    #fake test
    def test_fake(self):
        self.assertTrue(True)
    
    # Each method in the class to execute a test
    #def test_write_fillable_pdf_template(self):
    #    self.assertTrue(path.isfile(template_path))
    #def test_write_fillable_pdf_output(self):
    #    self.assertFalse(path.exists(output_path))
    #def test_write_fillable_pdf_dictionary_values(self):
    #    self.assertTrue(set(data_dict.keys())==set(['introduction','name','description']))

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
