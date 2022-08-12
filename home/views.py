from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

def index(request):
    template_name = 'home/index.html'
    context={}
    return render(request, template_name=template_name, context=context)

class CustomLoginView(LoginView):
    template_name = 'home/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

def contact_us(request):
    template_name = 'home/contact.html'
    context={}
    return render(request, template_name=template_name, context=context)
