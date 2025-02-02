import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_list_view():
    client = APIClient()
    FAQ.objects.create(question="Test?", answer="Test!")
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert len(response.data) > 0