# Generated by Django 2.2.5 on 2020-02-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qresult',
            name='res_text',
            field=models.CharField(max_length=500),
        ),
    ]
