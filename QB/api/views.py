from rest_framework import generics
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests
import urllib.parse
# Create your views here.

def delete_special_symbols_in_url(st):
    url = st.replace('%20', ' ').replace('%3A', ':').replace(r'%2F', '/').replace(r'%3F', '?')
    return url

class StatusView(generics.GenericAPIView):
    def post(self, request, format=None):
        
        req = request.data
        res = []

        st =delete_special_symbols_in_url(req['st'])
        est = urllib.parse.quote(st)
        nest = ''
        for item in est.split('%20'):
            print(item)
            nest = nest + '%20' if nest else '' + urllib.parse.quote(item)
        print(nest, est)
        in_ = req['in']

        params = {"st": st, "in": in_}
        url_with_params = f"{'https://www.mmnt.ru/get'}?st={est}&in={in_}"

        print(url_with_params)

        soup_mamont = BeautifulSoup(requests.get(url_with_params).text, 'html.parser')
        for font_tag in soup_mamont.find_all('font'):
            font_tag = 'p'

        for p_cache in soup_mamont.find_all('p', class_='cache_p'):
            p_cache.a['href'] = 'https://www.mmnt.ru' + p_cache.a['href']

        if in_ == 'w':
            for item in soup_mamont.find_all('span', class_='mark_rkn'):
                obj = {
                    'link': str(item.find('p', class_='link_p')),
                    'desc': str(item.find('p', class_='desc_p')),
                    'arch': str(item.find('p', class_='arch_p') if item.find('p', class_='arch_p') else ''),
                    'saved': str(item.find('p', class_='cache_p')),
                    'url': str(item.find('p', class_='url_p').find_all('font')[1]),
                    'class': 'rkn'
                }
                res.append(obj)

            for item in soup_mamont.find_all('span', class_='mark_archive'):
                obj = {
                    'link': str(item.find('p', class_='link_p')),
                    'desc': str(item.find('p', class_='desc_p')),
                    'arch': str(item.find('p', class_='arch_p') if item.find('p', class_='arch_p') else ''),
                    'saved': str(item.find('p', class_='cache_p')),
                    'url': str(item.find('p', class_='url_p').find_all('font')[1]),
                    'class': 'arch'
                }
                res.append(obj)

            for item in soup_mamont.find_all('span', class_='mark_link'):
                obj = {
                    'link': str(item.find('p', class_='link_p')),
                    'desc': str(item.find('p', class_='desc_p')),
                    'arch': str(item.find('p', class_='arch_p') if item.find('p', class_='arch_p') else ''),
                    'saved': str(item.find('p', class_='cache_p')),
                    'url': str(item.find('p', class_='url_p').find_all('font')[1]),
                    'class': 'link'
                }
                res.append(obj)
        else:
            for item in soup_mamont.find_all('table'):
                try:
                    obj = {
                        'link': str(item.find_all('tr')[0].find_all('td')[1].a),
                        'table': str(item.find_all('tr')[1].find_all('td')[0].find_all('tt')[0].table)
                    }

                    if obj['link'] == 'None':
                        continue
                except IndexError as e:
                    print(item.find_all('tr'), '\n =================================')
                    continue
                res.append(obj)
            
        req['obj'] = res[2:]
        return Response(req)