from django.contrib import admin

# Register your models here.
from .models import Mindtest, Question, Choice, Qresult, Mypage

# Register your models here.
admin.site.register(Mindtest)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Qresult)
admin.site.register(Mypage)