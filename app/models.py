from django.db import models

# Create your models here.


class Confession(models.Model):

    confession_title = models.CharField(max_length=256, blank=True, null=True)
    confession_note = models.TextField(max_length=5120, blank=True, null=True)
    secret_key = models.CharField(max_length=128, blank=True, null=True)
    sender_info = models.TextField(max_length=512, blank=True, null=True)

    # state => new | approved | rejeted
    state = models.CharField(max_length=16, default="new", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_star = models.BooleanField(default=False)

    # public
    comment_allowed = models.BooleanField(default=True)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Comment(models.Model):

    confession = models.ForeignKey(Confession, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=512, blank=True, null=True)

    is_deleted = models.BooleanField(default=False)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
