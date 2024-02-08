from django.shortcuts import render
import logging
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def log(func):
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        logger.info(f'The function {func.__name__} was returned: Посещена страница {request.path}')
        return response

    return wrapper


@log
def index(request):
    html = f"""<h1 align="center">"Это мой первый проект на Django"</h1>    
    <p align="center">
        <b>Когда-нибудь здесь будем сам проект</b>
    </p>
    """
    return HttpResponse(html)


@log
def about(request):
    html = f"""<h1 align="center">"Обо мне"</h1>    
    <p align="center">
        Я учу Python
    </p>    
    """
    return HttpResponse(html)
