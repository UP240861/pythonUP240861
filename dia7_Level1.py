it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Level 1
#1
print('Las cantidad de compañias en it_commpanies es de: ', len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['Intel', 'Nvidia', 'Amd', 'Radeon'])
print(it_companies)
#4
it_companies.remove('Apple')
print(it_companies)
#5
it_companies.remove('Amd')
it_companies.add('Qualcomm')
it_companies.remove('Qualcomm')
it_companies.discard('Samsung')
print(it_companies)