from django.shortcuts import render
from django.views.generic import View

from django.http import Http404
from djplatter.models import ContentCollection


class ServeTemplates(View):
    template_dir = None

    def __init__(self, *args, **kwargs):
        assert self.template_dir, (
            'Configuration error. Class variable template_dir must be set.')
        return super(View, self).__init__(*args, **kwargs)

    def get_content_collection(self):
        return ContentCollection(self.template_dir)

    def dispatch(self, request, *args, **kwargs):
        content = self.get_content_collection()

        try:
            template_path = content.select(request, self.kwargs['path'])
        except:
            raise Http404("No template found for that path.")

        return render(request, template_path)
