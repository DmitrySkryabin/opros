from django.db import models


class Question_group(models.Model):
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_group_id = models.ForeignKey(Question_group, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
