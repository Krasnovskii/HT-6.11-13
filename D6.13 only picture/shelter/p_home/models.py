from django.db import models


class Type(models.Model):
    type = models.CharField('Вид животного', max_length=100)

    def __str__(self):
        return (self.type)





class Breed(models.Model):
    breed = models.CharField('порода', max_length=100)

    def __str__(self):
        return (self.breed)


class Animal(models.Model):
    ISBN = models.CharField(max_length=13)
    name = models.CharField('Имя', max_length=50)
    description = models.TextField('Описание животного')
    date = models.DateField('Дата поступления')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatars/%Y/%m/%d', blank=True)

    def __str__(self):
        return (self.name)



