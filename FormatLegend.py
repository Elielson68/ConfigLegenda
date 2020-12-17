import math
def abs(num):
    if(num < 0):
        num *= -1
    if len(str(num)) < 2:
        num = str("0"+str(num))
    return num
arquivo = open('new_legend.txt','r')
arquivo2 = open('C:\\Users\\Elielson\\Pictures\\LegendaParasita.srt','w')
indexa = []
for linha in arquivo:
    indexa.append(linha)
count = 1334
for linha in indexa:
    row = str(count)+"\n"
    if linha == row:
        min_i = 1
        sec_i = 50
        min_f = 1
        sec_f = 50
        i = indexa.index(linha)
        tempo = indexa[i+1]
        print("Tempo 1: "+tempo)
        tempo = tempo.split("-->")


        tempo_inicial = tempo[0]
        tempo_inicial = tempo_inicial.split(",")
        tempo_inicial_lv = tempo_inicial[1]
        tempo_inicial = tempo_inicial[0].split(":")

        if (int(tempo_inicial[2])) >= sec_i:
            tempo_inicial[2] = str(abs(int(tempo_inicial[2]) - sec_i))
        else:
            min_i += 1
            second = sec_i - int(tempo_inicial[2])
            tempo_inicial[2] = str(abs(60-second))
        hour_i = 0
        if (int(tempo_inicial[1]) - min_i >= 0):
            tempo_inicial[1] = str(abs(int(tempo_inicial[1]) - min_i))
        else:
            hour_i += 1
            minute_i = min_i - int(tempo_inicial[1])
            tempo_inicial[1] = str(abs(60 - minute_i))

        tempo_inicial[0] = abs(int(tempo_inicial[0]) - hour_i)

        tempo_inicial = "{}:{}:{},{}".format(tempo_inicial[0], tempo_inicial[1], tempo_inicial[2], tempo_inicial_lv )

        tempo_final = tempo[1]
        tempo_final = tempo_final.split(",")
        tempo_final_lv = tempo_final[1]
        tempo_final = tempo_final[0].split(":")

        if (int(tempo_final[2])) >= sec_f:
            tempo_final[2] = str(abs(int(tempo_final[2]) - sec_f))
        else:
            min_f += 1
            second = sec_f - int(tempo_final[2])
            tempo_final[2] = str(abs(60-second))
        hour_f = 0
        if (int(tempo_final[1]) - min_f >= 0):
            tempo_final[1] = str(abs(int(tempo_final[1]) - min_f))
        else:
            hour_f += 1
            minute_f = min_f - int(tempo_final[1])
            tempo_final[1] = str(abs(60 - minute_f))

        tempo_final[0] = abs(int(tempo_final[0]) - hour_f)
        tempo_final = "{}:{}:{},{}".format(tempo_final[0], tempo_final[1], tempo_final[2], tempo_final_lv)

        tempo = tempo_inicial+" --> "+tempo_final
        print("Tempo 2: "+tempo)
        indexa[i + 1] = tempo
        count += 1
print(indexa)
arquivo2.writelines(indexa)
arquivo.close()
arquivo2.close()

