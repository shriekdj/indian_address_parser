import re
import csv

def get_words_list(raw_text: str):
	words_list = list()
	for single_data in raw_text.split(sep=','):
		if (single_data != '') or (single_data != ' '):
			if single_data.strip() not in words_list:
				words_list.append(single_data.strip())

	return words_list

class PostalAddress:
	def __init__(self, keywords_csv_file: str, encoding = None) -> None:
		self.keywords_for_street_name = set()
		self.keywords_for_landmarks = set()
		self.keywords_for_shop_house_no = set()
		self.keywords_for_district_name = set()
		self.keywords_for_village_or_city = set()
		self.raw_address = ''
		self.words_in_address = list()

		self.street_name_found = set()
		self.landmarks_found = set()
		self.shop_house_no_found = set()
		self.district_name_found = set()
		self.village_or_city_found = set()

		self.pin_codes_found = ', '.join(set(re.findall("\d{6,}", self.raw_address)))

		# parse states
		self.states_found = set()


		if encoding == None:
			encoder = 'utf-8'
		else:
			encoder = encoding

		with open(keywords_csv_file,encoding = encoder, newline='\n') as csv_file:
			csv_reader = csv.DictReader(csv_file, delimiter=',')

			for row in csv_reader:
				if (row['keywords_for_street_name'] != ''):
					self.keywords_for_street_name.add(row['keywords_for_street_name'])
				if (row['keywords_for_landmarks'] != ''):
					self.keywords_for_landmarks.add(row['keywords_for_landmarks'])
				if (row['keywords_for_shop_house_no'] != ''):
					self.keywords_for_shop_house_no.add(row['keywords_for_shop_house_no'])
				if (row['keywords_for_district_name'] != ''):
					self.keywords_for_district_name.add(row['keywords_for_district_name'])
				if (row['keywords_for_village_or_city'] != ''):
					self.keywords_for_village_or_city.add(row['keywords_for_village_or_city'])

	def parse(self, raw_address: str):
		self.raw_address = raw_address.lower().strip()
		self.words_in_address = get_words_list(self.raw_address)

		for word in self.words_in_address:
			for street_name in self.keywords_for_street_name:
				if street_name in word:
					self.street_name_found.add(word)
					self.words_in_address.remove(word)

			for landmark in self.keywords_for_landmarks:
				if landmark in word:
					self.landmarks_found.add(word)
					self.words_in_address.remove(word)

			for shop_house_no in self.keywords_for_shop_house_no:
				if shop_house_no in word:
					self.shop_house_no_found.add(word)
					self.words_in_address.remove(word)

			for district_name in self.keywords_for_district_name:
				if district_name in word:
					self.district_name_found.add(word)
					self.words_in_address.remove(word)


test_address = PostalAddress('keywords_file.csv')

print(test_address.landmarks_found)
