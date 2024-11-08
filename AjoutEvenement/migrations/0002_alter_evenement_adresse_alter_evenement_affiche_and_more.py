# Generated by Django 5.1.1 on 2024-10-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AjoutEvenement", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evenement",
            name="adresse",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="evenement",
            name="affiche",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="evenement",
            name="date_debut",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="evenement",
            name="date_fin",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="evenement",
            name="nom",
            field=models.CharField(max_length=200),
        ),
    ]
