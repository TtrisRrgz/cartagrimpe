# Generated by Django 5.1.1 on 2024-10-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AjoutEvenement", "0004_alter_evenement_type_evenement"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="evenement",
            name="lien_internet",
        ),
        migrations.AddField(
            model_name="evenement",
            name="lien",
            field=models.URLField(
                help_text="(https://www.MonEvenement.com)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="evenement",
            name="lien_logo",
            field=models.URLField(max_length=2000),
        ),
    ]
