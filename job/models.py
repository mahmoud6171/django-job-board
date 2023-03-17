from django.db import models

def image_upload(instance, filname):
    _, extention = filname.split('.')
    return "jobs/%s.%s"%(instance.id,extention)


class Job(models.Model):
    JOB_TYPE = (
        ('Part Time','Part Time'),
        ('Full Time','Full Time'),
    )
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

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)
    

    def __str__(self):
        return self.name
