from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from enfermaria.models import Enfermaria,BloodRequest,BloodRequestResponse
from patient.models import Patient
from doador.models import DoadorBloodPackage


class DateInput(forms.DateInput):
	input_type = 'date'

class EnfermariaForm(forms.ModelForm):
	class Meta:
		model = Enfermaria
		fields = ['name']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)


class BloodRequestForm(forms.ModelForm):
	date_of_request = forms.DateField(label='Data Pedidu', widget=DateInput())
	description = forms.CharField(label='Deskrisaun',widget=forms.Textarea(attrs={'rows':3}))
	class Meta:
		model = BloodRequest
		fields = ['package','date_of_request','description']
		exclude = ['patient','enfermaria','is_locked','is_sent','is_approved','is_rejected','rejected_info','user_created','hashed']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			HTML(""" <p class="text-primary text-center">Informasaun/Dadus Pasiente <hr>  """),
			HTML(""" {% load crispy_forms_tags %} {% crispy formPatient %} <hr>  """),
			HTML(""" <p class="text-primary text-center">Informasaun/Dadus Pedidu</p> <hr>  """),
			Row(
				Column('date_of_request', css_class='form-group col-md-4 mb-0'),
				Column('package', css_class='form-group col-md-4 mb-0'),
				Column('description', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit"> <i class="fa fa-save"></i> Save</button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class BloodRequestForm1(forms.ModelForm):
	date_of_request = forms.DateField(label='Data Halo Pedidu', widget=DateInput(),required=False)
	description = forms.CharField(label='Deskrisaun',widget=forms.Textarea(attrs={'rows':3}))
	patient = forms.ModelChoiceField(queryset=Patient.objects.order_by('firstname'),required=False)
	package = forms.CharField(label='Total Pakote',required=False)
	class Meta:
		model = BloodRequest
		fields = ['patient','package','date_of_request','description']
		exclude = ['enfermaria','is_locked','is_sent','is_approved','is_rejected','rejected_info','user_created','hashed']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('patient', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('date_of_request', css_class='form-group col-md-4 mb-0'),
				Column('package', css_class='form-group col-md-4 mb-0'),
				Column('description', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)



class BloodRequestResponseForm(forms.ModelForm):
	date_of_response = forms.DateField(label='Data Responde Pedidu', widget=DateInput(),required=False)
	description = forms.CharField(label='Deskrisaun',widget=forms.Textarea(attrs={'rows':3}))
	class Meta:
		model = BloodRequestResponse
		fields = ['doador','date_of_response','description']
		exclude = ['doador','bloodRequest','user_created','hashed','is_locked','is_sent','is_used']

	def __init__(self, *args, **kwargs):
		# grupuRan = kwargs.pop('grupuRan',None)
		super().__init__(*args, **kwargs)
		# self.fields['doador'].queryset = DoadorBloodPackage.objects.filter(bloodGroup__name=grupuRan,packageStatus="Banked").order_by('id')
		self.helper = FormHelper()
		self.helper.layout = Layout(
			
			Row(
				Column(
					HTML("""
						<label>Lista Doasaun :</label> <small class="badge badge-info">Hili pakote ran</small><br>
						{% for item in listaDoador %}
							<label class="checkbox-inline">
		                        <input id="inlineCheckbox1" type="checkbox" name="doador" value="{{item.id}}"> {{item}}
		                    </label>  
						{% endfor %}
						{% if listaDoador|length == 0 %}
							<small><i>Pakote Grupu Ran ne'ebe pedidu mai stock mamuk hela!</i></small>
						{% endif %}
		            <hr>"""),		
				),
				Column('date_of_response', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('description', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)
