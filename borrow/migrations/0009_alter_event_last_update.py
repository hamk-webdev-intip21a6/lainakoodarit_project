# Generated by Django 4.1.7 on 2023-04-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0008_merge_20230415_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='last_update',
            field=models.CharField(default='2023/04/15 12:48:22', editable=False, max_length=30),
        ),
    ]