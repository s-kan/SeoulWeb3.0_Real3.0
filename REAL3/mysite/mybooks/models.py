from django.db import models
from django.contrib.auth.models import User

# 책 정보들
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

# 유저 프로필
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 다른 사용자 프로필 속성들을 추가할 수 있습니다.

    # 찜한 책들을 Many-to-Many 관계로 정의합니다.
    wish_list = models.ManyToManyField(Book, related_name='wish_list', blank=True)