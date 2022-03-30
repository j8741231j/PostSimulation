from django.shortcuts import render,redirect
from .models import *
from .forms import UploadModelForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("Errors", form.errors)
		if form.is_valid():
			form.save()
			return redirect('')
		else:
			return render(request, 'registration/register.html', {'form':form})
	else:
		form = UserCreationForm()
		context = {'form': form}
		return render(request, 'registration/register.html', context)

@login_required() #沒登入不能進這一頁
def postarea(request):
    form = UploadModelForm()
    posts = Post.objects.all() #讀取一筆資料
    for post in posts:
        print(type(post.image))
    return render(request, 'postarea.html', locals())

def addpost(request):
    if request.method == "POST":
        myfile = request.FILES['image']
        fs = FileSystemStorage('./media/photos') #defaults to   MEDIA_ROOT  
        filename = fs.save(myfile.name, myfile) #如果圖片名重複，系統會在圖片後加上亂碼，所以檔名這裡在取一次才正確
        #搭配ModelForm的方法(比較不好用)
        # form = UploadModelForm(request.POST,request.FILES)
        # print(form)
        # if form.is_valid():
        #     form.save()
        if Location.objects.filter(name=request.POST["location"]).exists() == False :
            db = Location.objects.create(
                name=request.POST["location"],
                phone_number='',
                address=''
                ) 
            db.save()  #寫入資料庫
        db = Post.objects.create(
            subject=request.POST["subject"],
            content=request.POST["content"],
            image='photos/'+filename,
            author=request.POST["author"],
            location=Location.objects.get(name=request.POST["location"]),
            ) 
        db.save()  #寫入資料庫
        return redirect('/postarea')

