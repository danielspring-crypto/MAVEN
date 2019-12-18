from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = "MAVEN ADMIN"
admin.site.site_title = "MAVEN Admin Panel"
admin.site.index_title = "Welcome to MAVEN Researcher Portal"
# Register your models here.
from .models import Mentors, Courses, Register

class MentorsAdmin(admin.ModelAdmin):
	list_display = ('mentor_name', 'post', 'pub_date')
	search_fields = ('mentor_name', 'post',)
	list_filter = ['pub_date']

class CoursesAdmin(admin.ModelAdmin):
	list_display = ('course_name', 'id')
	search_fields = ('course_name', 'course_outline',)

class RegisterAdmin(admin.ModelAdmin):
	list_display = ('student_name', 'course', 'fees', 'paid','duration', 'start', 'end')
	search_fields = ('student_name',)


admin.site.register(Mentors, MentorsAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Register, RegisterAdmin)