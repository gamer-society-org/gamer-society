# Generated by Django 4.1.2 on 2022-11-03 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("championships", "0004_alter_championship_entry_amount_and_more"),
        ("teams", "0003_team_championship"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="championship",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teams",
                to="championships.championship",
            ),
        ),
    ]