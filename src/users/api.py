from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.permissions import RoleIsAdmin
from users.models import User
from users.serializers import (
    UserLightSerializer,
    UserRegistrationSerializer,
    UserSerializer,
)

# from django.contrib.auth import get_user_model
# User = get_user_model()


class UserAPISet(ModelViewSet):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list":
            permission_classes = [RoleIsAdmin]
        elif self.action == "create":
            permission_classes = [AllowAny]
        elif self.action == "retrieve":
            permission_classes = [RoleIsAdmin]
        elif self.action == "update":
            permission_classes = [RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)

    def retrieve(self, request, pk: int):
        instance = self.get_object()
        serializer = UserLightSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request):
        context: dict = {"request": self.request}
        serializer = UserRegistrationSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk: int):
        instance: User = self.get_object()

        context: dict = {"request": self.request}
        serializer = UserSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, pk: int):
        instance: User = self.get_object()
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)


# User = get_user_model()


# class UserCreateAPI(CreateAPIView):
#     serializer_class = UserRegistrationSerializer
#     permission_classes = [AllowAny]

# from tickets.serializers import (
#     TicketSerializer,
#     TicketLightSerializer,
# )
# from django.http import JsonResponse
# from tickets.models import Ticket
# from rest_framework.viewsets import ViewSet
# from rest_framework import status
# from shared.serializers import ResponseSerializer, ResponseMultiSerializer
#
#
# class UserAPISet(ViewSet):
#     def list(self, request):
#         queryset = Ticket.objects.all()
#         serializer = TicketLightSerializer(queryset, many=True)
#         response = ResponseMultiSerializer({"results": serializer.data})
#         return JsonResponse(response.data)
#
#     def retrieve(self, request, id_: int):
#         instance = Ticket.objects.get(id=id_)
#         serializer = TicketSerializer(instance)
#         response = ResponseSerializer({"result": serializer.data})
#         return JsonResponse(response.data)
#
#     def create(self, request):
#         context: dict = {
#             "request": self.request,
#         }
#         serializer = TicketSerializer(data=request.data, context=context)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         response = ResponseSerializer({"result": serializer.data})
#
#         return JsonResponse(response.data, status=status.HTTP_201_CREATED)
#
#
# ticket_create = TicketAPISet.as_view({"post": "create"})
# tickets_list = TicketAPISet.as_view({"get": "list"})
# ticket_retrieve = TicketAPISet.as_view({"get": "retrieve"})
