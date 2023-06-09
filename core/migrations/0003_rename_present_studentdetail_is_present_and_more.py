# Generated by Django 4.1.7 on 2023-04-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_studentdetail_subject_subject_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdetail',
            old_name='present',
            new_name='is_present',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ManyToManyField(to='core.studentdetail', verbose_name='student detail'),
        ),
    ]
