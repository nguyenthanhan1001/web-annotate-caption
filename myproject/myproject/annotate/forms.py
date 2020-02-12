from django import forms
from .models import Caption

class NewCaption(forms.ModelForm):
    img_id = forms.CharField(
            widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'img_id', 'readonly': True, 'label_tag':'Tên ảnh'}
        ),
        max_length=256,
        # help_text='Tên ảnh'
    )

    worker = forms.CharField(
            widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'Họ và tên Cộng tác viên', 'label_tag':'Tên CTV'}
        ),
        max_length=64,
        # help_text='Tên cộng tác viên'
    )

    caption = forms.CharField(
            widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'Viết câu mô tả tại đây', 'label_tag':'Mô tả'}
        ),
        max_length=2048,
        #help_text=':)'
    )

    class Meta:
        model = Caption
        fields = ['img_id', 'worker', 'caption']
