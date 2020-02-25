from django.db import models 

class Tutorial(models.Model):
    tutorial_category = models.CharField(max_length = 200)
    tutorial_content = models.TextField()

    def __str__(self):
        return self.tutorial_category