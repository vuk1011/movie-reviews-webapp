# Generated by Django 4.2.15 on 2024-08-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
