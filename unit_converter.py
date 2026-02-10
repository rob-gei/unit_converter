#unit converter

units = {
    "1": "Weight",
    "2": "Length",
    "3": "Volume",
}

a = True

while a:
    print("\033[94mWhat do you want to convert? \033[0m")
    for number, unit in units.items():
        print(f"{number}. {unit}")

    choose_unit = input()

    keys_1 = list(units.keys())

    while True:
        if choose_unit in units:
            break
        else:
            choose_unit = input(f"\033[91mEnter a right Number from {keys_1[0]}-{keys_1[-1]} : \033[0m")

    weight_units = {
        "1": "Ton (t)",
        "2": "Kilogramm (kg)",
        "3": "Gramm (g)",
        "4": "Pound (lb)"
    }
    length_units = {
        "1": "Kilometer (km)",
        "2": "Meter (m)",
        "3": "Centimeter (cm)",
        "4": "Millimeter (mm)",
        "5": "Inch (in)",
        "6": "Foot(ft)",
        "7": "Yard(yd)",
        "8": "Mile(mi)"
    }
    volume_units = {
        "1": "Liter (l)",
        "2": "Mililiter (ml)",
        "3": "Gallone"
    }

    choose_unit_1 = {
        "1" : weight_units,
        "2" : length_units,
        "3" : volume_units
    }

    selected_unit = choose_unit_1[choose_unit]

    print("\033[94mChose which Unit you want to convert from \033[0m")

    for number, unit in selected_unit.items():
        print(f"{number}. {unit}")

    choose_from = input()
    keys_2 = list(selected_unit.keys())

    while True:
        if choose_from in selected_unit:
            break
        else:
            choose_from = input(f"\033[91mEnter a Number from {keys_2[0]}-{keys_2[-1]}: \033[0m")

    from_unit = selected_unit[choose_from]

    value = float(input(f"\033[94mEnter the Value in {from_unit}: \033[0m"))



    def convert_weight(value, from_unit, to_unit):

        if from_unit == "Ton (t)":
            value_kg = value * 1000
        elif from_unit == "Kilogramm (kg)":
            value_kg = value
        elif from_unit == "Gramm (g)":
            value_kg = value / 1000
        elif from_unit == "Pound (lb)":
            value_kg = value * 0.45359237

        if to_unit == "Ton (t)":
            return value_kg / 1000
        elif to_unit == "Kilogramm (kg)":
            return value_kg
        elif to_unit == "Gramm (g)":
            return value_kg * 1000
        elif to_unit == "Pound (lb)":
            return value_kg / 0.45359237

    def convert_length(value, from_unit, to_unit):
        
        if from_unit == "Kilometer (km)":
            value_m = value * 1000
        elif from_unit == "Meter (m)":
            value_m = value
        elif from_unit == "Centimeter (cm)":
            value_m = value / 100
        elif from_unit == "Millimeter (mm)":
            value_m = value / 1000
        elif from_unit == "Inch (in)":
            value_m = value * 0.0254
        elif from_unit == "Foot(ft)":
            value_m = value * 0.3048
        elif from_unit == "Yard(yd)":
            value_m = value * 0.9144
        elif from_unit == "Mile(mi)":
            value_m = value * 1609.34

        if to_unit == "Kilometer (km)":
            return value_m / 1000
        elif to_unit == "Meter (m)":
            return value_m
        elif to_unit == "Centimeter (cm)":
            return value_m * 100
        elif to_unit == "Millimeter (mm)":
            return value_m * 1000
        elif to_unit == "Inch (in)":
            return value_m / 0.0254
        elif to_unit == "Foot(ft)":
            return value_m / 0.3048
        elif to_unit == "Yard(yd)":
            return value_m / 0.9144
        elif to_unit == "Mile(mi)":
            return value_m / 1609.34
        
    def convert_volume(value, from_unit, to_unit): 
        
        if from_unit == "Liter (l)":
            value_ml = value * 1000
        elif from_unit == "Mililiter (ml)":
            value_ml = value
        elif from_unit == "Gallone":
            value_ml = value * 3785

        if to_unit == "Liter (l)":
            return value_ml / 1000
        elif to_unit == "Mililiter (ml)":
            return value_ml
        elif to_unit == "Gallone":
            return value_ml / 3785

    print("\033[94mEnter the desired convert to Unit\033[0m")

    for number, unit in selected_unit.items():
        if unit != from_unit:
            print(f"{number}. {unit}")

    choose_to = input()

    keys_3 = [k for k, u in selected_unit.items() if u != from_unit]

    while True:
        if choose_to in selected_unit:
            break
        else:
            choose_to = input(f"\033[91mEnter {" or ".join(keys_3)}: \033[0m")

    to_unit = selected_unit[choose_to]

    if choose_unit == "1":
        answer = convert_weight(value, from_unit, to_unit)
    elif choose_unit == "2":
        answer = convert_length(value, from_unit, to_unit)  
    elif choose_unit == "3":
        answer = convert_volume(value, from_unit, to_unit)     


    print(f"\033[92m{value} {from_unit} = \033[95m{answer} \033[92m{to_unit}\033[0m")

    while True:
        print("\033[92mDo you want to convert again? (Yes/No)\033[0m")
        restart = input().lower()

        if restart == "yes":
            break
        elif restart == "no":
            a = False
            break
        else:
            print("\033[91mEnter Yes / No\033[0m")