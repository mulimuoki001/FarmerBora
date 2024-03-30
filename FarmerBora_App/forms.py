from FarmerBora_App.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    role = forms.CharField(label="Role", max_length=100)
    profile_picture = forms.FileField(
        label="Profile Picture", required=False, widget=forms.FileInput
    )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "profile_picture",
            "password1",
            "password2",
        ]

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get("profile_picture")
        if profile_picture:
            img = Image.open(profile_picture)
            output = BytesIO()
            img = img.resize(
                (50, 80)
            )  # Replace desired_width and desired_height with the desired dimensions
            img.save(output, format="JPEG", quality=100)
            output.seek(0)
            profile_picture = InMemoryUploadedFile(
                output,
                "ImageField",
                "%s.jpg" % profile_picture.name.split(".")[0],
                "image/jpeg",
                sys.getsizeof(output),
                None,
            )
            return profile_picture
        else:
            return profile_picture
