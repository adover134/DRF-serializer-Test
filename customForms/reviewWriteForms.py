from django import forms
from customForms import customFields


#리뷰 작성 시 사용될 폼입니다.
class ReviewWriteForm(forms.Form):
    title = forms.CharField(widget=customFields.NonStickyTextInputField())
    address = forms.CharField(widget=customFields.NonStickyTextInputField())
    images = forms.ImageField(label='room_images', widget=customFields.NonStickyImageField(attrs={'multiple': True, 'autocomplete': 'off'}), required=False)


class TextReviewWriteForm(ReviewWriteForm):
    review_sentence = forms.CharField(widget=customFields.NonStickyTextarea(attrs={'rows': 5, 'cols': 20, 'style': 'resize:none;', 'autocomplete': 'off'}))
    review_type = forms.CharField(label=False, initial='text', widget=forms.TextInput(attrs={'style': 'display:none;', 'autocomplete': 'off'}))

    field_order = ['title', 'address', 'review_sentence', 'images']


class ImageReviewWriteForm(ReviewWriteForm):
    icon_info = forms.CharField(widget=customFields.NonStickyTextarea(attrs={'rows': 5, 'cols': 20, 'style': 'resize:none;'}))
    review_type = forms.CharField(label=False, initial='image', widget=forms.TextInput(attrs={'style': 'display:none;', 'autocomplete': 'off'}))

    field_order = ['title', 'address', 'icon_info', 'images']


class UserInfoForm(forms.Form):
    user_nickname = forms.CharField()
    user_email = forms.EmailField()
    user_warn_count = forms.IntegerField(required=False, disabled=True)
