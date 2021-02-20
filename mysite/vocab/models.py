from django.db import models

class Vocab(model.Model):
    vocab_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text #แสดงคำศัพท์

