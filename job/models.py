from django.db import models

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

 
    def __str__(self):
        return self.title

        
