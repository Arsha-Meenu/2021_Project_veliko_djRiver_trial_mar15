from django.contrib import admin
from .models import AdmissionYearMaster
# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe

def create_river_button(obj, transition_approval):
    approve_data_url = reverse('approve_data', kwargs={'id': obj.pk, 'next_state_id': transition_approval.transition.destination_state.pk})
    return f"""
        <input
            type="button"
            style="margin:2px;2px;2px;2px;"
            value="{transition_approval.transition.source_state}  >>  {transition_approval.transition.destination_state}"
            onclick="location.href=\'{approve_data_url}\'"
        />
    """
class AdmissionYearMasterAdmin(admin.ModelAdmin):
    list_display =('admission_year','academic_year','created_by','updated_by','status','river_actions')

    def get_list_display(self,request):
        self.user = request.user
        return super(AdmissionYearMasterAdmin,self).get_list_display(request)


    def river_actions(self,obj):
        content  = ""
        for transition_approval in obj.river.status.get_available_approvals(as_user = self.user):
            content += create_river_button(obj,transition_approval)
        return mark_safe(content) 

admin.site.register(AdmissionYearMaster,AdmissionYearMasterAdmin)

