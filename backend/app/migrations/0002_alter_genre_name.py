# Generated by Django 4.2.15 on 2024-08-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(db_column="Zanr", max_length=30),
        ),
    ]
