is_gender_male=False
age = 36
weight_in_kg = 84
fat_percentage = None
height_in_cm = 180

calory_requirements = 0
weight_target = 'HIGH'
target_calory = 0

number_of_meals = 3

if fat_percentage == None:
    carb_protein_fat_ratio = (0.5,0.35,0.15)
elif fat_percentage > 0.25:
    carb_protein_fat_ratio = (0.55,0.35,0.10)
else:
    carb_protein_fat_ratio = (0.5,0.3,0.2)


def get_calory_requirements():
    if fat_percentage is not None:
        return 370 + 21.6 * (1 - fat_percentage) * weight_in_kg 
    else:
        if is_gender_male:
            calory_requirements = (13.397 * weight_in_kg) + (4.799 * height_in_cm ) - (5.677 * age) + 88.362
        else:
            calory_requirements =  (9.247 * weight_in_kg ) + (3.098 * height_in_cm) - (4.330 * age) + 447.593
    return calory_requirements        

current_calory_req = get_calory_requirements()
if weight_target == 'HIGH':
    current_calory_req = current_calory_req * 0.8
elif weight_target == 'MEDIUM':
    current_calory_req = current_calory_req * 0.85
else:
    current_calory_req = current_calory_req * 0.9

print(current_calory_req)
carb_in_gram_needed =   ((current_calory_req) * carb_protein_fat_ratio[0]) / 4.0
protein_in_gram_needed =   ((current_calory_req) * carb_protein_fat_ratio[1]) / 4.0
fat_in_gram_needed =   ((current_calory_req) * carb_protein_fat_ratio[2]) / 8.0

print(carb_in_gram_needed,protein_in_gram_needed,fat_in_gram_needed)




