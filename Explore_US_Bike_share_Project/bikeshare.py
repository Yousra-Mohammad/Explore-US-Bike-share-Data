import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! ')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input("Which City would u like to see data from ?(chicago, new york city or washington) \n ").lower()
    while city not in ['chicago', 'new york city', 'washington'] :
        print("Invalid city plz try again ")
        city= input("Which City would u like to see data from ?(chicago, new york city or washington) \n ").lower()
    


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month would u like to see data for ? (all, january, february, ... , june) \n").lower()
    while month not in ['january', 'february', 'march' ,'april' ,'may', 'june', 'all']:
       print("invald month plz try again")
       month = input("Which month would u like to see data for ? (all, january, february, ... , june) \n ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =input("Which day would u like to see data for ?( Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday or all) \n").lower()  
    Days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    while day not in Days:
        print ("Invaild day plz try again ")
        day =input("Which day would u like to see data for ?( Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday or all) \n").lower()
            
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.day_name()
    df['hour']= df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march' ,'april' ,'may', 'june']
        month = months.index(month)+1
        df = df[df['month']==month]
        
    if day != 'all':
        df=df[df['day']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print(most_common_month)
    print(most_common_day)
    print(most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    most_commonly_end_station = df['End Station'].mode()[0] 

    # TO DO: display most frequent combination of start station and end station trip
    trip=[]
    df['trip']=df['Start Station']+"to"+df['End Station']
    '''df['trip']=zip(df['Start Station'],df['End Station'])'''
    most_common_trip =df['trip'].mode()[0]
    print(most_commonly_start_station)
    print(most_commonly_end_station)
    print(most_common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    # TO DO: display mean travel time
    Average_travel_time = df['Trip Duration'].mean()
    print(Total_travel_time)
    print(Average_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Counts_of_users_type= df['User Type'].value_counts()
    print(Counts_of_users_type)
    print()
    # TO DO: Display counts of gender
    try: 
         Counts_of_gender=df['Gender'].value_counts().to_frame()
         print(Counts_of_gender)
         # TO DO: Display earliest, most recent, and most common year of birth
         Earliest_year_of_birth = df['Birth Year'].min()
         print(Earliest_year_of_birth)
         print()   
         Most_recent_year_of_birth = df['Birth Year'].max()
         print(Most_recent_year_of_birth)
         print()
         Most_common_year_of_birth = df['Birth Year'].mode()[0]
         print(Most_common_year_of_birth)
         print()
    except :
         print("This data is not available for Washington")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def Display_Raw_Data(df):
    View_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? \n").lower()
    while View_data == 'yes' :
        print(df.sample(5))
        View_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? \n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Display_Raw_Data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
             
           break


if __name__ == "__main__":
	main()
