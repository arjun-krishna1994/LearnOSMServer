from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __unicode__(self):
        return unicode(self.name)


class Course(models.Model):
    subject = models.ForeignKey(Subject, related_name='courses')
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return unicode(self.name)


class CourseChapter(models.Model):
    name = models.CharField(max_length=40)
    course = models.ForeignKey(Course, related_name='chapters')

    def __unicode__(self):
        return unicode(self.name)


class CourseConcept(models.Model):
    name = models.CharField(max_length=40)
    chapter = models.ForeignKey(CourseChapter, related_name='concepts')
    weightage = models.IntegerField(default=0.5)

    def __unicode__(self):
        return unicode(self.name)



