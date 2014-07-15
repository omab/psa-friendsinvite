from requests import request

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def done(request):
    return render(request, 'home.html')


@login_required
def invite(request):
    # Check if user access-token has got granted access to friends list and
    # retrieve friends. This value can be cached later on a model, or session,
    # or any place it's better for the project.
    if has_friends_permission(request.user):
        friends = get_friends(request.user)
    else:
        friends = []
    return render(request, 'invite.html', {
      'friends': friends,
      'SOCIAL_AUTH_FACEBOOK_KEY': settings.SOCIAL_AUTH_FACEBOOK_KEY
    })


@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')


# Call /me/permissions to check the permissions granted to the access_token
def has_friends_permission(user):
    facebook = user.social_auth.get(provider='facebook')
    url = 'https://graph.facebook.com/me/permissions'
    permissions = request('GET', url, params={
      'access_token': facebook.extra_data['access_token']
    }).json()
    return permissions['data'][0].get('user_friends') or False


# Call /me/friends to get the user friends list, Facebook will provide a list
# of objects with the following keys: {id: '...', name: ''}
def get_friends(user):
    facebook = user.social_auth.get(provider='facebook')
    url = 'https://graph.facebook.com/me/friends'.format(facebook.uid)
    friends = request('GET', url, params={
      'access_token': facebook.extra_data['access_token']
    }).json()
    return friends['data']
