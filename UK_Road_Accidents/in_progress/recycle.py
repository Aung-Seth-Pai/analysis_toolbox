# # get address for each coordinate
# # re-run this cell if ConnectionTimeoutError
# # it will start from last checkpoint of address column
# # bins = np.arange(0, geo_df.shape[0]-1, 100) # bin indices for geometry data

# # get the starting index of missing addresses and start creating bins from there
# bins = np.arange(geo_df[geo_df.address==-1].index[0], geo_df.shape[0]-1, 100)
# print(f"starting from {bins[0]}")

# for i in range(len(bins)):
#     if i+1 < len(bins): # as long as index doesn't exceed the end of bins
        
#         current_bin = geo_df.geometry[(bins[i]):(bins[i+1])] # get coordinate points within bin range
        
#         current_address = gpd.tools.reverse_geocode(current_bin.values, timeout=4).address # lookup address
#         current_address.index = current_bin.index # reset to current index of geo_df
        
#         geo_df.loc[current_address.index,"address"] = current_address # save address data
#         print(f"{bins[i]}, {bins[i+1]}")

#     else:
#         current_bin = geo_df.geometry[bins[i]:]
        
#         current_address = gpd.tools.reverse_geocode(current_bin.values, timeout=4).address # lookup address
#         current_address.index = current_bin.index # reset to current index of geo_df
        
#         geo_df.loc[current_address.index,"address"] = current_address # save address data
#         print(f"{bins[i]} done")
    
#         # save to file
#         geo_df.to_file("data/geo_df.geojson", driver='GeoJSON') # export and save geo_df

*****************************************# severity x casuality # ***********************************************

data = accidents[accidents.number_of_casualties<20] # remove outlier (41 casualty)
color = np.array(['', 'magenta', 'yellow', 'red']) # most severe to least severe

# calculate marker density
xy = np.vstack([data.accident_severity, data.number_of_casualties])
density = gaussian_kde(xy)(xy)

fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(data.accident_severity, data.number_of_casualties, s=density*20, \
           c=color[np.array(data.accident_severity)])

plt.xticks([1,2,3])
plt.yticks(np.arange(0,18,3))
plt.xlim(0.5,3.5)
# plt.grid(visible=True, axis='y', linestyle="-", linewidth=0.5)
plt.title("Relation Between Accident Severity and Number of Casualties");
plt.xlabel("Accident Severity")
plt.ylabel("Number of Casualties");

num_accidents_by_severity = data.accident_severity.value_counts()
percent_accidents_by_severity = round(100*(num_accidents_by_severity/num_accidents_by_severity.sum()),2)

for i in range(1,4):
    ax.text(i-0.1 , 12, f"{num_accidents_by_severity[i]}")
    ax.text(i-0.1 , 11, f"({percent_accidents_by_severity[i]}%)")
    ax.text(0.6, 13, "Total Number of Accidents for each severity category");

plt.tight_layout()

*************************** # animated heatmap # *******************************************************
import folium
from folium import plugins

data = geo_df[geo_df.is_major_accident==1] # filter data for major accidents

# get UK from OpenStreetMap 
uk_map = folium.Map(location=[51.5, 0.127], zoom_start=8, tiles="OpenStreetMap") 

# heat map animation hourly 
data.loc[:, "hour"] = data.hour.astype(int)
heat_data = [[[row["latitude"],row["longitude"]] for index, row in data[data["hour"] == i].iterrows()] for i in range(0,24)]
heat_time = plugins.HeatMapWithTime(heat_data,auto_play=True,max_opacity=0.8)
heat_time.add_to(uk_map);

print(uk_map)
*************************************************************************************************