# Generated by Django 5.0.3 on 2024-04-03 02:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FarmerBora_App", "0006_alter_comment_user_alter_reply_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, max_length=400),
        ),
    ]
