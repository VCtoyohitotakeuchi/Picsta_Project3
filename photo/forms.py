from django.forms import ModelForm
from .models import PhotoPost,subPost

class PhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス

        Attributes:
         model: モデルのクラス
         friends: フォームで使用するモデルのフィールドを指定
        '''
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2', 'image3', 'image4','mov1']

class subPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス

        Attributes:
         model: モデルのクラス
         friends: フォームで使用するモデルのフィールドを指定
        '''
        model = subPost
        fields = ['comment',]