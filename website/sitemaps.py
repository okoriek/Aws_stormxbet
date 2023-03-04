from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSiteMap(Sitemap):

    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return [
            'home',
            'affiliate',
            'help'
        ]
    def location(self, item):
        return reverse(item)