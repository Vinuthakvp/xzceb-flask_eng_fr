import unittest
import translator

class Test_translator(unittest.TestCase):
    """
    Class to test translator module
    """
    def test_english_to_french_equal(self):
        """
        Test english to french translation
        """
        translationText = "Hello"
        frenchText = translator.english_to_french(translationText)
        self.assertEqual(frenchText,"Bonjour","Equal")

    def test_english_to_french_notequal(self):
        """
        Test english to french translation
        """
        translationText = "welcome"
        frenchText = translator.english_to_french(translationText)
        self.assertNotEqual(frenchText,"Bonjour","Not Equal")

    def test_french_to_english_equal(self):
        """
        Test french to english translation
        """
        translationText = "Bonjour"
        englishText = translator.french_to_english(translationText)
        self.assertEqual(englishText,"Hello","Equal")

    def test_french_to_english_notequal(self):
        """
        Test french to english translation
        """
        translationText = "welcome"
        englishText = translator.french_to_english(translationText)
        self.assertNotEqual(englishText,"Hello","Not Equal")

if __name__ == '__main__':
    unittest.main()
    