from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# def main(request):
#   # 数据库里以发布日期排序的最近 5 个投票问题
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   context = { 'latest_question_list': latest_question_list }
#   return render(request, 'api/index.html', context)

# # 返回详情
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'api/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'api/results.html', {'question': question})


class MainView(generic.ListView):
    template_name = 'api/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'api/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'api/results.html'

def vote(request, question_id):
    
    # 使用id找到问题
    question = get_object_or_404(Question, pk=question_id)

    try:
        # 查找这个问题下的选项
        choiceId = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choiceId)
    except (KeyError, Choice.DoesNotExist):
        # 重新显示问题投票表。
        return render(request, 'api/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 重定向到 results 路由
        return HttpResponseRedirect(reverse('api:results', args=(question.id,)))