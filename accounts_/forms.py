from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#
#
#
# class AssociationData_FORM(forms.ModelForm):  
#         class Meta:  
#             model = AssociationData_MODEL  
#             fields = '__all__' # ظهور جميع الحقول في النموذج
#             # fields = ['ASS_AssociationLogo', 'ASS_NameAssociation'] # ظهور حقول محددة في النموذج
#
#
# Create/Signup Profile For User
# The model that is customized 
class SignUpForm(UserCreationForm):
    # Customization 3 fields In Form Signup.
    email         = forms.EmailField(max_length=150  , required=True  , widget=forms.EmailInput() , help_text='Required Field') # 03
    #
    class Meta:
        # Data Table
        model      = User 
        #-------------
        # Table Fields
        fields     = {'username','password2','password1','email'} 
        #-------------
        labels     = {'username' : ('User Name')} # change the Field Title
        labels     = {'Password1': ('Password')} # change the Field Title
        labels     = {'password2': ('Confirm Passwoerd')} # change the Field Title
        #-------------
        help_texts = {'email'    : ('Please Enter a Valid Email.')} 
#
#
# 
# Profile Update
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User # Data Table
        fields = [ # Fields Table
            'username',
            'first_name', 
            'last_name', 
            'email',
            ]
#
#
#
# Create All User Data
# The model that is customized 
# class GeneralUserRecordForm(UserCreationForm):
#     # Customization 3 fields In Form Signup.
#     email         = forms.EmailField(max_length=150  , required=True  , widget=forms.EmailInput() , help_text='Required Field') # 03
#     your_name     = forms.CharField(label='Your name', max_length=100)
#     subject       = forms.CharField(max_length=100)
#     message       = forms.CharField(widget=forms.Textarea)
#     sender        = forms.EmailField()
#     cc_myself     = forms.BooleanField(required=False
#     #
#     class Meta:
#         model      = User # Data Table
#         #-------------
#         fields     = {'password2','password1','username','email'} # Table Fields
#         #-------------
#         labels     = {'username' : ('User Name')} # change the Field Title
#         labels     = {'Password1': ('Password')} # change the Field Title
#         labels     = {'password2': ('Confirm Passwoerd')} # change the Field Title
#         #-------------
#         help_texts = {'email'    : ('Please Enter a Valid Email.')} 
#
#
# 