from django.db import models

# Create your models here.

class InfoDatabase(models.Model):
    id = models.AutoField(primary_key = True)
    dbname = models.CharField(max_length = 25, unique = True)
    description = models.CharField(max_length = 25, null=True, blank=True)
    host = models.CharField(max_length = 25)
    port = models.CharField(max_length = 25)
    user = models.CharField(max_length = 25)
    passwd = models.CharField(max_length = 25)
    type = models.CharField(max_length = 25)
    create_time = models.CharField(max_length = 25)
    update_time = models.CharField(max_length = 25)
    jdbcurl = models.CharField(max_length=50)
    jdbcdriver = models.CharField(max_length=25)

    class Meta:
        db_table = "info_database"
        app_label = 'manna'
