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
