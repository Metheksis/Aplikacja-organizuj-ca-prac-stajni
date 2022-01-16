from datetime import date, datetime

#zmienne globalne
delimiter = ';'
today = date.today()
file_encoding = 'utf-8'

class Horse:

    def __init__(self, name, breed='', sex='', parents='', feeding='2 times per day', feeding_type='oat',
                 feeding_hours ='8:00, 16:00', quantity=1, medicament=''):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.parents = parents
        self.feeding = feeding
        self.feeding_type = feeding_type
        self.feeding_hours = feeding_hours
        self.quantity = quantity #w gramach, system nie przyjmuje przecinkow i kropek
        self.medicament = medicament
        self.ride_dict = {}

    def __str__(self):
        tmp = ''
        for i in self.ride_dict.keys():
            #konkatenacja zabookowanych jazd (kazdy kon ma swoj grafik)
            tmp = f'{tmp}\n\t * {i}\t->\t{self.ride_dict[i]}'
        return f"name = {self.name} breed = {self.breed} sex = {self.sex} parents = {self.parents} feeding = {self.feeding} feeding_type = {self.feeding_type} feeding_hours = {self.feeding_hours}, quantity = {self.quantity}, medicament = {self.medicament}\n" \
               f"Booked rides: {tmp}"

class Stable:

    dict_horse_key_counter = 0  #licznik nastepnego elemetu - konia w slowniku

    def __init__(self, name):
        self.dict_horses = {}
        self.name = name

    def __str__(self):
        temp = f'Stable name: {self.name}\n Horses: \n'
        for key in self.dict_horses.keys():
            temp = temp + str(key) + ') ' + self.dict_horses[key].__str__() + '\n'
        return temp

    def addHorse(self, name, breed='unspecified', sex='unspecified', parents='unspecified', feeding='unspecified', feeding_type='unspecified',
                 feeding_hours='8:00, 16:00', quantity=1, medicament='unspecified'):

        #sprawdzanie poprawnosci pola quantity
        try:
            quantity = int(quantity)
        except ValueError:
            print("błęda wartość quantity")
            return -1

        new_horse = Horse(name, breed, sex, parents, feeding, feeding_type, feeding_hours, quantity, medicament)
        self.dict_horses[self.dict_horse_key_counter] = new_horse
        self.dict_horse_key_counter = self.dict_horse_key_counter + 1   #inkrementacja klucza slownika, czeka na kolejnego konia:)

    def deleteHorse(self, passed_horse_id):
        del self.dict_horses[passed_horse_id]

    def get_horse_by_id(self, passed_horse_id):     #pobieranie testowe
        return self.dict_horses[passed_horse_id]

    def get_horse_by_name(self, passed_horse_name):
        for key in self.dict_horses.keys():
            if passed_horse_name == self.dict_horses[key].name:
                return self.dict_horses[key]

    def update_stable(self, passed_id, passed_horse):
        self.dict_horses[passed_id] = passed_horse

    def change_name(self, passed_name):
        self.name = passed_name

    def generate_plan(self, groom_list, instructor_list):
        with open(f"{self.name}_plan.csv", 'w') as out_file:
            #zapisanie do plikow parametrow klasy stable
            out_file.write(self.__str__())

            #wylistowanie wszystkich pracownikow stajni
            for groom in groom_list:
                out_file.write(groom.__str__())
            for instructor in instructor_list:
                out_file.write(instructor.__str__())

class Groom:

    def __init__(self, name):
        self.name = name
        for i in range(31):
            self.calendar = {i: True}
        self._skill_list = []
        self._horse_to_care_list = []

    def __str__(self):
        temp = f'Groom name = {self.name}\nSkills: \n'
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
        with open(f'{self.name}_groom_plan.csv', 'w', encoding=file_encoding) as out_file:
            out_file.write(f"Groom_name: {self.name}\n")
            out_file.write(f"Date: {today}\n")
            out_file.write(f"Stable: {passed_stable.name}\n")
            out_file.write(f'Horses to care:\n')
            #nagłówki
            out_file.write(f'Horse name{delimiter}Feeding hour{delimiter}Feed{delimiter}Quantity{delimiter}Medicament (if applicable){delimiter}\n')

            for horse in self._horse_to_care_list:
                temp_feeding_hours = ''
                for hour in horse.feeding_hours:
                    temp_feeding_hours = temp_feeding_hours + str(hour) + ":00 "
                out_file.write(f'{horse.name}{delimiter}{temp_feeding_hours}{delimiter}{horse.feeding_type}{delimiter}{horse.quantity}kg{delimiter}{horse.medicament}{delimiter}\n')

