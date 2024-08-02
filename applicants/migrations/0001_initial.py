# Generated by Django 5.0.7 on 2024-08-02 05:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('template', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('school', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('interview_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('submitted', 'Submitted'), ('interview_scheduled', 'Interview Scheduled'), ('interview_in_progress', 'Interview In Progress'), ('interview_completed', 'Interview Completed')], default='submitted', max_length=50)),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='template.applicationtemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.question')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='applicants.application')),
            ],
        ),
    ]
