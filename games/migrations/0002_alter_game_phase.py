# Generated by Django 4.1.2 on 2022-11-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="phase",
            field=models.CharField(
                choices=[
                    ("Quartas Upper", "Quarters Upper"),
                    ("Semi Upper", "Semi Upper"),
                    ("Semi Lower 1", "Semi Lower 1"),
                    ("Semi Lower 2", "Semi Lower 2"),
                    ("Final Upper", "Final Upper"),
                    ("Final Lower", "Final Lower"),
                    ("Final Champions", "Final Champions"),
                    ("Not Subscribed", "Default"),
                ],
                default="Not Subscribed",
                max_length=20,
            ),
        ),
    ]