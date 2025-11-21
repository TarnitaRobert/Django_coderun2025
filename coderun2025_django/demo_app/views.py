from django.shortcuts import render
from .models import UserInfo, DemoModel
from .my_forms import UserDataForm, job_choices
# Create your views here.


def demo_app_page(request):
    users = UserInfo.objects.all().order_by('-date') # order my newest
    if request.method == "POST":
        user_form = UserDataForm(request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            user_info  = UserInfo(name= data['name'], 
                                  surname = data['surname'],
                                  age=data['age'],
                                  mail = data['mail'],
                                  job = (job_choices[int(data['job'])])[1] )
            user_info.save()        
    user_form = UserDataForm()
    return render(request, 'demo_app/demo_app.html', 
                context={'users' : users, 
                        'user_form' : user_form})