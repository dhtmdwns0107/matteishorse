from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_pw = models.CharField(max_length=10)
#     user_name = models.CharField(max_length=10)
#     user_email = models.CharField(max_length=30)
#     user_age = models.IntegerField(max_length=10)
#     user_sex = models.CharField(max_length=10)
#     user_add = models.CharField(max_length=30)

#     class Meta():
#         db_table = 'user'
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    p_id = models.AutoField(primary_key=True)
    gender = models.TextField(max_length=2, blank=True)
    age = models.IntegerField()
    addr = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        db_table = 'profile'

class Mindtest(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_text = models.CharField(max_length=40)
    test_info = models.CharField(max_length=100)

    class Meta():
        db_table = 'mindest'

class Question(models.Model):
    q_id = models.AutoField(primary_key=True)
    q_text = models.CharField(max_length=200)
    test = models.ForeignKey(Mindtest, on_delete=models.CASCADE) # test -> test_id

    class Meta():
        db_table = 'question'

    def __str__(self):
        return self.q_text

class Choice(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_val = models.IntegerField()
    c_date = models.DateTimeField('date published')
    q = models.ForeignKey(Question, on_delete=models.CASCADE) # q -> q_id
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user -> user_id

    class Meta():
        db_table = 'choice'

class Qresult(models.Model):
    res_id = models.AutoField(primary_key=True)
    res_text = models.CharField(max_length=100)
    res_title = models.CharField(max_length=500)
    res_div = models.IntegerField()
    test = models.ForeignKey(Mindtest, on_delete=models.CASCADE) # test -> test_id

    class Meta():
        db_table = 'qresult'

class Mypage(models.Model):
    mp_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user -> user_id
    test = models.ForeignKey(Mindtest, on_delete=models.CASCADE) # test -> test_id
    test_date = models.DateTimeField('date published')

    class Meta():
        db_table = 'mypage'