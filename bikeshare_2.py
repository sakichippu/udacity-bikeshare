import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago','new york','washington']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?").lower()
        if city in CITIES:
            break
        else:
            print("Sorry! It seems you have a typo or inputted a wrong city. We can only handle Chicago, New York, or Washington. Try again!  ")

    # get user input for month (all, january, february, ... , june)
    month = input("Which month - January, February, March, April, May, or June? Type 'All' if no month filter.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Type 'All' if no day filter.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'All':
        months = ['January','February','March','April','May','June']
        month = months.index(month) + 1 # to make 1=January, 6=June
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    common_month_counts = df['month'].value_counts().max()
    print('Most Common Month is {} and count is {}.'.format(common_month,common_month_counts))

    # display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    common_weekday_counts = df['day_of_week'].value_counts().max()
    print('Most Common Day of Week is {} and count is {}.'.format(common_weekday, common_weekday_counts))

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    common_hour_counts = df['hour'].value_counts().max()
    print('Most Common Hour is {} and count is {}.'.format(common_hour, common_hour_counts))

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    #start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    #common_start_station = df['Start Station'].value_counts()
    print('Most Common Start Station:',common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    #common_end_station = df['End Station'].value_counts()
    print('Most Common End Station:',common_end_station)

    # display most frequent combination of start station and end station trip
    common_start_end_station = df[['Start Station','End Station']].mode().iloc[0] # iloc for integer indexing
    print('Most Common Start-End Station Combination: {} and {}'.format(common_start_end_station[0],common_start_end_station[1]))

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    #start_time = time.time()

    # display total travel time
    total_traveltime = df['Trip Duration'].sum()
    print('Total Travel Time (seconds):',total_traveltime)

    # display mean travel time
    mean_traveltime = df['Trip Duration'].mean()
    print('Mean Travel Time (seconds):',mean_traveltime)

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_type(df):
    """Displays statistics on bikeshare user types."""

    print('\nCalculating User Type...\n')
    #start_time = time.time()

    # Display counts of user types
    user_type_nulls = df['User Type'].isnull().any() # returns True if there are missing values
    if user_type_nulls == True:
        print("There are some missing values...but we'll ignore those.")
    user_types = df['User Type'].value_counts()
    print(user_types)

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def other_user_stats(df):
    """Displays statistics on bikeshare user gender and birth year."""

    print('\nCalculating User Gender and Birth Year...\n')
    #start_time = time.time()

    # Display counts of gender
    gender_nulls = df['Gender'].isnull().any()
    if gender_nulls == True:
        print("There are some missing values...but we'll ignore those.")
    gender = df['Gender'].value_counts()
    print(gender)

    # Display earliest, most recent, and most common year of birth
    birthyr_earliest = df['Birth Year'].min()
    print("Earlist year of birth:",int(birthyr_earliest))

    birthyr_recent = df['Birth Year'].max()
    print("Most recent year of birth:",int(birthyr_recent))

    birthyr_common = df['Birth Year'].mode()[0]
    print("Most common year of birth:",int(birthyr_common))

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def disp_raw_data(df):

    """Displays raw data used to compute statistics."""

    disp_data = input("Would you like to see a couple of raw data used to compute the above statistics? Type 'Y' or 'N'. (Expand your window to see the data unabbreviated.)")
    index = 0
    if disp_data == 'Y':
        print('\nDisplaying some raw data...\n')
        print(df[index:index+5])
        index += 5
    elif disp_data == 'N':
        print("Ok, we won't bombard you with more info.")

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_type(df)
        if city == 'washington':
            print("Sorry, we don't have gender and birth year stats for Washington.")
        else:
            other_user_stats(df)

        disp_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
