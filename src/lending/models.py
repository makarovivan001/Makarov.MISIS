from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'
        ordering = ['name']


class Club(models.Model):
    photo = models.ImageField(upload_to='clubs/', null=True, default=None)
    name = models.CharField(max_length=35, db_index=True)
    description = models.TextField(null=True, default=None)
    country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        null=True,
        default=None,
    )
    coach = models.OneToOneField(
        'Coach',
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'club'
        ordering = ['id']


def upload_files(instance, filename):
    return 'players/' + filename.replace(' ', '_')


class Player(models.Model):
    photo = models.ImageField(upload_to=upload_files, null=True, default=None)
    surname = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    middle_name = models.CharField(
        max_length=35,
        null=True,
        default=None,
        blank=True)
    country_of_birth = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        null=True,
        default=None
    )
    number = models.PositiveSmallIntegerField()
    club = models.ForeignKey(
        Club,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='player'
    )

    def __str__(self):
        return f"{self.number} {self.surname} {self.name}"

    class Meta:
        db_table = 'player'
        ordering = ['id']


class Coach(models.Model):
    photo = models.ImageField(upload_to='coaches/', null=True, default=None)
    surname = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    middle_name = models.CharField(
        max_length=35,
        null=True,
        default=None,
        blank=True
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        db_table = 'coach'
        ordering = ['surname']
