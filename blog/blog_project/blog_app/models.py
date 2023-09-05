from django.db import models
from user.models import BlogUsers


class BlogLists(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.TextField(blank=True, null=True)
    blog_content = models.TextField(blank=True, null=True)
    userid = models.ForeignKey(BlogUsers, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    isUpdate = models.BooleanField(default=False, blank=True, null=True)
    isDelete = models.BooleanField(default=False,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'blog_lists'


class BlogUserComments(models.Model):
    cmt_id = models.AutoField(primary_key=True)
    cmt_content = models.TextField(blank=True, null=True)
    blog = models.ForeignKey(BlogLists, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(BlogUsers, models.DO_NOTHING, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    isUpdate = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_user_comments'

class BlogUsersLikes(models.Model):
    like_id = models.AutoField(primary_key=True)
    like_blog = models.ForeignKey(BlogLists, models.DO_NOTHING, blank=True, null=True)
    like_user = models.ForeignKey(BlogUsers, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    isLike = models.BooleanField(blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'blog_users_likes'