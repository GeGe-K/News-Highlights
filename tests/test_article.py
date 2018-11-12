import unittest
from app.models import Articles



class TArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("Julia Macfarlane, ABC News", "The European leaders face a rise in alt-right sentiment in their countries",
                                    "https://abcnews.go.com/International/angela-merkel-emmanuel-macron-show-liberal-unity-armistice/story?id=59122446", "https://s.abcnews.com/images/Politics/macron-merkel-gty-er-181111_hpMain_16x9_992.jpg", "2018-11-11T20:17:39Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))



