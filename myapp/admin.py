from django.contrib import admin
from .models import CoverPage ,UserProfile , Expertise ,Education  # Import your model

@admin.register(CoverPage)
class CoverPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'position')  # Customize this as needed
    # Optionally, add more customizations here

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'date_of_birth')  # Customize list display
    search_fields = ('email', 'phone_number')  # Add search functionality
    list_filter = ('date_of_birth',)  # Add filtering by date of birth
    ordering = ('email',)  # Order by email by default
    
@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('position', 'start_date', 'end_date', 'short_description')
    search_fields = ('position', 'short_description')
    list_filter = ('start_date', 'end_date')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'short_description')
    search_fields = ('title', 'short_description')
    list_filter = ('start_date', 'end_date')