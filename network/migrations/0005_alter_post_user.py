# Generated by Django 4.1.1 on 2022-10-28 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0004_post_user_alter_post_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
