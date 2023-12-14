from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from patient.models import Patient


class DateInput(forms.DateInput):
	input_type = 'date'

class PatientForm(forms.ModelForm):
	date_of_birth = forms.DateField(label='Data Moris', widget=DateInput())
	class Meta:
		model = Patient
		fields = ['firstname','lastname','sex','date_of_birth','weight','address','pressure','bloodGroup']
		exclude = ['enfermaria','user_created','hashed']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('firstname', css_class='form-group col-md-6 mb-0'),
				Column('lastname', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('sex', css_class='form-group col-md-4 mb-0'),
				Column('date_of_birth', css_class='form-group col-md-4 mb-0'),
				Column('address', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('bloodGroup', css_class='form-group col-md-4 mb-0'),
				Column('weight', css_class='form-group col-md-4 mb-0'),
				Column('pressure', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
		)

