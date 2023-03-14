# Analysis of the UK's Road Accidents in 2020


## Background
I did this project for DataCamp's competition on [reducing the number of high fatality accidents](https://app.datacamp.com/learn/competitions/high-fatality-accidents). There are other competitions available on their website. which are quite interesting with real-world datasets. It's like Kaggle but I think there should be a publicly viewable feedback system after the competition so that participants learn from feedback loops as well.        

## The Data
The data is published by the UK [Department for Transport](https://data.gov.uk/dataset/road-accidents-safety-data). It contains records of accidents in 2020 separated into 3 categories: fatal, serious, and slight. The features include location, time, road characteristics and facilities, weather, light conditions, and etc., related to each accident. They also provided a lookup file to view the meaning of numerical feature labels. Although DfT has vehicle and casualty data, they were not included since the competition limits to the vehicle data only.

## Project Overview
The purpose of this analysis is to find insights and interesting characteristics that could guide the road safety team's efforts and discussions in developing measures to reduce the number of major accidents. According to DataCamp, fatal accidents with 3+ casualties are labelled as major accidents. For this project, I used comparative analysis to look at the different patterns and trends between different locations, times, severity levels, and other variables.

The EDA process is broken down into 4 sections. The following is a summary of insights resulting from the EDA process.

#### TIME
<ul>
    <li> Evening rash hours (around 4-5PM) have the highest number of accidents. </li>
    <li> Accidents tends to be more severe between evening and midnight. </li>
    <li> Fridays have the highest number of accidents and Saturday have the highest percentage of major accidents. </li>
</ul>

#### LOCATION
<ul>
    <li> Accidents are more common in Southern regions of the UK. </li>
    <li> Urban areas have more accidents than rural areas but accidents in rural areas tends to be more severe. </li>
</ul>

#### ROAD CHARACTERISTICS & FACILITIES
<ul>
    <li> Higher speed limits causes more severe accidents in rural areas. </li>
    <li> Single carriageway are the most hazardous type of roads.  </li>
    <li> T or Staggered junctions are the most common place of accidents in urban areas. </li>
    <li> Leaving uncontrolled or using giveway signs are not effective measure of junction control. </li>
    <li> Roadwords, muds and defective road surfaces are the most hazardous road conditions. </li> 
</ul>

#### WEATHER & ENVIRONMENT
<ul>
    <li> In terms of percentage, fog or mist causes more accident followed by high wind conditions in each weather. </li>
    <li> Previous accidents and animals on carriageway tends to cause more severe accidents. </li>
    <li> Lighting could also be one of the reason for high number of major accidents in rural areas. </li>
</ul>

## Conclusion

In general, the safety team should use more resources for traffic control, speed regulation, and emergency response plans for times with the highest number of accidents. For rural areas, it will be safer with more lighting and speed regulation measures. It is also necessary to check if junctions have the appropriate type of junction control. Drivers' awareness of hazards in some weather and special conditions is also necessary.

## Future Work

This analysis, by no means, is complete especially because it only uses 2020 data alone. However, it gave some clue of what might be going on with some trends and patterns that should be carefully observed for other years. For more granular estimates of locations, addresses can be reverse geocoded with Photon's API in geopanda. In order to develop a predictive model, hourly traffic flows will be a good variable to have along with other locational and environmental features.

#### REFERENCES
<ol>
    <li> https://app.datacamp.com/learn/competitions/high-fatality-accidents </li>
    <li> https://data.gov.uk/dataset/road-accidents-safety-data </li>
    <li> www.instituteforgovernment.org.uk/sites/default/files/timeline-lockdown-web.pdf </li>
    <li> www.timeanddate.com/holidays/uk/2020 </li>
    <li> https://coronavirus.data.gov.uk/details/cases?areaType=overview&areaName=United%20Kingdom </li>
    <li> https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1028165/road-traffic-estimates-in-great-britain-2020.pdf </li>
</ol>