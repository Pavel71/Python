import pandas as pd




Years = range(1880, 2011)

pieces = []
columns =['Name', 'Sex', 'Births']

for year in Years:

    path = r'C:\projects\Python\data\babynames/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['Year'] = year
    pieces.append(frame)


#Собрать все данные в один объект DataFrame

Data_names_1880_2010 = pd.concat(pieces, ignore_index=True)



total_births = Data_names_1880_2010.pivot_table('Births', columns='Sex', aggfunc=sum,index='Year')

# print(total_births.tail())

total_births.plot(title ="Tota1 Ьirths Ьу sex and year")

print(total_births)
