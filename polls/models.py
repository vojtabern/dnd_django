from django.db import models


def class_path(instance, filename):
    return "class/" + str(instance.name) + "/skin/" + filename


def character_path(instance, filename):
    return "character/" + str(instance.name) + "/name/" + filename


def player_path(instance, filename):
    return "player/" + str(instance.name) + "/his_name/" + filename


class Player(models.Model):
    player_id = models.IntegerField(default=0, primary_key=True)
    surrname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    player_picture = models.ImageField(upload_to='player_path', default='NULL')

    class Meta:
        ordering = ["lastname", "surrname"]

    def __str__(self):
        return self.lastname


class Level(models.Model):
    level = models.IntegerField(default=0, primary_key=True)
    health_dice = models.CharField(max_length=45)
    max_health = models.IntegerField(default=10)

    class Meta:
        ordering = ["level"]

    def __str__(self):
        return str(self.level)


class Weapons(models.Model):
    STANDARD = (
        ("axe", "axe"),
        ("sword", "sword"),
        ("bow", "bow"),
        ("knife", "knife"),
        ("mace", "mace"),
        ("spear", "spear"),
        ("crossbow", "crossbow"),
        ("stick", "stick"),
    )
    DMG = (
        ("bludgeoning", "bludgeoning"),
        ("fire", "fire"),
        ("radiant", "radiant"),
        ("cold", "cold"),
        ("slashing", "slashing"),
    )
    idweapon = models.IntegerField(default=0, primary_key=True)
    name_of_weapon = models.CharField(max_length=45)
    type_of_weapon = models.CharField(max_length=45, choices=STANDARD, default="axe")
    damage = models.CharField(max_length=20, default="2x4d")
    damage_type = models.CharField(max_length=45, choices=DMG, default="fire")
    price = models.IntegerField()

    class Meta:
        ordering = ["type_of_weapon"]

    def __str__(self):
        return self.name_of_weapon

class Skills(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length=50)
    skill_description = models.TextField()

    class Meta:
        ordering = ["skill_name"]

    def __str__(self):
        return self.skill_name


class Class(models.Model):
    class_name = models.CharField(max_length=20, primary_key=True)
    class_description = models.TextField()
    bonuses = models.TextField()
    class_picture = models.ImageField(upload_to='class_path', default='NULL')
    skill_id = models.ManyToManyField(Skills, verbose_name="Skills")

    class Meta:
        ordering = ["class_name"]

    def __str__(self):
        return self.class_name


class Character(models.Model):
    character_name = models.CharField(max_length=50)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name="Name of the player")
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapons, on_delete=models.CASCADE)
    dnd_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    character_image = models.ImageField(upload_to='character_path', default='NULL')
    character_background = models.TextField(verbose_name="Background story", default='Homeless')

    class Meta:
        ordering = ["character_name"]

    def __str__(self):
        return self.character_name
