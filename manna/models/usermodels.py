from django.db import models

# Create your models here.

class Infouser(models.Model):
    uid = models.AutoField(primary_key = True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    token = models.CharField(max_length=25)
    introduction = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    roles = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    create_time = models.CharField(max_length=25)
    update_time = models.CharField(max_length=25)

    class Meta:
        db_table = "info_user"
        app_label = 'manna'