# Generated by Django 5.0 on 2024-01-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produto", "0002_alter_variacao_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
