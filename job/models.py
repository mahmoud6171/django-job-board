from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

def image_upload(instance, filname):
    _, extention = filname.split('.')
    return "jobs/%s.%s"%(instance.id,extention)


class Job(models.Model):
    JOB_TYPE = (
        ('Part Time','Part Time'),
        ('Full Time','Full Time'),
    )
    owner = models.ForeignKey(User , related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50, choices = JOB_TYPE)
    description = models.TextField(max_length=1000, null= True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    # 'images/%y/%m/%d'
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Job,self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)
    

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name=("apply"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='apply/', max_length=100)
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
