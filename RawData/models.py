from django.db import models


class StaffData(models.Model):
    objects = models.Manager()
    surName = models.CharField(max_length=500, default='', null=False, blank=False)
    firstName = models.CharField(max_length=500, default='', null=False, blank=False)
    middleName = models.CharField(max_length=500, default='', null=False, blank=False)
    extensionName = models.CharField(max_length=500, default='', null=False, blank=False)
    dateBirth = models.DateField(null=True)
    placeBirth = models.CharField(max_length=500, default='', null=False, blank=False)
    sex = models.CharField(max_length=500, default='', null=False, blank=False)
    civilStatus = models.CharField(max_length=500, default='', null=False, blank=False)
    gsisId = models.CharField(max_length=500, default='', null=False, blank=False)
    pagibigId = models.CharField(max_length=500, default='', null=False, blank=False)
    philhealthId = models.CharField(max_length=500, default='', null=False, blank=False)
    tinId = models.CharField(max_length=500, default='', null=False, blank=False)
    mobileNum = models.CharField(max_length=500, default='', null=False, blank=False)
    depedEmail = models.CharField(max_length=500, default='', null=False, blank=False)
    positionType = models.ForeignKey('RawData.PositionType', default='', null=False, blank=False,
                                     on_delete=models.CASCADE)
    positionName = models.ForeignKey('RawData.Position', default='', null=False, blank=False,
                                     on_delete=models.CASCADE)
    districtName = models.ForeignKey('RawData.District', default='', null=False, blank=False,
                                     on_delete=models.CASCADE)
    schoolName = models.ForeignKey('RawData.School', default='', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.surName


class District(models.Model):
    objects = models.Manager()
    districtName = models.CharField(max_length=255, default='', null=False, blank=False)

    def __str__(self):
        return self.districtName


class School(models.Model):
    objects = models.Manager()
    districtName = models.ForeignKey('RawData.District', default='', null=False, blank=False,
                                     on_delete=models.CASCADE)
    schoolName = models.CharField(max_length=255, default='', null=False, blank=False)

    def __str__(self):
        return self.schoolName


class PositionType(models.Model):
    objects = models.Manager()
    positionType = models.CharField(max_length=255, default='', null=False, blank=False)

    def __str__(self):
        return self.positionType


class Position(models.Model):
    objects = models.Manager()
    positionType = models.ForeignKey('RawData.PositionType', default='', null=False, blank=False,
                                     on_delete=models.CASCADE)
    positionName = models.CharField(max_length=255, default='', null=False, blank=False)

    def __str__(self):
        return self.positionName

