from django.db import models


class CoverPage(models.Model):
    background_image = models.ImageField(upload_to='cover_images/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    position = models.CharField(max_length=200)  # or use TextField if needed

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True, help_text="Upload a profile picture.")
    description = models.TextField(help_text="A brief description, max 150 words.")
    date_of_birth = models.DateField(help_text="Date of birth in YYYY-MM-DD format.")
    phone_number = models.CharField(max_length=15, help_text="Contact phone number.")
    email = models.EmailField(unique=True, help_text="Email address.")
    address = models.CharField(max_length=70 ,help_text="Residential address.")
    upload_cv = models.FileField(upload_to='cvs/', help_text="Upload your CV in PDF or DOC format.")
    

    def __str__(self):
        return f"{self.email} - {self.phone_number}"
    
class Expertise(models.Model):
    start_date = models.DateField(help_text="The start date of the expertise.")
    end_date = models.DateField(null=True, blank=True,help_text="The end date of the expertise.")
    position = models.CharField(max_length=200, help_text="The position held during the expertise.")
    short_description = models.TextField(help_text="A brief description of the expertise.", max_length=500)
    tools_and_technology = models.CharField(max_length=500, help_text="Tools and technologies used during the expertise.")

    def __str__(self):
        return f"{self.position} from {self.start_date} to {self.end_date}"
    
class Education(models.Model):
    start_date = models.DateField(help_text="The start date of the education.")
    end_date = models.DateField(null=True, blank=True, help_text="The end date of the education (optional).")
    title = models.CharField(max_length=200, help_text="The title of the education, e.g., Master, Bachelor of Information Technology.")
    short_description = models.TextField(help_text="A brief description of the education.", max_length=500)

    def __str__(self):
        return f"{self.title} from {self.start_date} to {self.end_date if self.end_date else 'Present'}"           
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(help_text="Proficiency as a percentage (0-100)")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(help_text="Proficiency as a percentage (0-100)")

    def __str__(self):
        return self.name    