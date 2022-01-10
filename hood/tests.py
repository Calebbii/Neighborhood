from django.test import TestCase
from .models import Business,Profile,Neighborhood,Post
from hood.views import neighborhood
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Caleb', password='Access')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

# class NeighborhoodTestClass(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(id=1, username='Caleb')
#         self.neighborhood = Neighborhood.objects.create(id=1, name='Kapsoya', description='Kapsoya estate is one of the oldest suburbs in Eldoret.',neighborhood_logo='https://cloudinary url',user=self.user,email='cal@gmail.com')
#         self.neighborhood.save()

#     def test_create_neighborhood(self):
#         self.neighborhood.create_neighborhood()
#         neighborhood = Neighborhood.objects.all()
#         self.assertTrue(len(neighborhood) > 0)

#     def test_get_neighborhood(self, id):
#         self.neighborhood.save()
#         neighborhood = Neighborhood.get_neighborhood(neighborhood_id=id)
#         self.assertTrue(len(neighborhood) == 1)

# class PostTestClass(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(id=1, username='Josh')
#         self.neighborhood = Neighborhood.objects.create(id=1, name='home')
#         self.post = Post.objects.create(id=1, title='Falling Rocks', post='Be aware of rocks falling down hill after heavy rains',image='https://cloudinary url',post_date='2022,1,2',user=self.user,neighborhood=self.neighborhood)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.post, Post))

#     def test_display_posts(self):
#         self.post.save()
#         posts = Post.all_posts()
#         self.assertTrue(len(posts) > 0)

#     def test_save_post(self):
#         self.post.save_post()
#         post = Post.objects.all()
#         self.assertTrue(len(post) > 0)

#     def test_delete_post(self):
#         self.post.delete_post()
#         post = Post.search_post('random_post')
#         self.assertTrue(len(post) < 1)

# class BusinessTestClass(TestCase):
#   def setUp(self):
#     self.user = User.objects.create(id=1, username='Caleb')
#     self.neighborhood = Neighborhood.objects.create(id=1, name='home')
#     self.busines = Business.objects.create(id=1, name='Farm Fresh', description='Best Grocery Shop in the estate',neighborhood=self.neighborhood,user=self.user,email='cal@gmail.com',image='https://cloudinary url')

#   def test_instance(self):
#     self.assertTrue(isinstance(self.busines, Business))

#   def test_create_business(self):
#     self.busines.create_business()
#     business = Business.objects.all()
#     self.assertTrue(len(business) > 0)

#   def test_get_business(self, id):
#     self.business.save()
#     business = Business.get_businesss(post_id=id)
#     self.assertTrue(len(business) == 1)
