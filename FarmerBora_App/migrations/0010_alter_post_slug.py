# Generated by Django 5.0.3 on 2024-04-03 02:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FarmerBora_App", "0009_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, max_length=400, unique=True),
        ),
    ]
