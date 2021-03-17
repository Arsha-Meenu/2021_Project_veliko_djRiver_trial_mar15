from django.db import models
# Create your models here.
from django.contrib.auth.models import User

from river.models.fields.state import StateField

class AdmissionYearMaster(models.Model):

    admission_year = models.CharField("admission year",max_length=20)
    academic_year = models.CharField("academic year",max_length=20)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField()
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='scheme_master_admission_set')
    updated_on = models.DateTimeField( null=True, blank=True)
    status=StateField(editable=False)
 
    
    # def natural_key(self):
    #     return self.admission_year
 
 