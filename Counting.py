def countSpecies(data, name):
    species = data['scientific_name'].value_counts()
    species = species.to_frame()
    species.reset_index(inplace=True)
    species.columns = ['scientific_name', 'count']
    species.sort_values(by=['count'], inplace=True, ascending=False)
    species.to_csv('Counted' + name + '.csv')
