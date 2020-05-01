try:
    from django.conf.urls import url
    from django.conf.urls.static import static
    from django.conf import settings
    from django.urls import path
except ImportError:
    from django.urls import re_path as url


from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake, QuizList, \
    QuestionList, CategoryList, ProgressList, MarkingList, SubCategoryList, \
    UserRegistrationFormView, UserLoginFormView, UserLogoutView

# app_name = 'quiz'

urlpatterns = [   
    
    path('register/', UserRegistrationFormView.as_view(), name='register'),

    path('login/', UserLoginFormView.as_view(), name='login'),

    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('list/', QuizList.as_view(), name='quiz_list_index'),

    path('',QuizListView.as_view(), name='quiz_index'),

    path('progress/list/', ProgressList.as_view(), name='quiz_progress'),

    path('marking/list/', MarkingList.as_view(), name='quiz_marking_list'),

    path('category/list/', CategoryList.as_view(), name='category_list'),

    path('category/<str:category_name>/list/', SubCategoryList.as_view(), name='sub_category_list'),

    path('<slug:quiz_name>/list/', QuestionList.as_view(), name='question_list'),

    path('category/', CategoriesListView.as_view(), name='quiz_category_list_all'),
    
    path('category/<str:category_name>/', ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),

    path('progress/', QuizUserProgressView.as_view(), name='quiz_progress'),

    path('marking/', QuizMarkingList.as_view(), name='quiz_marking'),

    path('marking/<int:pk>/', QuizMarkingDetail.as_view(), name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    path('<slug>/', QuizDetailView.as_view(), name='quiz_start_page'),

    path('<slug:quiz_name>/take/', QuizTake.as_view(), name='quiz_question'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)