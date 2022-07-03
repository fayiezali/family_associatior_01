from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
# Q object encapsulates a SQL expression in a Python object that can be used in database-related operations. 
# Using Q objects we can make complex queries with less and simple code.
from django.db.models import Q

# create class
class EmailBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None,**kwargs):
        try:
            ''' check username or email & password is a valid user'''
            user = User.objects.get(
                Q(username__iexact=username) | 
                Q(email__iexact=username)
            )
        except User.DoesNotExist:
            # If Can't find It , do Nothing
            return None

        except:
            # If You find Email Choose The First Email
            return User.objects.filter(email=username).order_by('id').first()

        else:
            # Verify The Validity Of The Password and The Validaity Of The User And Then Return USER
            if user.check_password(password) and self.user_can_authenticate(user):
                return user


    def get_user(self,user_id):
        try :
            # ٍSave "User" In The Variable user
            user = User.objects.get(pk=user_id)

        except User.DoesNotExist:
            return None
        # Gving Access to The User
        #If It Has No Validity do Not Return Anything
        return user if self.user_can_authenticate(user) else None