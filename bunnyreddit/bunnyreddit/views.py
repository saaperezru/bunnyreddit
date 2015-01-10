from django.shortcuts import get_object_or_404, render
import helpers
from django.conf import settings

def home(request):
    """
    this will render the home page
    :param request:
    :return: home page of the project
    """
    context = {'posts': helpers.getTrending(1)}
    return render(request, 'home.html',context)
