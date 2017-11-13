from django.shortcuts import render
from .models import Products, ProductMainCate, ProductSecondCate, ApplicationCate, Brands, News, AboutUs
from django.views.generic import DetailView, ListView
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
    application_list = ApplicationCate.objects.all()
    productMainCate_list = ProductMainCate.objects.all()
    brand_list = Brands.objects.all()

    if productMainCate_list.count()>0:
        fistProductMainCate = productMainCate_list[0]
    else:
        fistProductMainCate = None
    if application_list.count()>0:
        fistApplication = application_list[0]
    else:
        fistApplication = None

    # try:
    #     fistProductMainCate = productMainCate_list[0]
    # except:
    #     return
    # try:
    #     fistApplication = application_list[0]
    # except:
    #     return
    #前六个分类
    if ProductMainCate.objects.all().count()>6:
        productMainCate_list_1 = productMainCate_list[:6]
        productMainCate_list_2 = productMainCate_list[6:]
    else:
        productMainCate_list_1 = productMainCate_list[:6]
        productMainCate_list_2 = None


    context = {'productMainCate_list': productMainCate_list,
               'application_list': application_list,
               'brand_list': brand_list,
               'important_list': important_list,
               'fistProductMainCate': fistProductMainCate,
               'fistApplication': fistApplication,
               'productMainCate_list_1': productMainCate_list_1,
               'productMainCate_list_2': productMainCate_list_2,
               }
    return render(request, 'index_base.htm', context)


def productSecondCateList(request, category_id):
    important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
    application_list = ApplicationCate.objects.all()

    productSecondCate_list = ProductSecondCate.objects.filter(productMainCate_id=category_id)
    productMainCate_list = ProductMainCate.objects.all()
    selectProductMainCate = ProductMainCate.objects.get(id=category_id)

    if productMainCate_list.count()>0:
        fistProductMainCate = productMainCate_list[0]
    else:
        fistProductMainCate = None
    if application_list.count()>0:
        fistApplication = application_list[0]
    else:
        fistApplication = None

    context = {'productSecondCate_list': productSecondCate_list,
               'productMainCate_list': productMainCate_list,
               'category_id': category_id,
               'selectProductMainCate': selectProductMainCate,
               'important_list': important_list,
               'application_list': application_list,
               'fistProductMainCate': fistProductMainCate,
               'fistApplication': fistApplication,
               }
    return render(request, 'productCategory.htm', context)


def productList(request, category_id, secondCate_id):
    important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
    application_list = ApplicationCate.objects.all()

    productSecondCate_list = ProductSecondCate.objects.filter(productMainCate_id=category_id)
    productMainCate_list = ProductMainCate.objects.all()

    selectProductMainCate = ProductMainCate.objects.get(id=category_id)
    selectProductSecondCate = ProductSecondCate.objects.get(id=secondCate_id)
    product_list = Products.objects.filter(productSecondCate_id=secondCate_id)

    if productMainCate_list.count()>0:
        fistProductMainCate = productMainCate_list[0]
    else:
        fistProductMainCate = None
    if application_list.count()>0:
        fistApplication = application_list[0]
    else:
        fistApplication = None

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(product_list, 4, request=request)
    articles = p.page(page)

    context = {'selectProductMainCate': selectProductMainCate,
               'selectProductSecondCate': selectProductSecondCate,
               'productSecondCate_list': productSecondCate_list,
               'productMainCate_list': productMainCate_list,
               'category_id': category_id,
               'secondCate_id': secondCate_id,
               'product_list': articles,

               'important_list': important_list,
               'application_list': application_list,
               'fistProductMainCate': fistProductMainCate,
               'fistApplication': fistApplication,
               }
    return render(request, 'secondCate.htm', context)




class ProductDetail(DetailView):
    model = Products
    template_name = "productInfo.htm"
    context_object_name = "product"

    pk_url_kwarg = 'product_id'

    def get_object(self):
        obj = super(ProductDetail, self).get_object()
        return obj

    def get_context_data(self, **kwargs):
        important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
        application_list = ApplicationCate.objects.all()
        productMainCate_list = ProductMainCate.objects.all()
        if productMainCate_list.count() > 0:
            fistProductMainCate = productMainCate_list[0]
        else:
            fistProductMainCate = None
        if application_list.count() > 0:
            fistApplication = application_list[0]
        else:
            fistApplication = None
        kwargs['important_list'] = important_list
        kwargs['application_list'] = application_list
        kwargs['productMainCate_list'] = productMainCate_list
        kwargs['fistProductMainCate'] = fistProductMainCate
        kwargs['fistApplication'] = fistApplication

        return super(ProductDetail, self).get_context_data(**kwargs)


