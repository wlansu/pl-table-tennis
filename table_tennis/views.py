"""Views for the table tennis app."""
import random

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView

from table_tennis.forms import UpdatePlayerChampionShipForm
from table_tennis.mixins import FieldCSSMixin
from table_tennis.models import Player, IndividualMatch, ChampionshipPairing, ChampionShip


class HomeView(TemplateView):

    """Homepage of the table tennis app."""

    template_name = "homepage.html"

    @staticmethod
    def players():
        """Return a queryset of all :class:`~table_tennis.models.Player` instances."""
        return Player.objects.all()

    @staticmethod
    def latest_matches():
        """Return a queryset of the last 10 :class:`~table_tennis.models.IndividualMatch` instances."""
        return IndividualMatch.objects.all()[:10]

    @staticmethod
    def individual_match_of_the_day():
        """Return a somewhat random selection of two players that are due to play that day."""
        raise NotImplementedError("This hasn't been implemented yet.")


class PlayerView(DetailView):

    """:class:`~table_tennis.models.Player` detail page."""

    template_name = "player_detail.html"
    model = Player
    context_object_name = "player"

    def matches_won(self):
        """Return a queryset of all :class:`~table_tennis.models.IndividualMatch` instances the player has won."""
        return self.object.singles_won.all()

    def matches_lost(self):
        """Return a queryset of all :class:`~table_tennis.models.IndividualMatch` instances the player has lost."""
        return self.object.singles_lost.all()


class CreatePlayerView(SuccessMessageMixin, FieldCSSMixin, CreateView):

    """:class:`~table_tennis.models.Player` creation page."""

    template_name = "player_create.html"
    model = Player
    fields = ["name"]
    success_message = "New player created."
    success_url = reverse_lazy("home")


class UpdatePlayerView(SuccessMessageMixin, FieldCSSMixin, UpdateView):

    """:class:`~table_tennis.models.Player` update page.

    Shows only the fields someone can update for a player:
        - competing_in_championships.
    """

    template_name = "player_update.html"
    context_object_name = "player"
    model = Player
    form_class = UpdatePlayerChampionShipForm
    success_message = "Player updated."
    success_url = reverse_lazy("player.detail")


class IndividualMatchListView(ListView):

    """:class:`~table_tennis.models.IndividualMatch` overview page."""

    template_name = "individual_match_list.html"
    model = IndividualMatch
    context_object_name = "match_list"
    paginate_by = 20

    def get_queryset(self):
        """Return queryset of all :class:`~table_tennis.models.IndividualMatch` instances ordered by date."""
        return super(IndividualMatchListView, self).get_queryset().order_by("date_played")


class IndividualMatchView(DetailView):

    """:class:`~table_tennis.models.IndividualMatch` detail page."""

    template_name = "individual_match.html"
    model = IndividualMatch
    context_object_name = "match"


class CreateIndividualMatch(SuccessMessageMixin, FieldCSSMixin, CreateView):

    """:class:`~table_tennis.models.IndividualMatch` creation page."""

    template_name = "create_individual_match.html"
    model = IndividualMatch
    fields = [field.name for field in IndividualMatch._meta._field_name_cache
              if field.name not in ["id", "championship_match"]]
    success_message = "Your match was added."
    success_url = reverse_lazy("home")


class ChampionShipsView(ListView):

    """:class:`~table_tennis.models.ChampionShip` list page."""

    template_name = "championship_list.html"
    model = ChampionShip
    context_object_name = "championship_list"
    paginate_by = 20


class ChampionshipDetailView(DetailView):

    """View for viewing and creating championship pairings."""

    template_name = "championship_detail.html"
    model = ChampionShip
    context_object_name = "championship"

    def pairings(self):
        """Return any :class:`~table_tennis.models.ChampionshipPairing` objects for this championship that exist.

        :return: Queryset of ChampionshipPairing objects.
        """
        return ChampionshipPairing.objects.filter(round_number__championship=self.object)

    def post(self, request, *args, **kwargs):
        """Creates initial matches for a championship.

        Randomly matches players against each other.
        """
        try:
            all_players = [x for x in Player.objects.filter(competing_in_championships__id__exact=self.object.id)]
            random.shuffle(all_players)
            players_done = []
            if all_players:
                if len(all_players) % 2 == 0:
                    for player in all_players:
                        if player not in players_done:
                            opponent = all_players[all_players.index(player) + 1]

                            ChampionshipPairing(
                                player1=player,
                                player2=opponent
                            ).save()

                            players_done.append(player)
                            players_done.append(opponent)
                    messages.success(self.request, "Championship pairings created.")
                else:
                    messages.error(self.request, "There are not enough players to create pairings for all of them.")

            else:
                messages.warning(self.request, "There are no players currently competing in the championships.")
        except:
            messages.error(self.request, "Something went wrong.")

        return HttpResponseRedirect(reverse_lazy("championships.pairings"))
