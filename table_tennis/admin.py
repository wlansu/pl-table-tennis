"""Everything related to the admin pages of the table_tennis application."""
from django.contrib import admin

from table_tennis.models import (
    Player,
    IndividualMatch,
    ChampionShip)


def competing_in_championship(modeladmin, request, queryset):
    """Mark selected players as competing in the championship.

    :param modeladmin: :class:`~django.contrib.admin.options.ModelAdmin` object.
    :param request: :class:`~django.http.request.HttpRequest` object.
    :param queryset: :class:`~django.db.models.query.QuerySet` of player objects.
    """
    queryset.update(competing_in_championship=True)


competing_in_championship.short_description = "Mark as competing in the championship."


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    """Admin view for the :class:`~table_tennis.models.Player` objects."""

    actions = [competing_in_championship]


@admin.register(IndividualMatch)
class IndividualMatchAdmin(admin.ModelAdmin):
    """Admin view for the :class:`~table_tennis.models.IndividualMatch` objects."""


@admin.register(ChampionShip)
class ChampionShipAdmin(admin.ModelAdmin):
    """Admin view for the :class:`~table_tennis.models.ChampionShip` objects."""
