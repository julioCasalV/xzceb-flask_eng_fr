import unittest

import translator

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.englishToFrench(None), "Write something")
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.frenchToEnglish(None), "Write something")
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello")
        
unittest.main()