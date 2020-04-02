from django.contrib import admin
from .models import Question, Answer, Upvote

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Upvote)