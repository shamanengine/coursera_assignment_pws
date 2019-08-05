from django.utils import timezone

from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self):
        return f'User: {{' \
            f'Id=\t{self.id}, ' \
            f'First Name=\t{self.first_name}, ' \
            f'Last Name=\t{self.last_name}' \
            f'}}'

    def __str__(self):
        return self.__repr__()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    subscribers = models.ManyToManyField(User, related_name='subscriptions')

    def __str__(self):
        return f'Blog: {{' \
            f'Id=\t{self.id}, ' \
            f'Title=\t{self.title}, ' \
            f'Author Id=\t{self.author_id}, ' \
            f'Created=\t{self.created}' \
            f'}}'

    def __repr__(self):
        return self.__str__()


class Topic(models.Model):
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    likes = models.ManyToManyField(User, related_name='likes')

    def __repr__(self):
        return f'Topic: {{' \
            f'Id=\t{self.id}, ' \
            f'Title=\t{self.title}, ' \
            f'Blog Id=\t{self.blog_id}, ' \
            f'Author Id=\t{self.author_id}, ' \
            f'Created=\t{self.created}' \
            f'}}'

    def __str__(self):
        return self.__repr__()
