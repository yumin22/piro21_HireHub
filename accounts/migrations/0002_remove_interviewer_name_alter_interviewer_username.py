# Generated by Django 5.0.7 on 2024-07-31 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewer',
            name='name',
        ),
        migrations.AlterField(
            model_name='interviewer',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
