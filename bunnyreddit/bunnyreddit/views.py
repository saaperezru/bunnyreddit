def home(request):
    """
    this will render the home page
    :param request:
    :return: home page of the project
    """
    return render(request, 'home.html')  
