from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from singletournaments import views as tournament_views

app_name = 'singletournaments'

urlpatterns = [

    url(r'^$', tournament_views.List.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/join/$', login_required(tournament_views.SingleTournamentJoin.as_view()), name='join'),
    url(r'^(?P<pk>\d+)/$', tournament_views.SingleTournamentDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/rules/$', login_required(tournament_views.SingleTournamentRules.as_view()), name='ruleset'),
    url(r'^(?P<pk>\d+)/bracket/$', login_required(tournament_views.SingleTournamentBracket.as_view()), name='bracket'),
    url(r'^(?P<pk>\d+)/teams/$', login_required(tournament_views.SingleTournamentTeamsList.as_view()), name='teams'),
    url(r'^(?P<pk>\d+)/matches/$', login_required(tournament_views.SingleTournamentMatchList.as_view()), name='matches'),
    url(r'^(?P<pk>\d+)/leave/$', login_required(tournament_views.SingleTournamentLeave.as_view()), name='leave'),

]
