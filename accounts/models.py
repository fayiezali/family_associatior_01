from django.db import models
#
from typing import ClassVar
# 
from django.contrib.auth.models import User # إستيراد اسم المستخدم
# 
from django.urls import reverse  # To generate URLS by reversing URL patterns
#
from django.db.models.signals import post_save # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده
#
# Association Data
# class AssociationData_MODEL(models.Model):
#     ASS_Address         =   models.CharField(max_length=250                       , db_index=True , blank=False , null=False , verbose_name="العنوان")
#     ASS_Mobile          =   models.CharField(max_length=10                        , db_index=True , blank=False , null=False , verbose_name="الجوال")
#     ASS_BankAccount     =   models.CharField(max_length=50                        , db_index=True , blank=False , null=False , verbose_name="الحساب البنكي - الآيبان"  ,help_text='مثال: SA000000')
#     # 
#     # 'admin'عرض إسم الحقل في صفحة
#     def __str__(self):
#         return self.ASS_NameAssociation
#     # 
#     class Meta: #'admin'عرض إسم المودل/الجدول في صفحة
#         verbose_name_plural = 'AssociationData_MODEL'
#     # 
#     # 'A-Z' ترتيب تصاعدي 
#     class Meta:
#         ordering = ['ASS_NameAssociation'] 
# 
# 
# 
# 
# 
# 
# Personal Data
class ProfilesMODEL(models.Model):
# 
    P_User                   = models.OneToOneField(User                         , on_delete=models.CASCADE                 , verbose_name="اسم المشترك")
    P_Avialable              = models.BooleanField(default=True                  , db_index=True , blank=False , null=False , verbose_name="حالة المشترك_نشط")
    P_Slug                   = models.SlugField(unique=False                     , db_index=True , blank=True  , null=False , verbose_name="الإسم التعريفي")
    P_FirstName              = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="الإسم الأول")
    P_FatherName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الاب")
    P_GrandFatherName        = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم الجد")
    P_FamilyName             = models.CharField(max_length=50                    , db_index=True , blank=False , null=False , verbose_name="إسم العائلة")
    P_Photo                  = models.ImageField(upload_to='PersonaFile_Photo/'  , db_index=True , blank=False , null=False , verbose_name="الصورة الشخصية"      ,default='Default_Image.png')
    P_Mobile                 = models.CharField(max_length=10                    , db_index=True , blank=False , null=False , verbose_name="الجوال")
    P_Address                = models.CharField(max_length=100                   , db_index=True , blank=False , null=False ,verbose_name="العنوان")
    P_Notes                  = models.CharField(max_length=100                   , db_index=True , blank=True  , null=True  , verbose_name="الملاحظات")
# #
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.P_User)
    # 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['P_User'] 
