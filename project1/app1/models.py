from django.db import models
from django.utils import timezone


# 景點位置
class Location(models.Model):
    name = models.CharField(max_length=255)  #位置名稱
    phone_number = models.CharField(max_length = 20,default='') # 當地電話號碼
    address = models.CharField(max_length = 100,default='') # 地址
    # 覆寫 __str__
    def __str__(self):
        return self.name

#景點貼文
class Post(models.Model):
    subject = models.CharField(max_length=255)  #標題
    content = models.CharField(max_length=255)  #內容
    image = models.ImageField(upload_to='photos',blank=True)  #圖片 圖片會存在 project1/photos 會自動建photos資料夾
    author = models.CharField(max_length=20)  #貼文者
    create_date = models.DateField(default=timezone.now)  #貼文時間
    location = models.ForeignKey(Location, on_delete=models.CASCADE,blank=True) #景點位置，on_delete=models.CASCADE 如果Location被刪除 那ForeignKey也跟著刪除
    def __str__(self):
        return self.subject
    def image_url(self):
        if self.image and hasattr(self.image, 'url'): #回傳image的路徑
            return self.image.url

