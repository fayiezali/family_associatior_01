from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from accounts.models import PersonalsMODEL  , DatesReceivingMoneyPaymentsMODEL
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
# Create/Signup Profile For User     email = forms.EmailField(label = "Email")
# The model that is customized 
class SignUpForm(UserCreationForm):
    # Customization 3 fields In Form Signup.
    email       = forms.EmailField(max_length=150   , required=True  , widget=forms.EmailInput()   , help_text='Required Field' ,label = 'Email') # 03
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+966999999999'. Up to 12 digits allowed.") # Mobile Number Verification
    # Mobile      = forms.CharField(validators=[phone_regex], max_length=12 , label = 'Mobile')
    # department = forms.ChoiceField(choices = (('1','CSE'),('2','IT'),('3','ECE'),('4','EEE')))
    # file =  forms.FileField()
    #
    class Meta:
        # Data Table
        model      = User 
        #-------------
        # Table Fields
        fields     = {'username','password2','password1','email'}  
        #-------------
        labels     = {'username' : ('User Name - إسم المستخدم')} # change the Field Title
        labels     = {'Password1': ('Password - كلمة المرور')} # change the Field Title
        labels     = {'password2': ('Confirm Passwoerd - تأكيد كلمة المرور')} # change the Field Title
        #-------------
        help_texts = {'email'    : ('Please Enter a Valid Email - الرجاء إدخال بريد إلكتروني صحيح.')}  
        # help_texts = {'Mobile'   : ('Please Enter a Valid Mobile.')}   
    #
#
#
# 
# Profile Update
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User # Data Table
        fields = [ # Fields Table
            # 'first_name', 
            # 'last_name', 
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
# class SignUpForm______(UserCreationForm):
#     # Customization 3 fields In Form Signup.
#     # email       = forms.EmailField(max_length=150   , required=True  , widget=forms.EmailInput()   , help_text='Required Field' ,label = 'Email') # 03
#     # first_name = forms.CharField(max_length=30)
#     # last_name = forms.CharField(max_length=150)
#     #
#     class Meta:
#         # Data Table
#         model      = User 
#         #-------------
#         # Table Fields
#         fields     = ('username','password2','password1','email','first_name','last_name')  
#         #-------------
#         # labels     = {'username' : ('User Name')} # change the Field Title
#         # labels     = {'Password1': ('Password')} # change the Field Title
#         # labels     = {'password2': ('Confirm Passwoerd')} # change the Field Title
#         # #-------------
#         # help_texts = {'email'    : ('Please Enter a Valid Email.')}  
#         # help_texts = {'Mobile'   : ('Please Enter a Valid Mobile.')}   
#     #
#     def save(self, commit = True):
#         user = super().save(commit=False)
        
#         # user.email     =self.cleaned_data['email']
#         # user.first_name=self.cleaned_data['first_name']
#         # user.last_name =self.cleaned_data['last_name']
        
#         if commit:
#             user.save()
#         return user

# class ProfileForm(forms.ModelForm):
#     # Customization 3 fields In Form Signup.
#     # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+966999999999'. Up to 12 digits allowed.") # Mobile Number Verification
#     # mobile      = forms.CharField(validators=[phone_regex], max_length=12 , label = 'Mobile')
#     # department = forms.ChoiceField(choices = (('1','CSE'),('2','IT'),('3','ECE'),('4','EEE')))
#     # file =  forms.FileField()
#     #
#     class Meta:
#         # Data Table
#         model      = PersonalsMODEL 
#         #-------------
#         # Table Fields
#         fields     = ('slug','P_FirstName','P_FatherName','P_GrandFatherName','P_FamilyName','P_Photo','P_Mobile','P_Address','P_Notes') 
#         #------------- 
#         # labels     = {'P_Mobile' : ('Mobile Number')} # change the Field Title

#         #-------------
#         # help_texts = {'Mobile Number'   : ('Please Enter a Valid Mobile.')}   






# class SignUpForm(UserCreationForm):
#     mob = forms.IntegerField() # newly added 
#     class Meta:
#         model = User
#         fields = ('username', 'mob', 'password1', 'password2', )
#         labels = {'mob': 'Mobile Number',} # newly added

















































































class SignUpForm______(UserCreationForm):
    # Customization 3 fields In Form Signup.
    email       = forms.EmailField(max_length=150   , required=True  , widget=forms.EmailInput()   , help_text='Required Field' ,label = 'Email') # 03
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+966999999999'. Up to 12 digits allowed.") # Mobile Number Verification
    # Mobile      = forms.CharField(validators=[phone_regex], max_length=12 , label = 'Mobile')
    # department = forms.ChoiceField(choices = (('1','CSE'),('2','IT'),('3','ECE'),('4','EEE')))
    # file =  forms.FileField()
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
        # help_texts = {'Mobile'   : ('Please Enter a Valid Mobile.')}   
    #
