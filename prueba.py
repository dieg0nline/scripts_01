import pandas as pd

# leer los archivos de excel
df1 = pd.read_excel('libro1.xlsx', usecols=['A'])
df2 = pd.read_excel('libro2.xlsx', usecols=['A'])

# combinar los datos en un nuevo DataFrame
df3 = pd.concat([df1, df2], axis=1)
df3['c'] = df3['a'] + df3['b']

# escribir el resultado en un nuevo archivo de excel
writer = pd.ExcelWriter('resultado.xlsx', engine='xlsxwriter')
df3.to_excel(writer, index=False, sheet_name='Hoja1', 
             header=['Archivo1', 'Archivo2', 'Concatenacion'])
writer.save()