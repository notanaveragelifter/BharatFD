from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = RichTextField(blank=True, null=True)       # Hindi
    answer_bn = RichTextField(blank=True, null=True)       # Bengali

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):
        return self.question

    from googletrans import Translator

translator = Translator()

def translate_text(text, dest_lang):
    try:
        return translator.translate(text, dest=dest_lang).text
    except:
        return text  # Fallback to original text

class FAQ(models.Model):
    ...

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)    
