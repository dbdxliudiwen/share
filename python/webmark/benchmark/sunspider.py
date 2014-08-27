from benchmark import *


class sunspider(Benchmark):
    CONFIG = {
        'name': 'SunSpider',
        'metric': 'ms',
        # Webkit all versions: http://www.webkit.org/perf/sunspider/versions.html
        'path': {
            '0.9': {
                'external': 'http://www.webkit.org/perf/sunspider-0.9/sunspider-driver.html',
                'internal': 'webbench/sunspider/0.9/sunspider-0.9/driver.html'
            },
            '0.9.1': {
                'external': 'http://www.webkit.org/perf/sunspider-0.9.1/sunspider-0.9.1/driver.html',
                'internal': 'webbench/sunspider/0.9.1/sunspider-0.9.1/driver.html'
            },
            '1.0': {
                'external': 'http://www.webkit.org/perf/sunspider-1.0/sunspider-1.0/driver.html',
                'internal': 'webbench/sunspider/1.0/sunspider-1.0/driver.html'
            },
            '1.0.1': {
                'external': 'http://www.webkit.org/perf/sunspider-1.0.1/sunspider-1.0.1/driver.html',
                'internal': 'webbench/sunspider/1.0.1/sunspider-1.0.1/driver.html'
            },
            '1.0.2': {
                'external': 'http://www.webkit.org/perf/sunspider-1.0.2/sunspider-1.0.2/driver.html',
                'internal': 'webbench/sunspider/1.0.2/sunspider-1.0.2/driver.html'
            },
            # Google all versions: http://sunspider-mod.googlecode.com/svn/data/hosted/versions.html
            '0.9.1-google-new': {
                'external': 'http://sunspider-mod.googlecode.com/svn/data/hosted/sunspider-0.9.1/driver.html?type=new',
                'internal': ''
            },
            '0.9.1-google-standard': {
                'external': 'http://sunspider-mod.googlecode.com/svn/data/hosted/sunspider-0.9.1/driver.html?type=standard',
                'internal': ''
            }
        },
        'version': '1.0.2',
    }

    def __init__(self, driver, case):
        super(sunspider, self).__init__(driver, case)

    def cond0(self, driver):
        if re.search('results', driver.current_url):
            return True
        else:
            return False

    def act0(self, driver):
        str = self.driver.find_element_by_id('console').text
        pos = str.find('Total:') + len('Total:')
        str = str[pos:].strip()
        pos = str.find('ms')

        self.result.append(str[:pos])