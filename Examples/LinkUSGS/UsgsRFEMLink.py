import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
sys.path.append(dirName + r'/../..')

from RFEM.enums import AddOn, ObjectTypes
from RFEM.initModel import Model, AddOn, GetAddonStatus, SetAddonStatus, FirstFreeIdNumber
from RFEM.DynamicLoads.responseSpectrum import ResponseSpectrum
from access import getAsceDataMulti, getAsceDataMultiMCEr, getAsceDataTwo, getAsceDataTwoMCEr
from PIL import Image
try:
    import streamlit as st
except:
    print('Streamlit library is not installed in your Python env.')
    instStreamlit = input('Do you want to install it (y/n)?')
    instStreamlit = instStreamlit.lower()
    if instStreamlit == 'y':
        import subprocess
        try:
            subprocess.call('python -m pip install streamlit --user')
        except:
            print('WARNING: Installation of streamlit library failed!')
            print('Please use command "pip install streamlit --user" in your Command Prompt.')
            input('Press Enter to exit...')
            sys.exit()
    else:
        input('Press Enter to exit...')
        sys.exit()
try:
    import plotly.express as px
except:
    print('plotly.express library is not installed in your Python env.')
    instPlotly = input('Do you want to install it (y/n)?')
    instPlotly.lower()
    if instPlotly == 'y':
        import subprocess
        try:
            subprocess.call('python -m pip install plotly.express  --user')
        except:
            print('WARNING: Installation of plotly.express  library failed!')
            print('Please use command "pip install plotly.express  --user" in your Command Prompt.')
            input('Press Enter to exit...')
            sys.exit()
    else:
        input('Press Enter to exit...')
        sys.exit()

