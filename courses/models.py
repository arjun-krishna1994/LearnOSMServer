from django.db import models
from ckeditor.fields import RichTextField

class Subject(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __unicode__(self):
        return unicode(self.name)

    def get_name(self):
        return self.name


class Course(models.Model):
    subject = models.ForeignKey(Subject, related_name='courses')
    name = models.CharField(max_length=40)
    details = RichTextField()

    def __unicode__(self):
        return unicode(self.name)

    def get_name(self):
        return self.name

    @property
    def subject_name(self):
        return unicode(self.subject.get_name())


class CourseChapter(models.Model):
    class Meta:
        verbose_name_plural = "Course's Chapters"
    name = models.CharField(max_length=40)
    course = models.ForeignKey(Course, related_name='chapters')
    details = RichTextField()

    def __unicode__(self):
        return unicode(self.name)

    @property
    def course_name(self):
        return unicode(self.course.get_name())

    def get_name(self):
        return self.name


class CourseConcept(models.Model):
    class Meta:
        verbose_name_plural = "Chapter's Concepts"
    name = models.CharField(max_length=40)
    chapter = models.ForeignKey(CourseChapter, related_name='concepts')
    weightage = models.IntegerField(default=0.5, help_text="This is used while calculating the percentage"
                                                           " completion of the course for a user")

    def __unicode__(self):
        return unicode(self.name)

    @property
    def chapter_name(self):
        return unicode(self.chapter.name)

    @property
    def course_name(self):
        return self.chapter.course_name()

    def get_name(self):
        return self.name

class CourseConceptContent(models.Model):
    course_concept = models.OneToOneField(CourseConcept, related_name='content')
    content = RichTextField()

    def __unicode__(self):
        return self.course_concept.name + "\'s" + "Content"

    @property
    def concept_name(self):
        return unicode(self.course_concept.get_name())

    @property
    def chapter_name(self):
        return unicode(self.course_concept.chapter_name())

    @property
    def course_name(self):
        return unicode(self.course_concept.course_name())




