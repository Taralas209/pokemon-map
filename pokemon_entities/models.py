from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(null=True, upload_to='pokemons')

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    Lat = models.FloatField()
    Lon = models.FloatField()


