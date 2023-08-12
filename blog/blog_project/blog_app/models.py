from django.db import models

# Create your models here.
class BlogLists(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.TextField(blank=True, null=True)
    blog_content = models.TextField(blank=True, null=True)
    userid = models.ForeignKey('BlogUsers', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'blog_lists'


class BlogUsers(models.Model):
    id=models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    emailid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    username = models.CharField(unique=True, max_length=255, blank=True, null=True)
    mobile_no = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'blog_users'


class UserComments(models.Model):
    cmt_id = models.AutoField(primary_key=True)
    cmt_content = models.TextField(blank=True, null=True)
    blog = models.ForeignKey(BlogLists, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(BlogUsers, models.DO_NOTHING, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'user_comments'