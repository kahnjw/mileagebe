import re


class StravaQueryParamFixMiddleware:
    def process_request(self, request):
        if request.path == '/api/v1/social-auth/complete/strava/':
            get = request.GET.copy()
            queryparam = get['redirect_state']
            m = re.search(r'(\w+)[?]code=(\w+)', queryparam)
            get['redirect_state'] = m.group(1)
            get['code'] = m.group(2)
            request.GET = get

        return None
