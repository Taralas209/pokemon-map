# Generated by Django 3.1.14 on 2023-08-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(null=True, upload_to='pokemons'),
        ),
    ]
