from django.contrib import admin

# Register your models here.
from .models import User, Test, Question, Choice, Result, Mypage

# Register your models here.
admin.site.register(User)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Result)
admin.site.register(Mypage)