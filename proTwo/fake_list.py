import os
os.environ.setdefault('django_settings_module', 'proTwo.settings')

import django
django.setup()

from faker import Faker
from appTwo.models import User
faker=Faker()

def fake_list(N=5):
    for entry in range(N):

        fake_name = faker.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = faker.email()

        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)
if __name__ == '__main__':
    print('populating data base')
    fake_list(20)
    print('completed')
