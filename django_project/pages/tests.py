from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

class HomepageTerst(SimpleTestCase):
    def setUp(self): # use setUp to change response for each test case
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self): # test statuscode
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):   # test template
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self): # test url
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)