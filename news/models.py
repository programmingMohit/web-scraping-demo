from django.db import models

class Headline(models.Model):

      title = models.CharField(max_length=200)
      company = models.TextField()
      """URLField(null=True, blank=True)"""
      location = models.TextField()
      
      def __str__(self):
          return self.title
