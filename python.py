#%%
counties = ["Arapahoe","Denver","Jefferson"]
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
# %%
x = 0
while x <= 5:
    print(x)
    x = x + 1

# %%
count = 7

while count < 1:

    print("Hello World")

# %%
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(counties_dict.get(county))

# %%
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county, voters in counties_dict.items():
    print(county, voters)

# %%
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# %%
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict['county'])

# %%
