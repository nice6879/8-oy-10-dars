from django import forms
from .models import Banner, FooterBottom, FooterBottomImg

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['title', 'sub_title', 'img', 'is_active']
        
        
class FooterBottomForm(forms.ModelForm):
    class Meta:
        model = FooterBottom
        fields = ['call_center', 'location', 'title', 'facebook_link', 'twitter_link', 'linkedin_link']

class FooterBottomImgForm(forms.ModelForm):
    class Meta:
        model = FooterBottomImg
        fields = ['img']
