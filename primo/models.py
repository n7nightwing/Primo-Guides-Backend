from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)


class Game(models.Model):
    name = models.charField(max_length=256)
    publisher = models.charField(max_length=100)
    Genre = models.charField(max.length=100)


class Guide(models.Model):
    title = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='guides')
    skill_level = models.charField(max_length=5)
    content = models.TextField()

# tags added as a different class with a related field back to guides?
# blog posts
# favorites
