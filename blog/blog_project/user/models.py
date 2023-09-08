from django.db import models

class BlogUsers(models.Model):
    id=models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50)
    emailid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    username = models.CharField(unique=True, max_length=255, blank=True, null=True)
    mobile_no = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'blog_users'