class ApplicationDetail(DetailView):
    model = ApplicationCate
    template_name = "application.htm"
    context_object_name = "selectedApplication"

    pk_url_kwarg = 'application_id'

    def get_object(self):
        obj = super(ApplicationDetail, self).get_object()
        return obj

    def get_context_data(self, **kwargs):
        important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
        productMainCate_list = ProductMainCate.objects.all()
        application_list = ApplicationCate.objects.all()
        if productMainCate_list.count() > 0:
            fistProductMainCate = productMainCate_list[0]
        else:
            fistProductMainCate = None
        if application_list.count() > 0:
            fistApplication = application_list[0]
        else:
            fistApplication = None

        kwargs['application_list'] = application_list
        kwargs['important_list'] = important_list
        kwargs['productMainCate_list'] = productMainCate_list
        kwargs['fistProductMainCate'] = fistProductMainCate
        kwargs['fistApplication'] = fistApplication
        return super(ApplicationDetail, self).get_context_data(**kwargs)


def NewsList(request):
    important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
    application_list = ApplicationCate.objects.all()
    productMainCate_list = ProductMainCate.objects.all()

    news_list = News.objects.all().order_by('-pub_date')

    if productMainCate_list.count()>0:
        fistProductMainCate = productMainCate_list[0]
    else:
        fistProductMainCate = None
    if application_list.count()>0:
        fistApplication = application_list[0]
    else:
        fistApplication = None

    # solutionCate_list = SolutionCate.objects.all()
    # productCate_list = ProductCate.objects.all()
    # newsCate_list = NewsCate.objects.all()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(news_list, 6, request=request)
    articles = p.page(page)

    context = {'news_list': articles,
               'important_list': important_list,
               'application_list': application_list,
               'productMainCate_list': productMainCate_list,
               'fistProductMainCate': fistProductMainCate,
               'fistApplication': fistApplication,
               # 'newsCate_list': newsCate_list,
               }
    return render(request, 'newList.htm', context)


class NewsDetail(DetailView):
    model = News
    template_name = "newInfo.htm"
    context_object_name = "news"

    pk_url_kwarg = 'news_id'

    def get_object(self):
        obj = super(NewsDetail, self).get_object()
        obj.click_count = obj.click_count + 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
        application_list = ApplicationCate.objects.all()
        productMainCate_list = ProductMainCate.objects.all()
        if productMainCate_list.count() > 0:
            fistProductMainCate = productMainCate_list[0]
        else:
            fistProductMainCate = None
        if application_list.count() > 0:
            fistApplication = application_list[0]
        else:
            fistApplication = None

        kwargs['important_list'] = important_list
        kwargs['application_list'] = application_list
        kwargs['productMainCate_list'] = productMainCate_list
        kwargs['fistProductMainCate'] = fistProductMainCate
        kwargs['fistApplication'] = fistApplication
        return super(NewsDetail, self).get_context_data(**kwargs)


def BrandsList(request):
    important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
    application_list = ApplicationCate.objects.all()
    productMainCate_list = ProductMainCate.objects.all()

    brands_list = Brands.objects.all().order_by('pub_date')
    if productMainCate_list.count()>0:
        fistProductMainCate = productMainCate_list[0]
    else:
        fistProductMainCate = None
    if application_list.count()>0:
        fistApplication = application_list[0]
    else:
        fistApplication = None
    context = {
        'important_list': important_list,
        'application_list': application_list,
        'productMainCate_list': productMainCate_list,
        'brands_list': brands_list,
        'fistProductMainCate': fistProductMainCate,
        'fistApplication': fistApplication,
    }
    return render(request, 'brands.htm', context)


def Aboutus(request):
    important_list = News.objects.filter(isImportant=True).order_by('-pub_date')[:5]
    application_list = ApplicationCate.objects.all()
    productMainCate_list = ProductMainCate.objects.all()

    aboutus_list = AboutUs.objects.all().order_by('-pub_date')
    if productMainCate_list.count()>0:
        fistProductMainCate = productMainCate_list[0]
    else:
        fistProductMainCate = None
    if application_list.count()>0:
        fistApplication = application_list[0]
    else:
        fistApplication = None

    # solutionCate_list = SolutionCate.objects.all()
    # productCate_list = ProductCate.objects.all()
    # newsCate_list = NewsCate.objects.all()
    if aboutus_list.count()>0:
        aboutus = aboutus_list[0]
    else:
        aboutus = None
    # try:
    #     aboutus = aboutus_list[0]
    # except:
    #     return
    context = {'aboutus': aboutus,
               'important_list': important_list,
               'application_list': application_list,
               'productMainCate_list': productMainCate_list,
               'fistProductMainCate': fistProductMainCate,
               'fistApplication': fistApplication,
               }
    return render(request, 'aboutUs.htm', context)
