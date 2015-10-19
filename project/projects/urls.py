from django.conf.urls import url
from . import views

urlpatterns = [
    # Project URLs
    url(r'^attack-on-blocks', views.AttackOnBlocksView.as_view(), name="attack-on-blocks"),
    url(r'^bsod-enabler', views.BSODEnablerView.as_view(), name='bsod-enabler'),
    url(r'^hipchat-emoticons-for-all', views.HipChatEmoticonsForAllView.as_view(), name='hipchat-emoticons'),
    url(r'^pithos', views.PithosView.as_view(), name='pithos'),

    # Code URLs
    url(r'^morse-code-decoder', views.MorseCodeDecoderView.as_view(), name='morse-code-decoder'),
    url(r'^wiki-game-solver', views.WikiGameSolverView.as_view(), name='wiki-game-solver'),

    url(r'^', views.AllProjectsView.as_view(), name="index")
]
