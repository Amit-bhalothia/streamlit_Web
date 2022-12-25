import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='Startup analysis')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year


# data cleaning
# df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')


def load_overall_details():
    st.title('Overall Analysis')
    # total invested amount
    total = round(df['amount'].sum())

    # maximum infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

    # average ticket size
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())

    # total funded startups
    num_startups = df['startup'].nunique()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')
    with col3:
        st.metric('Average', str(avg_funding) + ' Cr')
    with col4:
        st.metric('Funded Startups', num_startups)

    st.header('Month on Month Graph')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig6, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig6)


def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investment')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head()
        st.subheader('Biggest Investment')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sector wise Investment')
        fig1, ax = plt.subplots()
        ax.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        stage_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader('Stage wise Investment')
        fig2, ax = plt.subplots()
        ax.pie(stage_series, labels=stage_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)

    with col4:
        city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('City wise Investment')
        fig3, ax = plt.subplots()
        ax.pie(city_series, labels=city_series.index, autopct="%0.01f%%")
        st.pyplot(fig3)

    col5, col6 = st.columns(2)
    with col5:
        year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader('Year On Year Investment')
        fig4, ax1 = plt.subplots()
        ax1.plot(year_series.index, year_series.values)
        st.pyplot(fig4)


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('select one', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    # btn0 = st.sidebar.button('Find Startup Details')
    # if btn0:
    load_overall_details()

elif option == 'Startup':
    st.sidebar.selectbox('select startup', sorted(list(df['startup'].unique())))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('Startup Analysis')
else:
    selected_investor = st.sidebar.selectbox('select Investors', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
    # st.title('Investor Analysis')
