"""Forms for the table_tennis application."""
from django import forms

from table_tennis.models import ChampionShip, Player


class UpdatePlayerChampionShipForm(forms.ModelForm):
    """Form to update which :class:`~table_tennis.models.ChampionShip` a player is competing in."""

    competing_in_championships = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={"class": ""}),
        choices=[(obj.id, obj.name) for obj in ChampionShip.active.all()],
    )

    class Meta:
        model = Player
        fields = ["competing_in_championships"]
