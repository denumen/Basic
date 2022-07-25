import numpy
i = numpy.array([1, 2, 3, 4, 5, 6, 7])
j = numpy.array([1, 9, 0, 10, 5, 6, 7])
k = ([11, 22, 83, 10, 3, 4, 6])
nvector = numpy.array([1, 3, 5])

# andazeye vector
#print(nvector.shape)

# moshahede kole matrix
import sys
numpy.set_printoptions(threshold=sys.maxsize)


# sakhte matrix ba moalefe haye mokhtalef
# n_matrix = numpy.matrix([i, j, k])
#print(n_matrix)

# taghire andaze  vector be matrix baraye test
#print(numpy.resize(nvector, (4, 4)))

# taghire andaze vector be matrix va zakhire
#nvector.resize((3, 3))
#print(nvector)

# printe andazeye vector va matrix
#print(nvector.shape)

# sakhte matrix zeros ya ones be halate float hast chon 0. ashar ham dare
#print(numpy.zeros((3, 3)))

# sakhte matrix zeros ya ones be halate int
#print(numpy.zeros((3, 3), int))

# peyda kardan adade ghotre asli matrix
#print(numpy.diag([i, j , k]))

# tekrare arghame poshte ham dar array
# print(numpy.repeat((1, 3, 5), 3))

# chasbidane 2matrix behamdige sotoon ha bayad barabar bashad satr mohem nist
matrix_1 = numpy.ones((3, 5), int)
matrix_2 = numpy.zeros((5, 5), int)
#print(numpy.vstack((matrix_1, matrix_2)))

# chasbidane 2matrix behamdige satr ha bayad barabar bashad sotoon mohem nist
#matrix_1 = numpy.ones((5, 3), int)
#matrix_2 = numpy.zeros((5, 5), int)
#print(numpy.hstack((matrix_1, matrix_2)))

# chasbidan besoorate tuple
#print(list(zip(matrix_1, matrix_2)))

# amaliat haye 2  array
#print(i + j)
#print(j/i)
#print(i-j)
#print (j//i)

# be tavan resoondan array
#print(i**3)

#zarbe dakheli ya noghtei array
#print(i.dot(j))

# taranahade matrix
#print(matrix_1.T)

# tabdile int be float matrix
#print(matrix_1.astype('f'))

#amaliat dar matrix
#print(matrix_1.sum())
#print(matrix_1.min())
#print(matrix_1.max())
#print(matrix_1.mean())

#print jaigahe min ya max dar araye (adade khoonei ke tooshe) argoman
#print(matrix_1.argmax())
#print(matrix_1.argmin())

# mohasebe enheraf standard (parakandegi nesbat be miangin)
#print((matrix_1.std()))

# sakhte array az 0 ta n
#print(numpy.arange(15))

# bakhsh bandie matrix avali satr dovomi sotoon
#print(matrix_1[:2 , 0:3])

# peyda kardane khoonehaye bozorgtar ya kochiktar az n
#print(matrix_1 >= 2)
#print(matrix_2[matrix_2 >= 2])
#print(matrix_2[matrix_2 >= 0])

# taghire array be adade digar
#print(i)
#i[:3] = 1
#print(i)

#copy kardane ye array tuye ye array dige bejaye inke taghir kone ba taghire array mabda
#matrix_3 = matrix_2.copy()

#random sazi
#print(numpy.random.randint(0, 10, (4, 3)))

# for baraye satr o sotoon dar matrix
#for i, r in enumerate(matrix_2):
#    print('index ' + str(i) + ' is' , r)

