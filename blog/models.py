from django.db import models

# Create your models here.
class post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 13)
    email = models.EmailField()
    content = models.TextField()
    slug = models.CharField(max_length = 130)
    timeStamp = models.DateTimeField(blank=True)
    title_image = models.ImageField(upload_to = 'blog/images',default="")

    def __str__(self):
            return self.title + " by " +self.author

class comment(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=80)
    body = models.TextField()
    post = models.ForeignKey(post, on_delete=models.CASCADE,related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_on']


    