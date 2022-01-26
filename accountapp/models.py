from django.db import models


# Create your models here.

class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class HelloWorld(BaseModel):
    text = models.CharField(max_length=255, null=False)
