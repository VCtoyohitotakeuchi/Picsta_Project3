from django.shortcuts import render
#django.views.genericからTemplateView、ListViewをインポート
from django.views.generic import TemplateView, ListView
#django.views.genericからCreateViewをインポート
from django.views.generic import CreateView,View
#django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
#formsモジュールからPhotoPostFormをインポート
from .forms import PhotoPostForm,subPostForm
#method_decoratorをインポート
from django.utils.decorators import method_decorator
#login_requiredをインポート
from django.contrib.auth.decorators import login_required
#modelsモジュールからモデルPhotoPostをインポート
from .models import PhotoPost,subPost
#django.views.genericからDetailViewをインポート
from django.views.generic import DetailView
#django.views.genericからDeleteViewをインポート
from django.views.generic import DeleteView
from django.db.models import F
from django.urls import path

class IndexView(ListView):
    '''トップページのビュー'''
    #index.htmlをレンダリングする
    template_name = 'index.html'
    #モデルBlogPostのオブジェクトにorder_by()を適用して
    #投稿日時の降順で並び替える
    queryset = PhotoPost.objects.order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 9

#デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
#ログイン状態でなければsettings.pyのLOGUN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    '''写真投稿ページのビュー

    PhotoPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する

    Attributes:
     from_class: モデルとフィールドが登録されたフォームクラス
     template_name: レンタリングするテンプレート
     success_url: データベースへの登録完了後のリダイレクト先
   '''
    #form.pyPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    #レンタリングするテンプレート
    template_name = "post_photo.html"
    #フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーランド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う

        parameters:
          form(django.forms.Form):
            form_classに格納されているPhotoPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトされる
        '''
        #commit= FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        #投稿ユーザのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        #投稿データをデータベースに登録
        postdata.save()
        #戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
        
    Attributes:
        template_name: レタリングするテンプレート
    '''
    #index.htmlをレンダリングする
    template_name = 'post_success.html'

class CategoryView(ListView):
    '''カテゴリページのビュー

    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    #index.htmlをレンダリングする
    template_name = 'index.html'
    #1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        '''クエリを実行する

        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する

        Returns:
            クエリによって取得されたレコード
        '''
        #self.kwargsでキーワードの辞書を取得し、
        #categoryキーの値(Categorysテーブルのid)取得
        category_id = self.kwargs['category']
        #filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        #クエリによって取得されたレコードを返す
        return categories
    
class UserView(ListView):
    '''ユーザーの投稿一覧のビュー'''
    #index.htmlをレンダリングする
    template_name ='index.html'
    #1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):


        #userキーの値（ユーザーテーブルのid）を取得
        user_id = self.kwargs['user']
        #filter(フィールド名=id)で絞り込む
        user_list = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        #クエリによって取得されたレコードを返す
        return user_list
    
class CommentView(ListView):
    '''ユーザーの投稿一覧のビュー'''
    # レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "object_list"
    #post.htmlをレンダリングする
    template_name = 'subposts_list.html'
    #クラス変数modelにモデルBlogPostを設定
    model = subPost

"""     def get_queryset(self):

        #userキーの値（ユーザーテーブルのid）を取得
        superpost_id = self.kwargs['pk']
        #filter(フィールド名=id)で絞り込む
        #filter(superpost=superpost_id)
        comment_list = subPost.objects.filter(superpost=superpost_id).order_by('-posted_at')
        #クエリによって取得されたレコードを返す
        return comment_list """

class DetailView(View):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承する
    Attributes:
     template_name: レンダリングするテンプレート
     model: モデルのクラス
    '''
    def get(self, request, *args, **kwargs):
        detail = PhotoPost.objects.get(pk=self.kwargs['pk'])
        subpost = subPost.objects.filter(superpost = detail.pk).order_by('-posted_at')

        context = { 
            "detail": detail,
            "subpost": subpost,
        }
        return render(request, "detail.html", context)
    

    """ #post.htmlをレンダリングする
    template_name = 'detail.html'
    #クラス変数modelにモデルBlogPostを設定
    model = PhotoPost """
    """ def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object_list'] = subPost.objects.filter(superpost = self.kwargs["pk"])
     """
    


#UserView, DetailViewの後に以下のコードを追加する
class MypageView(ListView):
    '''マイページのビュー

    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    #mypage.htmlをレンダリングする
    template_name = 'mypage.html'
    #1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        '''クエリを実行する

        self.kwargsの取得が必要なため、クラス変数uerysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する

        Returns:
            クエリによって取得されたレコード
        '''
        #現在ログインしているユーザー名はHttpRequest.userに格納されている
        #filter(userフィールド=userオブジェクト)で絞り込む
        queryset = PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        #クエリによって取得されたレコードを返す
        return queryset
        


class PhotoDeleteView(DeleteView):
    '''レコードの削除を行うレビュー
    
    Attributes:
        model:モデル
        template_name:レンダリングするテンプレート
        paginate_by:1ページに表示するレコードの件数
        success_url: 削除完了後のリダイレクト先のURL
    '''
    #操作の対象はPhotoPost
    model = PhotoPost
    #Photo_delete.htmlをレンダリングする
    template_name = 'photo_delete.html'
    #処理完了後にマイページにリダイレクト
    success_url = reverse_lazy('photo:mypage')

    def delete(self, request, *args, **kwargs):
        '''レコードの削除を行う
        
        Parameters:
            self: PhotoDeleteViewオブジェクト
            request: WSGIRequest(HttpRequest)オブジェクト
            args: 引数として渡される辞書(dict)
            kwargs: キーワード付きの辞書(dict)
            {'pk':21}のようにレコードのidが渡される
        
        Returns
            HttpResponseRedirect(success_url)を返して
            sucsess_urlにダイレクト
            '''
        #スーパークラスのdelete()を実行
        return super().delete(request, *args, **kwargs)
    '''
    def get_queryset(self):


        #userキーの値（ユーザーテーブルのid）を取得
        user_id = self.kwargs['user']
        #filter(フィールド名=id)で絞り込む
        user_list = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        #クエリによって取得されたレコードを返す
        return user_list
    '''

@method_decorator(login_required, name='dispatch')
class subPostView(CreateView):
    #form.pyPhotoPostFormをフォームクラスとして登録
    form_class = subPostForm
    #レンタリングするテンプレート
    template_name = "subpost_photo.html"
    #フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:subpost_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーランド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う

        parameters:
          form(django.forms.Form):
            form_classに格納されているPhotoPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトされる
        '''
        #commit= FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        #投稿ユーザのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        postdata.superpost=self.kwargs["pk"]
        #投稿データをデータベースに登録
        postdata.save()
        PhotoPost.objects.filter(pk=self.kwargs["pk"]).update(commentcount=F('commentcount')+1)
        #戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
    
        

class subPostSuccessView(TemplateView):
    '''投稿完了ページのビュー
        
    Attributes:
        template_name: レタリングするテンプレート
    '''
    #index.htmlをレンダリングする
    template_name = 'subpost_success.html'