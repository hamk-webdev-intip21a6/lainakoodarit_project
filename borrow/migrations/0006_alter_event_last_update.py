# Generated by Django 4.1.7 on 2023-04-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0005_alter_event_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='last_update',
            field=models.CharField(default='2023/04/15 11:24:12', editable=False, max_length=30),
        ),
    ]
