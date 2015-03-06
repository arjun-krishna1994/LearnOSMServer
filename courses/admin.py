from django.contrib import admin
import models
#from nested_inline.admin import NestedStackedInline, NestedModelAdmin
class ContentConceptInline(admin.StackedInline):
    model = models.CourseConceptContent
    max_num = 1

class ConceptChapterInline(admin.StackedInline):
    model = models.CourseConcept
    max_num = 4

class ChapterCourseInline(admin.StackedInline):
    model = models.CourseChapter
    max_num = 4

class CoursesSubjectInline(admin.StackedInline):
    model = models.Course
    max_num = 1

class CourseModelAdmin(admin.ModelAdmin):
    inlines = [ChapterCourseInline]
    search_fields = ['name','details']
    list_filter = ['subject']
    list_display = ['name', 'subject_name']

class SubjectModelAdmin(admin.ModelAdmin):
    inlines = [CoursesSubjectInline]
    search_fields = ['name']


class ChapterModelAdmin(admin.ModelAdmin):
    inlines = [ConceptChapterInline]
    list_filter = ['course_name']

class ConceptModelAdmin(admin.ModelAdmin):
    list_filter = ['chapter_name', 'course_name']
    list_display = ['name', 'chapter_name', 'course_name']

class ConceptContentModelAdmin(admin.ModelAdmin):
    list_filter = ['course_name']
    search_fields = ['content', 'chapter_name', 'course_name', 'concept_name']
    list_display = ['__unicode__', 'chapter_name', 'course_name']


admin.site.register(models.Subject, SubjectModelAdmin)
admin.site.register(models.Course, CourseModelAdmin)
admin.site.register(models.CourseChapter, CourseModelAdmin)
admin.site.register(models.CourseConcept, ConceptModelAdmin)
admin.site.register(models.CourseConceptContent, ConceptContentModelAdmin)

