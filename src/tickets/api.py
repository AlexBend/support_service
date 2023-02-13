from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.permissions import (
    IsManagerProcessing,
    IsUserOwner,
    RoleIsAdmin,
    RoleIsManager,
    RoleIsUser,
)
from tickets.serializers import TicketLightSerializer, TicketSerializer
from users.constants import Role


class TicketAPISet(ModelViewSet):
    queryset = Ticket.objects.all()
    model = Ticket
    serializer_class = TicketSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list":
            permission_classes = (RoleIsAdmin | RoleIsManager,)
        elif self.action == "create":
            permission_classes = [RoleIsUser]
        elif self.action == "retrieve":
            permission_classes = (IsUserOwner | RoleIsAdmin | IsManagerProcessing,)
        elif self.action == "update":
            permission_classes = (IsManagerProcessing | RoleIsAdmin,)
        elif self.action == "destroy":
            permission_classes = (RoleIsAdmin | IsManagerProcessing,)
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def list(self, request):
        if request.user.role == Role.ADMIN:
            queryset = self.get_queryset()
        elif request.user.role == Role.MANAGER:
            queryset = Ticket.objects.filter(manager=request.user)
        else:
            queryset = Ticket.objects.filter(customer=request.user)

        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)

    def retrieve(self, request, pk: int):
        instance = self.get_object()
        serializer = TicketSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request):
        context: dict = {"request": self.request}
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk: int):
        instance: Ticket = self.get_object()

        context: dict = {"request": self.request}
        serializer = TicketSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, pk: int):
        instance: Ticket = self.get_object()
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
