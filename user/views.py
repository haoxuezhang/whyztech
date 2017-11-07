from django.shortcuts import render
from .models import Products, ProductMainCate, ProductSecondCate, ApplicationCate, Brands, News
from django.views.generic import DetailView, ListView
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    # applicationCate_list = Important.objects.all().order_by('-pub_date')[:4]
    # solution_list = Solutions.objects.all().order_by('-pub_date')[:4]
    # product_list = Products.objects.all().order_by('-pub_date')[:8]
    # news_list = News.objects.all().order_by('-pub_date')[:2]
    # example_list = Example.objects.all().order_by('-pub_date')

    applicationCate_list = ApplicationCate.objects.all()
    productMainCate_list = ProductMainCate.objects.all()
    brand_list = Brands.objects.all()
    # newsCate_list = NewsCate.objects.all()

    context = {'productMainCate_list': productMainCate_list,
               'applicationCate_list': applicationCate_list,
               'brand_list': brand_list,
               }
    return render(request, 'index.htm', context)


# def solutionsList(request, category_id):
#     article_list = Solutions.objects.filter(solutionCate_id=category_id).order_by('-pub_date')
#     solutionCate_list = SolutionCate.objects.all()
#     productCate_list = ProductCate.objects.all()
#     newsCate_list = NewsCate.objects.all()
#
#     try:
#         page = request.GET.get('page', 1)
#     except PageNotAnInteger:
#         page = 1
#
#     p = Paginator(article_list, 4, request=request)
#     articles = p.page(page)
#
#     context = {'article_list': articles,
#                'solutionCate_list': solutionCate_list,
#                'productCate_list': productCate_list,
#                'newsCate_list': newsCate_list,
#                }
#     return render(request, 'solutions.html', context)
#
#
# class SolutionDetail(DetailView):
#     # Django有基于类的视图DetailView,用于显示一个对象的详情页，我们继承它
#     model = Solutions
#     template_name = "solutions-inform.html"
#     context_object_name = "article"
#
#     pk_url_kwarg = 'article_id'
#
#     def get_object(self):
#         obj = super(SolutionDetail, self).get_object()
#         return obj
#
#     def get_context_data(self, **kwargs):
#         kwargs['solutionCate_list'] = SolutionCate.objects.all()
#         kwargs['productCate_list'] = ProductCate.objects.all()
#         kwargs['newsCate_list'] = NewsCate.objects.all()
#         return super(SolutionDetail, self).get_context_data(**kwargs)


def productSecondCateList(request, category_id):
    productSecondCate_list = ProductSecondCate.objects.filter(productMainCate_id=category_id)
    productMainCate_list = ProductMainCate.objects.all()
    # solutionCate_list = SolutionCate.objects.all()
    productMainCate_list = ProductMainCate.objects.all()
    selectProductMainCate = ProductMainCate.objects.get(id=category_id)
    # newsCate_list = NewsCate.objects.all()

    # try:
    #     page = request.GET.get('page', 1)
    # except PageNotAnInteger:
    #     page = 1
    #
    # p = Paginator(productSecondCate_list, 8, request=request)
    # articles = p.page(page)

    context = {'productSecondCate_list': productSecondCate_list,
               'productMainCate_list': productMainCate_list,
               'category_id': category_id,
               'selectProductMainCate': selectProductMainCate,
               }
    return render(request, 'productCategory.htm', context)


def productList(request, category_id, secondCate_id):
    productSecondCate_list = ProductSecondCate.objects.filter(productMainCate_id=category_id)
    productMainCate_list = ProductMainCate.objects.all()

    selectProductMainCate = ProductMainCate.objects.get(id=category_id)
    selectProductSecondCate = ProductSecondCate.objects.get(id=secondCate_id)
    product_list = Products.objects.filter(productSecondCate_id=secondCate_id)

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
               'product_list': articles
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
        # kwargs['solutionCate_list'] = SolutionCate.objects.all()
        # kwargs['productCate_list'] = ProductCate.objects.all()
        # kwargs['newsCate_list'] = NewsCate.objects.all()
        return super(ProductDetail, self).get_context_data(**kwargs)


class ApplicationDetail(DetailView):
    model = ApplicationCate
    template_name = "application.htm"
    context_object_name = "application"

    pk_url_kwarg = 'application_id'

    def get_object(self):
        obj = super(ApplicationDetail, self).get_object()
        return obj

    def get_context_data(self, **kwargs):
        # kwargs['solutionCate_list'] = SolutionCate.objects.all()
        # kwargs['productCate_list'] = ProductCate.objects.all()
        # kwargs['newsCate_list'] = NewsCate.objects.all()
        return super(ApplicationDetail, self).get_context_data(**kwargs)


def NewsList(request):
    news_list = News.objects.all().order_by('-pub_date')

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
               # 'hot_news_list': hot_news_list,
               # 'solutionCate_list': solutionCate_list,
               # 'productCate_list': productCate_list,
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
        # kwargs['solutionCate_list'] = SolutionCate.objects.all()
        # kwargs['productCate_list'] = ProductCate.objects.all()
        # kwargs['newsCate_list'] = NewsCate.objects.all()
        return super(NewsDetail, self).get_context_data(**kwargs)

#
# def exampleList(request):
#     article_list = Example.objects.all().order_by('-pub_date')
#
#     solutionCate_list = SolutionCate.objects.all()
#     productCate_list = ProductCate.objects.all()
#     newsCate_list = NewsCate.objects.all()
#
#     try:
#         page = request.GET.get('page', 1)
#     except PageNotAnInteger:
#         page = 1
#
#     p = Paginator(article_list, 3, request=request)
#     articles = p.page(page)
#
#     context = {'article_list': articles,
#                'solutionCate_list': solutionCate_list,
#                'productCate_list': productCate_list,
#                'newsCate_list': newsCate_list,
#                }
#     return render(request, 'examples.html', context)
#
#
# class ExampleDetail(DetailView):
#     model = Example
#     template_name = "examples-inform.html"
#     context_object_name = "article"
#
#     pk_url_kwarg = 'article_id'
#
#     def get_object(self):
#         obj = super(ExampleDetail, self).get_object()
#         return obj
#
#     def get_context_data(self, **kwargs):
#         kwargs['solutionCate_list'] = SolutionCate.objects.all()
#         kwargs['productCate_list'] = ProductCate.objects.all()
#         kwargs['newsCate_list'] = NewsCate.objects.all()
#         return super(ExampleDetail, self).get_context_data(**kwargs)
#
#
# def aboutus(request):
#     aboutus_list = Aboutus.objects.all().order_by('-pub_date')
#
#     solutionCate_list = SolutionCate.objects.all()
#     productCate_list = ProductCate.objects.all()
#     newsCate_list = NewsCate.objects.all()
#     try:
#         aboutus = aboutus_list[0]
#     except:
#         return
#     context = {'aboutus': aboutus,
#                'solutionCate_list': solutionCate_list,
#                'productCate_list': productCate_list,
#                'newsCate_list': newsCate_list,
#
#                }
#     return render(request, 'about-us.html', context)
