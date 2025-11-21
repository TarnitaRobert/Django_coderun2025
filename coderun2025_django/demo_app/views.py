from django.shortcuts import render
from .models import UserInfo, DemoModel
# Create your views here.

print(UserInfo.objects.all())
def demo_app_page(request):
    users = UserInfo.objects.all().order_by('-date') # order my newest

    return render(request, 'demo_app/demo_app.html', context={'users' : users})