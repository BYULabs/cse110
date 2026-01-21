max_life_expectancy = float("-inf")

min_life_expectancy = float("inf")

with open('data_analysis/life-expectancy.csv') as data_file:
    next(data_file) 


    for line in data_file:
        parts = line.strip().split(",")

        life_expectancy = float(parts[3].strip())

        # overall min/max
        if life_expectancy > max_life_expectancy:
          max_life_expectancy = life_expectancy

        if life_expectancy < min_life_expectancy:
          min_life_expectancy = life_expectancy

print()

print(f"The overall max life expectancy is: {max_life_expectancy:.3f} from max_country in max_year")
print(f"The overall min life expectancy is: {min_life_expectancy:.3f} from min_country in min_year")
