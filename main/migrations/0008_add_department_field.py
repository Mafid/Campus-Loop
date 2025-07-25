# Generated by Django 5.2.3 on 2025-07-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_remove_year_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="academicresource",
            name="department",
            field=models.CharField(
                choices=[
                    ("CSE", "Computer Science & Engineering"),
                    ("EEE", "Electrical & Electronic Engineering"),
                    ("CE", "Civil Engineering"),
                    ("DBA", "Business Administration"),
                    ("LAW", "Law"),
                ],
                default="CSE",
                max_length=10,
            ),
        ),
    ]
