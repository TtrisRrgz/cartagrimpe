# Generated by Django 5.1.1 on 2024-10-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AjoutEvenement", "0006_alter_evenement_lien_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evenement",
            name="commentaire",
            field=models.TextField(
                default="Pas de commentaire",
                help_text="(Non vide, Description, doutes, ...)",
            ),
        ),
        migrations.AlterField(
            model_name="evenement",
            name="lien_logo",
            field=models.URLField(
                blank=True,
                help_text="(Obligatoire si l'organisateur est Autre)",
                max_length=2000,
                null=True,
            ),
        ),
    ]
