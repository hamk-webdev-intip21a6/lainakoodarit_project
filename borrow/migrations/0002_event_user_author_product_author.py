# Generated by Django 4.1.7 on 2023-04-14 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Loaned', 'Loan'), ('Returned', 'Return'), ('Late', 'Late')], default='Loaned', max_length=10)),
                ('user_id', models.SmallIntegerField()),
                ('product_id', models.SmallIntegerField()),
                ('loaned_date', models.DateField(default=datetime.date.today)),
                ('is_returned', models.BooleanField()),
                ('last_update', models.CharField(default=datetime.datetime.now, editable=False, max_length=30)),
            ],
            options={
                'ordering': ['last_update'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=25)),
                ('real_name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ['real_name'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('home_country', models.CharField(blank=True, max_length=60, null=True)),
                ('works', models.ManyToManyField(related_name='authors', to='borrow.product')),
            ],
            options={
                'ordering': ['author_name'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ManyToManyField(to='borrow.author'),
        ),
    ]
