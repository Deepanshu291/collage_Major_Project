# Generated by Django 4.1.7 on 2023-04-18 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_subject_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MentorDetail',
            new_name='ProfessorDetail',
        ),
    ]
