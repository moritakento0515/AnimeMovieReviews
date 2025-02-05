from django.db import models
from django.utils import timezone 

class Director(models.Model):
    name =models.CharField(max_length=100, verbose_name="監督") #nameというfieldに文字列で監督名を入れる宣言
    def __str__(self): #以下2行は管理サイト使ってデータ入力したときに監督の名前で表示するための関数
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100,verbose_name="タイトル")
    watch_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE,verbose_name="監督")#directorっていうfieldは「Directorという表」から紐付けして持ってきますよという宣
    def __str__(self):                                                                  #Directorが親
        return self.title 
    
class Log(models.Model): 
    text = models.TextField() #textというfieldにはたくさん文字列を入力するための場所ですよという宣言
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="タイトル", related_name='log')
    def __str__(self):        #movieっていうfieldは「Movieという表」から紐付けして持ってきますよという宣言
        return self.text  
    
