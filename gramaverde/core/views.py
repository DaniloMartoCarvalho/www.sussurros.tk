from django.views import generic


class Index(generic.TemplateView):
    template_name = "pages/index.html"


index = Index.as_view()
