from django.db import models


class Genre(models.Model):
    name = models.CharField(verbose_name = "Название жанра", max_length=50)
    description = models.TextField(verbose_name = "Описание жанра", null = True, blank = True)

    class Meta:
        verbose_name = "Жанр группы"
        verbose_name_plural = "Жанры групп"

    def __str__(self):
        return self.name


class Group(models.Model):
    genres = models.ManyToManyField(Genre, related_name="groups")
    name = models.CharField(verbose_name = "Название группы", max_length=50)
    image = models.ImageField(verbose_name="Картинка", upload_to="groups/", null = True, blank = True)
    description = models.TextField(verbose_name = "Описание группы", null = True, blank = True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name


class Musician(models.Model):
    group = models.ForeignKey(Group, related_name="musicians")
    name = models.CharField(verbose_name = "Псевдоним музыканта", max_length = 100)
    first_name = models.CharField(verbose_name = "Имя музыканта", max_length = 50)
    last_name = models.CharField(verbose_name = "Фамилия музыканта", max_length = 50, null = True, blank = True)
    image = models.ImageField(verbose_name="Картинка", upload_to="musicians/", null = True, blank = True)
    about_musician = models.TextField(verbose_name = "Биография музыканте", null = True, blank = True)
    date_of_birth = models.DateField(verbose_name = "Дата рождения музыканта", null = True, blank = True)
    date_of_death = models.DateField(verbose_name = "Дата смерти", null = True, blank = True)

    class Meta:
        verbose_name = "Mузыкант"
        verbose_name_plural = "Музыканты"

    def __str__(self):
        return self.name


class Album(models.Model):
    group = models.ForeignKey(Group, related_name="albums")
    name = models.CharField(verbose_name = "Название альбома", max_length = 100)
    image = models.ImageField(verbose_name="Картинка", upload_to="album/", null = True, blank = True)
    description = models.TextField(verbose_name = "Описание альбома", null = True, blank = True)
    date_of_release = models.DateField(verbose_name = "Дата создания альбома", null = True, blank = True)
    
    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.name


class Song(models.Model):
    albums = models.ManyToManyField(Album, related_name = "songs")
    name = models.CharField(verbose_name = "Название песни", max_length = 100)
    image = models.ImageField(verbose_name = "Картинка", upload_to = "songs/", null = True, blank = True)
    text = models.TextField(verbose_name = "Текст пенси", null = True, blank = True)
    description = models.TextField(verbose_name = "Описание песни", null = True, blank = True)
    file = models.FileField(verbose_name = "Файл песни", upload_to="audio/")
    date_of_release = models.DateField(verbose_name = "Дата создания песни", null = True, blank = True)

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return self.name
