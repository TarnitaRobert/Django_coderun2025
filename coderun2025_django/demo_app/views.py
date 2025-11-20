from django.shortcuts import render
# Create your views here.
def demo_app_page(request):
    return render(request, 'demo_app/demo_app.html')