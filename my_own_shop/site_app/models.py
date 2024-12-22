from django.db import models

class UpPartField(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)
    date_field = models.DateField()

    def __str__(self):
        return self.title
