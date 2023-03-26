# Generated by Django 4.1.1 on 2023-03-24 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0003_rename_lattitude_jobtask_latitude"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobtask",
            name="uid",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]