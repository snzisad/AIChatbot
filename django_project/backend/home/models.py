from django.db import models

class ConversationHistory(models.Model):
    token = models.CharField(max_length=100)
    message = models.TextField()
    response = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)