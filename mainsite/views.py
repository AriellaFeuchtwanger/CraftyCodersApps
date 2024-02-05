from pipes import Template
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    TemplateView,
    FormView
)
from django.urls import reverse_lazy
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class AlefBaisBotsView(TemplateView):
    template_name = "alefbaisbots.html"


class ChanukahBotsView(TemplateView):
    template_name = "chanukahbots.html"


class NekudosBotsView(TemplateView):
    template_name = "nekudosbots.html"


class MitzvahBotTownView(TemplateView):
    template_name = "mitzvahbottown.html"


class PesachRunnerView(TemplateView):
    template_name = "pesachrunner.html"


class FantasyFootballersView(TemplateView):
    template_name = "fantasyfootballers.html"

class ColorShapeBotsGameView(TemplateView):
    template_name = "colorshapebotsplay.html"

class PrivacyPolicyView(TemplateView):
    template_name = "privacypolicy.html"


class SupportView(TemplateView):
    template_name = "support.html"


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Calls the custom send method
        if form.is_valid():
            form.send()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)


class SendEmailSuccessView(TemplateView):
    template_name = "send_email_success.html"
