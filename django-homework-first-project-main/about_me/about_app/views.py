from django.shortcuts import render
import logging
from django.http import HttpResponse
from lorem_text import lorem

"""
Вместо импорта:
from lorem_text import lorem
можно использовать встроенный в утилиты Джанго lorem_ipsum:
from django.utils import lorem_ipsum
"""

logger = logging.getLogger(__name__)


def log(func):
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        logger.info(f'The function {func.__name__} was returned: Посещена страница {request.path}')
        return response

    return wrapper


@log
def index(request):
    text = lorem.paragraph()
    html = f"""<h1 align="center">Один из моих первых Django-проектов</h1>    
    <p align="center">
        <b>{text}</b>
    </p>
    <br>
    <p>
        {text * 2}
    </p>
    """
    # logger.info(f'Посещена страница: {request.path}')
    return HttpResponse(html)


@log
def about(request):
    paragraph_length = 5
    text = lorem.paragraphs(paragraph_length)
    html = f"""<h1 align="center">Обо мне</h1>    
    <p align="center">
        {text}
    </p>    
    """
    # logger.info(f'Посещена страница: {request.path}')
    return HttpResponse(html)
