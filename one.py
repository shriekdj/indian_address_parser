new_df = pd.DataFrame()

for record in df.to_records():
    temp_dict = dict()
    for key in df.keys():
        temp_dict[key] = record[key]
    
    postal_address = PostalAddress(record['Postal Address of the Establishment'], keywords).__dict__

    for key in postal_address:
        temp_dict[key] = postal_address[key]
    
    new_df = new_df.append(temp_dict, ignore_index=True)

new_df