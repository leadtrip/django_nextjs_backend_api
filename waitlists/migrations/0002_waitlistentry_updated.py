# Generated by Django 4.2.15 on 2024-08-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("waitlists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="waitlistentry",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
