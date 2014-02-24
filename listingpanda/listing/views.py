from django.shortcuts import render
from django.views.generic import View
from listingpanda.settings import BASE_DIR, MEDIA_URL

import json
import os

# Create your views here.
class ListingView(View):

    template_name = 'home.html'
    sample_json = os.path.join(BASE_DIR, 'templates', 'sample.json')

    def load(self):
        json_data = open(self.sample_json)
     	listings = json.load(json_data)
     	listings['listings'] = listings['listings'][:15]
        json_data.close()
        return listings

    def get(self, request, *args, **kwargs):
        context = self.load()
        context['MEDIA_URL'] = MEDIA_URL
        return render(request, self.template_name, context)
