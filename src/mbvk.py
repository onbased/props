import argparse
import requests
import pprint
import http.client
from io import StringIO, BytesIO
from lxml import etree, html

class MBVKAuction:
    session = requests.Session()

    def get(self, auctionCaseIds):
        result = []

        resp = self.session.post("https://arveres.mbvk.hu")
        resp = self.session.post("https://arveres.mbvk.hu/arverezok")

        TYPES=[
            'normal_ingatlan',
            'ismetelt_ingatlan',
        ]

        for AUCTION_CASE_ID in auctionCaseIds:
            data = None

            for propType in TYPES:
                print(AUCTION_CASE_ID)
                resp = self.session.get(
                    f'https://arveres.mbvk.hu/arverezok/ajax/server_processing_arver_vendeg_af345689.php?sEcho=1&iColumns=15&sColumns=&iDisplayStart=0&iDisplayLength=10&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&mDataProp_5=5&mDataProp_6=6&mDataProp_7=7&mDataProp_8=8&mDataProp_9=9&mDataProp_10=10&mDataProp_11=11&mDataProp_12=12&mDataProp_13=13&mDataProp_14=14&p_ingatlan=true&p_online=true&p_faziskod={propType}&g_sort_mode=&g_sort_dir=&k_vegrehajtasiugyszam={AUCTION_CASE_ID}&k_elo=true&_=1581525130499',
                    headers={
                        'Connection': 'keep-alive',
                        'Pragma': 'no-cache',
                        'Cache-Control': 'no-cache',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-Mode': 'cors',
                        'Referer': 'https://arveres.mbvk.hu/arverezok/ingatlanhirdetmenyek.php',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7'
                    }
                )
                res = resp.json()
                if res and 'aaData' in res and len(res['aaData']) > 0:
                    data = res
                    break

            if data:
                resp = self.session.post(
                    "https://arveres.mbvk.hu/arverezok/reszletezo.php",
                    data={ "arveres_id" : data['aaData'][0][0], "arverestetel_id" : data['aaData'][0][1] },
                    headers={
                        'Connection': 'keep-alive',
                        'Pragma': 'no-cache',
                        'Cache-Control': 'no-cache',
                        'Origin': 'https://arveres.mbvk.hu',
                        'Upgrade-Insecure-Requests': '1',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
                        'Sec-Fetch-User': '?1',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-Mode': 'navigate',
                        'Referer': 'https://arveres.mbvk.hu/arverezok/ingatlanhirdetmenyek.php',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7'
                    }
                )

                parser = etree.HTMLParser()
                root   = etree.fromstring(resp.text, parser)
                images = root.xpath('//*[@id="content"]/a/@href')
                details={}
                detailsNode = root.xpath('//body/div[4]/div[2]/div/div[3]/div/div/label')
                for elem in detailsNode:
                    key = elem[0].text.strip()[:-1].strip()
                    value = self._transform(key, elem[1].text)
                    details[key] = value

                auctionerDetails={}
                auctionerDetailsNode = root.xpath('//body/div[5]/div[2]/div/div[3]/div/div/label')
                for elem in auctionerDetailsNode:
                    key = elem[0].text.strip()[:-1].strip()
                    value = self._transform(key, elem[1].text)
                    details[key] = value

                result.append({
                    'ID': AUCTION_CASE_ID,
                    'images': images,
                    'details': details
                })
                # print('Images:')
                # print(images)
                # print('Details:')
                # print('\n'.join(details))
                # print('Auctioner details:')
                # print('\n'.join(auctionerDetails))

        return result

    def _transform(self, key, value):
        result = value
        PRICE = [
            'Kikiáltási ár',
            'Licitlépcső',
            'Minimum ár',
            'Árverési előleg'
        ]
        if key in PRICE:
            result = int(value.replace(' ', ''))

        return result

# parser = argparse.ArgumentParser(description='Process command line arguments.')
# parser.add_argument('--auction-case-id', action='store', dest='auctionCaseId', help='The id of the auction case')
# args = parser.parse_args()

# main(args.auctionCaseId)
