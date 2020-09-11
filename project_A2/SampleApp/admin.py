from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Snippet
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html

admin.site.site_header = 'Admin Tutorial Dashboard'

class SnippetAdmin(admin.ModelAdmin):
	#exclude = ('title',)
	#fields = ('title',)
	list_display = ('title','body','created','font_size_html_display')
	list_filter = ('created',)
	change_list_template = 'admin/snippets/snippets_change_list.html'

	def get_urls(self):
		urls = super().get_urls()
		custom_urls = [
			path('fontsize/<int:size>/',self.change_font_size)
		]
		return custom_urls + urls

	def change_font_size(self , request, size):
		self.model.objects.all().update(fontsize=size)
		self.message_user(request, 'font size set successfully!')
		return HttpResponseRedirect("../../")

	def font_size_html_display(self, obj):
		display_size = obj.fontsize if obj.fontsize <= 50 else 50
		return format_html(
			f'<span style="font-size:{display_size}px">{obj.fontsize}</span>'

		)

	# def font_size_html_display(self, obj):
 #        display_size = obj.fontsize if obj.fontsize <=50 else 50
 #        return format_html(
 #            f'<span style="font-size:{display_size}px">{obj.fontsize}</span>'
 #        )

admin.site.register(Snippet,SnippetAdmin)
admin.site.unregister(Group)

# Register your models here.
