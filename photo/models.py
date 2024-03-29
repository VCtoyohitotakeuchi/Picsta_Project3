from django.db import models
# Create your models here.
#accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    '''投稿する写真のカテゴリを管理するモデル
    '''
    #カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ', #フィールドのタイトル
        max_length=20)

    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        '''
        return self.title

class PhotoPost(models.Model):
    '''投稿されたデータを管理するモデル
    '''

    #CustomUserモデル(のuser_id)とPhotoPostモデルを
    #1対多の関係で結びつける
    #CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        #ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    #Categoryモデル（のtitle）とPhotoPostモデルを
    #1対多の関係で結び付ける
    #Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(
        Category,
        #フィールドのタイトル
        verbose_name='カテゴリ',
        #カテゴリに関連付けられた投稿データが存在する場合は
        #そのカテゴリを削除できないようにする
        on_delete=models.PROTECT,
        default=1,
        )
    #タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル', #フィールドのタイトル
        max_length=50, #最大文字数は50文字
        blank=True, #フィールド値の設定は必須ではない
        null=True #データベースにnullが保存されることを許容
        )
    #コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント', #フィールドのタイトル
        max_length=200, #最大文字数は200文字
        blank=True, #フィールド値の設定は必須ではない
        null=True #データベースにnullが保存されることを許容
        )
    #イメージのフィールド１
    image1 = models.ImageField(
        verbose_name='イメージ１', #フィールドのタイトル
        upload_to = 'photos' #MEDIA_ROOT以下のphotosにファイルを保存
        )
    #イメージのフィード２
    image2 = models.ImageField(
        verbose_name='イメージ２', #フィールドのタイトル
        upload_to = 'photos', #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True, #フィールド値の設定は必須ではない
        null=True #データベースにnullが保存されることを許容
        )
    image3 = models.ImageField(
        verbose_name='イメージ３', #フィールドのタイトル
        upload_to = 'photos', #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True, #フィールド値の設定は必須ではない
        null=True, #データベースにnullが保存されることを許容
        #default = None
        )
    image4 = models.ImageField(
        verbose_name='イメージ４', #フィールドのタイトル
        upload_to = 'photos', #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True, #フィールド値の設定は必須ではない
        null=True, #データベースにnullが保存されることを許容
        #default = None
        )
    mov1 = models.FileField(
        verbose_name='ビデオ1', #フィールドのタイトル
        upload_to = 'photos', #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True, #フィールド値の設定は必須ではない
        null=True #データベースにnullが保存されることを許容
        )
    favorite =models.IntegerField(
        default=0
    )
    commentcount =models.IntegerField(
        default=0
    )
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', #フィールドのタイトル
        auto_now_add=True #日時を自動追加
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        Returns(str):投稿記事のタイトル
        '''
        return self.title

class subPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        #ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE,
        default=1
        )
    superpost =models.IntegerField(
        default=0
    )
    #コメント用のフィールド
    comment = models.TextField(
        verbose_name='本文', #フィールドのタイトル
        max_length=200, #最大文字数は200文字
        )
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', #フィールドのタイトル
        auto_now_add=True, #日時を自動追加
        )
    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        Returns(str):投稿記事のコメント
        '''
        return self.comment