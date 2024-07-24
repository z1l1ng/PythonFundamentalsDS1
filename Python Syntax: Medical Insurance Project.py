#PART 1
# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(insurance_cost)
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")
# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost of insurance after increasing the BMI by 3.1 years is " + str(change_in_insurance_cost) + " dollars.")
# Male vs. Female Factor
bmi = 26.1
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The in change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")

#Older people tend to have higher estimated insurance costs. Higher BMIs are associated with higher estimated insurance cost. Men tend to have lower medical costs on average than women.

----------------------------------------

#PART 2: Tidy up code with function
# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insuance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2,1, 0)

# Estimate my own insurance cost
ziling_insuance_cost = calculate_insurance_cost("Ziling", 20, 0, 21.3, 0, 0)

----------------------------------------

#PART 3: Implement Booleans
# smoker function
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

# Function to estimate insurance cost (no bmi):
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print("The estimated insuance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

# Analyze your own insurance cost Ziling's insurance cost
ziling_insuance_cost = estimate_insurance_cost("Ziling", 20, 0, 0, 0)

----------------------------------------

# Part 4: Lists
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Create lists
names = ["Maria", "Rohan", "Valentina"]

insurance_costs = [4150.0, 5320.0, 35210.0]
estimated_costs = [4222.0, 5442.0, 36368.0]

insurance_data = list(zip(names, insurance_costs))

# Append insurance data
estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina",  valentina_insurance_cost))

print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

print("Here is the actual insurance cost data" + str(insurance_data))

# Extra 
# Insurance cost difference
maria_cost_difference = estimated_insurance_data[0][1]-insurance_data[0][1]
rohan_cost_difference = estimated_insurance_data[1][1]-insurance_data[1][1]
valentina_cost_difference = estimated_insurance_data[2][1]-insurance_data[2][1]

# Append insurance cost list
insurance_cost_difference = []
insurance_cost_difference.append(("Maria", maria_cost_difference))
insurance_cost_difference.append(("Rohan", rohan_cost_difference))
insurance_cost_difference.append(("Valentina",  valentina_cost_difference))

print("Here is the difference in estimated insurance cost and actual insurance cost " + str(insurance_cost_difference))

# Estimate Akira
names.append("Akira")

insurance_costs.append(2930.0)

insurance_data = list(zip(names, insurance_costs))

# Print new insurance
print("Here is the actual insurance cost data" + str(insurance_data))

----------------------------------------

# Part 5: More Lists
# Lists 
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Adding Priscilla
names.append("Priscilla")
insurance_costs.append(8320.0)

# Merge together both lists
medical_records = list(zip(insurance_costs, names))
print(medical_records)

num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

# Selecting list items
first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))

# Sorting list items
medical_records_sort = sorted(medical_records)

print("Here are the medical records sorted by insurance cost: " + str(medical_records_sort))

# Slicing
cheapest_three = medical_records_sort[:3]

print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

priciest_three = medical_records_sort[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

# Counting elements in a list
occurances_paul = names.count("Paul")
print("There are " + str(occurances_paul) + " individuals with the name Paul in our medical records. ")

# Sort the medical records alphabetically by name.
# Merge together both lists
medical_records2 = list(zip(names, insurance_costs))

medical_records2_sort = sorted(medical_records2)
print("Here are the medical records sorted by name: " + str(medical_records2_sort))

# Selecting middle five records fro alphabetical list
middle_five_records = medical_records2_sort[3:8]
print("Here are the middle five medical records: " + str(middle_five_records))
