from django.db import models

class Question(models.Model):
    question_text = models.CharField('问题标题', max_length=200)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    # 链表 Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
