# Generated by Django 4.1.3 on 2022-12-28 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0006_alter_dishtype_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dishtype",
            options={"ordering": ["name"]},
        ),
    ]
