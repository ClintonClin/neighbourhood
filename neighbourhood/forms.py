from django import forms
from .models import Notifications, Business, Profile, BlogPost, Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']


class notificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        exclude = ['author', 'neighbourhood', 'post_date']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['username', 'neighbourhood', 'avatar']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'post']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'neighbourhood']


