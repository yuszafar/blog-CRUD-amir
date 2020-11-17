from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsNotAuthenticated
from accounts.serializers import AccountCreateSerializer, AccountSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class AccountCreate(CreateAPIView):
    serializer_class = AccountCreateSerializer
    permission_classes = [IsNotAuthenticated]


class AccountDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
