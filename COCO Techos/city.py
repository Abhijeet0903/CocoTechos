import random
from collections import defaultdict

# Function to generate random visit entries
def generate_data(cities, num_entries_per_city):
    data = []
    for city in cities:
        for _ in range(num_entries_per_city):
            user_id = random.randint(1, 30)
            time_of_day = random.choice(['morning', 'noon', 'evening', 'night'])
            time_spent_minutes = random.randint(5, 120)
            data.append({'city': city, 'user_id': user_id, 'time_of_day': time_of_day, 'time_spent_minutes': time_spent_minutes})
    return data

# Function to analyze the data
def analyze_data(data):
    # 1. Time of day with the most number of unique users
    time_of_day_counts = defaultdict(int)
    
    # 2. City with the most users at each time of day
    city_time_counts = defaultdict(lambda: defaultdict(int))

    for entry in data:
        time_of_day_counts[entry['time_of_day']] += 1
        city_time_counts[entry['time_of_day']][entry['city']] += 1

    most_users_time_of_day = max(time_of_day_counts, key=time_of_day_counts.get)

    most_users_city_time = {}
    for time_of_day, cities in city_time_counts.items():
        most_users_city = max(cities, key=cities.get)
        most_users_city_time[time_of_day] = f"{most_users_city} {cities[most_users_city]} users"

    return most_users_time_of_day, most_users_city_time

# Define cities and number of entries per city
cities = ['Pune', 'New York', 'Tokyo', 'London', 'Sydney']
num_entries_per_city = 100

# Generate data
web_traffic_data = generate_data(cities, num_entries_per_city)

# Analyze data
most_users_time_of_day, most_users_city_time = analyze_data(web_traffic_data)

# Output results
print(f"1. Time of day with the most number of unique users: {most_users_time_of_day}")
print("2. City with the most users at each time of day:")
for time_of_day, result in most_users_city_time.items():
    print(f"{time_of_day.capitalize()}: {result}")
