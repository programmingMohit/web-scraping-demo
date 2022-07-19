from django.db import models

class Headline(models.Model):

      title = models.CharField(max_length=200)
      image = models.TextField()
      """URLField(null=True, blank=True)"""
      snippet = models.TextField()
      
      def __str__(self):
          return self.title
