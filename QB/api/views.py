from rest_framework import generics
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests
import urllib.parse
from . import common
import g4f
from django.conf import settings


class GetGPTView(generics.GenericAPIView):
    def post(self, request, format=None):
        req = request.data
        try:
            content = req['content']
        except KeyError:
            res = 'Backend Error: no content in post data'
            return Response({'res': res}, status=500)
        

        response = g4f.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": content}])

        if not response:
            response = g4f.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": content}])
        if not response:
            response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])
        if not response:
            response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])
        
        response=response

        return Response({'res': response})
        

# Create your views here.
class GetFTPSView(generics.GenericAPIView):
    def get(self, request, format=None):
        manont_soup = BeautifulSoup(requests.get('https://www.mmnt.ru/ftp-sites').text, 'html.parser')
        res=[]
        
        for td_el in manont_soup.find_all('td'):
            try:
                temp = []
                temp.append(str(td_el.find('font')))
                a = td_el.find('a')
                a['href'] = 'ftp://' + a.get_text()
                temp.append(str(a))
                res.append([temp])
            except AttributeError as e:
                continue

        return Response(res)


class QVPNView(generics.GenericAPIView):
    def post(self, request, format=None):
        req = request.data
        try:
            url = req['url']


        except KeyError:
            res = 'Backend Error: no url in post data'
            return Response({'res': res, 'url': url, 'html': ''}, status=500)
        try:
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        except Exception as e:
            res = 'Backend Error: '+str(e)
            return Response({'res': res, 'url': url, 'html': ''}, status=500)
        for img_tags in soup.find_all('img'):
            if 'src' in img_tags.attrs:
                if not (img_tags.attrs['src'].startswith('http')):
                    img_tags.attrs['src'] = f'{common.get_domain(url)}'+img_tags.attrs['src']

            if '..' in img_tags.attrs['src']:
                img_tags.attrs['src'] = img_tags.attrs['src'].replace('..', '')


        for a_tags in soup.find_all('a'):

            if 'href' in a_tags.attrs:
                if a_tags.attrs['href'].startswith('http'):
                    a_tags.attrs['href'] = f'http://localhost:3003/qvpn/?url='+a_tags.attrs['href']
                else:
                    a_tags.attrs['href'] = f'http://localhost:3003/qvpn/?url={url}'+a_tags.attrs['href']

        return Response({'html': soup.prettify(encoding='utf-8'), 'url': url, 'res': 'OK'}, status=200)

class StatusView(generics.GenericAPIView):
    def post(self, request, format=None):
        try:
        
            req = request.data
            res = []
            in_ = req['in']
            try:
                ot = req['ot']
            except KeyError:
                ot = 1

            try: sg = req['sg']
            except KeyError: sg = ''

            try: sz = req['sz']
            except KeyError: sz = ''

            try: st =req['st']
            except KeyError: st = ''
            est=''
            if in_ == 'w':
                est = urllib.parse.quote(st)
                nest = ''
                for item in est.split('%20'):
                    print(item)
                    nest = nest + '%20' if nest else '' + urllib.parse.quote(item)
                print(nest, est)
            elif in_ == 'f':
                for item in st:
                    try:  
                        leter = common.CODE[item]
                    except KeyError:
                        leter=item
                    est = est + leter
                    
                print(est)

            

            url_with_params = f"{'https://www.mmnt.ru/get'}?st={est}&in={in_}&ot={ot}" + (f"&sg={sg}" if sg else '') + (f"&sz={sz}" if sz else '')

            print(url_with_params)

            soup_mamont = BeautifulSoup(requests.get(url_with_params).text, 'html.parser')
            try:
                cpages = str(soup_mamont.find('div', class_='info_block').find_all('b')[0].text)
            except AttributeError:
                cpages = str(soup_mamont.find('div', class_='nav_block').find_all('b')[0].text)
            for font_tag in soup_mamont.find_all('font'):
                font_tag['color'] = '#fff'

            for tr_tag in soup_mamont.find_all('tr'):
                tr_tag['bgcolor'] = '#232222'

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
                            'table': str(item.find_all('tr')[1].find_all('td')[0].find_all('tt')[0].table),
                            'simular_url': str(item.find_all('tr')[1].find_all('td')[0].find_all('tt')[0].find_all('font')[4].a['href']) if item.find_all('tr')[1].find_all('td')[0].find_all('tt')[0].find_all('font')[4].a else 'None',
                            'also_url': str(item.find_all('tr')[1].find_all('td')[0].find_all('tt')[0].find_all('font')[5].a['href']) if item.find_all('tr')[1].find_all('td')[0].find_all('tt')[0].find_all('font')[5].a else 'None',
                            
                        }

                        if sg == '':
                            obj['search_url']= common.decode_url(str(item.find_all('tr')[1].find_all('td')[0].find_all('tt')[0].find_all('font')[6].a['href'])) if item.find_all('tr')[1].find_all('td')[0].find_all('tt')[0].find_all('font')[6].a else 'None',

                        if obj['link'] == 'None':
                            continue
                    except IndexError as e:
                        print(e, item)
                        continue
                    res.append(obj)
                

            req['obj'] = res[0:]
            req['OK'] = True
            req['cpages'] = cpages
            return Response(req)
        except IndexError as e:
            return Response({'error': str(e), 'OK': False})