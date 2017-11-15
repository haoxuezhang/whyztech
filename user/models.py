from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField('呢称', max_length=50, default='好学长')
    gender = models.CharField('性别', default='male', max_length=6, choices=(("male", "男"), ("female", "女")))
    mobile = models.CharField('手机号', max_length=11, null=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class ApplicationCate(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name='分类ID(限英文字母)')
    name = models.CharField(max_length=50, verbose_name='应用领域名称')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='应用领域图片')
    describe = models.TextField(max_length=511, verbose_name='描述')
    context = UEditorField(verbose_name='具体介绍', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/", default='')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '应用领域'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Products(models.Model):
    productSecondCate = models.ForeignKey('ProductSecondCate', verbose_name='产品细化分类')
    title = models.CharField(max_length=255, verbose_name='产品名称')
    describe = models.TextField(max_length=511, verbose_name='产品描述')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='案例图片')
    context = UEditorField(verbose_name='具体介绍', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/", default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = '产品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ProductSecondCate(models.Model):
    productMainCate = models.ForeignKey('ProductMainCate', verbose_name='产品细化分类')
    name = models.CharField(max_length=50, verbose_name='细化分类名称')
    describe = models.TextField(max_length=511, verbose_name='类别介绍')
    logo = models.ImageField(upload_to='img/%Y/%m', verbose_name='分类产品logo')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='产品图片案例')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '产品具体分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProductMainCate(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name='产品分类ID(限英文字母)')
    name = models.CharField(max_length=50, verbose_name='产品分类')
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='类别图片')
    describe = models.TextField(max_length=511, verbose_name='类别介绍')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '产品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Brands(models.Model):
    title = models.CharField(max_length=255, verbose_name='代理品牌')
    describe = models.TextField(max_length=255, verbose_name='品牌描述')
    logo = models.ImageField(upload_to='img/%Y/%m', verbose_name='品牌logo')
    url = models.URLField(verbose_name='代理品牌网页地址')
    # image = models.ImageField(upload_to='img/%Y/%m', verbose_name='案例图片')
    # context = UEditorField(verbose_name='文章内容', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/", default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = '代理品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='新闻标题')
    describe = models.TextField(max_length=255, verbose_name='新闻描述')
    isImportant = models.BooleanField(verbose_name='是否添加为首页大图新闻', default=False)
    picture = models.ImageField(upload_to='img/%Y/%m', verbose_name='首页大图', blank=True)
    image = models.ImageField(upload_to='img/%Y/%m', verbose_name='新闻图例')
    context = UEditorField(verbose_name='新闻内容', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/", default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    click_count = models.IntegerField(default=0, verbose_name='点击数')

    class Meta:
        verbose_name = '新闻动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    context = UEditorField(verbose_name='公司介绍', width=1000, height=500, imagePath="ueditor/", filePath="ueditor/", default='')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




