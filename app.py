import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('data:im  age/jpeg;base64,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')

# skleaton code
user_menu =st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_lsit(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country =='Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country =='Overall':
        st.title("Medal Tally in " + str(selected_year) + " " + "Olympics")
    if selected_year == 'Overall' and selected_country !='Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country !='Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")


    st.table(medal_tally) # table/dataframe

# overall analysis
if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations over the Years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Events over the Years")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x="Edition", y="Name")
    st.title("Athletes over the Years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x= df.drop_duplicates(['Year','Sport','Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title("Most succe  ssful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':
    st.sidebar.title('Country-wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox('Select a Country',country_list)
    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year",y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df )

if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age")

    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

#    st.title('Height Vs Weight')
#    selected_sport = st.selectbox('Select a Sport', sport_list)
#    temp_df = helper.weight_v_height(df, selected_sport)
#    fig, ax = plt.subplots()
#    ax = sns.scatterplot(temp_df['Weight'],temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=60)
#    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=650)
    st.plotly_chart(fig)



 # athlete_df['Medal'].fillna('No Medal',inplace=True)
