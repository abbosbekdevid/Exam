# Generated by Django 4.2.2 on 2023-07-03 14:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=75)),
                ('date_birth', models.DateField(default=datetime.datetime.now)),
                ('country', models.CharField(default='', max_length=35)),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='BookCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
            ],
            options={
                'db_table': 'Category_book',
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=120)),
                ('page', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.authormodel')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.bookcategorymodel')),
            ],
            options={
                'db_table': 'Book',
            },
        ),
    ]
