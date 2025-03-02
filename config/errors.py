from django.shortcuts import render

from django.views import View


class CustomPageNotFoundView(View):
    """
    Custom view for 404 error pages.
    """

    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, status=404)


custom_page_not_found_as_view = CustomPageNotFoundView.as_view()
