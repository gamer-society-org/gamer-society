# Generated by Django 4.1.2 on 2022-11-07 13:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bet",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("initial_date", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                ("team_1", models.CharField(max_length=120)),
                ("team_2", models.CharField(max_length=120)),
                ("winner", models.CharField(default=None, max_length=120, null=True)),
                ("total_value", models.FloatField(blank=True, default=0.0)),
            ],
        ),
    ]
