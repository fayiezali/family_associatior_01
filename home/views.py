from django.shortcuts import render
#
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
#
"""
Post comments Here
"""

# Display The Home Page
class IndexPage(TemplateView):
    #
    # The Page HTML to Display
    template_name = "home/index_page.html"  
    
    # A Functin that Receives The Sent Data And Displays It On The Current Page
    def get_context_data(self, **kwargs):
        #
        context = super().get_context_data(**kwargs)
        #
        # Number Of visits To The Site:
        # Get a Session Value Setting a Default If It Is Not Present.
        num_visits = self.request.session.get('num_visits', 1)
        #
        # Render the HTML template index.html with the data in the context variable.
        context['number_of_visits_site'] = self.request.session['num_visits'] = num_visits+1
        #
        return context  # Send This Data To The Required Page HTML

# Display Them About Page
class AboutPage(TemplateView):
    #
    # The Page HTML to Display
    template_name = "home/about_page.html"  
#
# Display Them Contact Page
class ContactPage(TemplateView):
    #
    # The Page HTML to Display
    template_name = "home/contact_page.html"  
#
#
#