from django.views import generic
from django.conf import settings
from bakery.views import BuildableTemplateView


class HomeView(generic.TemplateView):
    template_name = "main/home.html"


class AboutView(generic.TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data(**kwargs)
        cxt["contact_mailto"] = settings.CONTACT_MAILTO
        return cxt


class WorkView(generic.TemplateView):
    template_name = "main/work.html"


class ResearchView(generic.TemplateView):
    template_name = "main/research.html"


class ProjectsView(generic.TemplateView):
    template_name = "main/projects.html"


class StaticHomeView(BuildableTemplateView):
    template_name = "main/home.html"
    build_path = "index.html"


class StaticAboutView(BuildableTemplateView):
    template_name = "main/about.html"
    build_path = "about/index.html"

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data(**kwargs)
        cxt["contact_mailto"] = settings.CONTACT_MAILTO
        return cxt


class StaticWorkView(BuildableTemplateView):
    template_name = "main/work.html"
    build_path = "work/index.html"


class StaticResearchView(BuildableTemplateView):
    template_name = "main/research.html"
    build_path = "research/index.html"


class StaticProjectsView(BuildableTemplateView):
    template_name = "main/projects.html"
    build_path = "projects/index.html"


class Static404View(BuildableTemplateView):
    template_name = "404.html"
    build_path = "404/index.html"
