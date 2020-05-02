===============
Django quiz app
===============

This is a configurable quiz app for Django.

Current features
----------------
* Question order randomisation
* Storing of quiz results under each user
* Previous quiz scores can be viewed on category page
* Correct answers can be shown after each question or all at once at the end
* Logged in users can return to an incomplete quiz to finish it and non-logged in users can complete a quiz if their session persists
* The quiz can be limited to one attempt per user
* Questions can be given a category
* Success rate for each category can be monitored on a progress page
* Explanation for each question result can be given
* Pass marks can be set
* Multiple choice question type
* True/False question type
* Essay question type
* Custom message displayed for those that pass or fail a quiz
* Custom permission (view_sittings) added, allowing users with that permission to view quiz results from users
* A marking page which lists completed quizzes, can be filtered by quiz or user, and is used to mark essay questions
* REST API call available for the functionality. To access just add /list at end in URL.

Requirements
------------

* django-model-utils
* django version >= 2.2


Installation
------------

  git clone https://github.com/manthandubal/tomwalker_quizsite2.git

  pip install -r requirements.txt

Add 'rest_framework','quiz', 'multichoice', 'true_false', and 'essay' to your 'INSTALLED_APPS' setting.

  INSTALLED_APPS = (

      ...
      'rest_framework',
      'quiz',	  
      'multichoice',
      'true_false',
      ...

  )

Add the following to your projects 'urls.py' file, substituting 'q'
for whatever you want the quiz base url to be.

  urlpatterns = patterns('',
      ...
      path('quiz/', include('quiz.urls')),
      path('register/', view=UserFormView.as_view(), name='register'),
      ...

  )