class RidingInstructor:

    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
        self.dict_rides = {}

    def __str__(self):
        tmp = 'Booked rides:'
        for key in self.dict_rides.keys():
            tmp = f'{tmp}\n\t {key}\t->\t{self.dict_rides[key]}'

        if tmp == '':
            tmp = 'No booked rides'

        return f'RidingInstructor name = {self.name}, specialisation = {self.specialisation}' \
                f'{tmp}'

    def change_name_and_specialisation(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation

    def book_ride(self, passed_stable, passed_horse_name, passed_start_hour, passed_rider_name):
        horse = passed_stable.get_horse_by_name(passed_horse_name)
        if passed_start_hour not in self.dict_rides and passed_start_hour not in horse.ride_dict.keys():
            self.dict_rides[passed_start_hour] = f'{passed_stable.name}{delimiter}{passed_horse_name}{delimiter}{passed_rider_name}'
            horse.ride_dict[passed_start_hour] = f'{passed_rider_name}'
            return 'You are good to ride'
        else:
            return f'No ride for {passed_rider_name} my friend -> {passed_start_hour} is already booked'

    def generate_plan(self):
        with open(f'{self.name}_Riding_Instructor.csv', 'w', encoding=file_encoding) as out_file:
            out_file.write(f'Instructor name: {self.name}\n')
            out_file.write(f'Skill: {self.specialisation}\n')
            out_file.write(f'Date: {today}\n')
            out_file.write(f'------\n')
            out_file.write(f'Planed rides:\n')
            out_file.write(f'Stable{delimiter}Horse{delimiter}Rider name{delimiter}Hour\n')

            for date_key in self.dict_rides.keys():
                out_file.write(f'{self.dict_rides[date_key]}{delimiter}{date_key}\n')

class Stable_owner:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Stable owner name = {self.name}'

#dane do testowania przed zrobieniem GUI
def generate_test_data(passed_stable, passed_groom):
    passed_stable.addHorse("Klopsik", sex="gelding")
    passed_stable.addHorse("Płotka", sex="mare")
    passed_stable.addHorse("Kasztanka", parents="Klopsik, Płotka")
    passed_stable.addHorse("Poldek")
    passed_groom.add_skill("asd")
    passed_groom.add_skill("asd2")
    groom.add_horse_to_care(stable.get_horse_by_id(0))
    groom.add_horse_to_care(stable.get_horse_by_id(1))
    groom2.add_horse_to_care(stable.get_horse_by_id(2))
    groom2.add_horse_to_care(stable.get_horse_by_id(3))
    riding_instructor.book_ride(passed_horse_name='Klopsik', passed_rider_name='Zosia', passed_start_hour='2022-01-02 10:00:00', passed_stable=stable)
    print(riding_instructor.book_ride(passed_horse_name='Klopsik', passed_rider_name='Adam', passed_start_hour='2022-01-02 11:00:00', passed_stable=stable))
    print(riding_instructor.book_ride(passed_horse_name='Płotka', passed_rider_name='Adam', passed_start_hour='2022-01-02 12:00:00', passed_stable=stable))


if __name__ == "__main__":
    owner = Stable_owner("Krzysiek")
    stable = Stable("Pędzący wiatr")
    groom = Groom("Maciek")
    groom2 = Groom("Katarzyna")
    riding_instructor = RidingInstructor("Tomek", 'show jumping')
    riding_instructor2 = RidingInstructor("Anna", 'show jumping')
    generate_test_data(stable, groom)

   #print(stable)
    print(riding_instructor)
    riding_instructor.generate_plan()
    groom.generate_plan(stable)
    groom2.generate_plan(stable)
