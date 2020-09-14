from django.db import models

# Create your models here.


class Map:
    yPos = 33.450701
    xPos = 126.570667
    
    def moveLocation(self, yPos, xPos):
        self.yPos = yPos
        self.xPos = xPos
<<<<<<< HEAD
=======
        
class User2(models.Model):
    user_id = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
>>>>>>> 48f4589801339f4be8845132a9fa05a69f91db46
