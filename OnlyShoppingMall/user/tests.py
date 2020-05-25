from django.test import TestCase

# Create your tests here.

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlyShoppingMall.settings')
django.setup()
from user.models import UserInfo


obj = UserInfo.objects.all()

