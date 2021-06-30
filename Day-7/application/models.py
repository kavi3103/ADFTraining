from django.db import models


# Create your models here.
class Request(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=200)
    current_city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    qualification = models.CharField(max_length=200)
    salary = models.IntegerField()
    pan = models.CharField(max_length=10)
    created_at = models.DateTimeField()


class Response(models.Model):
    response = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)
    request_id = models.IntegerField()
    json_object = models.JSONField()
