import calcula_mare_equilibrio as cm
import matplotlib.pyplot as plt


q1 = cm.questao_1()
fig = plt.figure(figsize=(16,8))
xax = range(24 * 3)

plt.plot(xax, q1[0], color = 'red', label = 'lon 0')
plt.plot(xax, q1[45], color = 'green', label = 'lon 45')
plt.plot(xax, q1[90], color = 'black', label = 'lon 90')

# plt.ylim(-3, 3)
plt.grid()
plt.ylabel('Elevação de Superfície')
plt.xlabel('Hora')
plt.legend()

# plt.show()


plt.savefig('fig/questao1.png')
##############

q2 = cm.questao_2()
fig = plt.figure(figsize=(16,8))
xax = range(24 * 3)

plt.plot(xax, q2[0], color = 'red', label = 'lat 0')
plt.plot(xax, q2[45], color = 'green', label = 'lat 45')
plt.plot(xax, q2[60], color = 'orange', label = 'lat 60')
plt.plot(xax, q2[90], color = 'black', label = 'lat 90')

# plt.ylim(-3, 3)
plt.grid()
plt.ylabel('Elevação de Superfície')
plt.xlabel('Hora')
plt.legend()

# plt.show()


plt.savefig('fig/questao2.png')

##############

q3 = cm.questao_3()
fig = plt.figure(figsize=(16,8))
xax = range(24 * 3)

plt.plot(xax, q3[0], color = 'red', label = 'lat 0')
plt.plot(xax, q3[45], color = 'green', label = 'lat 45')
plt.plot(xax, q3[60], color = 'orange', label = 'lat 60')
plt.plot(xax, q3[90], color = 'black', label = 'lat 90')

# plt.ylim(-3, 3)
plt.grid()
plt.ylabel('Elevação de Superfície')
plt.xlabel('Hora')
plt.legend()

# plt.show()

plt.savefig('fig/questao3.png')


##########

q4 = cm.questao_4()
fig = plt.figure(figsize=(16,8))
xax = range(24 * 7)

plt.plot(xax, q4[-0.0583], color = 'red', label = 'lat 0')

# plt.ylim(-3, 3)
plt.grid()
plt.ylabel('Elevação de Superfície')
plt.xlabel('Hora')
# plt.legend()

# plt.show()

plt.savefig('fig/questao4.png')