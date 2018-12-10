from django.forms import ModelForm
from django import forms
from .models import Comment

#Create the form class

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','content']
        widgets = {
            # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
            # 例如 user_name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入昵称",
                'aria-describedby': "sizing-addon1",
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入邮箱",
                'aria-describedby': "sizing-addon1",
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '我来评两句~',
            }),
        }

