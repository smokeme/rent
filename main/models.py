from django.db import models
from django.utils import timezone  
from django.utils.http import urlquote  
from django.core.mail import send_mail  
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):  
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)
        
class CustomUser(AbstractBaseUser, PermissionsMixin):  
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    # fav_artists = models.ManyToManyField('main.Artist', null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
    	return self.email

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Gov(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return '%s' % self.name

class Area(models.Model):
	name = models.CharField(max_length=255)
	gov = models.ForeignKey('main.Gov')

	def __unicode__(self):
		return '%s' % self.name

class Apartment(models.Model):
	name = models.CharField(max_length=255)
	rent = models.IntegerField()
	bedrooms = models.IntegerField()
	bathrooms = models.IntegerField()
	livingrooms = models.IntegerField()
	space = models.IntegerField(null=True,blank=True)
	category = models.CharField(max_length=255)
	image = models.ImageField(null=True,blank=True, upload_to='apartment_images')
	description = models.TextField(null=True,blank=True)
	contactemail = models.CharField(max_length=255,null=True,blank=True)
	contactphone = models.IntegerField()
	address = models.TextField()
	floor = models.IntegerField(null=True,blank=True)
	longitude = models.FloatField(null=True,blank=True)
	latitude = models.FloatField(null=True,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	parking = models.IntegerField()
    internet = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    maidroom = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    bills = models.BooleanField(default=False)
	user = models.ForeignKey('main.CustomUser')

	def __unicode__(self):
		return '%s' % self.name