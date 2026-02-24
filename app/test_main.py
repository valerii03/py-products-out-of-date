import datetime
from unittest.mock import patch

from app.main import outdated_products


def test_outdated_products_some_outdated() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160,
        },
    ]

    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == ["duck"]


def test_outdated_products_none_outdated() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
    ]

    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
        mock_datetime.date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == []


def test_outdated_products_all_outdated() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 1, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 1, 5),
            "price": 120,
        },
    ]

    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == ["salmon", "chicken"]
