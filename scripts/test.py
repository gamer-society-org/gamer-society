from threading import Timer
from django.shortcuts import get_object_or_404
from transactions.serializers import TransactionSerializer

from users.models import User


def run():
    Timer(5, run).start()
    print("Din din na conta do pai")
    user = get_object_or_404(User, id="2bd4a6c8-0d74-4731-bd46-440c2641917a")

    money = {"value": 100}

    serializer = TransactionSerializer(data=money)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=user)
