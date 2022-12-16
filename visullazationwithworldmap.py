import plotly.express as px 
import pandas as pd 
gapminder = pd.read_csv("finaldataset.csv")
fig = px.choropleth(gapminder,
                   locations = "iso_code",
                   color = "daily_vaccinations",
                   scope = "world",
                   animation_frame ="date",
                   hover_name = "country",
                   color_continuous_scale=px.colors.sequential.Plasma)
fig.show()
#SMALL CODE BUT İT MAKES DATA MUCH MORE UNDERSTANDABLE 
