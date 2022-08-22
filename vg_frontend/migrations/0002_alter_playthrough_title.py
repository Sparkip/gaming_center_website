# Generated by Django 4.0.6 on 2022-08-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vg_frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playthrough',
            name='title',
            field=models.CharField(choices=[('Cult of the Lamb', 'Cult of the Lamb'), ('Overwatch', 'Overwatch'), ('Pokemon HeartGold', 'Pokemon HeartGold'), ('Pokemon Platinum', 'Pokemon Platinum'), ('Pokemon Ruby', 'Pokemon Ruby'), ('Pokemon Sapphire', 'Pokemon Sapphire'), ('RimWorld', 'RimWorld'), ('Stardew Valley', 'Stardew Valley'), ('Xenoblade Chronicles', 'Xenoblade Chronicles'), ('Xenoblade Chronicles 2', 'Xenoblade Chronicles 2'), ('Xenoblade Chronicles 3', 'Xenoblade Chronicles 3')], default=('Cult of the Lamb', 'Cult of the Lamb'), max_length=2000),
        ),
    ]