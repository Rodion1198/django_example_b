from django.db import models


class Interest(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"


class City(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"


class Human(models.Model):
    first_name = models.CharField("first_name", max_length=200)
    last_name = models.CharField("last_name", max_length=200)
    mobile = models.CharField("mobile", max_length=20)
    interests = models.ManyToManyField(Interest, verbose_name="interests", help_text="Select interest for this human")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class HumanAddress(models.Model):
    human = models.OneToOneField(Human, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.human.first_name}  ({self.street_address})"
