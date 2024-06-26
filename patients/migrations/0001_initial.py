# Generated by Django 5.0.6 on 2024-06-06 19:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("doctors", "0003_setdate"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Consultation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "Agendada"),
                            ("F", "Finalizada"),
                            ("C", "Cancelada"),
                            ("I", "Iniciada"),
                        ],
                        default="A",
                        max_length=1,
                    ),
                ),
                ("link", models.URLField(blank=True, null=True)),
                (
                    "data_aberta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="doctors.setdate",
                    ),
                ),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
