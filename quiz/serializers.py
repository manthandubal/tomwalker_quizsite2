from rest_framework import serializers
from .models import Category, SubCategory, Quiz, Progress, Sitting, Question, SittingManager
from multichoice.models import MCQuestion, Answer
from true_false.models import TF_Question
from essay.models import Essay_Question

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('__all__',)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        # fields = '__all__'
        exclude = ('id', 'category')
        read_only_fields = ('__all__',)

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ('__all__',)

class SittingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitting
        fields = ('id', 'quiz', 'current_score', 'get_max_score', 'get_percent_correct')
        read_only_fields = ('__all__',)


class ProgressSerializer(serializers.ModelSerializer):
    prev_exams_papers = serializers.SerializerMethodField()

    def get_prev_exams_papers(self, obj):
        ordered_queryset = Sitting.objects.filter(user_id=obj.user_id)
        return SittingSerializer(ordered_queryset, many=True, context=self.context).data

    class Meta:
        model = Progress
        fields = ('id', 'score', 'user', 'prev_exams_papers')
        read_only_fields = ('__all__',)

class MarkingSerializer(serializers.ModelSerializer):
    end = serializers.DateTimeField(format="%B %d, %Y")
    model = Sitting

    def get_queryset(self, obj):
        queryset = Sitting.objects.filter(complete=True)
        user_filter = self.request.GET.get('user_filter')
        if user_filter:
            queryset = Sitting.objects.filter(user__username__icontains=user_filter, complete=True)
        return Sitting(queryset, many=True, context=self.context).data

    class Meta:
        model = Sitting
        fields = ('user', 'quiz', 'end', 'get_percent_correct')
        read_only_fields = ('__all__',)

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'content','figure', 'explanation', 'category','sub_category','quiz')
        read_only_fields = ('__all__',)


class TF_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TF_Question
        fields = '__all__'
        read_only_fields = ('__all__',)