# Indian Address Parser In python

I Created this library to parse indian address as accurate as possible and this library is opensource so you can contribute to it also.

This package does not need any dependency at all to work.

You can run your code as follows

Just Do this to install indian_address_parser

```bash
pip install indian_address_parser
```

```python
from indian_address_parser import PostalAddress

postal_address = PostalAddress('Vidya Nagar, Kutagulla Kadiri, ANANTAPUR(Dist), Andhra Pradesh, Pincode - 515541').__dict__
# postal_address = postal_address.parse()

print('pin codes found',postal_address['pin_codes_found'])  # Press Ctrl+F8 to toggle the breakpoint.
print('states found',postal_address['states_found'])  # Press Ctrl+F8 to toggle the breakpoint.
```

if you have any other suggetion you can write issue on github.

```python
pin codes found ['515541']
states found ['Andhra Pradesh']
{'country': 'india',
 'districts_found': ['anantapur(dist)'],
 'landmarks_found': [],
 'pin_codes_found': ['515541'],
 'raw_address': 'vidya nagar, kutagulla kadiri, anantapur(dist), andhra '
                'pradesh, pincode - 515541',
 'shop_house_nos_found': [],
 'states_found': ['Andhra Pradesh'],
 'street_names_found': [],
 'village_or_citys_found': ['anantapur(dist)'],
 'words_in_address': ['vidya nagar',
                      'kutagulla kadiri',
                      'anantapur(dist)',
                      'pincode - 515541',
                      'andhra pradesh']}
```
