# Selin

Assigned topic: Urban Expansion

Team Members:
* Selin	Hekimgil (sh6104@nyu.edu)

## Introduction
In the introduction section of the [Atlas of Global Expansion](http://atlasofurbanexpansion.org/data) data source, a city is stated to be "a settlement of 100,000 people or more". The metrics of a sample of 200 cities is given as a dataset, out of the 4,245 identified cities in the world.
Urban expansion refers to the incerase in built-up area of a city, which in turn affects other metrics such as population, density, and urban planning. Thus, rapid growth of cities must be tracked in order to make certain accommodations.

### Problem Statement
We currently have data on urban expansion levels, making it possible to monitor growth. The next step would be to detect certain patterns based on this growth in order to then make accommodations. Given the limited time and limited knowledge of this topic, a simple regression approach was taken and applied to the regions that are presented within the dataset in order to find such patterns.

Geographical region as well as the level of development of a region might affect urban expansion. The United Nations has already defined two "mega-regions", and sub-regions within them. Intuitively, the developed countries of the world are expected to adjust accordingly to population growth and urban expansion. The purpose of this project is to analyze whether this holds true, and if not, what conclusion can be made from it.

## Data & Analysis
The dataset that was used was 'Areas_and_Densities_Table_1.csv', found [on this website](http://atlasofurbanexpansion.org/data) (Areas and Densities .csv link). This dataset depicts 200 cities, where each condition is given from 3 different time periods in order to track change.

The dataset looked like this:
| City Name | Country | Region | CBD Location | ... | Added Area: Inclusion (Annual Change) |
| --- | --- | --- | --- | --- | --- |
| Accra | Ghana | Sub-Saharan Africa | 5.615 | ... | 18% |
| Addis Ababa |	Ethiopia | Sub-Saharan Africa | 9.001 | ... | 10% |
| Ahmedabad |	India | South and Central Asia | 23.037 | ... | 11% |
| ⋮ | ⋮ | ⋮ | ⋮ | ... | ⋮ |
| Zwolle | Netherlands | Europe and Japan | 52.513 | ... | 12% |

Certain initializations and cleansing was performed. There include: 
* dropping the NaN values after row 200 as only 200 cities are given
* categorizing columns (ex. columns 1-3: name, country, region; columns 4-5: CBD location (latitude, longitude))
* categorizing the 8 regions, as defined by the United Nations

Below is a world map that was created using the 'Latitude' and 'Longitude' columns of the dataset.

<img width="390" alt="Screen Shot 2022-11-07 at 8 46 17 AM" src="https://user-images.githubusercontent.com/108428198/200349233-4fca8032-3a41-4b05-bc91-d58c067dfa21.png">

This validates the manipulated DataFrame as this map resembles the one given [here](http://atlasofurbanexpansion.org/). 

Next, the data was divided based on regions and analyzed. The regions are:
* Sub-Saharan Africa (18 cities)
* South and Central Asia (32 cities)
* Western Asia and North Africa (15 cities)
* East Asia and the Pacific (42 cities)
* Europe and Japan (34 cities)
* Land-Rich Developed Countries (18 cities)
* Southeast Asia (15 cities)
* Latin America and the Caribbean (26 cities)

As a form of analysis, the population changes of each city was plotted against the urban area changes, and simple regression was performed. Below are the results of each region, from strongest relationship to least strongest, where the x-axis represents population change and the y-axis represents urban area change.

### Southeast Asia
![image](https://user-images.githubusercontent.com/108428198/200358899-9d05bb6e-77cb-46a2-8ecc-50ec114963d7.png)
### Western Asia and North Africa
![image](https://user-images.githubusercontent.com/108428198/200358247-de8fe83d-c3b6-4382-8c70-b57d4197edfe.png)
### Land-Rich Developed Countries
![image](https://user-images.githubusercontent.com/108428198/200358575-727e5cba-2e25-4b87-beee-63a53e38b2bf.png)
### East Asia and the Pacific
![image](https://user-images.githubusercontent.com/108428198/200358333-69853275-b5e3-431c-a7f3-77275a8a0ed3.png)
### South and Central Asia
![image](https://user-images.githubusercontent.com/108428198/200358146-387f9c9a-2990-45f0-ba80-7922e2efd361.png)
### Europe and Japan
![image](https://user-images.githubusercontent.com/108428198/200358500-3c3a49eb-1794-413c-9989-81bd3e6f64db.png)
### Sub-Saharan Africa
![image](https://user-images.githubusercontent.com/108428198/200358005-8a421d67-12e8-40ae-955b-06849f59c24d.png)
### Latin America and the Caribbean
![image](https://user-images.githubusercontent.com/108428198/200358743-6f447515-0ac0-45b0-a5e8-c89ff4aaa57e.png)

## Results
The main idea was to track urban expansion by region. The goal of this simple regression analysis was to see if geographic location affects the ability to adjust to population growth accordingly. The success level of this adjustment greatly affects the function of a city.

It was found that Southeast Asia had the strongest relationship between population growth of its cities and their urban area changes, whereas Latin America and the Caribbean had the weakest coefficient of determination. This means that in Southeast Asia, as the population grows, the cities are able to expand as well whereas in Latin America and the Caribbean, expansion is not as drastic.

As stated in the **problem statement**, it was expected for Land-Rich Developed Countries as well as Europe and Japan to come out on top since they are under the mega-region category of "more developed countries". Land-Rich Developed Countries comes in at third place, while Europe and Japan is in sixth place. A possible explanation for this is the physical ability, or rather the inability, to expand cities in these regions. Looking at geographical location, Land-Rich Developed Countries are capable of expansion whereas the Europe and Japan region does not have the physical space to do so.

This conclusion can lead to different questions, such as how this affects the functioning of cities in these regions. Is it better to be more densely populated? Will this be a point of concern in the future?

## Discussion
Most of the time was spent on researching urban expansion: its causes, effects, and importance. Given the limited amount of time, only 2 columns from the dataset were used, and the decision of which column to choose came from the results of the mentioned research that was done.

If given more time to put into this project, the goals of it would be greater. One of which would be to include different parameters in analysis. Another goal would be to create a prediction model based on the analysis of these parameters. A prediction model with multiple parameters would be more effective than simple linear regression when foreseeing these growth and expansion patterns.

Another disparity that this cide has from one that could have resulted, given more time, is the variable names and uses. During the data initialization, several categories were created yet were not able to be put into full use. Druing the regional analysis section as well, the code was a bit brute forced, with columns still having the name of 'Unnamed: 11' and 'Unnamed: 19' as opposed to their proper titles, 'population changes' and 'urban area changes'.

These shortcomings can be traced back to limited time, limited knowledge, and individual approach. Nevertheless, it was a pleasure learning more about this topic and getting the chance to work with a dataset that has the potential to lead to useful discoveries!
