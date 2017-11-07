from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='index.htm'), name='index'),
    url(r'^$', views.index, name='index'),
    # url(r'^solutions/(?P<category_id>[a-z]+)/(?P<article_id>\d+)$', views.SolutionDetail.as_view(), name='solution_detail'),
    # url(r'^solutions/(?P<category_id>[a-z]+)/$', views.solutionsList, name='solution_list'),
    url(r'^productMainCate/(?P<category_id>[a-z]+)/(?P<secondCate_id>\d+)/(?P<product_id>\d+)$', views.ProductDetail.as_view(), name='product_detail'),
    url(r'^productMainCate/(?P<category_id>[a-z]+)/$', views.productSecondCateList, name='productMainCate_list'),
    url(r'^productMainCate/(?P<category_id>[a-z]+)/(?P<secondCate_id>\d+)$', views.productList, name='product_list'),
    url(r'^news/(?P<news_id>\d+)$', views.NewsDetail.as_view(), name='news_detail'),
    # url(r'^news/(?P<category_id>[a-z]+)/$', views.newsList, name='news_list'),
    # url(r'^examples/$', views.exampleList, name='example_list'),
    url(r'^application/(?P<application_id>[a-z]+)$', views.ApplicationDetail.as_view(), name='application_detail'),
    url(r'^news/$', views.NewsList, name='news_list')
    # url(r'^aboutus/$', views.AboutUs, name='aboutus'),
]
