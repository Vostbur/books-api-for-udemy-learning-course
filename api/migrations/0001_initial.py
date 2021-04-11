# Generated by Django 3.2 on 2021-04-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('published', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to='img')),
            ],
        ),
    ]