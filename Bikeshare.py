import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': r'G:\VDU\Udacity\chicago.csv',
              'new york city': r'G:\VDU\Udacity\new_york_city.csv',
              'washington': r'G:\VDU\Udacity\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("1.Chicago\n2.New York City\n3.Washington\nName a city: ").lower()
        if city not in CITY_DATA.keys():
            print("please enter one of the three choices")
        if city in CITY_DATA.keys():
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("choose one of the first six months: ").lower()
        if (month=="january") or (month=="february") or (month=="march") or (month=="may") or (month=="june") or (month=="april"):
            print("Great!")
            break
        if (month!="january") or (month!="february") or (month!="march") or (month!="may") or (month!="june") or (month!="april"):
            print("Wrong answer!")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekdays=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    day=input("filter by day: ").title()
    while True:
        if day not in weekdays:
            day=input("please enter a week day: ").title()
        if day in weekdays:
            print("Great!")
            break



    print('-'*40)
    return city, month, day

""""""
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
    if city != all:
        df = pd.read_csv(CITY_DATA[city])
    if month != all:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['Hour'] = df['Start Time'].dt.hour
        months = ['january', 'february', 'march', 'april', 'may', 'june',"all"]
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != all:
        df['day_of_week'] = df['Start Time'].dt.day_name()
        df = df[df['day_of_week'] == day.title()]
    return df

def show_me(df):
    l=input("Do you want to see the data: ")
    if l=="yes":
        show = input("Do you want to see the first five rows: ").lower()
        while True:
            k = ["yes", "no"]
            while show not in k:
                show = input("please, do you want see the first 5 rows?!: ").lower()
            while show == "yes":
                print(df.head(5))
                show = input("Again, do you want to show the first five rows of the data: ").lower()
            if show == "no":
                print("Thank you for your time")
                break
    if l=="no":
        print("Thank you for your time")



    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print("Most common month ",df["month"].mode()[0])
    # TO DO: display the most common day of week
    print("Most common day ",df["day_of_week"].mode()[0])
    # TO DO: display the most common start hour
    print("Most common Hour ",df["Hour"].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print("most common start station is " ,df["Start Station"].mode()[0])
    # TO DO: display most commonly used end station
    print("Most common end station is " ,df["End Station"].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    print("The most common trip in numbers was ",
          df[df.duplicated(['Start Station', 'End Station'])].count().mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    sum=df["End Time"]-df["Start Time"]
    print("Travel duration is ",sum.sum())
    # TO DO: display mean travel time
    a=df["End Time"]-df["Start Time"]
    print("average ",a.mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return(df)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print(df["User Type"].value_counts())
    # TO DO: Display counts of gender
    if "Gender" in df:
        print(df["Gender"].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return(df)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_me(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

