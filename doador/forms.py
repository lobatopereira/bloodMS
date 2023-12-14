from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from custom.models import Municipality,AdministrativePost,Village
from .models import Doador,Substitution,DoadorBloodPackage 


class DateInput(forms.DateInput):
	input_type = 'date'

class DoadorForm(forms.ModelForm):
	date_of_birth = forms.DateField(label='Data Moris', widget=DateInput())
	class Meta:
		model = Doador
		fields = ['firstname','lastname','sex','date_of_birth','weight','address','pressure','bloodGroup','image','municipality','administrativepost','village']
		exclude = ['user_created','hashed']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		if 'municipality' in self.data:
			try:
				municipality = int(self.data.get('municipality'))
				self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=municipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('name')

		if 'administrativepost' in self.data:
			try:
				administrativepost = int(self.data.get('administrativepost'))
				self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')
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
				Column('municipality', css_class='form-group col-md-4 mb-0'),
				Column('administrativepost', css_class='form-group col-md-4 mb-0'),
				Column('village', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('bloodGroup', css_class='form-group col-md-6 mb-0'),
				Column('weight', css_class='form-group col-md-6 mb-0'),
				Column('pressure', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),	
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit"> <i class="fa fa-save"></i> Save</button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class DoadorBloodPackageForm(forms.ModelForm):
	donationdate = forms.DateField(label='Data Doasaun', widget=DateInput())
	class Meta:
		model = DoadorBloodPackage
		fields = ['bloodGroup','package','donationdate','typeD']
		exclude = ['user_created','hashed','doador','packageStatus']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('bloodGroup', css_class='form-group col-md-6 mb-0'),
				Column('package', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('typeD', css_class='form-group col-md-6 mb-0'),
				Column('donationdate', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit"> <i class="fa fa-save"></i> Save</button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)



