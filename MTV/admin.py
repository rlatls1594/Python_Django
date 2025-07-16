from django.contrib import admin
from .models import Board, Question, Answer

# Register your models here.
admin.site.register(Board)
admin.site.register(Question)
admin.site.register(Answer)