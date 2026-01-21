# Creativity: Added per-country statistics (min/max/avg) query and detection of the largest year-to-year drop across countries.

input_year = int(input("Enter the year of interest: "))

max_life_expectancy = float("-inf")
max_country = ""
max_year = None

min_life_expectancy = float("inf")
min_country = ""
min_year = None

input_max_life_expectancy = float("-inf")
input_min_life_expectancy = float("inf")
input_max_country = ""
input_min_country = ""

total_life_expectancy = 0.0
count = 0

country_data = {}

with open('data_analysis/life-expectancy.csv') as data_file:
    next(data_file) 


    for line in data_file:
        parts = line.strip().split(",")
        if len(parts) < 4:
            continue
      
        country = parts[0]
        try:
            year = int(parts[2])
            life_expectancy = float(parts[3].strip())
        except ValueError:
            continue
        
        # store for per-country analysis
        country_data.setdefault(country, []).append((year, life_expectancy))

        # overall min/max
        if life_expectancy > max_life_expectancy:
          max_life_expectancy = life_expectancy
          max_country = country
          max_year = year

        if life_expectancy < min_life_expectancy:
          min_life_expectancy = life_expectancy
          min_country = country
          min_year = year

        # stats for the requested year
        if year == input_year:
          total_life_expectancy += life_expectancy
          count += 1
          if life_expectancy > input_max_life_expectancy:
            input_max_life_expectancy = life_expectancy
            input_max_country = country
          if life_expectancy < input_min_life_expectancy:
            input_min_life_expectancy = life_expectancy
            input_min_country = country

# detect the largest year-to-year drop across all countries
largest_drop = 0.0
largest_drop_country = None
drop_from_year = None
drop_to_year = None

for country, records in country_data.items():
    records.sort(key=lambda x: x[0])  # sort by year
    for i in range(1, len(records)):
        prev_year, prev_life = records[i - 1]
        cur_year, cur_life = records[i]
        drop = prev_life - cur_life
        if drop > largest_drop:
            largest_drop = drop
            largest_drop_country = country
            drop_from_year = prev_year
            drop_to_year = cur_year

print()
if max_year is not None:
    print(f"The overall max life expectancy is: {max_life_expectancy:.3f} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min_life_expectancy:.3f} from {min_country} in {min_year}")
else:
    print("No overall data found.")

print()
print(f"For the year {input_year}:")
if count > 0:
    average = total_life_expectancy / count
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {input_max_country} with {input_max_life_expectancy:.3f}")
    print(f"The min life expectancy was in {input_min_country} with {input_min_life_expectancy:.3f}")
else:
    print(f"No data available for the year {input_year}.")

# per-country query (extra feature)
country_query = input("\nEnter a country to analyze (or press Enter to skip): ").strip()
if country_query:
    # case-insensitive match (exact or substring)
    lc_map = {k.lower(): k for k in country_data}
    key = None
    if country_query.lower() in lc_map:
        key = lc_map[country_query.lower()]
    else:
        # try substring match
        matches = [k for k in country_data if country_query.lower() in k.lower()]
        key = matches[0] if matches else None

    if key:
        records = [life for (_, life) in country_data[key]]
        cmin = min(records)
        cmax = max(records)
        cavg = sum(records) / len(records)
        print(f"\nStats for {key}:")
        print(f"  Min: {cmin:.3f}")
        print(f"  Max: {cmax:.3f}")
        print(f"  Avg: {cavg:.2f}")
    else:
        print(f"No data found for country matching '{country_query}'.")

# report largest drop
if largest_drop_country:
    print()
    print(f"Largest year-to-year drop was {largest_drop:.3f} years in life expectancy for {largest_drop_country} from {drop_from_year} to {drop_to_year}.")
else:
    print("\nNo year-to-year drops detected.")
  