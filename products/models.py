from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=60)
    url = models.URLField(max_length=200, blank=True)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=800)
    hunter = models.ForeignKey(User,  on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100]
