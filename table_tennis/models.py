"""Models for the table tennis app."""
from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Player(models.Model):

    """A table tennis player."""

    name = models.CharField(_("Name"), max_length=255)
    points = models.PositiveIntegerField(_("Points"), default=0)
    rank = models.PositiveIntegerField(_("Rank"), null=True, blank=True)
    competing_in_championships = models.ManyToManyField("ChampionShip")

    _original_points = None
    _initial_rank_update = None

    class Meta:
        ordering = ("rank", "name")

    @property
    def is_competing_in_championship(self):
        """Return whether the player is currently competing in one or more championships.

        :return: True if self.competing_in_championships is not None.
        :rtype: bool
        """
        return self.competing_in_championships is not None

    def __init__(self, *args, **kwargs):
        """Constructor of the :class:`~table_tennis.models.Player` instance.

        Overridden to keep track of the original amount of points so we can check if it has changed.
        """
        super(Player, self).__init__(*args, **kwargs)
        self._original_points = self.points
        self._initial_rank_update = False

    def perform_rank_update(self):
        """Update players' ranks.

        Handles players having the same rank by looping over the list of players ordered by points descending and
        checking whether the previous higher ranked player has the same amount of points.

        Sets _initial_rank_update to True if there are no players with points yet.
        This is needed to ensure that the first time we set ranks the players have points to order by.
        Otherwise we would randomly be distributing ranks.
        """
        ranks = list(range(1, Player.objects.exclude(points=0).count() + 1))
        players = Player.objects.exclude(points=0).order_by("-points")
        for index, player in enumerate(players):
            try:
                previous = players[index - 1]
            except AssertionError:
                previous = None

            if previous and previous.points == player.points:
                player.rank = previous.rank
            else:
                player.rank = ranks.pop(0)  # Pop the first item in the "ranks" list instead of the default last.

            player.save(update_fields=['rank'])
        else:
            self._initial_rank_update = True

    def save(self, *args, **kwargs):
        """Save the :class:`~table_tennis.models.Player` instance.

        Overridden in order to update the rankings of all players if the points of a player changed.
        """
        if self._original_points != self.points:
            self.perform_rank_update()

        super(Player, self).save(*args, **kwargs)

        if self._initial_rank_update:
            self.perform_rank_update()

        self._original_points = self.points

    def __str__(self):
        return u"{0} ({1})".format(self.name, self.rank if self.rank and self.rank > 0 else "Unranked")


class Team(models.Model):

    """A table tennis team consisting of two players."""

    name = models.CharField(_("Name"), max_length=255)
    player1 = models.ForeignKey("Player", related_name="+")
    player2 = models.ForeignKey("Player", related_name="+")

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return u"{0}".format(self.name)


class Match(models.Model):

    """A table tennis match."""

    date_played = models.DateField(_("Date this match was played."), default=date.today())
    games_won = models.PositiveIntegerField(_("Games won by winner."))
    games_lost = models.PositiveIntegerField(_("Games lost the winner."))

    class Meta:
        ordering = ("date_played", )

    def __str__(self):
        return u"Match - {0}".format(self.id)


class IndividualMatch(Match):

    """A table tennis match between two players."""

    won = models.ForeignKey("Player", related_name="singles_won")
    lost = models.ForeignKey("Player", related_name="singles_lost")

    def save(self, *args, **kwargs):
        """Save the :class:`~table_tennis.models.IndividualMatch` instance.

        Overridden in order to add the point of a won match to the winner.
        A player receives 1 point for winning a match and the loser's total points divided by 10 as a bonus.
        This makes sure that defeating a player that has a lot of points is advantageous.
        """
        additional_points = self.lost.points / 10
        self.won.points += (additional_points + 10)
        self.won.save(update_fields=['points'])

        return super(IndividualMatch, self).save(*args, **kwargs)

    def __str__(self):
        return u"{0} (Won) vs. {1} (Lost)".format(self.won.name, self.lost.name)


class ActiveChampionShipManager(models.Manager):
    """:class:`~table_tennis.models.ChampionShip` manager that returns only the active objects."""

    def get_queryset(self):
        """Return only the active :class:`~table_tennis.models.ChampionShip` objects.

        :return: :class:`~django.db.models.query.QuerySet`.
        """
        return super(ActiveChampionShipManager, self).get_queryset().filter(is_active=True)


class ChampionShip(models.Model):
    """A championship."""

    name = models.CharField("Name of the championship", max_length=255)
    year = models.PositiveIntegerField(
        _("Year"),
        help_text="If this is the yearly competition fill in the year, otherwise leave it blank.",
        blank=True,
        null=True
    )
    is_active = models.BooleanField("Currently active.", default=True)

    objects = models.Manager()
    active = ActiveChampionShipManager()

    class Meta:
        ordering = ("year", "name")

    def __str__(self):
        return self.name


class ChampionShipRound(models.Model):
    """A round in a championship."""

    round_number = models.PositiveIntegerField("Round number")
    championship = models.ForeignKey("ChampionShip", related_name="rounds")

    def __str__(self):
        return u"{0} - Round {1}".format(self.championship.name, self.round)


class ChampionshipPairing(models.Model):
    """A championship match."""

    round_number = models.ForeignKey("ChampionShipRound", related_name="+", blank=True, null=True)
    player1 = models.ForeignKey("Player", related_name="+")
    player2 = models.ForeignKey("Player", related_name="+")
    winner = models.ForeignKey("Player", related_name="championship_matches_won", blank=True, null=True)
    loser = models.ForeignKey("Player", related_name="championship_matches_lost", blank=True, null=True)

    def __str__(self):
        return u"Championship match: {0} vs {1}".format(self.player1, self.player2)


class TeamMatch(Match):

    """A table tennis match between two teams."""

    won = models.ManyToManyField("Team", related_name="team_won")
    lost = models.ManyToManyField("Team", related_name="team_lost")

    def __str__(self):
        return u"{0} (Won) vs. {1} (Lost)".format(self.won.name, self.lost.name)
