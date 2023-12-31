from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона:")
    title_en = models.CharField(max_length=200, null=False, blank=True, verbose_name="Название покемона на английском:")
    title_jp = models.CharField(max_length=200, null=False, blank=True, verbose_name="Название покемона на японском:")
    photo = models.ImageField(null=True, blank=True, upload_to='pokemons', verbose_name="Изображение покемона:")
    description = models.TextField(null=False, blank=True, verbose_name="Описание покемона:")
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_evolutions', verbose_name="предыдущая эволюция:")

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities', verbose_name="Pokemon:")
    lat = models.FloatField(verbose_name="Lat:", null=True)
    lon = models.FloatField(verbose_name="Lon:", null=True)
    appeared_at = models.DateTimeField(verbose_name="Appeared at:", null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name="Disappeared at:", null=True, blank=True)
    level = models.IntegerField(verbose_name="Level:", null=True, blank=True)
    health = models.IntegerField(verbose_name="Health:", null=True, blank=True)
    strength = models.IntegerField(verbose_name="Strength:", null=True, blank=True)
    defence = models.IntegerField(verbose_name="Defence:", null=True, blank=True)
    stamina = models.IntegerField(verbose_name="Stamina:", null=True, blank=True)

    def __str__(self):
        return self.pokemon.title if self.pokemon else 'No Pokemon'
