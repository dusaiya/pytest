# encoding: utf-8
'''
Created on 2017年5月4日

@author: alibaba
'''

from weibo import APIClient  
import webbrowser #python内置的web框架
from __builtin__ import raw_input
import datetime

APP_KEY_LIST=['2188666401','2922462603','2215007837','317551245',
              '996752544','4074934133','1156719470','560195693',
              '3343397376','2000006122',
              '991282944','2320543166','2965462286','2319684540',
              '2113983413','3408744017','738001546','829174382',
              '2364496459','2848583238',
              '1085708363','3259319436','114098119','4151695204',
              '1675294076','1089330661','527684776','4090498614',
              '2542793575','516336241',
              '2409325156','3000399976','1945910489','961492856',
              '198604565','2341714000','631502425','2057441709',
              '1278883655','2111569940'
            ]
APP_SECRET_LIST=['9315033c6b91198e71881ed062bfdd49','1f09bbd6ee7bd405015f7c2b516b4594',
                 '78299eea4c6f9badee39e0acdfec3041','01ccfd1dda98b00c89a3fee31f2d295d',
                 '965738380338bae62d7a7f5256e1985b','fc3d2f11b25ba385336a0715f0a90680',
                 '9349ee885e4be09c657cc665892556f7','618745371070c0d27e3fef8c2456f81a',
                 'b96f6ddc74f5cb18df83601dff5a7bf6','14230c6c76df9f78845024b465392d5c',
                 '0eab3803af72f039d556610d3c9025e2','4eac3badbab537994662401fd386f182',
                 'b0bc52da8f9486beda8f43f3ad723984','1e6686b67c2f28935f9cbbf51dc6ef73',
                 'f2e3480ff4d24013765221ab1d01bab2','e33a21a9b4544ff167826387fc73eaf1',
                 '76554fd3f84b9455a0e3f9789289b6e8','b71476f22f7222ce413b0744472e4738',
                 '89101d44e0a1dabe65cc1955905f0e2a','a654715a7c6709cd5fcac00998dc5b1b',
                 '79186db1fc2b7efc31954d5dcd9e2b02','e4c5aa2fcad368dd48514d4ccb9d5ef7',
                 'a1e6e41edd18cf34643e07c6fa10b20b','6be91d2b2f4a8a73416c684866a975c6',
                 '549f7f8435b834c6db6e251bae2cfbc6','6af0e5cc409c076120444fa2d8b8e248',
                 '6e2ea1f2d4a77b4981d57256a0065b75','872b39aba24d08d26de1f27558e448bc',
                 'e01edc8c62350b9ac1c4e97760704f62','c7ce4f757e8b497258e1d1c5fc37f441',
                 '4111868432f6e490f4e330864e8b2650','7d0a46b378913393de8d6e8443bc3fa5',
                 '608e59a20727ad7aa97f08fb15ee76df','1acaefbb099724fb338bd74f0923c532',
                 'd6c7b88ed8b6d4b77329a1ee053b3db8','30ffc633d98c08dfc127703afc326a58',
                 '13f4eabf7eda67c3b53751bab5277b78','a820525a6d32986e4ba2dd046792c051',
                 '6382c45ded63cca1956e607e6655e621','90f918fe40ff6c0026044d352043a844']
token_list=['2.00UIuP3BzG7H5C23bacb5a88Sn8lXD','2.00UIuP3BbB3mLDa89c08b4bdublSAC', ##01
       '2.00UIuP3Briwt6Cb0f12452e00kANPh','2.00UIuP3B0Ra6U20b5467ecf1CRez_E',
       '2.00UIuP3BwrQ9FB1a32521cbeZCGnPE','2.00UIuP3BFWAm8E79403803c30Z9BlM',
       '2.00UIuP3BeZTRQBd83a059cf80Qen4n','2.00UIuP3B06UWubdabfdd74d5woouOE',
       '2.00UIuP3BI5YQeD1d95b25a27Pr3JmC','2.00UIuP3BQxo2LCcc0f7325f3tadvPB',
       '2.00NEMetGay_FFBbc52958f4difW5OC','2.00NEMetGaRlCXCdddf3906a5tPdzFD',##02
       '2.00NEMetGsMmgODcd28e420000NmFLw','2.00NEMetGmuJzWC4aeba2485cGsJYoB',
       '2.00NEMetGfeDE_Ce6935c6064miSZ8E','2.00NEMetGNCkgiD7707de324eVlbMWD',
       '2.00NEMetG0kuZwn1b4c1d3cdeBPO8WD','2.00NEMetG03IIHu6948de5f52ZNOSFC',
       '2.00NEMetGfXLBaC9256ee0202tvFLME','2.00NEMetGwc3mGD26f955ec93i3CRSB',
       '2.00LCBusCN2WTLBbed61de5420XGIVR','2.00LCBusC1slZYD708b15a0ad0svBNk',##03
       '2.00LCBusC0PIkiH83aba463dc2pqcSC','2.00LCBusCsZFyWE52970e5eb0uSGVPD',
       '2.00LCBusCMW34pB253bcbc2b4BjYTdE','2.00LCBusC4fiiLBf433c67bf1B6vMcC',
       '2.00LCBusC0muGiZaffef56b9a0JtOn6','2.00LCBusCGY_p9E58b3714882HPzV_C',
       '2.00LCBusCblSFmC330cc1ea3bgTzLlC','2.00LCBusC0tdUwYbe9e603934JlzlCD',
       '2.00d2PwWCKXRDdC5606d3e3c2w_qd7D','2.00d2PwWCAG4DRD5459836577D5A4lC',##04
       '2.00d2PwWCDNqgHC6ade683ee9kEm9GC','2.00d2PwWCSN1EDB5c11c68808nUs6SC',
       '2.00d2PwWC08H18Na105709e0ehvZGZC','2.00d2PwWCemaTYCce7b3565760idYVS',
       '2.00d2PwWC0zcijg74bd1db8e9LJKq6B','2.00d2PwWChZoOPC710033d0edND8odE',
       '2.00d2PwWCjDEY5Bf2e631900908Tk8d','2.00d2PwWCgnvtSC205404068aVw5lxC']

idx =39
APP_KEY=APP_KEY_LIST[idx]
APP_SECRET=APP_SECRET_LIST[idx]
CALLBACK_URL = 'http://www.csdn.net'  
##code='96d0c900c69a0b76cf4b39085d154997'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()  
webbrowser.open_new(url)  
print '输入url中code后面的内容后按回车键：'  
code=raw_input()
r = client.request_access_token(code)  
access_token = r.access_token # 新浪返回的token，类似abc123xyz456  
print access_token.__class__
print access_token
expires_in = r.expires_in 
print  expires_in.__class__
print expires_in
dateArray = datetime.datetime.utcfromtimestamp(expires_in)
print dateArray




