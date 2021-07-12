from django.db import models


class age(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = 'age'
        verbose_name = 'age'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.age)

class ethnicity(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    ethnicity = models.CharField(max_length=265)
    ethnicity_fr = models.CharField(max_length=265)

    class Meta:
        verbose_name_plural = 'ethinicty'
        verbose_name = 'ethinicty'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.ethnicity) + ' - ' + str(self.ethnicity_fr)

class family(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    familyPlans = models.CharField(max_length=265)
    familyPlans_fr = models.CharField(max_length=265)

    class Meta:
        verbose_name_plural = 'family'
        verbose_name = 'family'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.familyPlans) + ' - ' + str(self.familyPlans_fr)

class politics(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    politics = models.CharField(max_length=265)
    politics_fr = models.CharField(max_length=265)

    class Meta:
        verbose_name_plural = 'politics'
        verbose_name = 'politics'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.politics) + ' - ' + str(self.politics_fr)

class religious(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    religious = models.CharField(max_length=265)
    religious_fr = models.CharField(max_length=265)

    class Meta:
        verbose_name_plural = 'religious'
        verbose_name = 'religious'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.religious) + ' - ' + str(self.religious_fr)

class tags(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    tag = models.CharField(max_length=265)
    tag_fr = models.CharField(max_length=265)

    class Meta:
        verbose_name_plural = 'tags'
        verbose_name = 'tags'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.tag) + ' - ' + str(self.tag_fr)

class zodiacSign(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    zodiacSign = models.CharField(max_length=265)
    zodiacSign_fr = models.CharField(max_length=265)

    class Meta:
        verbose_name_plural = 'zodiacSign'
        verbose_name = 'zodiacSign'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.zodiacSign) + ' - ' + str(self.zodiacSign_fr)