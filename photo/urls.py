from django.urls import path
from . import views

#URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

#URLパターンを登録する変数
urlpatterns = [
    path('start',views.startview.as_view(),name='drop'),

    #photoアプリへのアクセスはviewモジュールのIndexViewを実行
    path('',views.IndexView.as_view(),name='index'),

    #写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),

    #投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    path('subpost_done/',
         views.subPostSuccessView.as_view(),
         name='subpost_done'),
    
    #カテゴリ一覧ページ
    #photos/<Categorysテーブルのid値>にマッチング
    #<int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name = 'photos_cat'
         ),

    #ユーザーの投稿一覧ページ
    #photos/<ユーザーテーブルのid値>にマッチング
    #<int:user>は辞書{user: id値(int)}としてCategoryViewに流される
    path('user-list/<int:user>',
        views.UserView.as_view(),
        name = 'user_list'
        ),

    #p489 8行目
    #詳細ページ
    #photo-detail/<Photo postsテーブルのid値>にマッチング
    #<int:pk>は辞書{pk: id値{int}}としてDetailViewに渡される
    path('photo-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'photo_detail'
        ),
    #コメント機能
    path('photo-detail/<int:pk>/subpost',
         views.subPostView.as_view(),
         name = 'comment'
        ),
    

    #以下、7.9にて追加する
    
    #マイページ
    #mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    #投稿写真の削除
    #photo/<Photo postsテーブルのid値>/delete/にマッチング
    #<int:pk>は辞書{pk: id値(int)}としてDetailviewに渡される
    path('photo/<int:pk>/delete/',
        views.PhotoDeleteView.as_view(),
        name = 'photo_delete'
        ),
]