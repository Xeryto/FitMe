# Generated by Django 5.0 on 2024-01-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0011_alter_outfitpost_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='outfitpost',
            name='description',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outfitpost',
            name='title',
            field=models.CharField(blank=True, null=True),
        ),
    ]
