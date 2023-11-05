from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    
        
    CHOICES = (
        ('Energy', 'Energy'),
        ('Materials', 'Materials'),
        (' Media and Entertainment', 'Media and Entertainmen'),
        ('Captial goods', 'Captial goods'),
        ('Commercial & Professional Svc', 'Commercial & Professional Svc'),
        ('Transportation', 'Transportation'),
        ('Consumer Durables', 'Consumer Durables'),
        ('Consumer Services', 'Consumer Services'),
        ('Retailing', 'Retailing'),
        ('Food & Stables Retailing', 'Food & Stables Retailing'),
        ('Food & Beverages', 'Food & Beverages'),
        ('Health care Equipment & Svc', 'Health care Equipment & Svc'),
    )
    name = models.CharField(max_length=2048)
    description = models.TextField()
    local_score = models.FloatField()
    ikteva_score_now = models.FloatField()
    ikteva_score_before= models.FloatField()
    email =  models.CharField(max_length=2048)
    contact_number = models.CharField(max_length=2048)
    instagram_link = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    website = models.URLField(blank=True)
    sectors= models.TextField(max_length=2048,default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)





    def __str__(self) -> str:
        return f"{self.name}"



class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)






