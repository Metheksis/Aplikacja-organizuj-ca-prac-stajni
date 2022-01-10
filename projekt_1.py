from datetime import date


class Horse:

    def __init__(self, name, breed='', sex='', parents='', feeding='2 times per day', feeding_type='oat', feeding_hours=[6, 18], quantity=1, medicament=''):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.parents = parents
        self.feeding = feeding
        self.feeding_type = feeding_type
        self.feeding_hours = feeding_hours
        #w kg
        self.quantity = quantity
        self.medicament = medicament

    def __str__(self):
        return f"name = {self.name} breed = {self.breed} sex = {self.sex} parents = {self.parents} feeding = {self.feeding} feeding_type = {self.feeding_type} feeding_type = {self.feeding_hours} health = {self.medicament}"


class Stable:

    dict_horse_key_counter = 0  #licznik nastepnego elemetu (konia) w slowniku

    def __init__(self, name):
        self.dict_horses = {}
        self.name = name

    def __str__(self):
        temp = ''
        for key in self.dict_horses.keys():
            temp = temp + str(key) + ') ' + self.dict_horses[key].__str__() + '\n'
        return temp

    def addHorse(self, name, breed='', sex='', parents=''):
        new_horse = Horse(name, breed, sex, parents)
        self.dict_horses[self.dict_horse_key_counter] = new_horse
        self.dict_horse_key_counter = self.dict_horse_key_counter + 1   #inkrementacja klucza slownika, czeka na kolejnego konia:)

    def deleteHorse(self, passed_horse_id):
        del self.dict_horses[passed_horse_id]

    def get_horse_by_id(self, passed_horse_id):
        return self.dict_horses[passed_horse_id]

    def update_stable(self, passed_id, passed_horse):
        self.dict_horses[passed_id] = passed_horse

class Groom:
    _skill_list = []
    _horse_to_care_list = []

    def __init__(self, name):
        self.name = name
        for i in range(31):
            self.calendar = {i: True}

    def __str__(self):
        temp = f'Groom name = {self.name}\nSkills: '
        for skill in self._skill_list:
            temp = temp + '\n\t- ' + skill
        return temp

    def add_skill(self, passed_skill):
        self._skill_list.append(passed_skill)

    def add_horse_to_care(self, passed_horse):
        self._horse_to_care_list.append(passed_horse)

    def get_skill_list(self):
        return self._skill_list

    def generate_plan(self, passed_stable):
        delimeter = '\t'
        with open(f'{self.name}_groom_plan.csv', 'w', encoding='utf-8') as out_file:
            out_file.write(f"Groom_name: {self.name}\n")
            out_file.write(f"Date: {date.today()}\n")
            out_file.write(f"Stable: {passed_stable.name}\n")
            out_file.write(f'Horses to care:\n')
            #nagłówki
            out_file.write(f'Horse name{delimeter}Feeding hour{delimeter}Feed{delimeter}Quantity{delimeter}Medicament (if applicable){delimeter}\n')

            for horse in self._horse_to_care_list:
                temp_feeding_hours = ''
                for hour in horse.feeding_hours:
                    temp_feeding_hours = temp_feeding_hours + str(hour) + ":00 "
                out_file.write(f'{horse.name}{delimeter}{temp_feeding_hours}{delimeter}{horse.feeding_type}{delimeter}{horse.quantity}kg{delimeter}{horse.medicament}{delimeter}\n')


class RidingInstructor:

    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation

    def __str__(self):
        return f'RidingInstructor name = {self.name}, specialisation = {self.specialisation}'


class Stable_owner:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Stable owner name = {self.name}'

def generate_test_data(passed_stable, passed_groom):
    passed_stable.addHorse("Klopsik", sex="gelding")
    passed_stable.addHorse("Płotka", sex="mare")
    passed_stable.addHorse("Kasztanka", parents="Klopsik, Płotka")
    passed_stable.addHorse("Poldek")
    passed_groom.add_skill("Driving licence")
    passed_groom.add_skill("Horse riding")
    groom.add_horse_to_care(stable.get_horse_by_id(0))
    groom.add_horse_to_care(stable.get_horse_by_id(1))
    groom2.add_horse_to_care(stable.get_horse_by_id(2))
    groom2.add_horse_to_care(stable.get_horse_by_id(3))

if __name__ == "__main__":
    owner = Stable_owner("Krzysiek")
    stable = Stable("Expert Horses")
    groom = Groom("Maciek")
    groom2 = Groom("Katarzyna")
    riding_instructor = RidingInstructor("Tomek", 'show jumping')
    riding_instructor2 = RidingInstructor("Anna", 'show jumping')
    generate_test_data(stable, groom)

    print(stable)
    print(groom)
    print(groom2)
    print(riding_instructor)
    print(riding_instructor2)
    print(owner)

    groom.generate_plan(stable)
    groom2.generate_plan(stable)