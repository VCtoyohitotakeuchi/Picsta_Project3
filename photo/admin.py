from django.contrib import admin
# Register your models here.
#CustomUserをインポート
from .models import Category, PhotoPost,subPost

class CategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    #レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    #レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class subPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    #レコード一覧にidとtitleを表示
    list_display = ('id', 'comment')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'comment')

#django管理サイトにCategory,CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

#django管理サイトにPhotoPost,PhotoPostAdminを登録する
admin.site.register(PhotoPost, PhotoPostAdmin)

admin.site.register(subPost, subPostAdmin)