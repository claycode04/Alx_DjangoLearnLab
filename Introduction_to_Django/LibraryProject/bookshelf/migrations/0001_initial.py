# Generated by Django 5.2.4 on 2025-07-13 22:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the book title', max_length=200)),
                ('author', models.CharField(help_text="Enter the author's name", max_length=100)),
                ('publication_year', models.PositiveIntegerField(help_text='Enter the publication year')),
                ('isbn', models.CharField(help_text='Enter the 13-character ISBN', max_length=13, unique=True)),
                ('pages', models.PositiveIntegerField(help_text='Enter the number of pages')),
                ('cover', models.CharField(choices=[('hard', 'Hardcover'), ('soft', 'Softcover')], default='soft', help_text='Select cover type', max_length=10)),
                ('language', models.CharField(default='English', help_text='Enter the language', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the library name', max_length=100)),
                ('location', models.CharField(help_text='Enter the library location', max_length=200)),
                ('books', models.ManyToManyField(blank=True, help_text='Select books in this library', to='bookshelf.book')),
            ],
            options={
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('library', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookshelf.library')),
            ],
        ),
    ]