##
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها 
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها 
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ 
    def create_profiles(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            ProfilesMODEL.objects.create(P_User=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف 
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن 
    post_save.connect(create_profiles , sender=User)
# 
# 
# 
# 
#
# Financial Statements
class  FinancialStatementsMODEL(models.Model):
    # # متغير لحفظ رموز طريقة الدقع'
    # CASH     = 'CA'
    # CHECK    = 'CH'
    # TRANSFER = 'TR'
    # # قائمة بطريقة الدفع/الاستلام 
    # METHOD_PAYMENT_CHOICES = [
    #     (CASH,     'Cash'),
    #     (CHECK,    'Check'),
    #     (TRANSFER, 'Transfer'),
    # ]
    # 
    FS_User                    = models.OneToOneField(User      , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    FS_SubscriptionAmount      = models.DecimalField(default=50 , max_digits=8 , decimal_places=2   , db_index=True , blank=False  , null=False  , verbose_name="مبلغ الإشتراك")
    FS_NumberPaymentsDue       = models.IntegerField(default=1                                      , db_index=True , blank=False  , null=False  , verbose_name="عدد الدفعات")
    FS_BankName                = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="إسم البنك")
    FS_BankAccount             = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="الحساب البنكي - الآيبان")
    FS_Notes                   = models.CharField(max_length=100                                    , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات")
    # 
    # 'admin'عرض إسم الحقل في صفحة
    def __str__(self):
        return str(self.FS_User)
    # 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering = ['FS_User'] 
# #
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها 
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها 
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ 
    def create_financial_statements(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            FinancialStatementsMODEL.objects.create(FS_User=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف 
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن 
    post_save.connect(create_financial_statements , sender=User)
#
# 
# 
# 
# 
#
# Housing Data
# class  HousingData_MODEL(models.Model):
#     # HOU_Association  = models.ForeignKey(AssociationData_MODEL  , on_delete=models.CASCADE                 ,verbose_name="اسم الجمعية")
#     HOU_User         = models.OneToOneField(User                , on_delete=models.CASCADE                 ,verbose_name="اسم المشترك")
#     HOU_Region       = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="المنطقة")
#     HOU_City         = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="المدينة")
#     HOU_District     = models.CharField(max_length=25           , db_index=True , blank=False , null=False ,verbose_name="الحي")
#     HOU_HomeAddress  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="عنوان المنزل")
#     HOU_CurrentWork  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="العمل الحالي")
#     HOU_WorkAddress  = models.CharField(max_length=100          , db_index=True , blank=False , null=False ,verbose_name="عنوان العمل")
#     # 
#     # 'admin'عرض إسم الحقل في صفحة
#     def __str__(self):
#         return str(self.HOU_User) 
#     # 
#     # 'Z-A' ترتيب تنازلي
#     class Meta:
#         ordering = ['HOU_User'] 
# # #
# # #
#     # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
#     # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها 
#     # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها 
#     # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
#     # user:
#     # ['instance']: هي البيانات التي تسم إستقبالها
#     # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ 
#     def create_housing_data(sender, **kwargs):
#         if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
#             HousingData_MODEL.objects.create(HOU_Customer=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف 
#     # "" "user"والمستخدم  "post_save" الربط بين الفانكشن 
#     post_save.connect(create_housing_data , sender=User)
# 
# 
# 
    # #
    # #  في حالة عدم قيام المستخدم بذلك"slug" فاكشن تقوم بتعبئة حقل 
    # # هذه الفانكش ممكن نربطها إي مودل/جدول نريده
    # # self , *args , **kwargs):بارمترات تقوم بإستقبال البيانات المرسلة من سجل المستخدم
    # #  slugify(self.user.username:
    # def save(self , *args , **kwargs):
    #     if not self.slug: # نفذ الكود أدناه "slug"في حالة عدم إستقبال بيانات من قبل المستخدم لحقل 
    #         self.slug = slugify(self.user.username) # "slug" ضع إسم المستخدم في الحقل 
    #     super(Profile , self).save(*args , **kwargs)

    # class Meta:
    #     verbose_name = ("Profile")
    #     verbose_name_plural = ("Profile")
    # #
    # #  "admin" في صفحة "user"تقوم بإظهار  اسم  
    # def __str__(self): 
    #     return '%s' %(self.user.username) #  يمكن ان تضع اي حقل  من حقول  الجدول ترغب فيه ان اردت "admin"  الذي سوف يظهر في صفحة  "user"  هذا هو إسم المستخدم 

    # # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها 
    # # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها 
    # # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # # user:
    # # ['instance']: هي البيانات التي تسم إستقبالها
    # # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ 
    # def create_profile(sender, **kwargs):
    #      if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
    #          Profile.objects.create(user=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "profile" قم بإنشاء ملف 

    # # "" "user"والمستخدم  "post_save" الربط بين الفانكشن 
    # post_save.connect(create_profile , sender=User)
#
#
#
    # # متغير لحفظ رموز طريقة الدقع'
    # CASH     = 'CA'
    # CHECK    = 'CH'
    # TRANSFER = 'TR'
    # # قائمة بطريقة الدفع/الاستلام 
    # METHOD_PAYMENT_CHOICES = [
    #     (CASH,     'Cash'),
    #     (CHECK,    'Check'),
    #     (TRANSFER, 'Transfer'),
    # ]

# Comprehensive Record
class  DatesReceivingMoneyPaymentsMODEL(models.Model):
    # Variable To Save The Number Of Months
    CHOOSE_MONTH_NUMBER = '00'
    JAN                 = '01'
    FEB                 = '02'
    MAR                 = '03'
    APR                 = '04'
    MAY                 = '05'
    JUN                 = '06'
    JUL                 = '07'
    AUG                 = '08'
    SEP                 = '09'
    OCT                 = '10'
    NOV                 = '11'
    DEC                 = '12'

    # The Number Of Months 
    MONTH_NUMBER = [
    (CHOOSE_MONTH_NUMBER ,  'Choose The Month Number'),
    (JAN                 ,                       '01'),
    (FEB                 ,                       '02'),
    (MAR                 ,                       '03'),
    (APR                 ,                       '04'),
    (MAY                 ,                       '05'),
    (JUN                 ,                       '06'),
    (JUL                 ,                       '07'),
    (AUG                 ,                       '08'),
    (SEP                 ,                       '09'),
    (OCT                 ,                       '10'),
    (NOV                 ,                       '11'),
    (DEC                 ,                       '12'),
    ]
    # 
    #
    # Variable To Save The Month Code
    # The Data Will be Saved in the Database 
    JANUARY             = '01-January__Jumada Al-Awwal-(05)'
    FEBRUARY            = '02-February_Jumada Al-Thani-(06)'
    MARCH               = '03-March______________Rajab-(07)'
    APRIL               = '04-April_____________Shaban-(08)'
    MAY                 = '05-May______________Ramadan-(09)'
    JUNE                = '06-June_____________Shawwal-(10)'
    JULY                = '07-July__________Dhul-Qadah-(11)'
    AUGUST              = '08-August_______Dhul-Hijjah-(12)'
    SEPTEMBER           = '09-September_______Muharram-(01)'
    OCTOBER             = '10-October____________Safar-(02)'
    NOVEMBER            = '11-November___Rabi Al-Awwal-(03)'
    DECEMBER            = '12-December___Rabi Al-Thani-(04)'
    All                 = '00-All_______________Al-Kol-(00)'

    
    # List Of The Names Of The Months
    # This Data Will Be shown In the Menu
    MONTH_NAME = [
    (JANUARY            ,  '01-January__Jumada Al-Awwal-(05)')  ,
    (FEBRUARY           ,  '02-February_Jumada Al-Thani-(06)')  ,
    (MARCH              ,  '03-March______________Rajab-(07)')  ,
    (APRIL              ,  '04-April_____________Shaban-(08)')  ,
    (MAY                ,  '05-May______________Ramadan-(09)')  ,
    (JUNE               ,  '06-June_____________Shawwal-(10)')  ,
    (JULY               ,  '07-July__________Dhul-Qadah-(11)')  ,
    (AUGUST             ,  '08-August_______Dhul-Hijjah-(12)')  ,
    (SEPTEMBER          ,  '09-September_______Muharram-(01)')  ,
    (OCTOBER            ,  '10-October____________Safar-(02)')  ,
    (NOVEMBER           ,  '11-November___Rabi Al-Awwal-(03)')  ,
    (DECEMBER           ,  '12-December___Rabi Al-Thani-(04)')  ,
    (All                ,  '00-All_______________Al-Kol-(00)')  ,
    ]
    # 
    DRP_User                             = models.ForeignKey(User         , on_delete=models.CASCADE                                                       , verbose_name="اسم المشترك")
    DRP_DateReceivigMoneyPayments_Long   = models.CharField(max_length=50                                     , db_index=True , blank=False  , null=False  , verbose_name="موعد إستلام المال - بالشهر"     , choices=MONTH_NAME , default='Please Choose ' , help_text='Required Field')    
    DRP_DateReceivigMoneyPayments_Short  = models.DateField(                                                    db_index=True , blank=True   , null=True   , verbose_name="موعد إستلام المال - بالتاريخ"                                                                , help_text='Required Field')
    DRP_Notes                            = models.CharField(max_length=100                                     , db_index=True , blank=True   , null=True   , verbose_name="الملاحظات")    
    
    # 
    # Display The Name Of This Field In The Admin Page
    def __str__(self):
        return str(self.DRP_DateReceivigMoneyPayments_Long)
    # 
    # Arrange The Fields In Ascending Order 'Z-A'
    class Meta:
        ordering = ['DRP_DateReceivigMoneyPayments_Long'] 
#
#
#
#
#
#
# class Monthes_Menu_MODEL(models.Model):
#     MM_MonthName = models.CharField(unique=True  , max_length=50)
#     #
#     # Display The Name Of This Field In The Admin Page
#     def __str__(self):
#             return self.MM_MonthName
#     #
#     # Arrange The Fields In Ascending Order 'Z-A'
#     class Meta:
#         ordering = ['MM_MonthName'] 



# # Create your models here.
# class main_menu(models.Model):
#     m_menu_id = models.AutoField(primary_key=True)
#     m_menu_name = models.CharField(max_length=50)
#     m_menu_link = models.CharField(max_length=100)


# class sub_menu(models.Model):
#     s_menu_id = models.AutoField(primary_key=True)
#     m_menu_id = models.IntegerField()
#     s_menu_name = models.CharField(max_length=50)
#     s_menu_link = models.CharField(max_length=100)