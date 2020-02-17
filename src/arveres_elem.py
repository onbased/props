import argparse
import requests
import pprint
import http.client
from io import StringIO, BytesIO
from lxml import etree, html

pp = pprint.PrettyPrinter(indent=4)
s = requests.Session()

def main(auctionCaseId):
    # conn = http.client.HTTPSConnection("arveres.mbvk.hu")
    # conn.request("POST","/arverezok/reszletezo.php")
    # res = conn.getresponse()
    # root = etree.fromstring(res.read())
    #table = root.xpath('//x:table', namespaces={'x': root.nsmap[None]})
    resp = s.post("https://arveres.mbvk.hu")
    resp = s.post("https://arveres.mbvk.hu/arverezok")
    
    # s.cookies['SpryMedia_DataTables_arver_tabla_ingatlanhirdetmenyek.php']="%7B%22iCreate%22%3A1581507122930%2C%22iStart%22%3A0%2C%22iEnd%22%3A0%2C%22iLength%22%3A10%2C%22aaSorting%22%3A%5B%5B0%2C%22asc%22%2C0%5D%5D%2C%22oSearch%22%3A%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%22aoSearchCols%22%3A%5B%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%2C%7B%22bCaseInsensitive%22%3Atrue%2C%22sSearch%22%3A%22%22%2C%22bRegex%22%3Afalse%2C%22bSmart%22%3Atrue%7D%5D%2C%22abVisCols%22%3A%5Bfalse%2Cfalse%2Cfalse%2Cfalse%2Cfalse%2Cfalse%2Cfalse%2Cfalse%2Cfalse%2Cfalse%2Cfalse%2Cfalse%2Ctrue%2Cfalse%2Cfalse%5D%7D"
    # s.cookies['cookieconsent_status']='true'
    # s.cookies['tajekoztato20170321']='20200129154523'
    #    data={
    #        'iColumns': '15',
    #        'sColumns': '',
    #        'iDisplayStart': '0',
    #        'iDisplayLength': '10',
    #        'mDataProp_0':'0',
    #        'mDataProp_1':'1',
    #        'mDataProp_2':'2',
    #        'mDataProp_3':'3',
    #        'mDataProp_4':'4',
    #        'mDataProp_5':'5',
    #        'mDataProp_6':'6',
    #        'mDataProp_7':'7',
    #        'mDataProp_8':'8',
    #        'mDataProp_9':'9',
    #        'mDataProp_10':'10',
    #        'mDataProp_11':'11',
    #        'mDataProp_12':'12',
    #        'mDataProp_13':'13',
    #        'mDataProp_14':'14',
    #        'p_ingatlan':'true',
    #        'p_online':'true',
    #        'p_faziskod':'ismetelt_ingatlan',
    #        'g_sort_mode':'',
    #        'g_sort_dir':'',
    #        'k_vegrehajtasiugyszam':'0007.V.0608/2012/285',
    #        'k_elo':'true',
    #        '_':'1581525130499'
    #    },

    TYPES=[
        'normal_ingatlan',
        'ismetelt_ingatlan',
    ]
    AUCTION_CASE_ID=auctionCaseId
    data = None

    for propType in TYPES:
        print(AUCTION_CASE_ID)
        resp = s.get(
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
        pp.pprint(res)
        if res and 'aaData' in res and len(res['aaData']) > 0:
            data = res
            break
    
    if not data:
        print('No property found')
        return

    resp = s.post(
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

    details=[]
    detailsNode =          root.xpath('//body/div[4]/div[2]/div/div[3]/div/div/label')
    for elem in detailsNode:
        details.append(f'{elem[0].text} {elem[1].text}')
    
    auctionerDetails=[]
    auctionerDetailsNode = root.xpath('//body/div[5]/div[2]/div/div[3]/div/div/label')
    for elem in auctionerDetailsNode:
        auctionerDetails.append(f'{elem[0].text} {elem[1].text}')
    
    print('Images:')
    print(images)
    print('Details:')
    print('\n'.join(details))
    print('Auctioner details:')
    print('\n'.join(auctionerDetails))


parser = argparse.ArgumentParser(description='Process command line arguments.')
parser.add_argument('--auction-case-id', action='store', dest='auctionCaseId', help='The id of the auction case')
args = parser.parse_args()

main(args.auctionCaseId)
