try:
    from django.conf.urls import url
    from django.conf.urls.static import static
    from django.conf import settings
    from django.urls import path
except ImportError:
    from django.urls import re_path as url


from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake, UserFormView, QuizList, \
    QuestionList, CategoryList, ProgressList, MarkingList, SubCategoryList


urlpatterns = [   
     
    path('list/', view=QuizList.as_view(), name='quiz_list_index'),

    path('',view=QuizListView.as_view(), name='quiz_index'),

    path('progress/list/', view=ProgressList.as_view(), name='quiz_progress'),

    path('marking/list/', view=MarkingList.as_view(), name='quiz_marking_list'),

    path('category/list/', view=CategoryList.as_view(), name='category_list'),

    path('category/<str:category_name>/list/', view=SubCategoryList.as_view(), name='category_list'),

    path('<slug:quiz_name>/list/', view=QuestionList.as_view(), name='question_list'),

    path('category/', view=CategoriesListView.as_view(), name='quiz_category_list_all'),
    
    path('category/<str:category_name>/', view=ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),

    path('progress/', view=QuizUserProgressView.as_view(), name='quiz_progress'),

    path('marking/', view=QuizMarkingList.as_view(), name='quiz_marking'),

    path('marking/<int:pk>/', view=QuizMarkingDetail.as_view(), name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    path('<slug>/', view=QuizDetailView.as_view(), name='quiz_start_page'),

    path('<slug:quiz_name>/take/', view=QuizTake.as_view(), name='quiz_question'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)