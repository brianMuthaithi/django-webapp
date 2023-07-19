from django.db import models

# Create your models here.
class BikeModel(models.Model):
    bike_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bike_type = models.CharField(max_length=255)
    wheels = models.IntegerField()
    weight = models.FloatField(max_length=255)
    material = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class RouteModel(models.Model):
    route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    route_type = models.CharField(max_length=255)
    length = models.FloatField(max_length=255)
    date = models.DateField()
    weather = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BranchModel(models.Model):
    branch_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CustomerModel(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=20)
    bike = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    route = models.ForeignKey(RouteModel, on_delete=models.CASCADE)
    branch = models.ForeignKey(BranchModel, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Return_bike(models.Model):
    customer_id = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    bike_id = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(BranchModel, on_delete=models.CASCADE)
    return_time = models.DateTimeField()

    def __str__(self):
        return self.return_time
    