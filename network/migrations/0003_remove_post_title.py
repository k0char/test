# Generated by Django 4.1.1 on 2022-10-28 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0002_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="title",
        ),
    ]