# Generated by Django 4.0.6 on 2022-07-13 19:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("plataforma", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paciente",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
