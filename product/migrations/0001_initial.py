# Generated by Django 4.2.3 on 2024-03-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=120)),
                ("conttne", models.TextField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
