from django.urls import path
#viewsモジュールをインポート
from . import views
#Viewをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_views

#URLパターンを逆引きできるように名前を付ける
app_name = 'accounts'

#URLパターンを登録する変数
urlpatterns = [
    #サインアップページのビューの呼び出し
    #「http://<ホスト名>/signup/」へのアクセスに対して、
    #viewsモジュールのSignUpViewをインスタンス化する
    path('signup/',views.SignUpView.as_view(),name='signup'),
    #サインアップ完了ページのビューの呼び出し
    #「http://<>/signup_success/」へのアクセスに対して、
    #viewsモジュールのSignUpSuccessViewをインスタンス化する
    path('signup_success/',views.SignUpSuccessView.as_view(),name='signup_success'),
    
    #ログインページの表示
    #「http://<ホスト名>/signup/」へのアクセスに対して、
    #django.contrib.auth.LoginViewをインスタンス化して、
    #ログインページを表示
    path('login/',
         #ログイン用のテンプレート（フォーム）をレンダリング
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    #ログアウトを実行
    #「http://<ホスト名>/logout/」へのアクセスに対して、
    #django.contrib.auth.LoginViewをインスタンス化して、
    #ログアウトさせる
    path('logout/',
         #ログイン用のテンプレート（フォーム）をレンダリング
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),
]