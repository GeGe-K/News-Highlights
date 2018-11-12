import unittest
from app.models import Sources


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("al-jazeera-english", "Al Jazeera English", "News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.",
                                  "http://www.aljazeera.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_init(self):
            '''
            test_init to ensure objects are instantiated correctly
            :return:
            '''
            self.assertEqual(self.new_source.id, "al-jazeera-english)
            self.assertEqual(self.new_source.name, "Al Jazeera English")
            self.assertEqual(self.new_source.description,
                             'News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.')
            self.assertEqual(self.new_source.url, "http://www.aljazeera.com")
