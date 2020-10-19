from hashlib import md5

open_file = open('N0003966.290', 'r', encoding='ISO-8859-1')
file = open_file.read().lower().rstrip('\n\r ').strip('\n\r')

m = md5()
m.update(b'file')
print(m.hexdigest())