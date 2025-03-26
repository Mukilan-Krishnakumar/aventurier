from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(BaseModel):
    name = models.TextField()


class LanguageFramework(BaseModel):
    name = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class Levels(BaseModel):
    language_framework = models.OneToOneField(
        LanguageFramework, on_delete=models.CASCADE, primary_key=True
    )
    choices = models.JSONField()


class PartOfSpeech(BaseModel):
    name = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    choices = models.JSONField()


class VocabItem(BaseModel):
    term = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    definition = models.TextField()
    examples = models.TextField()
    # TODO: Modify this to a self-referential field
    synonyms = models.TextField()
    part_of_speech = models.ForeignKey(PartOfSpeech, on_delete=models.CASCADE)
