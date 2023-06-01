#UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス
    '''
    class meta:
        '''UserCreationFormのインナークラス
        Attributes:
            model:連携するUserモデル
            fieldes:フォームで使用するフィールド
        '''
        #連携するUserモデルを設定
        model =CustomUser
        #ふぉーむで使用するフィールドを設定
        #ユーザー名、メールアドレス、パスワード、パスワード確認用
        fields = ('username', 'email', 'password1', 'password2')
