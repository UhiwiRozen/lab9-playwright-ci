import pytest

APP_URL = "http://127.0.0.1:8000/delivery.html"


@pytest.fixture
def delivery_page(page):
    page.goto(APP_URL)
    return page
