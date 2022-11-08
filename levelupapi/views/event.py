"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game


class EventView(ViewSet):
    """Level up eventEvent types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single eventEvent type

        Returns:
            Response -- JSON serialized eventEvent type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """
        event_list = []

        if "game" in request.query_params:
            events_fetched = Event.objects.all()
            gameId_variable = request.query_params['game']
            event_list = events_fetched.filter(game=gameId_variable)
            serializer = EventSerializer(event_list, many=True)
        else:
            event_list = Event.objects.all()
        
        serializer = EventSerializer(event_list, many=True)
        return Response(serializer.data)
            
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["gameToPlay"])

        event = Event.objects.create(
            game = game,
            description=request.data["description"],
            date=request.data["dateOfEvent"],
            time=request.data["timeOfEvent"],
            organizer= gamer
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer')