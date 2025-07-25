# Generated by Django 5.2.3 on 2025-07-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="department_year",
        ),
        migrations.AddField(
            model_name="review",
            name="department",
            field=models.CharField(
                blank=True,
                choices=[
                    ("CSE", "CSE"),
                    ("EEE", "EEE"),
                    ("LAW", "LAW"),
                    ("CE", "CE"),
                    ("ENGLISH", "English"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="level_term",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1-I", "Level-1 Term-I"),
                    ("1-II", "Level-1 Term-II"),
                    ("2-I", "Level-2 Term-I"),
                    ("2-II", "Level-2 Term-II"),
                    ("3-I", "Level-3 Term-I"),
                    ("3-II", "Level-3 Term-II"),
                    ("4-I", "Level-4 Term-I"),
                    ("4-II", "Level-4 Term-II"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]
