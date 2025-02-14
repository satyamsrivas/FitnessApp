from users.models import User
from django.db.models.functions import Upper
from django.db import connection

def run():
    user = User.objects.filter().values_list('first_name',flat=True)
    print(user)
    print(connection.queries)