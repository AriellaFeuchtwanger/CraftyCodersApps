from django.urls import path

from . import views
from .views import IndexView, AboutView, AlefBaisBotsView, ChanukahBotsView, NekudosBotsView, PrivacyPolicyView, ContactView, SendEmailSuccessView, FantasyFootballersView, MitzvahBotTownView, SupportView, PesachRunnerView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path("about", AboutView.as_view(), name='about'),
    path("alefbaisbots", AlefBaisBotsView.as_view(), name='alefbaisbots'),
    path("chanukahbots", ChanukahBotsView.as_view(), name='chanukahbots'),
    path("nekudosbots", NekudosBotsView.as_view(), name='nekudosbots'),
    path("mitzvahbottown", MitzvahBotTownView.as_view(), name='mitzvahbottown'),
    path("pesachrunner", PesachRunnerView.as_view(), name='pesachrunner'),
    path("privacypolicy", PrivacyPolicyView.as_view(), name='privacy_policy'),
    path("support", SupportView.as_view(), name='support'),
    # path("contact", ContactView.as_view(), name='contact'),
    path("email-confirmation", SendEmailSuccessView.as_view(), name='success'),
]
