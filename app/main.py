#dependencies are the libraries used for the project
from dependencies import *
#models are the object used all along on the database
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.proxy import *

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

#luminati proxy connection string
random_number_ = str(np.random.randint(low=10000, high= 11000, size=1)[0])
proxy_port = 22225
username = 'lum-customer-firewant-zone-zone1'
password = ''
session_id = random_number_
proxy = ('http://%s-country-us-session-%s:%s@zproxy.lum-superproxy.io:%s' %
    (username, session_id, password, proxy_port))

# Create the session and set the proxies.
@app.route('/proxy_tester')
def proxy_test_():
    url = "http://whatsmyip.org"
    #simple connection example
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver.title

if __name__ == "__main__":
    debugging = True
    app.run(host='0.0.0.0', debug=debugging, port=80, threaded=True)
