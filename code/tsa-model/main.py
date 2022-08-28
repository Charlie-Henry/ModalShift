from datetime import date, timedelta, datetime
import os
import pytz

import statsmodels.api as sm
import pandas as pd
import tweepy
import plotly.graph_objects as go

TW_API_KEY = os.getenv("TW_API_KEY")
TW_API_Key_Secret = os.getenv("TW_API_Key_Secret")
TW_ACCESS_TOKEN = os.getenv("TW_ACCESS_TOKEN")
TW_ACCESS_TOKEN_SECRET = os.getenv("TW_ACCESS_TOKEN_SECRET")

DATA_URL = "https://raw.githubusercontent.com/mikelor/TsaThroughput/main/data/processed/tsa/throughput/TsaThroughput.AUS.csv"
ARMA_PARAMS = (2, 1, 2)
SEASONAL_PARAMS = (0, 1, 2, 7)


def twitter_connection():
    twitter_auth_keys = {
        "consumer_key": TW_API_KEY,
        "consumer_secret": TW_API_Key_Secret,
        "access_token": TW_ACCESS_TOKEN,
        "access_token_secret": TW_ACCESS_TOKEN_SECRET,
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys["consumer_key"], twitter_auth_keys["consumer_secret"]
    )
    auth.set_access_token(
        twitter_auth_keys["access_token"], twitter_auth_keys["access_token_secret"]
    )
    api = tweepy.API(auth)

    return api


def clean_data(df):
    df["Passengers"] = (
        df["AUS AUS01"]
        + df["AUS AUS02"]
        + df["AUS AUS02E"]
        + df["AUS AUS02W"]
        + df["AUS AUS03"]
    )
    df.index = pd.DatetimeIndex(df.index)
    all_days = pd.date_range(df.index.min(), df.index.max(), freq="D")
    df = df.reindex(all_days)
    y = df[["Passengers"]]
    y["Passengers"] = y["Passengers"].fillna(0)

    return y


def train_model(y):
    mod = sm.tsa.statespace.SARIMAX(
        y,
        order=ARMA_PARAMS,
        seasonal_order=SEASONAL_PARAMS,
        enforce_stationarity=True,
        enforce_invertibility=False,
    )
    results = mod.fit(disp=0)
    fcast = results.get_forecast(steps=30).summary_frame()
    today_cast = fcast.loc[
        date.strftime(datetime.now(tz=pytz.timezone("US/Central")), format="%Y-%m-%d")
    ]

    return today_cast


def forecast_plot(today_val, y):
    y = y[y.index < date.strftime(date.today() - timedelta(90), format="%Y-%m-%d")]

    lowest = y["Passengers"].median() - (2 * y["Passengers"].std())
    highest = y["Passengers"].median() + (2 * y["Passengers"].std())

    v_low = y["Passengers"].median() - (1 * y["Passengers"].std())
    v_high = y["Passengers"].median() + (1 * y["Passengers"].std())

    low = y["Passengers"].median() - (0.5 * y["Passengers"].std())
    high = y["Passengers"].median() + (0.5 * y["Passengers"].std())

    if today_val <= v_low:
        title_text = "Below normal wait times expected today"
        tweet = "AUS Airport is expected to be not busy today."

    elif today_val <= low:
        title_text = "Below normal wait times expected today"
        tweet = "AUS Airport is expected to be not busy today."

    elif today_val > low and today_val <= high:
        title_text = "Relatively normal wait times expected today"
        tweet = "AUS Airport's wait times is expected to be normal today."

    elif today_val > high:
        title_text = "Above normal wait times expected today"
        tweet = "AUS Airport is expected to be busy today."

    elif today_val > high:
        title_text = "Long wait times expected today"
        tweet = "AUS Airport is expected to be very busy today."

    fig = go.Figure(
        go.Indicator(
            mode="gauge",
            value=today_val,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": title_text},
            gauge={
                "axis": {"range": [lowest, highest], "visible": False},
                "bar": {"color": "black"},
                "steps": [
                    {"range": [lowest, v_low], "color": "#1a9641"},
                    {"range": [v_low, low], "color": "#a6d96a"},
                    {"range": [low, high], "color": "#ffffbf"},
                    {"range": [high, v_high], "color": "#fdae61"},
                    {"range": [v_high, highest], "color": "#d7191c"},
                ],
            },
        )
    )
    fig.write_image("/tmp/tsa_plot.png")

    return tweet


def main(event, context):
    tw_api = twitter_connection()

    df = pd.read_csv(DATA_URL)
    df = df.pivot_table(index="Date", aggfunc="sum")
    y = clean_data(df)

    today_cast = train_model(y)

    tweet = forecast_plot(today_cast["mean"], y)

    media = tw_api.media_upload("/tmp/tsa_plot.png")
    post_result = tw_api.update_status(status=tweet, media_ids=[media.media_id])


if __name__ == "__main__":
    main()
