from django.db import models
from django.contrib.auth.models import User
#from tinymce.models import HTMLField
import uuid,os
# Create your models here.
#上传图片位置自定
def user_directory_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
	sub_folder = 'file'
	if ext.lower() in ["jpg", "png", "gif"]:
		sub_folder = "avatar"
	if ext.lower() in ["pdf", "docx"]:
		sub_folder = "document"
	return os.path.join(str(instance.user.id), sub_folder, filename)


class Category(models.Model):
    """
    博客分类
    """
    name=models.CharField('名称',max_length=30)
    class Meta:
        verbose_name="类别"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField('名称',max_length=16)

    class Meta:
        verbose_name="标签"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

"""class Image(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    image=models.ImageField(upload_to=user_directory_path, verbose_name="插图",null=True,blank=True)
    class Meta:
        verbose_name="图片"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name"""




class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile',null=True)
    title=models.CharField('标题',max_length=32)
    author=models.CharField('作者',max_length=16)
    content=models.TextField("内容")
    image=models.ImageField(upload_to=user_directory_path, verbose_name="插图",null=True,blank=True)
    pub=models.DateField('发布时间',auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类')#多对一（博客--类别）
    tag=models.ManyToManyField(Tag,verbose_name='标签')#(多对多）
    view=models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name="博客"
        verbose_name_plural=verbose_name


    def __str__(self):
        return self.title
    

    def increase_views(self):
        self.view+=1
        self.save(update_fields=['view'])


class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name='博客')#(博客--评论:一对多)
    name=models.CharField('称呼',max_length=16)
    email=models.EmailField('邮箱')
    content=models.CharField('内容',max_length=240)
    pub=models.DateField('发布时间',auto_now_add=True)

    class Meta:
        verbose_name="评论"
        verbose_name_plural="评论"
    def __str__(self):
        return self.content
