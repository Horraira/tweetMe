# Generated by Django 3.2 on 2022-06-02 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id']},
        ),
    ]
