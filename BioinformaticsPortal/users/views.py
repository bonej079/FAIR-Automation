from django.urls import reverse_lazy
from django.views import generic

from .forms import PortalUserCreationForm

class SignUp(generic.CreateView):
    form_class = PortalUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
