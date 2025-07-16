from django.db import models

# Create your models here.
class Board(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField(max_length=500)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return self.title
  
class Question(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
      return self.title

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
      return self.content