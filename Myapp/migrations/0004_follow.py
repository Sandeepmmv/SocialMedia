# Generated by Django 4.1.4 on 2023-05-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_like_alter_post_nos_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]