import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
# count views from each utm source
print(ad_clicks.groupby("utm_source").user_id.count().reset_index())
# new column where True indicates that the ad was clicked otherwise false
ad_clicks["is_click"] = ad_clicks.ad_click_timestamp.isnull()
# how many users clicked on and add by each utm source
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
# generate a pivot table
clicks_pivot = clicks_by_source.pivot(columns="is_click", index="utm_source", values="user_id").reset_index()
print("Pivot table for clicked ads by each utm source\n")
print(clicks_pivot)
print("\n\n")
# new column that shows the percentage of users which clicked the add
clicks_pivot["percent_clicked"] = clicks_pivot.apply(lambda row: row[True]/(row[True]+row[False]), axis=1)
print("Pivot table with percentage of users clicked on an add for each utm source\n")
print(clicks_pivot)
print("\n\n")
print("Table which showcase the different experimental groups\n")
print(ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index())
print("\n\n")
# get the clicks from each experimental group
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
print("Group A count of users who clicked on an ad grouped by day\n")
print(a_clicks.groupby(["day", "is_click"]).user_id.count().reset_index())
print("\n\n")
print("Group B count of users who clicked on an ad grouped by day\n")
print(b_clicks.groupby(["day", "is_click"]).user_id.count().reset_index())