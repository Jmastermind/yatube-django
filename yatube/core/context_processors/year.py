from datetime import date
from typing import Dict

from django.http import HttpRequest


def year(request: HttpRequest) -> Dict[str, int]:
    """Добавляет переменную с текущим годом.

    Args:
        request: Запрос на рендер элемента.

    Returns:
        Cловарь содержащий переменную с текущим годом.
    """
    del request
    return {
        'year': date.today().year,
    }
