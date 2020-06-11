from django.db import models

# Create your models here.

class Map:
    yPos = 33.450701
    xPos = 126.570667
    
    def moveLocation(self,yPos,xPos):
        self.yPos = yPos
        self.xPos = xPos
        