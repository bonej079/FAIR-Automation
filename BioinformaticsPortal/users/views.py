from django.urls import reverse_lazy
from django.views import generic

from .forms import AdminPortalUserCreationForm

class SignUp(generic.CreateView):
    form_class = AdminPortalUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
