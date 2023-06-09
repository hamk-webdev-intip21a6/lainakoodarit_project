# Generated by Django 4.1.7 on 2023-04-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0003_alter_user_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='descrtiption',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='description not available', max_length=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='last_update',
            field=models.CharField(default='2023/04/15 09:06:19', editable=False, max_length=30),
        ),
    ]
