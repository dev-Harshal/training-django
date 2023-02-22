from django.db import models
from atomicloops.models import ATLBaseModel,Users

# Create your models here

class UserMessages(ATLBaseModel):

    author = models.ForeignKey(Users,db_column="author",on_delete=models.CASCADE)
    message=models.CharField(max_length=100,db_column="message",null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True,db_column="created_at")

    def __str__(self):
        return self.author.email