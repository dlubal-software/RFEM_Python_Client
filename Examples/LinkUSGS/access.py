import requests
import json
import pandas as pd

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

    return asceDataTwo

def getAsceDataTwoMCEr(lat, long, risk, site, title):

    asceDataTwoMCEr = pd.DataFrame(columns=["twoPeriodMCErSpectrumPeriods", "twoPeriodMCErSpectrumOrdinates"])

    url = f"https://earthquake.usgs.gov/ws/designmaps/asce7-22.json?latitude={lat}&longitude={long}&riskCategory={risk}&siteClass={site}&title={title}"

    r = requests.get(url)

    schema = json.loads(r.text)

    ## Two period MCEr Spectrum
    asceDataTwoMCEr['twoPeriodMCErSpectrumPeriods'] = schema['response']['data']['twoPeriodMCErSpectrum']['periods']
    asceDataTwoMCEr['twoPeriodMCErSpectrumOrdinates'] = schema['response']['data']['twoPeriodMCErSpectrum']['ordinates']

    return asceDataTwoMCEr
