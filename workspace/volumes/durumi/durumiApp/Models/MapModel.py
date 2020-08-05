from django.db import models

# Create your models here.


class Map:
    def moveLocation(self, yPos, xPos):
        self.yPos = yPos
        self.xPos = xPos
        
class User2(models.Model):
    user_id = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
