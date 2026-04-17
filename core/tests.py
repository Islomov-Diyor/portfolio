from django.test import TestCase, Client
from .models import HeroSection, AboutSection, ContactInfo, ContactMessage


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        HeroSection.objects.create(
            pk=1, name="TEST", badge="TAYYOR", desc="desc",
            btn1_text="b1", btn2_text="b2", roles="Dev"
        )
        AboutSection.objects.create(
            pk=1, bio_uz="uz", bio_en="en",
            stat_years=1, stat_students=1, stat_projects=1
        )
        ContactInfo.objects.create(
            pk=1, github="#", telegram="#", linkedin="#",
            email="test@test.com", location="UZ", youtube="#"
        )

    def test_index_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_context_has_hero(self):
        response = self.client.get('/')
        self.assertIn('hero', response.context)
        self.assertEqual(response.context['hero'].name, 'TEST')

    def test_contact_form_post_saves_message(self):
        response = self.client.post('/', {
            'name': 'Ali',
            'email': 'ali@test.com',
            'message': 'Salom!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.first().name, 'Ali')

    def test_invalid_form_does_not_save(self):
        self.client.post('/', {
            'name': '',
            'email': 'notanemail',
            'message': '',
        })
        self.assertEqual(ContactMessage.objects.count(), 0)
