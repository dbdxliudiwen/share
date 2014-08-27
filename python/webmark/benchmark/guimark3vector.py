﻿from benchmark import *


class guimark3vector(Benchmark):
    CONFIG = {
        'name': 'GUIMark3 Vector',
        'metric': 'FPS',
        'path': {
            'external': 'http://www.craftymind.com/factory/guimark3/vector/GM3_JS_Vector.html',
            'internal': 'webbench/GUIMark3/vector/GM3_JS_Vector.html'
        },
        'times_run': 3,
    }

    def cond0(self, driver):
        self.e = driver.find_element_by_id('testaction')
        if self.e:
            return True
        else:
            return False

    def act0(self, driver):
        self.e.click()

    def cond1(self, driver):
        self.e = driver.find_element_by_id('testlabel')
        if self.e.text.find('Test Results:') != -1:
            return True
        else:
            return False

    def act1(self, driver):
        pattern = re.compile('(\d+\.?\d*) fps')
        match = pattern.search(self.e.text)
        self.result.append(match.group(1))