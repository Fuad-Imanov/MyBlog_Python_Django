from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,verbose_name='Url',unique=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('P_Category', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,verbose_name='Url',unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,verbose_name='Url',unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Yaradılma tarixi')
    photo  = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    views = models.IntegerField(default=0,verbose_name='Baxış sayı')
    category = models.ForeignKey(Category,related_name='posts',on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag,related_name='posts',blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
