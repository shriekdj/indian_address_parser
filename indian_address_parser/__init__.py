import re
from pprint import pprint
import csv

keywords_for_street_name = ('street name', 'street', 'marg', 'road', 'path', 'rasta')

keywords_for_landmarks = ('behind', 'near', 'above', 'opp.', 'opp:', 'opposite')

keywords_for_shop_house_no = ('shop n', 'shop number', 'gala n', 'store n', 'house n', 'home n', 'apartment', 'appt', 'flat', 'building n', 'room n', 'niwas')

keywords_for_district_name = ('dist', 'district', 'jilha')
keywords_for_village_or_city = ('gaon', 'gav', 'village', 'pur', 'shahar', 'city', 'taluka', 'town')

dict_of_states = {
    "Andaman and Nicobar Islands": [
        'andaman', 'nikobar', 'andaman'
    ],
    "Andhra Pradesh": [
        'andhra', 'andra pradesh', 'andhrapradesh', 'andhra pradesh'
    ],
    "Arunachal Pradesh": [
        'arunachal', 'arunachal pradesh', 'arunachalpradesh'
    ],
    "Assam": [
        'assam', 'aasam', 'asaam', 'aasaam'
    ],
    "Bihar": [
        'bihar', 'bihaar'
    ],
    "Chandigarh": [
        'chandigarh', 'chandigad'
    ],
    "Chhattisgarh": [
        'chattisgarh', 'chattisgad', 'chhattisgarh', 'chhattisgad'
    ],
    "Dadra and Nagar Haveli": [
        'dadra', 'nagar haveli'
    ],
    "Daman and Diu": [
        'daman', 'diu'
    ],
    "Goa": [
        'goa'
    ],
    "Gujarat": [
        'gujrat', 'gujarat'
    ],
    "Haryana": [
        'haryana'
    ],
    "Himachal Pradesh": [
        'himachal', 'himachal pradesh', 'himachalpradesh'
    ],
    "Jammu and Kashmir": [
        'jammu', 'kashmir', 'jammu & kashmir'
    ],
    "Jharkhand": [
        'jharkhand'
    ],
    "Karnataka": [
        'karnataka'
    ],
    "Kerala": [
        'kerla', 'kerala'
    ],
    "Lakshadweep": [
        'lakshadweep', 'lakshadveep', 'lakshadwip', 'lakshadvip'
    ],
    "Madhya Pradesh": [
        'madhya pradesh', 'madhyapradesh'
    ],
    "Maharashtra": [
        'maharashtra', 'maha rashtra'
    ],
    "Manipur": [
        'manipur'
    ],
    "Meghalaya": [
        'meghalay'
    ],
    "Mizoram": [
        'mizoram', 'mijhoram'
    ],
    "Nagaland": [
        'nagaland'
    ],
    "NCT of Delhi": [
        'delhi', 'nct of delhi','delli','dilli','dilli'
    ],
    "Odisha": [
        'odisa'
    ],
    "Puducherry": [
        'pondicherry', 'puducherry'
    ],
    "Punjab": [
        'punjab'
    ],
    "Rajasthan": [
        'rajasthan', 'rajastan'
    ],
    "Sikkim": [
        'sikkim'
    ],
    "Tamil Nadu": [
        'tamilnadu', 'tamil nadu'
    ],
    "Tripura": [
        'tripura'
    ],
    "Uttar Pradesh": [
        'uttarpradesh', 'uttar pradesh'
    ],
    "Uttarakhand": [
        'uttarakhand'
    ],
    "West Bengal": [
        'west bengal', 'bengal state'
    ],
}

class KeywordsProvider:
    def __init__(self, csv_file_name):
        self.keywords_for_street_name = set()
        self.keywords_for_landmarks = set()
        self.keywords_for_shop_house_no = set()
        self.keywords_for_district_name = set()
        self.keywords_for_village_or_city = set()
        self.dict_of_states = dict_of_states


        with open(csv_file_name, encoding='utf-8', newline='\n') as csv_file:
            reader = reader = csv.DictReader(csv_file)

            for row in reader:
                if row['keywords_for_street_name'] != '':
                    self.keywords_for_street_name.add(row['keywords_for_street_name'])
                if row['keywords_for_landmarks'] != '':
                    self.keywords_for_landmarks.add(row['keywords_for_landmarks'])
                if row['keywords_for_shop_house_no'] != '':
                    self.keywords_for_shop_house_no.add(row['keywords_for_shop_house_no'])
                if row['keywords_for_district_name'] != '':
                    self.keywords_for_district_name.add(row['keywords_for_district_name'])
                if row['keywords_for_village_or_city'] != '':
                    self.keywords_for_village_or_city.add(row['keywords_for_village_or_city'])
                # if (row['state_name'] != '') and (row['state_keyword'] != ''):
                #     self.dict_of_states[row['state_name']].append(row['state_keyword'])


class PostalAddress:
    def __init__(self, raw_address: str, keywords):

        self.raw_address: str = raw_address.lower().strip()
        self.country: str = "india"

        self.words_in_address = list(
                set(
                    [single_data.strip() for single_data in self.raw_address.split(sep=',')]
                )
            )
        self.pin_codes_found = ', '.join(set(re.findall("\d{6,}", self.raw_address)))

        # parse states

        self.states_found = set()

        for key in keywords.dict_of_states.keys():
            for keyword in dict_of_states[key]:
                for word in self.words_in_address:
                    if word.find(keyword) != -1:
                        self.states_found.add(key)

        self.states_found = ', '.join(self.states_found)

        self.street_names_found = set()
        self.landmarks_found = set()
        self.shop_house_nos_found = set()
        self.districts_found = set()
        self.village_or_citys_found = set()

        # parse other details
        for word in self.words_in_address:
            for street_name in keywords.keywords_for_street_name:
                if word.find(street_name) != -1:
                    self.street_names_found.add(word.capitalize())
            
            for landmark in keywords.keywords_for_landmarks:
                if word.find(landmark) != -1:
                    self.landmarks_found.add(word.capitalize())
            
            for shop_house_no in keywords.keywords_for_shop_house_no:
                if word.find(shop_house_no) != -1:
                    self.shop_house_nos_found.add(word.capitalize())

            for district in keywords.keywords_for_district_name:
                if word.find(district) != -1:
                    self.districts_found.add(word.capitalize())

            for village_or_city in keywords.keywords_for_village_or_city:
                if word.find(village_or_city) != -1:
                    self.village_or_citys_found.add(word.capitalize())
        
        self.street_names_found = ', '.join(self.street_names_found)
        self.landmarks_found = ', '.join(self.landmarks_found)
        self.shop_house_nos_found = ', '.join(self.shop_house_nos_found)
        self.districts_found = ', '.join(self.districts_found)
        self.village_or_citys_found = ', '.join(self.village_or_citys_found)


def main():
    # Use a breakpoint in the code line below to debug your script.
    postal_address = PostalAddress('Vidya Nagar, Kutagulla Kadiri, ANANTAPUR(Dist), Andhra Pradesh, Pincode - 515541').__dict__
    # postal_address = postal_address.parse()

    print('pin codes found',postal_address['pin_codes_found'])  # Press Ctrl+F8 to toggle the breakpoint.
    print('states found',postal_address['states_found'])  # Press Ctrl+F8 to toggle the breakpoint.
    print(postal_address)
    # postal_address = postal_address.parse_dict()
    # pprint(address_as_dict)  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    main()
