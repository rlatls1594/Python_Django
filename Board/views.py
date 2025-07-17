from django.shortcuts import render

# Create your views here.
def board_list(request):
    return render(request, 'Board/board_list.html')

def board_detail(request):
    return render(request, 'Board/board_detail.html')

def board_form(request):
    return render(request, 'Board/board_form.html')

def board_form_update(request):
    return render(request, 'Board/board_form_update.html')

def board_login(request):
    return render(request, 'common/login.html')

def board_signup(request):
    return render(request, 'common/signup.html')