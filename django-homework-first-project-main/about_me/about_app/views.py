from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.utils import lorem_ipsum


logger = logging.getLogger(__name__)


def log(func):
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        logger.info(f'The function {func.__name__} was returned: Посещена страница {request.path}')
        return response

    return wrapper


@log
def index(request):
    text = lorem_ipsum.paragraph()
    html = f"""<h1 align="center">"Это мой первый проект на Django</h1>    
    <p align="center">
        <b>{text}</b>
    </p>
    <br>
    <p>
        {text * 2}
    </p>
    """
    return HttpResponse(html)


@log
def about(request):
    paragraph_length = 5
    text = lorem_ipsum.paragraphs(paragraph_length)
    html = f"""<h1 align="center">Обо мне</h1>    
    <p align="center">
        {text}
    </p>    
    """
    return HttpResponse(html)
