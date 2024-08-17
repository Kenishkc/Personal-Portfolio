from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from .models import CoverPage,UserProfile ,Expertise ,Education

def index(request):
    cover=CoverPage.objects.first()
    userprofile =UserProfile.objects.first()
    expertise_list = Expertise.objects.all()[:3]
    # Get the URL of the background image
    image_url = cover.background_image.url if cover and cover.background_image else ''
    
     # Retrieve all Education instances
    education_list = Education.objects.all()



    return render(request,'index.html', {'info': cover , 'image_url': image_url ,
                                         'user':userprofile , 'expertise_list': expertise_list,
                                         'education_list': education_list
                                         })

def download_cv(request, user_id):
    user_profile = get_object_or_404(UserProfile, id=user_id)
    if user_profile.upload_cv:
        response = HttpResponse(user_profile.upload_cv, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{user_profile.upload_cv.name}"'
        return response
    raise Http404("CV not found.")
