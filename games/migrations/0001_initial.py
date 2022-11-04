# Generated by Django 4.1.2 on 2022-11-04 00:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("championships", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Game 1", "Game 1"),
                            ("Game 2", "Game 2"),
                            ("Game 3", "Game 3"),
                            ("Game 4", "Game 4"),
                        ],
                        default="Game 1",
                        max_length=20,
                    ),
                ),
                (
                    "phase",
                    models.CharField(
                        choices=[
                            ("Quartas Upper", "Quarters Upper"),
                            ("Semi Upper", "Semi Upper"),
                            ("Semi Lower", "Semi Lower"),
                            ("Final Upper", "Final Upper"),
                            ("Final Lower", "Final Lower"),
                            ("Final Champions", "Final Champions"),
                            ("Not Subscribed", "Default"),
                        ],
                        default="Not Subscribed",
                        max_length=20,
                    ),
                ),
                ("winner", models.CharField(default=None, max_length=20, null=True)),
                (
                    "result_team_1",
                    models.IntegerField(blank=True, default=None, null=True),
                ),
                (
                    "result_team_2",
                    models.IntegerField(blank=True, default=None, null=True),
                ),
                (
                    "team_1",
                    models.CharField(
                        blank=True, default=None, max_length=120, null=True
                    ),
                ),
                (
                    "team_2",
                    models.CharField(
                        blank=True, default=None, max_length=120, null=True
                    ),
                ),
                (
                    "championship",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="games",
                        to="championships.championship",
                    ),
                ),
            ],
        ),
    ]
