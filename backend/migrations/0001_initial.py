# Generated by Django 5.0.2 on 2024-02-19 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lawyer",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("description", models.CharField(max_length=200)),
                ("img", models.URLField(null=True)),
                ("certificate", models.URLField()),
                ("password", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Ngo",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("description", models.CharField(max_length=200)),
                ("img", models.URLField(null=True)),
                ("certificate", models.URLField()),
                ("password", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Therapist",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("description", models.CharField(max_length=200)),
                ("img", models.URLField(null=True)),
                ("certificate", models.URLField()),
                ("password", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserPost",
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
                ("description", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("img", models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Opportunity",
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
                ("title", models.CharField(max_length=200)),
                ("contact_no", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=200)),
                ("prize", models.IntegerField()),
                ("certification", models.BooleanField()),
                ("date", models.DateTimeField()),
                (
                    "ngo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.ngo"
                    ),
                ),
            ],
        ),
    ]
