from django.db import models

import random


def random_string():
    return str(random.randint(10000, 99999))


class Game(models.Model):
    game_name = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s" % (self.game_name)


class Person(models.Model):
    game = models.ForeignKey(Game)
    person_name = models.CharField(max_length=200)
    # assigns a random integer to each person to determine the order they play in
    order = models.CharField(default=random_string, max_length=20)

    def __unicode__(self):
        return "%s" % (self.person_name)


class Gift(models.Model):
    person = models.ForeignKey(Person)
    gift_name = models.CharField(max_length=200)
    gift_description = models.TextField()

    def __unicode__(self):
        return "%s" % (self.gift_name)
