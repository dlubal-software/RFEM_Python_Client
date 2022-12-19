import requests
import json
import sys

try:
    import pandas as pd
except:
    print('Pandas library is not installed in your Python env.')
    instPandas = input('Do you want to install it (y/n)?')
    instPandas = instPandas.lower()
    if instPandas == 'y':
        import subprocess
        try:
            subprocess.call('python -m pip install pandas --user')
        except:
            print('WARNING: Installation of pandas library failed!')
            print('Please use command "pip install pandas" in your Command Prompt')
            input('Please Enter to exit...')
            sys.exit()
    else:
        input('Please Enter to exit...')
        sys.exit()

def getAsceDataMulti(lat, long, risk, site, title):

    asceDataMulti = pd.DataFrame(columns=["multiPeriodDesignSpectrumPeriods", "multiPeriodDesignSpectrumOrdinates"])

    url = f"https://earthquake.usgs.gov/ws/designmaps/asce7-22.json?latitude={lat}&longitude={long}&riskCategory={risk}&siteClass={site}&title={title}"

    r = requests.get(url)

    schema = json.loads(r.text)

    # Multi Period Design Spectrum
    asceDataMulti['multiPeriodDesignSpectrumPeriods'] = schema['response']['data']['multiPeriodDesignSpectrum']['periods']
    asceDataMulti['multiPeriodDesignSpectrumOrdinates'] = schema['response']['data']['multiPeriodDesignSpectrum']['ordinates']

    return asceDataMulti

def getAsceDataMultiMCEr(lat, long, risk, site, title):

    asceDataMultiMCEr = pd.DataFrame(columns=["multiPeriodMCErSpectrumPeriods", "multiPeriodMCErSpectrumOrdinates"])

    url = f"https://earthquake.usgs.gov/ws/designmaps/asce7-22.json?latitude={lat}&longitude={long}&riskCategory={risk}&siteClass={site}&title={title}"

    r = requests.get(url)

    schema = json.loads(r.text)

    ## Multi Period MCEr Spectrum
    asceDataMultiMCEr['multiPeriodMCErSpectrumPeriods'] = schema['response']['data']['multiPeriodMCErSpectrum']['periods']
    asceDataMultiMCEr['multiPeriodMCErSpectrumOrdinates'] = schema['response']['data']['multiPeriodMCErSpectrum']['ordinates']

    return asceDataMultiMCEr

def getAsceDataTwo(lat, long, risk, site, title):

    asceDataTwo = pd.DataFrame(columns=["twoPeriodDesignSpectrumPeriods", "twoPeriodDesignSpectrumOrdinates"])

    url = f"https://earthquake.usgs.gov/ws/designmaps/asce7-22.json?latitude={lat}&longitude={long}&riskCategory={risk}&siteClass={site}&title={title}"

    r = requests.get(url)

    schema = json.loads(r.text)

    ## Two period Design Spectrum
    asceDataTwo['twoPeriodDesignSpectrumPeriods'] = schema['response']['data']['twoPeriodDesignSpectrum']['periods']
    asceDataTwo['twoPeriodDesignSpectrumOrdinates'] = schema['response']['data']['twoPeriodDesignSpectrum']['ordinates']

    return asceDataTwo.drop(10)

def getAsceDataTwoMCEr(lat, long, risk, site, title):

    asceDataTwoMCEr = pd.DataFrame(columns=["twoPeriodMCErSpectrumPeriods", "twoPeriodMCErSpectrumOrdinates"])

    url = f"https://earthquake.usgs.gov/ws/designmaps/asce7-22.json?latitude={lat}&longitude={long}&riskCategory={risk}&siteClass={site}&title={title}"

    r = requests.get(url)

    schema = json.loads(r.text)

    ## Two period MCEr Spectrum
    asceDataTwoMCEr['twoPeriodMCErSpectrumPeriods'] = schema['response']['data']['twoPeriodMCErSpectrum']['periods']
    asceDataTwoMCEr['twoPeriodMCErSpectrumOrdinates'] = schema['response']['data']['twoPeriodMCErSpectrum']['ordinates']

    return asceDataTwoMCEr.drop(10)



