# Generated by Django 3.1.6 on 2021-02-15 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0004_auto_20210211_2113"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="url",
        ),
    ]