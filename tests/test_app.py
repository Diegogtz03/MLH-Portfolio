import unittest
import os
os.environ["TESTING"] = "true"

from app import app, TimelinePost, mydb

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/welcome')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<span class="prevent-select" id="welcome-span">Welcome</span><br>' in html
        assert '<span class="prevent-select" id="name-span">Diego</span><br>' in html
        assert '<span class="prevent-select" id="name-span">Gutierrez' + "'s</span><br>" in html
        assert '<span class="prevent-select" id="subtitle-span">Journey</span><br>' in html
