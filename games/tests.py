from django.test import TestCase
from django.urls import reverse
from datetime import date

from .models import Game


class GameTestView(TestCase):
    def setUp(self):
        self.game = Game.objects.create(
            title="Test Game",
            launch_date=date(2025, 5, 6),
            price=140000,
            rating=7,
            stars=5,
            download_link="#",
            pic="media/Games/pictures/2e116631-ca61-408d-b132-1af757a863a7.png",
            media="media/Games/media/360_F_122363039_sWnWRkYn2Z1aCX9XMExlsq3cL95GsHEa.jpg",
            description="این یه تست است...",
        )

    def test_create_new_game(self):
        game = Game.objects.get(id=self.game.pk)
        self.assertEqual(game.price, 140000)
        self.assertEqual(game.stars, 5)

     

    def test_game_detail_pattern(self):
        response = self.client.get(reverse("game_detail", args=[self.game.pk]))
        self.assertEqual(response.status_code, 200)
