from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(null=True, upload_to='pokemons')

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, verbose_name="Pokemon", null=True)
    lat = models.FloatField(verbose_name="Lat", null=True)
    lon = models.FloatField(verbose_name="Lon", null=True)


2