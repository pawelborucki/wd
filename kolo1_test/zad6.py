def rosnaco():
    	with open('plik.txt', 'r+') as p:
            n = [int(i) for i in p.read().split()]
            p.seek(0)
            p.write('\n'.join([str(i) for i in sorted(n)]))

rosnaco()
