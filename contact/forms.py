from django import forms 
from .models import Contact

# CREATING A FORM FOR THE SPECIFIED MODEL
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact      
        # fields = ['fname', 'email']
        fields = '__all__'
        # exclude = ['fname', 'message']
        labels = {
            'fname': 'Full Name',
        }
        # help_texts = {
        #     'message': 'Enter some text...'
        # }
        error_messages = {
            'email': {
                'required': "Enter proper mail id"
            }
        }
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Type something',
                'rows': 10,
                'cols': 30,
                'class':'txt-box'
            })
        }



# MANUAL WAY OF CREATING THE FORM
# class ContactForm(forms.Form):
#     full_name = forms.CharField(max_length=50, label="Full Name", required=True)
#     name = forms.CharField(max_length=50, label="Name", disabled=False)
#     email = forms.EmailField(required=True)
#     message = forms.CharField(widget=forms.Textarea)