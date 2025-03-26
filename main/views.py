from django.conf import settings
from bakery.views import BuildableTemplateView


class HomeView(BuildableTemplateView):
    template_name = "main/home.html"
    build_path = "index.html"


class AboutView(BuildableTemplateView):
    template_name = "main/about.html"
    build_path = "about/index.html"

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data(**kwargs)
        cxt["contact_mailto"] = settings.CONTACT_MAILTO
        return cxt


class WorkView(BuildableTemplateView):
    template_name = "main/work.html"
    build_path = "work/index.html"


class ResearchView(BuildableTemplateView):
    template_name = "main/research.html"
    build_path = "research/index.html"


class ProjectsView(BuildableTemplateView):
    template_name = "main/projects.html"
    build_path = "projects/index.html"


class Custom404View(BuildableTemplateView):
    template_name = "404.html"
    build_path = "404/index.html"
