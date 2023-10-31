# from collections.abc import Mapping
# from typing import Any
from django import forms
# from .models import GoodOne


# from django.forms.utils import ErrorList

class AddImageToGoodForm (forms.Form):
    image = forms.ImageField()
    