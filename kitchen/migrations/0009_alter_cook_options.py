# Generated by Django 4.1.3 on 2023-01-03 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0008_alter_dish_dish_type"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"ordering": ["username"]},
        ),
    ]
