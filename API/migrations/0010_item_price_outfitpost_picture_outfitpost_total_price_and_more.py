# Generated by Django 5.0 on 2024-01-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_alter_item_material_alter_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outfitpost',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/outfits/'),
        ),
        migrations.AddField(
            model_name='outfitpost',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='budget',
            field=models.CharField(blank=True, choices=[('LOW', '$0-100'), ('MID', '$100-300'), ('HIGH', '$300-500'), ('DESIGNER', '$500+')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile-pictures/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(upload_to='images/items/'),
        ),
    ]
