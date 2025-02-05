from django.views import generic
from django.urls import reverse
from django.shortcuts import render
from myapp.models import Movie, Director, Log
from myapp.form import DirectorForm, MovieForm, LogForm

class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'movie_list' #集めたデータの名前を'movie_list'にする 
    queryset = Movie.objects.all()     #model = Movieではだめなのか？ーMovie.objects.all() ではなく Movie.objects.filter(条件) などを使って、表示するデータを制限したい場合があるため。
    #属性(＝attribute)

class MovieDetailView(generic.DetailView):
    model = Movie                       #表示するデータはmodelのMovieから持ってきなさい
    template_name = 'myapp/detail.html' #ではだめなのか？ーURL パターンの pk（または slug）に基づいて、自動的に適切な querysetを作成してくれるから、
    #Movie.objects.get(pk=3)など
    
class RegisterDirectorView(generic.CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:registermovie')#reverse関数とは()に書かれたアドレスへ飛んでいけという意味。


class RegisterMovieView(generic.CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'myapp/register.html'
    def get_success_url(self): #データの入力も、データベースへの格納も上手くいったら、どこのページを表示するか
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.pk }) 

class WritingLogView(generic.CreateView):
    model = Log
    form_class = LogForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.movie.pk }) 
    
class EditMovieView(generic.DetailView):
    model = Movie                       
    template_name = 'myapp/editmovie.html' 
    

class UpdateLogView(generic.UpdateView):
    model = Log
    form_class = LogForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:index',)
    
#削除画面無しで一覧画面にリダイレクトもできるけど汎用クラスビューでやるならオーバーライド？しないといけない
class DeleteMovieView(generic.DeleteView):
    model = Movie
    template_name = "myapp/deletemovie.html"
    def get_success_url(self):
        return reverse('myapp:index',)
    
def unavailable_page(request):
    return render(request, 'myapp/unavailable.html')