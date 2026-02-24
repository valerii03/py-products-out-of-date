import datetime
from unittest.mock import patch
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, products, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5), "price": 120},
                {"name": "duck", "expiration_date": datetime.date(2022, 2, 1), "price": 160},
            ],
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 1),
            [
                {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5), "price": 120},
            ],
            [],
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {"name": "salmon", "expiration_date": datetime.date(2022, 1, 10), "price": 600},
                {"name": "chicken", "expiration_date": datetime.date(2022, 1, 5), "price": 120},
            ],
            ["salmon", "chicken"],
        ),
    ],
)
def test_outdated_products(today, products, expected) -> None:
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today
        mock_datetime.date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == expected
