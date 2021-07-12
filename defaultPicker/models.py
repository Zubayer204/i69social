from django.db import models
from googletrans import Translator

translator = Translator()


class age(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    age = models.IntegerField()
    age_fr = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'age'
        verbose_name = 'age'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.age)

    def save(self, *args, **kwargs):
        if not self.age_fr:
            self.age_fr = self.age
        return super().save(*args, **kwargs)

class ethnicity(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    ethnicity = models.CharField(max_length=265)
    ethnicity_fr = models.CharField(max_length=265, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'ethinicty'
        verbose_name = 'ethinicty'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.ethnicity) + ' - ' + str(self.ethnicity_fr)

    def save(self, *args, **kwargs):
        if not self.ethnicity_fr:
            self.ethnicity_fr = translator.translate(self.ethnicity, dest='fr').text
        return super().save(*args, **kwargs)

class family(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    familyPlans = models.CharField(max_length=265)
    familyPlans_fr = models.CharField(max_length=265, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'family'
        verbose_name = 'family'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.familyPlans) + ' - ' + str(self.familyPlans_fr)

    def save(self, *args, **kwargs):
        if not self.familyPlans_fr:
            self.familyPlans_fr = translator.translate(self.familyPlans, dest='fr').text
        return super().save(*args, **kwargs)

class politics(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    politics = models.CharField(max_length=265)
    politics_fr = models.CharField(max_length=265, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'politics'
        verbose_name = 'politics'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.politics) + ' - ' + str(self.politics_fr)

    def save(self, *args, **kwargs):
        if not self.politics_fr:
            self.politics_fr = translator.translate(self.politics, dest='fr').text
        return super().save(*args, **kwargs)

class religious(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    religious = models.CharField(max_length=265)
    religious_fr = models.CharField(max_length=265, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'religious'
        verbose_name = 'religious'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.religious) + ' - ' + str(self.religious_fr)

    def save(self, *args, **kwargs):
        if not self.religious_fr:
            self.religious_fr = translator.translate(text=self.religious, dest='fr').text
        return super().save(*args, **kwargs)

class tags(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    tag = models.CharField(max_length=265)
    tag_fr = models.CharField(max_length=265, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'tags'
        verbose_name = 'tags'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.tag) + ' - ' + str(self.tag_fr)

    def save(self, *args, **kwargs):
        if not self.tag_fr:
            self.tag_fr = translator.translate(self.tag, dest='fr').text
        return super().save(*args, **kwargs)

class zodiacSign(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    zodiacSign = models.CharField(max_length=265)
    zodiacSign_fr = models.CharField(max_length=265, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'zodiacSign'
        verbose_name = 'zodiacSign'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.zodiacSign) + ' - ' + str(self.zodiacSign_fr)

    def save(self, *args, **kwargs):
        if not self.zodiacSign_fr:
            self.zodiacSign_fr = translator.translate(self.zodiacSign, dest='fr').text
        return super().save(*args, **kwargs)