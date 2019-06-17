import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
months = ['January', 'February',
            'March', 'April',
            'May', 'June', 'All']
days = ['All', 'Monday', 'Tuesday',
    'Wednesday', 'Thursday', 'Friday',
    'Saturday', 'Sunday']

def get_filters():

    print('\n\nHello! Let\'s explore some US bikeshare data! Make sure all your entries begin with a capital letter.')

    while True:
        city = input(str('\nWhich city would you like to see data on?\n'
        'New York City, Chicago, or Washington?\n '))
        if city in ('Washington', 'Chicago', 'New York City'):
            break
        else:
            print('\n\n City not found. Please try again.\n')

    while True:
        month = input(str('\nWould you like to search by one of the following months?\nJanuary, February, March, April, May, June, or all?\n '))
        if month in months:
            break
        else:
            print ('Invalid month. Please try again.\n')

    while True:
        day = input(str('\nWould you like to search by one of the following days?\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all of them?\n' ))
        if day in days:
            break
        else:
            print ('Invalid day. Please try again.\n')
    return str(city),str(month),str(day)
    print('-')*40
        

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

    # load data file into a dataframe
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday
    df['hour']=df['Start Time'].dt.hour
   
    if month!='All':
        month=months.index(month)+1
        df=df[df['month']==month]
        
    if day !='All':
        day=days.index(day)+1
        df=df[df['day']==day]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", months[common_month])

    # display the most common day of week
    common_day = df['day'].value_counts().idxmax()
    print("The most common day of week is :", days[common_day])

    # display the most common start hour

    common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print("Most common Start Station:"+ " " + common_start_station + "\n")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()
    print("Most common End Station:"+" "+ common_end_station +"\n")

    # TO DO: display most frequent combination of start station and end station trip
    print( "Best Start Time CombinationL"+" "+ common_start_station +"--&--"+ common_end_station+ "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time:"+" "+ str(total_travel_time) + "hours \n")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Average Travel Time:"+" "+ str(mean_travel_time) + "hours \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("User Type Count:"+" "+ str(count_user_type) +"\n")


    # TO DO: Display counts of gender

    count_gender = df['Gender'].value_counts()
    print('Gender Count:'+" "+ str(count_gender) + "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    recent_birth_year = df['Birth Year'].max()


    common_birth_year = df['Birth Year'].mode()

    print("The most recent year of birth is:" + " "+ str(recent_birth_year) + " & " + "the most common year of birth is:"+" "+str(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter Yes or No.\n')
        if restart.lower() != 'Yes':
            break

if __name__ == "__main__":
    main()
#I am adding this line for making changes for the git project



