from django import forms
from django.forms import Select, FileInput,DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from .models import LandownerListingsModel

#class RegisterLandownerForm(UserCreationForm):
 #   class Meta:
  #      model = RegisterLandownerModel
   #     fields = ['username', 'contact_number', 'description','password1', 'password2']



class LandownerListingForm(forms.ModelForm):
    class Meta:
        model = LandownerListingsModel
        widgets ={ 'sale_type': Select(attrs={'class':'form-control'}),
                   'photo_main':FileInput(attrs={'class':'form-control'}),
                   'photo_1':FileInput(attrs={'class':'form-control'}),
                   'photo_2':FileInput(attrs={'class':'form-control'}),
                   'photo_3':FileInput(attrs={'class':'form-control'}),
                   'list_date':DateTimeInput(attrs={'class':'form-control'}),}
        fields = ['title', 'address','city','state', 'zipcode','price','sqft','lot_size',
                  'sale_type','contact_number','photo_main','photo_1','photo_2','photo_3','is_published',
                  'list_date','complete']


#class EditListingForm(forms.ModelForm):
 #   class Meta:
  #      model = LandownerListingsModel
   #     widgets = {'sale_type': Select(attrs={'class':'form-control'}),
    #               'photo_main': FileInput(attrs={'class':'form-control'}),
     #              'photo_1': FileInput(attrs={'class':'form-control'}),
      #             'photo_2': FileInput(attrs={'class':'form-control'}),
       #            'photo_3': FileInput(attrs={'class':'form-control'}),
        #           'list_date':DateTimeInput(attrs={'class':'form-control'}),}
        #fields = ['title', 'address', 'city', 'state', 'zipcode', 'price', 'sqft', 'lot_size',
         #         'sale_type', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'is_published',
          #        'list_date', 'complete']




