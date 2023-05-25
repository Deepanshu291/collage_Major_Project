# Generated by Django 4.1.7 on 2023-05-25 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_studentdetail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='is_present',
            field=models.BooleanField(default=False, unique_for_date=True, verbose_name='Present'),
        ),
    ]