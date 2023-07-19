import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)
    
    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        print('')
        print('Creating post_1 and post_2')
        post_1 = TimelinePost.create(name='Diego', email='example@gmail.com', content='This is a test post')
        post_2 = TimelinePost.create(name='John', email='example2@gmail.com', content='This is another test post')
        print('Checking post_1 (Created)')
        assert post_1.id == 1
        assert post_1.name == 'Diego'
        assert post_1.email == 'example@gmail.com'
        assert post_1.content == 'This is a test post'
        print('Checking post_2 (Created)')
        assert post_2.id == 2
        assert post_2.name == 'John'
        assert post_2.email == 'example2@gmail.com'
        assert post_2.content == 'This is another test post'
        print('Deleting post_1')
        post_1.delete_instance()
        print('Checking post_1 (deleted)')
        assert TimelinePost.select().where(TimelinePost.id == 1).count() == 0
        print('Checking post_2 (exists)')
        assert TimelinePost.select().where(TimelinePost.id == 2).count() == 1
        print('Checking post_2 (correct)')