if __name__ == '__main__':
    # set page configs and title
    st.set_page_config(layout="wide")

    logoColumn, titleColumn = st.columns([1,10], gap='large')
    with logoColumn:
        logo = Image.open(dirName + '/assets/logo_round.png')
        st.image(logo, width=100)
    with titleColumn:
        st.title("USGS-RFEM6 WebService Link")

    # create initial graphs
    initAsceMulti = getAsceDataMulti(38, -110, 'III', 'C', 'rfemCall')
    initPeriodsMulti = initAsceMulti['multiPeriodDesignSpectrumPeriods']
    initOrdinatesMulti = initAsceMulti['multiPeriodDesignSpectrumOrdinates']

    fig_1 = px.line(x = initPeriodsMulti, y = initOrdinatesMulti, labels = {'x': 'Period (s)', 'y': 'Ground Motion (g)'}, title = "Multi Period")

    fig_1.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 0.5,
            dtick = 0.75,
        ),
        xaxis_range=[0,5],
    )

    initAsceMultiMCEr = getAsceDataMultiMCEr(38, -110, 'III', 'C', 'rfemCall')
    initPeriodsMultiMCEr = initAsceMultiMCEr['multiPeriodMCErSpectrumPeriods']
    initOrdinatesMultiMCEr = initAsceMultiMCEr['multiPeriodMCErSpectrumOrdinates']

    initAsceMultiMCEr = getAsceDataMultiMCEr(38, -110, 'III', 'C', 'rfemCall')
    initPeriodsMultiMCEr = initAsceMultiMCEr['multiPeriodMCErSpectrumPeriods']
    initOrdinatesMultiMCEr = initAsceMultiMCEr['multiPeriodMCErSpectrumOrdinates']

    fig_2 = px.line(x = initPeriodsMultiMCEr, y = initOrdinatesMultiMCEr, labels = {'x': 'Period (s)', 'y': 'Ground Motion (g)'}, title = "Multi Period MCEr")

    fig_2.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 0.5,
            dtick = 0.75,

        ),
        xaxis_range=[0,5],
    )

    initAsceTwoData = getAsceDataTwo(38, -110, 'III', 'C', 'rfemCall')
    initPeriodsTwoData = initAsceTwoData['twoPeriodDesignSpectrumPeriods']
    initOrdinatesTwoData = initAsceTwoData['twoPeriodDesignSpectrumOrdinates']

    fig_3 = px.line(x = initPeriodsTwoData, y = initOrdinatesTwoData, labels = {'x': 'Period (s)', 'y': 'Ground Motion (g)'}, title = "Two Period Spectrum")

    fig_3.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 0.5,
            dtick = 0.75,

        ),
        xaxis_range=[0,5],
    )

    initAsceTwoDataMCEr = getAsceDataTwoMCEr(38, -110, 'III', 'C', 'rfemCall')
    initPeriodsTwoDataMCEr = initAsceTwoDataMCEr['twoPeriodMCErSpectrumPeriods']
    initOrdinatesTwoDataMCEr = initAsceTwoDataMCEr['twoPeriodMCErSpectrumOrdinates']

    fig_4 = px.line(x = initPeriodsTwoDataMCEr, y = initOrdinatesTwoDataMCEr, labels = {'x': 'Period (s)', 'y': 'Ground Motion (g)'}, title = "Two Period MCEr Spectrum")

    fig_4.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 0.5,
            dtick = 0.75,

        ),
        xaxis_range=[0,5],
    )

    psudeoColumn1, latitudeColumn, longitudeColumn, soilColumn, psudeoColumn2 = st.columns(5)

    with latitudeColumn:
        latitude = st.number_input("Location Latitude", value=36.25048)

    with longitudeColumn:
        longitude = st.number_input("Location Longitude", value=-81.86759)

    with soilColumn:
        site = st.selectbox("Site Category", ["A", "B", "C", "D", "E"])

    psudeoColumn3, psudeoColumn4, buttonColumn, psudeoColumn5, psudeoColumn6 = st.columns(5)

    with buttonColumn:
        getSpectrumButton = st.button("Get Design Spectrum Data and Update Graphs")

    if getSpectrumButton:

        initAsceMulti = getAsceDataMulti(latitude, longitude, 'III', site, 'rfemCall')
        initPeriodsMulti = initAsceMulti['multiPeriodDesignSpectrumPeriods']
        initOrdinatesMulti = initAsceMulti['multiPeriodDesignSpectrumOrdinates']

        fig_1 = px.line(x = initPeriodsMulti, y = initOrdinatesMulti, labels = {'x': 'Period (s)', 'y': 'Ground Motion (g)'}, title = "Multi Period")

        fig_1.update_layout(
            xaxis = dict(
                tickmode = 'linear',
                tick0 = 0.5,
                dtick = 0.75,
            ),
            xaxis_range=[0,5],
        )

        initAsceMultiMCEr = getAsceDataMultiMCEr(latitude, longitude, 'III', site, 'rfemCall')
        initPeriodsMultiMCEr = initAsceMultiMCEr['multiPeriodMCErSpectrumPeriods']
        initOrdinatesMultiMCEr = initAsceMultiMCEr['multiPeriodMCErSpectrumOrdinates']

        fig_2 = px.line(x = initPeriodsMultiMCEr, y = initOrdinatesMultiMCEr, labels = {'x': 'Period (s)', 'y': 'Ground Motion (g)'}, title = "Multi Period MCEr")

        fig_2.update_layout(
            xaxis = dict(
                tickmode = 'linear',
                tick0 = 0.5,
                dtick = 0.75,

            ),
            xaxis_range=[0,5],
        )

        initAsceTwoData = getAsceDataTwo(latitude, longitude, 'III', site, 'rfemCall')
        initPeriodsTwoData = initAsceTwoData['twoPeriodDesignSpectrumPeriods']
        initOrdinatesTwoData = initAsceTwoData['twoPeriodDesignSpectrumOrdinates']

        fig_3 = px.line(x = initPeriodsTwoData, y = initOrdinatesTwoData, labels = {'x': 'Period (s)', 'y': 'Ground Motion (g)'}, title = "Two Period Spectrum")

        fig_3.update_layout(
            xaxis = dict(
                tickmode = 'linear',
                tick0 = 0.5,
                dtick = 0.75,

            ),
            xaxis_range=[0,5],
        )

        initAsceTwoDataMCEr = getAsceDataTwoMCEr(latitude, longitude, 'III', site, 'rfemCall')
        initPeriodsTwoDataMCEr = initAsceTwoDataMCEr['twoPeriodMCErSpectrumPeriods']
        initOrdinatesTwoDataMCEr = initAsceTwoDataMCEr['twoPeriodMCErSpectrumOrdinates']

        fig_4 = px.line(x = initPeriodsTwoDataMCEr, y = initOrdinatesTwoDataMCEr, labels = {'x': 'Period (s)', 'y': 'Ground Motion (g)'}, title = "Two Period MCEr Spectrum")

        fig_4.update_layout(
            xaxis = dict(
                tickmode = 'linear',
                tick0 = 0.5,
                dtick = 0.75,

            ),
            xaxis_range=[0,5],
        )

    multiColumn, multiMcerColumn = st.columns(2)
    twoDataColumn, twoDataMcerColumn = st.columns(2)

    with multiColumn:
        st.plotly_chart(fig_1)
        send_1 = st.button("Send Multi Period Spectrum to RFEM6")

    with multiMcerColumn:
        st.plotly_chart(fig_2)
        send_2 = st.button("Send Multi Period MCEr to RFEM6")

    with twoDataColumn:
        st.plotly_chart(fig_3)
        send_3 = st.button("Send Two Data Spectrum to RFEM6")

    with twoDataMcerColumn:
        st.plotly_chart(fig_4)
        send_4 = st.button("Send Two Data MCEr to RFEM6")


    if send_1:
        with multiColumn:
            with st.spinner("Wait for it..."):
                if Model.clientModel is None:
                    Model(True, "USGS_Spectrum.rf6")

                Model.clientModel.service.begin_modification()

                if GetAddonStatus(Model.clientModel, AddOn.spectral_active) == False:
                    try:
                        SetAddonStatus(Model.clientModel, AddOn.spectral_active, True)
                    except:
                        with multiColumn:
                            st.error('There is an occured during the process of accessing Response Spectrum Analysis AddOn. Please check if you have valid license.', icon="🚨")

                multiSpectrumData = []
                for i, j in zip(initPeriodsMulti.to_list(), initOrdinatesMulti.to_list()):
                    multiSpectrumData.append([i, j])

                ResponseSpectrum.UserDefinedGFactor((FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_RESPONSE_SPECTRUM, 0)), user_defined_spectrum=multiSpectrumData)

                Model.clientModel.service.finish_modification()
                Model.clientModel.service.close_connection()
                st.success('Succesful Transer!')

    if send_2:
        with multiMcerColumn:
            with st.spinner("Wait for it..."):
                if Model.clientModel is None:
                    Model(True, "USGS_Spectrum.rf6")

                Model.clientModel.service.begin_modification()

                if GetAddonStatus(Model.clientModel, AddOn.spectral_active) == False:
                    try:
                        SetAddonStatus(Model.clientModel, AddOn.spectral_active, True)
                    except:
                        with multiMcerColumn:
                            st.error('There is an occured during the process of accessing Response Spectrum Analysis AddOn. Please check if you have valid license.', icon="🚨")

                multiSpectrumMcerData = []
                for i, j in zip(initPeriodsMultiMCEr.to_list(), initOrdinatesMultiMCEr.to_list()):
                    multiSpectrumMcerData.append([i, j])

                ResponseSpectrum.UserDefinedGFactor((FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_RESPONSE_SPECTRUM, 0)), user_defined_spectrum=multiSpectrumMcerData)

                Model.clientModel.service.finish_modification()
                Model.clientModel.service.close_connection()
                st.success('Succesful Transer!')

    if send_3:
        with twoDataColumn:
            with st.spinner("Wait for it..."):
                if Model.clientModel is None:
                    Model(True, "USGS_Spectrum.rf6")

                Model.clientModel.service.begin_modification()

                if GetAddonStatus(Model.clientModel, AddOn.spectral_active) == False:
                    try:
                        SetAddonStatus(Model.clientModel, AddOn.spectral_active, True)
                    except:
                        with twoDataColumn:
                            st.error('There is an occured during the process of accessing Response Spectrum Analysis AddOn. Please check if you have valid license.', icon="🚨")

                twoDataData = []
                for i, j in zip(initPeriodsTwoData.to_list(), initOrdinatesTwoData.to_list()):
                    twoDataData.append([i, j])

                ResponseSpectrum.UserDefinedGFactor((FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_RESPONSE_SPECTRUM, 0)), user_defined_spectrum=twoDataData)

                Model.clientModel.service.finish_modification()
                Model.clientModel.service.close_connection()
                st.success('Succesful Transer!')

    if send_4:
        with twoDataMcerColumn:
            with st.spinner("Wait for it..."):
                if Model.clientModel is None:
                    Model(True, "USGS_Spectrum.rf6")

                Model.clientModel.service.begin_modification()

                if GetAddonStatus(Model.clientModel, AddOn.spectral_active) == False:
                    try:
                        SetAddonStatus(Model.clientModel, AddOn.spectral_active, True)
                    except:
                        with twoDataMcerColumn:
                            st.error('There is an occured during the process of accessing Response Spectrum Analysis AddOn. Please check if you have valid license.', icon="🚨")

                twoDataMcerData = []
                for i, j in zip(initPeriodsTwoDataMCEr.to_list(), initOrdinatesTwoDataMCEr.to_list()):
                    twoDataMcerData.append([i, j])

                ResponseSpectrum.UserDefinedGFactor((FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_RESPONSE_SPECTRUM, 0)), user_defined_spectrum=twoDataMcerData)

                Model.clientModel.service.finish_modification()
                Model.clientModel.service.close_connection()
                st.success('Succesful Transer!')

