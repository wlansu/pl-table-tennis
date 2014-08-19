"""Url routes for the table_tennis application."""
from django.conf.urls import patterns, include, url
from django.contrib import admin

from table_tennis.views import (
    HomeView,
    PlayerView,
    CreatePlayerView,
    IndividualMatchView,
    IndividualMatchListView,
    CreateIndividualMatch,
    ChampionshipDetailView,
    ChampionShipsView,
    UpdatePlayerView)


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),

    # Players
    url(r'^player/(?P<pk>\d+)/$', PlayerView.as_view(), name='player.detail'),
    url(r'^player/update/(?P<pk>\d+)/$', UpdatePlayerView.as_view(), name='player.update'),
    url(r'^new_player/$', CreatePlayerView.as_view(), name='player.create'),

    # # Matches
    url(r'^match/(?P<pk>\d+)/$', IndividualMatchView.as_view(), name='individual_match.detail'),
    url(r'^matches/$', IndividualMatchListView.as_view(), name='individual_match.list'),
    url(r'^new_match/$', CreateIndividualMatch.as_view(), name='individual_match.create'),

    # Championships
    url(r'^championships/$', ChampionShipsView.as_view(), name='championship.list'),
    url(r'^championships/(?P<pk>\d+)/$', ChampionshipDetailView.as_view(), name='championships.detail'),

    # Admin
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
