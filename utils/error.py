"""
handle error pages
"""

from django.shortcuts import render


def render404(request, page=None):
    return render(request, 'web/404.html')