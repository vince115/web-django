import os
import sys
import django
from faker import Faker

# 把專案根目錄加入 sys.path（很關鍵！）
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 初始化 Django 環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from users.models import CustomUser

fake = Faker()

def create_fake_users(n=10):
    for _ in range(n):
        username = fake.user_name()
        password = 'test1234'
        email = fake.email()
        bio = fake.sentence()

        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            email=email,
            bio=bio
        )
        print(f'✅ Created user: {username}')

if __name__ == '__main__':
    create_fake_users(10)
