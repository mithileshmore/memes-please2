from django.db import models


class UserLogin(models.Model):  
    username = models.CharField(max_length=100)  
    cookie_consent = models.CharField(max_length=10, default=None, blank=True)

    class Meta:
        db_table = "user_cookie_consent" 
