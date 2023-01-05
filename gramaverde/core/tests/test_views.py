from django.test import TestCase
from django.urls import reverse


class TestArticleListView(TestCase):
    def setUp(self) -> None:
        self.request = self.client.get(reverse("core:index"))

    def test_the_template_name_used(self) -> None:
        self.assertTemplateUsed(self.request, "pages/index.html")
