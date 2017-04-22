from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .forms import PostForm
from .models import Post
# Create your views here.

# For this case, I simply raise Http404 error if the post does not exist. It can also be treated another way by redirection.
# For example, 
#	if not Post.objects.get(pk=id):
#		HttpResponseRedirect("namespace:name")
# The parameter namespace is the app name set in project urls.py, name is the routing name set in app urls.py
class PostView(TemplateView):
	form = PostForm

	def post(self, request, id=None, *args, **kwargs):
		if id:
			post_obj = get_object_or_404(Post, pk=id)
			form = self.form(request.POST, instance=post_obj)
		else:
			form = self.form(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")

		context={
			"form" : form,
		}
		return render(request, self.template_name, context)

	def get(self, request, id=None, *args, **kwargs):
		
		if id:
			post_obj = get_object_or_404(Post, pk=id)
			form = self.form(instance=post_obj)
		else:
			form = self.form()
		print(id)
		context={
			"form" : form,
			"id" : id,
		}
		return render(request, self.template_name, context)

def listview(request, *args, **kwargs):
	post_obj = Post.objects.all()
	print(post_obj)
	context = {
		"post" : post_obj,
	}
	return render(request, kwargs["template_name"], context)

def delete_post(request, id, *args, **kwargs):
	post_obj = get_object_or_404(Post, pk=id)
	if request.POST:
		post_obj.delete()
		return HttpResponseRedirect("/")

	context = {
		"form" : post_obj,
	}
	return render(request, kwargs["template_name"], context)




