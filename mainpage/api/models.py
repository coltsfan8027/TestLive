# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

 # Field name made lowercase.






class ClientName(models.Model):
    clientid = models.IntegerField(db_column='clientID', primary_key=True)  # Field name made lowercase.
    clientname = models.CharField(max_length=45, blank=True, null=True)
    clienttype = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.clientname
    class Meta:
        managed = False
        db_table = 'client name'











class Location(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    address1 = models.CharField(max_length=45, blank=True, null=True)
    address2 = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    postalcode = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    phonenumber = models.CharField(max_length=45, blank=True, null=True)
    faxnumber = models.CharField(max_length=45, blank=True, null=True)
    clientid = models.ForeignKey(ClientName, on_delete=models.CASCADE, db_column='clientID')  # Field name made lowercase.
    def __str__(self):
        return self.address1
    class Meta:
        managed = False
        db_table = 'location'

class TestSequence(models.Model):
    sequenceid = models.IntegerField(db_column='sequenceID', primary_key=True)  # Field name made lowercase.
    sequencename = models.CharField(db_column='sequenceName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.sequencename
    class Meta:
        managed = False
        db_table = 'test sequence'

class PerformanceData(models.Model):
    modelnumber = models.OneToOneField('Product', on_delete=models.CASCADE, db_column='modelNumber', primary_key=True)  # Field name made lowercase.
    test_sequence_sequenceid = models.ForeignKey('TestSequence', on_delete=models.CASCADE, db_column='Test Sequence_sequenceID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maxsysvolt = models.CharField(db_column='maxSysVolt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    voc = models.CharField(db_column='VOC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isc = models.CharField(db_column='ISC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vmp = models.CharField(db_column='VMP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    imp = models.CharField(db_column='IMP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pmp = models.CharField(db_column='PMP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ff = models.CharField(db_column='FF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.modelnumber
    class Meta:
        managed = False
        db_table = 'performance data'
        unique_together = (('modelnumber', 'test_sequence_sequenceid'),)


class Product(models.Model):
    modelnumber = models.IntegerField(db_column='modelNumber', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celltech = models.CharField(db_column='cellTech', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cellman = models.CharField(db_column='cellMan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numberofcells = models.CharField(db_column='numberOfCells', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cellsinseries = models.CharField(db_column='cellsInSeries', max_length=45, blank=True, null=True)  # Field name made lowercase.
    seriesinstrings = models.CharField(db_column='seriesInStrings', max_length=45, blank=True, null=True)  # Field name made lowercase.
    diodes = models.CharField(max_length=45, blank=True, null=True)
    productlen = models.CharField(db_column='productLen', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productwidth = models.CharField(db_column='productWidth', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productweight = models.CharField(db_column='productWeight', max_length=45, blank=True, null=True)  # Field name made lowercase.
    superstatetype = models.CharField(db_column='superstateType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    substrateman = models.CharField(db_column='substrateMan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    frametype = models.CharField(db_column='frameType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    frameadhesive = models.CharField(db_column='frameAdhesive', max_length=45, blank=True, null=True)  # Field name made lowercase.
    encapsulanttype = models.CharField(db_column='encapsulantType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    encapsulantman = models.CharField(db_column='encapsulantMan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    junctionboxtype = models.CharField(db_column='junctionBoxType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    junctionboxman = models.CharField(db_column='junctionBoxMan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.productname
    class Meta:
        managed = False
        db_table = 'product'

class TestStandard(models.Model):
    standardid = models.IntegerField(db_column='standardID', primary_key=True)  # Field name made lowercase.
    standardname = models.CharField(db_column='standardName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=45, blank=True, null=True)
    publisheddate = models.CharField(db_column='publishedDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.standardname
    class Meta:
        managed = False
        db_table = 'test standard'

class Service(models.Model):
    serviceid = models.IntegerField(db_column='serviceID', primary_key=True)  # Field name made lowercase.
    servicename = models.CharField(db_column='serviceName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=45, blank=True, null=True)
    isflrequired = models.CharField(db_column='isFLrequired', max_length=45, blank=True, null=True)  # Field name made lowercase.
    flfrequency = models.CharField(db_column='Flfrequency', max_length=45, blank=True, null=True)  # Field name made lowercase.
    standardid = models.ForeignKey('TestStandard', on_delete=models.CASCADE, db_column='standardID')  # Field name made lowercase.
    def __str__(self):
        return self.servicename
    class Meta:
        managed = False
        db_table = 'service'








class User(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45, blank=True, null=True)
    mname = models.CharField(max_length=45, blank=True, null=True)
    jobtitle = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    officephone = models.CharField(max_length=45, blank=True, null=True)
    cellphone = models.CharField(max_length=45, blank=True, null=True)
    clientid = models.ForeignKey(ClientName, on_delete=models.CASCADE, db_column='clientID') 

    def __str__(self):
        return self.email
    class Meta:
        managed = False
        db_table = 'user'

class Certificate(models.Model):
    certificatenumber = models.IntegerField(db_column='certificateNumber', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    reportnumber = models.CharField(db_column='reportNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    issuedate = models.CharField(db_column='issueDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    certificatecol = models.CharField(db_column='Certificatecol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', on_delete=models.CASCADE, db_column='userID')  # Field name made lowercase.
    locationid = models.ForeignKey('Location', on_delete=models.CASCADE, db_column='locationID')  # Field name made lowercase.
    standardid = models.ForeignKey('TestStandard', on_delete=models.CASCADE, db_column='standardID')  # Field name made lowercase.
    modelnumber = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='modelNumber')  # Field name made lowercase.

    def __str__(self):
        return self.id
    class Meta:
        managed = False
        db_table = 'certificate'