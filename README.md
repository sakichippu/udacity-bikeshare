# Udacity DAND : Explore US Bikeshare Data

## Project Objective and Importance
This Python code imports the bikeshare data for three major US cities—Chicago, New York, and Washington—and provides descriptive statistics about the data. It takes in raw input from the user to create an interactive experience. Users can customize what kind of data they want to see.

Such analysis is useful not only for bikeshare companies that seek to analyze their bike share usage patterns but also for entrepreneurs who want to gain insight into the "sharing-economy" business which have become increasingly commonplace over the past decade.

## Required Files
You will need the following three city dataset files:
- chicago.csv
- new_york_city.csv
- washington_csv

Along with the Python script:
- bikeshare_2.py

## Project Requirements
Solicit user input regarding:
- Which city they would like to analyze
- Whether they would like to filter the data by month, day, both, or not at all

Provide the following bikeshare statistics:
- **Popular times of travel**
  - most common month
  - most common day of week
  - most common hour of day
- **Popular stations and trip**
  - most common start station
  - most common end station
  - most common trip from start to end
- **Trip duration**
  - total travel time
  - average travel time
- **User info**
  - counts of each user type (customer or subscriber)
  - counts of each gender (male or female)
  - earliest, most recent, and most common year of birth
 
 In addition:
 - Be able to handle typos and unexpected inputs
 - Be able to provide the raw data when asked by user
 
 ## Usage
 Open up your terminal, `cd` to the directory that contains all of the required files, and type:
 `python3 bikeshare_2.py`
 
 Example output (for analyzing bikeshare data on New York, May, and all days of the week):
 
 ```
Fujita-no-Air:bikeshare-2 fujitasaki$ python3 bikeshare_2.py 
Hello! Let's explore some US bikeshare data!
Would you like to see data for Chicago, New York, or Washington?New York
Which month - January, February, March, April, May, or June? Type 'All' if no month filter.May
Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Type 'All' if no day filter.All
----------------------------------------

Calculating The Most Frequent Times of Travel...

Most Common Month: 5
Most Common Day of Week: Wednesday
Most Common Hour: 17
----------------------------------------

Calculating The Most Popular Stations and Trip...

Most Common Start Station: Pershing Square North
Most Common End Station: Pershing Square North
Most Common Start-End Station Combination: Pershing Square North and Pershing Square North
----------------------------------------

Calculating Trip Duration...

Total Travel Time (seconds): 61988431
Mean Travel Time (seconds): 924.993374617623
----------------------------------------

Calculating User Type...

Subscriber    58649
Customer       8366
Name: User Type, dtype: int64
----------------------------------------

Calculating User Gender and Birth Year...

There are some missing values...but we'll ignore those.
Male      44051
Female    15202
Name: Gender, dtype: int64
Earlist year of birth: 1886
Most recent year of birth: 2001
Most common year of birth: 1989
----------------------------------------
Would you like to see a couple of raw data used to compute the above statistics? Type 'Y' or 'N'. (Expand your window to see the data unabbreviated.)Y

Displaying some raw data...

    Unnamed: 0          Start Time             End Time  Trip Duration                Start Station         End Station   User Type  Gender  Birth Year  month day_of_week  hour
1      4096714 2017-05-11 15:30:11  2017-05-11 15:41:43            692      Lexington Ave & E 63 St     1 Ave & E 78 St  Subscriber    Male      1981.0      5    Thursday    15
3      3945638 2017-05-08 19:47:18  2017-05-08 19:59:01            703        Barrow St & Hudson St     W 20 St & 8 Ave  Subscriber  Female      1986.0      5      Monday    19
18     4733837 2017-05-24 08:53:32  2017-05-24 09:04:30            658  Central Park West & W 76 St  E 72 St & York Ave  Subscriber    Male      1979.0      5   Wednesday     8
32     3676202 2017-05-02 21:43:28  2017-05-02 22:29:15           2746                Old Fulton St  Broadway & E 14 St    Customer     NaN         NaN      5     Tuesday    21
40     3873453 2017-05-07 10:50:22  2017-05-07 10:56:44            382       Perry St & Bleecker St     8 Ave & W 31 St  Subscriber    Male      1993.0      5      Sunday    10
----------------------------------------

Would you like to restart? Enter yes or no.
no

 ```
 
