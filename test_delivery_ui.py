import pytest
from playwright.sync_api import expect


def calculate(page, amount, zone="city"):
    page.get_by_test_id("amount").fill(amount)
    page.get_by_test_id("zone").select_option(zone)
    page.get_by_test_id("calc").click()
    return page.get_by_test_id("result")


@pytest.mark.parametrize("amount, zone, delivery, total", [
    ("0", "city", 1000, 1000),
    ("9999", "city", 1000, 10999),
    ("10000", "city", 0, 10000),
    ("10001", "city", 0, 10001),
    ("0", "region", 2000, 2000),
    ("9999", "region", 2000, 11999),
    ("10000", "region", 0, 10000),
    ("10001", "region", 0, 10001),
])
def test_delivery_cost(delivery_page, amount, zone, delivery, total):
    result = calculate(delivery_page, amount, zone)
    expect(result).to_have_text(
        f"Доставка: {delivery} тенге; итого: {total} тенге"
    )


@pytest.mark.parametrize("amount, message", [
    ("-1", "Ошибка: сумма не может быть отрицательной"),
    ("12.5", "Ошибка: введите целую сумму"),
    ("abc", "Ошибка: введите целую сумму"),
    ("", "Ошибка: введите целую сумму"),
], ids=["negative", "fraction", "letters", "empty"])
def test_invalid_amount(delivery_page, amount, message):
    result = calculate(delivery_page, amount)
    expect(result).to_have_text(message)
    expect(result).to_have_class("error")
