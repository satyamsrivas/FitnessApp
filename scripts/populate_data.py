from users.models import User,FitnessProfile
from faker import Faker
import random


fake = Faker()

def run():
    users = []
    for _ in range(20):
        user = User.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name() if random.choice([True, False]) else "",
            mobile_number=fake.unique.numerify("98########"),  # Generates a 10-digit number
            email=fake.email(),
            is_staff=random.choice([True, False]),
        )
        users.append(user)

        for user in users:
            FitnessProfile.objects.create(
                user=user,
                height=round(random.uniform(150, 200), 2),  # Height in cm
                weight=round(random.uniform(50, 100), 2),  # Weight in kg
                age=random.randint(18, 60),
                gender=random.choice(["M", "F"]),
            )
