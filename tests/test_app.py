import unittest
import os
os.environ["TESTING"] = "true"

from app import app

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

    def test_timeline(self):
        post = {
            "name": "Diego",
            "email": "example@gmail.com",
            "content": "This is a test"
        }
        print("")
        # Get the posts, should be empty at this
        print("Get the posts, should be empty at this")
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # Add a post
        print("Add a post")
        response = self.client.post('/api/timeline_post', data = post)
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == post["name"]
        assert json["email"] == post["email"]
        assert json["content"] == post["content"]

        # Check that the post was added
        print("Check that the post was added")
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == post["name"]
        assert json["timeline_posts"][0]["email"] == post["email"]
        assert json["timeline_posts"][0]["content"] == post["content"]

        # Check if the post is in the timeline page
        response = self.client.get('/timeline')
        assert response.status_code == 200
        html = response.get_data(as_text = True)
        assert '<div class="timeline-post">' in html
        assert '<div class="timeline-post-content">' in html
        assert '<div class="timeline-post-header">' in html
        assert '<h3>Diego</h3>' in html
        assert '<h4>- example@gmail.com</h4>' in html
        assert '<p>This is a test</p>' in html

        # Delete the post
        print("Delete the post")
        response = self.client.delete('/api/timeline_post', data = dict(
            id=json["timeline_posts"][0]["id"]
        ))
        assert response.status_code == 200
        assert response.get_data(as_text = True) == "OK"

        # Check that the post was deleted
        print("Check that the post was deleted")
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
