import random
from django.test import TestCase

class GttCi(TestCase):
    resp_code = 200
    random_chars = [" ", " not", " ", " not ", " ", " ", " ", " not ", " ", " ", " ", " not ", " ", " ", " ", " not "]
    resp_text1 = "This is not an acceptable response."
    resp_text2 = "This is{}an acceptable response.".format(random.choice(random_chars))

    def test_response_code(self):
        self.assertEquals(self.resp_code, 200)

    def test_response_text(self):
        print(self.resp_text2)
        self.assertNotEquals(self.resp_text1, self.resp_text2)
