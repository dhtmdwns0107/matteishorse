from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_pw = models.CharField(max_length=10)
    user_name = models.CharField(max_length=10)
    user_age = models.IntegerField(max_length=10)
    user_sex = models.CharField(max_length=10)
    user_add = models.CharField(max_length=30)

    class Meta():
        db_table = 'user'

class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_text = models.CharField(max_length=40)
    test_info = models.CharField(max_length=100)

    class Meta():
        db_table = 'test'

class Question(models.Model):
    q_id = models.AutoField(primary_key=True)
    q_text = models.CharField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE) # test -> test_id

    class Meta():
        db_table = 'question'

    def __str__(self):
        return self.q_text

class Choice(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_val = models.IntegerField(max_length=11)
    q = models.ForeignKey(Question, on_delete=models.CASCADE) # test -> test_id

    class Meta():
        db_table = 'choice'

class Result(models.Model):
    res_id = models.AutoField(primary_key=True)
    res_text = models.CharField(max_length=100)
    res_title = models.CharField(max_length=500)
    test = models.ForeignKey(Test, on_delete=models.CASCADE) # test -> test_id

    class Meta():
        db_table = 'result'

class Mypage(models.Model):
    mp_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # test -> test_id
    test = models.ForeignKey(Test, on_delete=models.CASCADE) # test -> test_id
    test_date = models.DateTimeField('date published')

    class Meta():
        db_table = 'mypage'