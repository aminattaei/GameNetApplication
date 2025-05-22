from django.test import TestCase
from .models import Article
from django.urls import reverse


class ArticleTestView(TestCase):
    def setUp(self):
        pic = "media\articles\chasing-the-northern-lights-px.jpg"
        write_time = "2025-05-02"
        title = "test article"
        content = "this is test for aricle model."
        Article.objects.create(
            pic=pic, write_time=write_time, title=title, content=content
        )

    def test_article_status_code(self):
        resp = self.client.get("/articles/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_name(self):
        resp = self.client.get(reverse("articles_list"))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse("articles_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'Articles/blog-sidebar.html')