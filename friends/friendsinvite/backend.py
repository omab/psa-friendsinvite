from social.backends.facebook import FacebookOAuth2 as BaseFacebookOAuth2


class FacebookOAuth2(BaseFacebookOAuth2):
    def get_scope(self):
        scope = super(FacebookOAuth2, self).get_scope()
        if self.data.get('invite'):
            scope.append('user_friends')
        return scope
