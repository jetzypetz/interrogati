import random
class5AD = ['alessandrini', 'angelini', 'animali', 'arduini',
            'cirillo', 'coletta', 'de felici', "d'errico",
            'di laura', 'romanucci', 'mancini', 'integlia',
            'police', 'famosi', 'mazzilli', 'limiti',
            'rita', 'mercuri', 'santacchini', 'gosti']
latin = []
points_list = []
chosen = []
checker = []
for h in range(len(class5AD)):
    latin.append([])
    for i in range(len(class5AD)):
        latin[h].append(class5AD[i])


def remove(person, position):
    position = int(position)
    position -= 1
    try:
        latin[position].remove(person)
        checker.append((person, position))
    except ValueError:
        pass
    except AttributeError:
        pass


def input_remove():
    print('''per iniziare, dimmi che posizioni non puoi proprio fare.
    scrivilo cosi: (cognome,giorno,giorno,giorno)
    animali,3,5,2,14,16''')
    answer = input('> ')
    while len(answer) > 0:
        answer = answer.split(',')
        person = answer[0]
        answer.pop(0)
        for b in range(len(answer)):
            remove(person, answer[b])
        answer = input('> ')


def prefer(person, position):
    position -= 1
    for c in range(len(class5AD)):
        points1 = 20
        distance = position - c
        if distance < 0:
            distance = - distance
        distance = 3 * distance
        points1 -= distance
        if points1 < 0:
            points1 = 0
        for d in range(points1):
            latin[c].append(person)


def input_prefer():
    print('''ora fammi sapere quando preferisci andare
    scrivilo cosi: (nome,posizione preferita)
    animali,18''')
    answer = input('> ')
    answer = answer.split(',')
    person = answer[0]
    position = int(answer[1])
    prefer(person, position)


def assign_weighted():
    for e in range(len(class5AD)):
        least_options = len(class5AD) - 1
        while least_options in chosen:
            least_options -= 1
        for f in range(len(class5AD)).__reversed__():
            if len(latin[f]) < len(latin[least_options]) and f not in chosen:
                least_options = f
        latin[least_options] = random.choice(latin[least_options])
        for g in range(len(class5AD)):
            if g != least_options and g not in chosen:
                while latin[g].count(latin[least_options]):
                    remove(latin[least_options], g + 1)
        chosen.append(least_options)


def for_input():
    input_remove()
    input_prefer()


def sim_remove():
    for j in range(1, 10):
        remove('animali', j)
    for k in [1, 4, 10, 11]:
        remove('de felici', k)
    for m in [4, 6, 7, 8, 9]:
        remove('alessandrini', m)
    for n in range(10, 11, 12):
        remove("d'errico", n)


def sim_prefer():
    prefer('alessandrini', 10)
    prefer('angelini', 14)
    prefer('animali', 20)
    prefer('arduini', 4)
    prefer('cirillo', 7)
    prefer('coletta', 4)
    prefer('de felici', 18)
    prefer("d'errico", 20)
    prefer('di laura', 16)
    prefer('romanucci', 11)
    prefer('mancini', 20)
    prefer('integlia', 20)
    prefer('police', 20)
    prefer('famosi', 20)
    prefer('mazzilli', 20)
    prefer('limiti', 20)
    prefer('rita', 20)
    prefer('mercuri', 20)
    prefer('santacchini', 20)
    prefer('gosti', 1)


def for_sim():
    sim_remove()
    sim_prefer()


def check():
    for o in checker:
        if latin[int(o[1])] == o[0]:
            return ValueError


for_sim()
assign_weighted()
check()
print(latin)
