from django.db import models

class Vocab(models.Model):
    vocab_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text #แสดงคำศัพท์

class Definition(models.Model):
    def_text = models.CharField(max_length=200)
    vocab = models.ForeignKey(Vocab, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text #แสดงคำศัพท์