# Generated by Django 4.1.3 on 2022-11-29 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"ordering": ["last_name"]},
        ),
        migrations.AlterModelOptions(
            name="dish",
            options={"ordering": ["name"], "verbose_name_plural": "dishes"},
        ),
    ]