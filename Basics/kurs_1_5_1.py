# 1. zadanie
sec = 1
minute= sec*60
hour = minute * 60
day = 24 * hour
week = 5 * day
month = 30* day
workday = 8 * hour
workweek = workday * 5
workmonth = workday * 22
workweek_minutes = 40 * hour / minute

# 2. zadanie

bit = 1
bajt = 8 * bit
kilobajt = 1024 * bajt
megabajt = 1024 * kilobajt
kilobit = 1024 * bit
megabit = 1024 * kilobit

print(f"Jeden Megabajt to {megabajt} bitów\r")
print(f"Megabajt od megabita różni się o {megabajt-megabit} bitów.\n")

# 3. zadanie

download_time = ((100*megabajt)/(100*megabit))
print(f"100 MB plik ściągniesz w czasie {download_time} sekund")

#4. zadanie
celsius_deg = 1
kelvin_deg = celsius_deg
Kelvin0_deg = -273 *celsius_deg
Celsius0_deg = 273 *kelvin_deg

# księzyc 180 st C w dzień
moon_day = Kelvin0_deg + (180 * kelvin_deg)

# księzyc 180 st C w noc
moon_night = Celsius0_deg + (93 * celsius_deg)

# mars srednia
mars = Kelvin0_deg - (63 * kelvin_deg)

# mars max
mars_max = Kelvin0_deg + (20 * kelvin_deg)

# mars min
mars_min = Celsius0_deg + (120 *celsius_deg)

print(f"1. {moon_day}°K \n")
print(f"2. {moon_night} °C\n ")
print(f"3. {mars}°K \n")
print(f"4.{mars_max}°K \n")
print(f"5. {mars_min}°C")