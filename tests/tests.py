import unittest

from translator import englishToFrench, frenchToEnglish

class testTranslator(unittest.TestCase):
    def test_englishToFrench1(self):
        englishText = "Hello"
        expectedFrenchText = "Bonjour"
        translatedFrenchText = englishToFrench(englishText)
        self.assertEqual(translatedFrenchText, expectedFrenchText)

    def test_englishToFrench2(self):
        englishText = "Hello"
        expectedFrenchText = "Salut"
        translatedFrenchText = englishToFrench(englishText)
        self.assertNotEqual(translatedFrenchText, expectedFrenchText)

    def test_frenchToEnglish1(self):
        frenchText = "Bonjour"
        expectedEnglishText = "Good morning"
        translatedEnglishText = frenchToEnglish(frenchText)
        self.assertEqual(translatedEnglishText, expectedEnglishText)

    def test_frenchToEnglish2(self):
        frenchText = "Bonjour"
        expectedEnglishText = "Hello"
        translatedEnglishText = frenchToEnglish(frenchText)
        self.assertNotEqual(translatedEnglishText, expectedEnglishText)

if __name__ == "__main__":
    unittest.main()

