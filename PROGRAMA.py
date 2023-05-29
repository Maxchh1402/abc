import streamlit as st
import numpy as np
import pandas as pd

def PROGRAMA():
    
    
    st.title("DATOS DE ENTRADA")
    st.write("Resultado")
    
    Cal. Calculador()

    st.title('My title')
    st.header('My header')
    st.subheader('My sub')
    st.text('Fixed width text')
    st.markdown('_Markdown_') # see *
    st.caption('Balloons. Hundreds of them...')
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    
    print("RED DE TUBERÍAS")
    print()
    print("Aquí, se proporciona un croquis isométrico de la red de tuberías como ayuda visual."
        " Sin embargo, se necesitan algunas especificaciones para estas tuberías y "
        "esta es la situación de diseño que debe enfrentar  un ingeniero.	")
    print()

    print("El objetivo de la red es suministrar agua en cuatro puntos  "
        "diferentes de una gran planta de proceso como parte de los servicios. "
        "Se han ideado unas válvulas de compuerta en la red, como se muestra, "
        "para que se pueda cortar el suministro en cualquiera de los cuatro puntos diferentes.")
    print()

    print(" Se estableció la disposición de la red de tuberías al considerar "
        "el equipo de proceso instalado, los soportes mecánicos de tubería "
        "plausibles y la seguridad. "
        "Sin embargo, no se determinaron los tamaños de las tuberías.")
    print()
    # Solicitar al usuario el valor de QA (caudal de alimentación)
    QA = float(input("Ingrese el valor de QA (caudal de alimentación): "))
    print()
    #DATOS
    # Declarar las variables de longitud de tuberías
    L1 = 74
    L2 = 113
    L3 = 73
    L4 = 198
    L5 = 22
    L6 = 13
    L7 = 61
    L8 = 33
    # Definir la velocidad constante
    velocidad = 1.5
    # Declarar los valores para gravedad, rugosidad, y viscosidad
    g= 9.81 # en m/s^2
    e= 4.60E-05  # en metros
    v= 1.085000E-06  # en m^2/s

    # Solicitar al usuario el valor de HGL en metros
    HGL = float(input("Ingrese el valor de HGL de alimentación (en metros): "))

    # Imprimir los valores declarados0.583146667
    print("Valor de rugosidad:",e, "metros")
    print("Valor de HGL:", HGL, "metros")
    print("Valor de viscosidad:",v, "m^2/s")
    print("Valor de gravedad:",g, "m/s^2")


    # Mostrar los valores asignados
    print("Valores de longitud de tuberías:")
    print("L1 =", L1,"mts")
    print("L2 =", L2,"mts")
    print("L3 =", L3,"mts")
    print("L4 =", L4,"mts")
    print("L5 =", L5,"mts")
    print("L6 =", L6,"mts")
    print("L7 =", L7,"mts")
    print("L8 =", L8,"mts")
    print()
    # Calcular las variables establecidas
    Q6 = QA * 0.35
    Q7 = QA * 0.5
    Q8 = Q6 * 0.35

    #Sustituir en los demás caudales
    Q1 = QA - Q6
    Q2 = QA - Q6 + Q7
    Q3 = (3/4) * QA + Q8 + Q7 - Q6
    Q4 = Q6 - Q7 - Q8 - (1/2) * QA
    Q5 = Q6 - (1/4) * QA


    # Imprimir los resultados
    print("Variables establecidas:")
    print("Q1 =", Q1,"m3/s")
    print("Q2 =", Q2,"m3/s")
    print("Q3 =", Q3,"m3/s")
    print("Q4 =", Q4,"m3/s")
    print("Q5 =", Q5,"m3/s")
    print("Q6 =", Q6,"m3/s")
    print("Q7 =", Q7,"m3/s")
    print("Q8 =", Q8,"m3/s")
    print()

    def asignar_diametro(*caudales):
        data = [
            (0.00001, 0.00013, "1/8"),
            (0.00013, 0.00019, "3/8"),
            (0.00019, 0.00038, "1/2"),
            (0.00038, 0.00063, "3/4"),
            (0.00063, 0.00158, "1"),
            (0.00158, 0.00284, "1 1/2"),
            (0.00284, 0.00789, "2"),
            (0.00789, 0.01577, "3"),
            (0.01577, 0.03469, "5"),
            (0.03469, 0.08832, "6"),
            (0.08832, 0.15772, "14"),
            (0.15772, 0.28402, "16"),
            (0.28402, 0.50461, "20"),
            (0.50461, 1.17685, "24")
        ]

        diametros = []
        for caudal in caudales:
            diametro = None
            for item in data:
                if item[0] <= caudal <= item[1]:
                    diametro = item[2]
                    break
            diametros.append(diametro)

        return diametros

    # Asignación de caudal
    caudal1 = abs(Q1)
    caudal2 = abs(Q2)
    caudal3 = abs(Q3)
    caudal4 = abs(Q4)
    caudal5 = abs(Q5)
    caudal6 = abs(Q6)
    caudal7 = abs(Q7)
    caudal8 = abs(Q8)

    diametros_asignados = asignar_diametro(caudal1, caudal2, caudal3, caudal4, caudal5, caudal6, caudal7, caudal8)

    # Guardar los valores de diámetro en una variable
    diametro1, diametro2, diametro3, diametro4, diametro5, diametro6, diametro7, diametro8 = diametros_asignados

    # Imprimir los valores de diámetro guardados en las variables
    print(f"El diámetro nominal asignado para caudal1 es: {diametro1}")
    print(f"El diámetro nominal asignado para caudal2 es: {diametro2}")
    print(f"El diámetro nominal asignado para caudal3 es: {diametro3}")
    print(f"El diámetro nominal asignado para caudal4 es: {diametro4}")
    print(f"El diámetro nominal asignado para caudal5 es: {diametro5}")
    print(f"El diámetro nominal asignado para caudal6 es: {diametro6}")
    print(f"El diámetro nominal asignado para caudal7 es: {diametro7}")
    print(f"El diámetro nominal asignado para caudal8 es: {diametro8}")
    print()

    def asignar_diametro_interno(diametros_nominales):

        resultados = []

        for d1 in diametros_nominales:
            if d1 == "1/8":
                ID = 0.0068
            elif d1 == "1/4":
                ID = 0.0092
            elif d1 == "3/8":
                ID = 0.0125
            elif d1 == "1/2":
                ID = 0.0158
            elif d1 == "3/4":
                ID = 0.021
            elif d1 == "1":
                ID = 0.0266
            elif d1 == "1 1/4":
                ID = 0.0351
            elif d1 == "1 1/2":
                ID = 0.0409
            elif d1 == "2":
                ID = 0.0525
            elif d1 == "2 1/2":
                ID = 0.0627
            elif d1 == "3":
                ID = 0.0779
            elif d1 == "3 1/2":
                ID = 0.0901
            elif d1 == "4":
                ID = 0.1023
            elif d1 == "5":
                ID = 0.1282
            elif d1 == "6":
                ID = 0.1541
            elif d1 == "8":
                ID = 0.2027
            elif d1 == "10":
                ID = 0.2545
            elif d1 == "12":
                ID = 0.3033
            elif d1 == "14":
                ID = 0.3333
            elif d1 == "16":
                ID = 0.381
            elif d1 == "18":
                ID = 0.4287
            elif d1 == "20":
                ID = 0.4778
            elif d1 == "24":
                ID = 0.5746
            else:
                ID = "Indefinido"

            resultados.append(ID)

        return resultados



    diametros_nominales = [diametro1, diametro2, diametro3, diametro4, diametro5, diametro6, diametro7, diametro8]
    diametros_internos = asignar_diametro_interno(diametros_nominales)
    # Guardar los valores de diámetro interno en una variable
    ID1,ID2,ID3,ID4,ID5,ID6,ID7,ID8 = diametros_internos

    # Imprimir los valores de diámetro guardados en las variables
    print(f"El diámetro interno para caudal1 es: {ID1}""mts")
    print(f"El diámetro interno para caudal2 es: {ID2}""mts")
    print(f"El diámetro interno para caudal3 es: {ID3}""mts")
    print(f"El diámetro interno para caudal4 es: {ID4}""mts")
    print(f"El diámetro interno para caudal5 es: {ID5}""mts")
    print(f"El diámetro interno para caudal6 es: {ID6}""mts")
    print(f"El diámetro interno para caudal7 es: {ID7}""mts")
    print(f"El diámetro interno para caudal8 es: {ID8}""mts")
    print()

    print("Con todos estos valores se calculan los caudales reales de cada rama, para eso se hace uso del método de Hardy Cross")
    print()

    def calcular_area_diametro(diametro):
        radio = diametro / 2
        area = math.pi * (radio ** 2)
        return area

    A1 = calcular_area_diametro(ID1)
    A2 = calcular_area_diametro(ID2)
    A3 = calcular_area_diametro(ID3)
    A4 = calcular_area_diametro(ID4)
    A5 = calcular_area_diametro(ID5)
    A6 = calcular_area_diametro(ID6)
    A7 = calcular_area_diametro(ID7)
    A8 = calcular_area_diametro(ID8)

    print("Áreas de los diámetros:")
    print("Tubo 1:", A1,"mts^2")
    print("Tubo 2:", A2,"mts^2")
    print("Tubo 3:", A3,"mts^2")
    print("Tubo 4:", A4,"mts^2")
    print("Tubo 5:", A5,"mts^2")
    print("Tubo 6:", A6,"mts^2")
    print("Tubo 7:", A7,"mts^2")
    print("Tubo 8:", A8,"mts^2")
    print()

    print("Se sabe que en cada ramal existen accesorios,tanto codos como válvulas:")
    print("Para aquellos que tienen dichos artículo se asignan")

    #Codos

    Codo1=3
    Codo2=4
    Codo3=2
    Codo4=7
    Codo5=0
    Codo6=0
    Codo7=4
    Codo8=0

    #Valores de K para accesorios

    kcodo=30
    kválvula=8

    #HARDY CROSS

    print("Cálculo de los caudales reales:")
    print("Para el cálculo de los nuevos caudales se realiza un proceso iterativo donde se incluye ajustar los valores iniciales para caudal a travez de una correción")
    print("gracias al cálculo de los hL (pérdidas del tubo correspondiente), igualando la suma de aquellos a 0 :")

    #ITERACIONES

    print("Intrucciones para la busqueda de los caudales reales")
    print("1.- Calcular los valores de los caudales en función al flujo")
    print("2.- Calcular el valor respectivo de número de Raynolds, con las dimenciones, el caudal y la viscocidad del fuido")
    print("3.- Obtener el valor de factor de fricción para el respectivo tubo")
    print("4.- Realizar la operación que ayuda a determinar la perdida de fricción K del tubo")
    print("5.- Con el valor K, tabular el hL del tubo")
    print("6.- Determinar la correción para el caudal, renombrarlo y continuar con la siguiente iteración")
    print("7.- En caso de tener un caudal en más de un circuto usar la correción común para caudal total de este")

    # Cálculo de D/e
    D_e_1 = ID1/e
    D_e_2 = ID2/e
    D_e_3 = ID3/e
    D_e_4 = ID4/e
    D_e_5 = ID5/e
    D_e_6 = ID6/e
    D_e_7 = ID7/e
    D_e_8 = ID8/e

    #ITERACIÓN 1

    I=1




    #CIRCUITO 1
    Q1_I1=Q1
    Q7_I7=-1*Q7
    Q5_I5=-1*Q5
    Q6_I6=-1*Q6

    #CIRCUITO 1 (signos)



    Signo1=Q1_I1/(abs(Q1_I1))
    Signo7=Q7_I7/(abs(Q7_I7))
    Signo5=Q5_I5/(abs(Q5_I5))
    Signo6=Q6_I6/(abs(Q6_I6))




    # Calcular números de Raynolds
    Nre1= (abs(Q1_I1*ID1))/(A1*v)
    Nre7= (abs(Q7_I7*ID7))/(A7*v)
    Nre5= (abs(Q5_I5*ID5))/(A5*v)
    Nre6= (abs(Q6_I6*ID6))/(A6*v)

    # Calcular el factor de fricción fT

    fT1 = (0.25 / (math.log10(1 / (3.7 * D_e_1) + 5.74 / (Nre1 ** 0.9))) ** 2)
    fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
    fT5 = (0.25 / (math.log10(1 / (3.7 * D_e_5) + 5.74 / (Nre5 ** 0.9))) ** 2)
    fT6 = (0.25 / (math.log10(1 / (3.7 * D_e_6) + 5.74 / (Nre6 ** 0.9))) ** 2)

    K1 = Codo1*kcodo*fT1 * (1 / (2 * g * A1 ** 2)) +kválvula*fT1 * (1 / (2 * g * A1 ** 2)) +fT1 * (L1 / ID1) * (1 / (2 * g * A1 ** 2))
    K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
    K5 = Codo5*kcodo*fT5 * (1 / (2 * g * A5 ** 2)) +kválvula*fT5 * (1 / (2 * g * A5 ** 2)) +fT5 * (L5 / ID5) * (1 / (2 * g * A5 ** 2))
    K6 = Codo6*kcodo*fT6 * (1 / (2 * g * A6 ** 2)) +fT6 * (L6 / ID6) * (1 / (2 * g * A6 ** 2))





    # Calcular de hL de los tubos, considerando el sentido del flujo

    hL1=K1*(Q1_I1**2)*Signo1
    hL7=K7*(Q7_I7**2)*Signo7
    hL5=K5*(Q5_I5**2)*Signo5
    hL6=K6*(Q6_I6**2)*Signo6




    # Calcular de 2kQ de los tubos, sin considerar el signo

    kQ1=2*K1*abs(Q1_I1)
    kQ7=2*K7*abs(Q7_I7)
    kQ5=2*K5*abs(Q5_I5)
    kQ6=2*K6*abs(Q6_I6)




    # Calcular de deltaQ CIRCUITO 1

    SUMAhL1=hL1+hL7+hL5+hL6
    SUMA2kQ1=kQ1+kQ7+kQ5+kQ6

    DeltaQ1=(SUMAhL1/SUMA2kQ1)




    Q1_I1=Q1_I1-DeltaQ1
    Q7_I7=Q7_I7-DeltaQ1
    Q5_I5=Q5_I5-DeltaQ1
    Q6_I6=Q6_I6-DeltaQ1





    #CIRCUITO 2
    Q2_I2=Q2
    Q7_I7_2=Q7
    Q8_I8=-1*Q8




    #CIRCUITO 2 (signos)
    Signo2=Q2_I2/(abs(Q2_I2))
    Signo7=Q7_I7_2/(abs(Q7_I7_2))
    Signo8=Q8_I8/(abs(Q8_I8))




    # Calcular números de Raynolds
    Nre2= (abs(Q2_I2*ID2))/(A2*v)
    Nre7= (abs(Q7_I7_2*ID7))/(A7*v)
    Nre8= (abs(Q8_I8*ID8))/(A8*v)


    # Calcular el factor de fricción fT

    fT2 = (0.25 / (math.log10(1 / (3.7 * D_e_2) + 5.74 / (Nre2 ** 0.9))) ** 2)
    fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
    fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)


    K2 = Codo2*kcodo*fT2 * (1 / (2 * g * A2 ** 2)) +fT2 * (L2 / ID2) * (1 / (2 * g * A2 ** 2))
    K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
    K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2)) +fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))





    # Calcular de hL de los tubos, considerando el sentido del flujo

    hL2=K2*(Q2_I2**2)*Signo2
    hL7=K7*(Q7_I7_2**2)*Signo7
    hL8=K8*(Q8_I8**2)*Signo8



    # Calcular de 2kQ de los tubos, sin considerar el signo

    kQ2=2*K2*abs(Q2_I2)
    kQ7=2*K7*abs(Q7_I7_2)
    kQ8=2*K8*abs(Q8_I8)



    # Calcular de deltaQ CIRCUITO 2

    SUMAhL1=hL2+hL7+hL8
    SUMA2kQ1=kQ2+kQ7+kQ8

    DeltaQ2=(SUMAhL1/SUMA2kQ1)

    Q2_I2=Q2_I2-DeltaQ2
    Q7_I7_2=Q7_I7_2-DeltaQ2
    Q8_I8=Q8_I8-DeltaQ2



    #CIRCUITO 3
    Q3_I3=Q3
    Q8_I8_2=Q8
    Q4_I4=-1*Q4



    #CIRCUITO 3 (signos)
    Signo3=Q3_I3/(abs(Q3_I3))
    Signo8=Q8_I8_2/(abs(Q8_I8_2))
    Signo4=Q4_I4/(abs(Q4_I4))



    # Calcular números de Raynolds
    Nre3= (abs(Q3_I3*ID3))/(A3*v)
    Nre8= (abs(Q8_I8_2*ID8))/(A8*v)
    Nre4= (abs(Q4_I4*ID4))/(A4*v)


    # Calcular el factor de fricción fT

    fT3 = (0.25 / (math.log10(1 / (3.7 * D_e_3) + 5.74 / (Nre3 ** 0.9))) ** 2)
    fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)
    fT4 = (0.25 / (math.log10(1 / (3.7 * D_e_4) + 5.74 / (Nre4 ** 0.9))) ** 2)


    K3 = Codo3*kcodo*fT3 * (1 / (2 * g * A3 ** 2)) +fT3 * (L3 / ID3) * (1 / (2 * g * A3 ** 2))
    K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2))+fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))
    K4 = Codo4*kcodo*fT4 * (1 / (2 * g * A4 ** 2)) +kválvula*fT4 * (1 / (2 * g * A4 ** 2)) +fT4 * (L4 / ID4) * (1 / (2 * g * A4 ** 2))





    # Calcular de hL de los tubos, considerando el sentido del flujo

    hL3=K3*(Q3_I3**2)*Signo3
    hL8=K8*(Q8_I8_2**2)*Signo8
    hL4=K4*(Q4_I4**2)*Signo4



    # Calcular de 2kQ de los tubos, sin considerar el signo

    kQ3=2*K3*abs(Q3_I3)
    kQ8=2*K8*abs(Q8_I8_2)
    kQ4=2*K4*abs(Q4_I4)



    # Calcular de deltaQ CIRCUITO 3

    SUMAhL1=hL3+hL8+hL4
    SUMA2kQ1=kQ3+kQ8+kQ4

    DeltaQ3=(SUMAhL1/SUMA2kQ1)

    Q3_I3=Q3_I3-DeltaQ3
    Q8_I8_2=Q8_I8_2-DeltaQ3
    Q4_I4=Q4_I4-DeltaQ3




    #Caudales comunes

    Q7_I7=Q7_I7+DeltaQ2
    Q7_I7_2=Q7_I7_2+DeltaQ1
    Q8_I8=Q8_I8+DeltaQ3
    Q8_I8_2=Q8_I8_2+DeltaQ2



    #PORCENTAJES DE ERROR

    Chg1=(DeltaQ1/(Q1_I1+DeltaQ1))*100
    Chg2=(DeltaQ2/(Q2_I2+DeltaQ2))*100
    Chg3=(DeltaQ3/(Q3_I3+DeltaQ3))*100
    Chg4=(DeltaQ3/(Q4_I4+DeltaQ3))*100
    Chg5=(DeltaQ1/(Q5_I5+DeltaQ1))*100
    Chg6=(DeltaQ1/(Q6_I6+DeltaQ1))*100
    Chg7=(DeltaQ1/(Q7_I7+DeltaQ1-DeltaQ2))*100
    Chg7_2=(DeltaQ2/(Q7_I7_2+DeltaQ2-DeltaQ1))*100
    Chg8=(DeltaQ2/(Q8_I8+DeltaQ2-DeltaQ3))*100
    Chg8_2=(DeltaQ3/(Q8_I8_2+DeltaQ3-DeltaQ2))*100





    #ITERACIÓN 2,3,4... (COPIAR CAUDALES ANTERIORES SOLAMENTE)

    iteracion = 2
    while iteracion <= 21:

        # Resto del código...

        #CIRCUITO 1 (signos)

        Signo1=Q1_I1/(abs(Q1_I1))
        Signo7=Q7_I7/(abs(Q7_I7))
        Signo5=Q5_I5/(abs(Q5_I5))
        Signo6=Q6_I6/(abs(Q6_I6))

        # Calcular números de Raynolds
        Nre1= (abs(Q1_I1*ID1))/(A1*v)
        Nre7= (abs(Q7_I7*ID7))/(A7*v)
        Nre5= (abs(Q5_I5*ID5))/(A5*v)
        Nre6= (abs(Q6_I6*ID6))/(A6*v)

        # Calcular el factor de fricción fT

        fT1 = (0.25 / (math.log10(1 / (3.7 * D_e_1) + 5.74 / (Nre1 ** 0.9))) ** 2)
        fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
        fT5 = (0.25 / (math.log10(1 / (3.7 * D_e_5) + 5.74 / (Nre5 ** 0.9))) ** 2)
        fT6 = (0.25 / (math.log10(1 / (3.7 * D_e_6) + 5.74 / (Nre6 ** 0.9))) ** 2)

        K1 = Codo1*kcodo*fT1 * (1 / (2 * g * A1 ** 2)) +kválvula*fT1 * (1 / (2 * g * A1 ** 2)) +fT1 * (L1 / ID1) * (1 / (2 * g * A1 ** 2))
        K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
        K5 = Codo5*kcodo*fT5 * (1 / (2 * g * A5 ** 2)) +kválvula*fT5 * (1 / (2 * g * A5 ** 2)) +fT5 * (L5 / ID5) * (1 / (2 * g * A5 ** 2))
        K6 = Codo6*kcodo*fT6 * (1 / (2 * g * A6 ** 2)) +fT6 * (L6 / ID6) * (1 / (2 * g * A6 ** 2))

        # Calcular de hL de los tubos, considerando el sentido del flujo

        hL1=K1*(Q1_I1**2)*Signo1
        hL7=K7*(Q7_I7**2)*Signo7
        hL5=K5*(Q5_I5**2)*Signo5
        hL6=K6*(Q6_I6**2)*Signo6

        # Calcular de 2kQ de los tubos, sin considerar el signo

        kQ1=2*K1*abs(Q1_I1)
        kQ7=2*K7*abs(Q7_I7)
        kQ5=2*K5*abs(Q5_I5)
        kQ6=2*K6*abs(Q6_I6)

        # Calcular de deltaQ CIRCUITO 1

        SUMAhL1=hL1+hL7+hL5+hL6
        SUMA2kQ1=kQ1+kQ7+kQ5+kQ6

        DeltaQ1=(SUMAhL1/SUMA2kQ1)

        Q1_I1=Q1_I1-DeltaQ1
        Q7_I7=Q7_I7-DeltaQ1
        Q5_I5=Q5_I5-DeltaQ1
        Q6_I6=Q6_I6-DeltaQ1

        #CIRCUITO 2

        #CIRCUITO 2 (signos)
        Signo2=Q2_I2/(abs(Q2_I2))
        Signo7=Q7_I7_2/(abs(Q7_I7_2))
        Signo8=Q8_I8/(abs(Q8_I8))

        # Calcular números de Raynolds
        Nre2= (abs(Q2_I2*ID2))/(A2*v)
        Nre7= (abs(Q7_I7_2*ID7))/(A7*v)
        Nre8= (abs(Q8_I8*ID8))/(A8*v)

        # Calcular el factor de fricción fT

        fT2 = (0.25 / (math.log10(1 / (3.7 * D_e_2) + 5.74 / (Nre2 ** 0.9))) ** 2)
        fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
        fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)

        K2 = Codo2*kcodo*fT2 * (1 / (2 * g * A2 ** 2)) +fT2 * (L2 / ID2) * (1 / (2 * g * A2 ** 2))
        K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
        K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2)) +fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))

        # Calcular de hL de los tubos, considerando el sentido del flujo

        hL2 = K2 * (Q2_I2 ** 2) * Signo2
        hL7 = K7 * (Q7_I7_2 ** 2) * Signo7
        hL8 = K8 * (Q8_I8 ** 2) * Signo8

        # Calcular de 2kQ de los tubos, sin considerar el signo

        kQ2=2*K2*abs(Q2_I2)
        kQ7=2*K7*abs(Q7_I7_2)
        kQ8=2*K8*abs(Q8_I8)

        # Calcular de deltaQ CIRCUITO 2

        SUMAhL1=hL2+hL7+hL8
        SUMA2kQ1=kQ2+kQ7+kQ8

        DeltaQ2=(SUMAhL1/SUMA2kQ1)

        Q2_I2=Q2_I2-DeltaQ2
        Q7_I7_2=Q7_I7_2-DeltaQ2
        Q8_I8=Q8_I8-DeltaQ2

        #CIRCUITO 3

        #CIRCUITO 3 (signos)
        Signo3=Q3_I3/(abs(Q3_I3))
        Signo8=Q8_I8_2/(abs(Q8_I8_2))
        Signo4=Q4_I4/(abs(Q4_I4))

        # Calcular números de Raynolds
        Nre3= (abs(Q3_I3*ID3))/(A3*v)
        Nre8= (abs(Q8_I8_2*ID8))/(A8*v)
        Nre4= (abs(Q4_I4*ID4))/(A4*v)

        # Calcular el factor de fricción fT

        fT3 = (0.25 / (math.log10(1 / (3.7 * D_e_3) + 5.74 / (Nre3 ** 0.9))) ** 2)
        fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)
        fT4 = (0.25 / (math.log10(1 / (3.7 * D_e_4) + 5.74 / (Nre4 ** 0.9))) ** 2)

        K3 = Codo3*kcodo*fT3 * (1 / (2 * g * A3 ** 2)) +fT3 * (L3 / ID3) * (1 / (2 * g * A3 ** 2))
        K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2))+fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))
        K4 = Codo4*kcodo*fT4 * (1 / (2 * g * A4 ** 2)) +kválvula*fT4 * (1 / (2 * g * A4 ** 2)) +fT4 * (L4 / ID4) * (1 / (2 * g * A4 ** 2))

        # Calcular de hL de los tubos, considerando el sentido del flujo

        hL3=K3*(Q3_I3**2)*Signo3
        hL8=K8*(Q8_I8_2**2)*Signo8
        hL4=K4*(Q4_I4**2)*Signo4

        # Calcular de 2kQ de los tubos, sin considerar el signo

        kQ3=2*K3*abs(Q3_I3)
        kQ8=2*K8*abs(Q8_I8_2)
        kQ4=2*K4*abs(Q4_I4)

        # Calcular de deltaQ CIRCUITO 3

        SUMAhL1=hL3+hL8+hL4
        SUMA2kQ1=kQ3+kQ8+kQ4

        DeltaQ3=(SUMAhL1/SUMA2kQ1)

        Q3_I3=Q3_I3-DeltaQ3
        Q8_I8_2=Q8_I8_2-DeltaQ3
        Q4_I4=Q4_I4-DeltaQ3

        #Caudales comunes

        Q7_I7=Q7_I7+DeltaQ2
        Q7_I7_2=Q7_I7_2+DeltaQ1
        Q8_I8=Q8_I8+DeltaQ3
        Q8_I8_2=Q8_I8_2+DeltaQ2

        #PORCENTAJES DE ERROR

        Chg1=(DeltaQ1/(Q1_I1+DeltaQ1))*100
        Chg2=(DeltaQ2/(Q2_I2+DeltaQ2))*100
        Chg3=(DeltaQ3/(Q3_I3+DeltaQ3))*100
        Chg4=(DeltaQ3/(Q4_I4+DeltaQ3))*100
        Chg5=(DeltaQ1/(Q5_I5+DeltaQ1))*100
        Chg6=(DeltaQ1/(Q6_I6+DeltaQ1))*100
        Chg7=(DeltaQ1/(Q7_I7+DeltaQ1-DeltaQ2))*100
        Chg7_2=(DeltaQ2/(Q7_I7_2+DeltaQ2-DeltaQ1))*100
        Chg8=(DeltaQ2/(Q8_I8+DeltaQ2-DeltaQ3))*100
        Chg8_2=(DeltaQ3/(Q8_I8_2+DeltaQ3-DeltaQ2))*100

    # Actualizar el valor de iteracion
        iteracion += 1

    print("ITERACIÓN",iteracion)
    print()

    #CAUDALES FINALES

    print("Q tubo 1=", Q1_I1)
    print("Q tubo 2=", Q2_I2)
    print("Q tubo 3=", Q3_I3)
    print("Q tubo 4=", Q4_I4)
    print("Q tubo 5=", Q5_I5)
    print("Q tubo 6=", Q6_I6)
    print("Q tubo 7=", Q7_I7)
    print("Q tubo 8=", Q8_I8)
    print()

    #PÉRDIDAS TOTALES POR LOS TUBOS YA ACCESORIOS

    print("hL de tubo 1:", hL1)
    print("hL de tubo 2:", hL2)
    print("hL de tubo 3:", hL3)
    print("hL de tubo 4:", hL4)
    print("hL de tubo 5:", hL5)
    print("hL de tubo 6:", hL6)
    print("hL de tubo 7:", hL7)
    print("hL de tubo 8:", hL8)
    print()

    #DIRECCIONES

    #SIGNOS DE CAUDALES SEGÚN CONVENCIÓN

    SQ1=1
    SQ2=1
    SQ3=1
    SQ4=-1
    SQ5=-1
    SQ6=-1
    SQ7=-1
    SQ8=-1

    #Q1
    if Q1_I1*SQ1 > 0:

        print("Dirección de Q1: AE")

    else:
        print("Dirección de Q1: EA")
    #Q2
    if Q2_I2*SQ2 > 0:

        print("Dirección de Q2: EJ")

    else:
        print("Dirección de Q2: JE")
    #Q3
    if Q3_I3*SQ3 > 0:

        print("Dirección de Q3: JM")

    else:
        print("Dirección de Q3: MJ")
    #Q4
    if Q4_I4*SQ4 > 0:

        print("Dirección de Q4: UM")

    else:
        print("Dirección de Q4: MU")
    #Q5
    if Q5_I5*SQ5 > 0:

        print("Dirección de Q5: ZU")

    else:
        print("Dirección de Q5: UZ")
    #Q6
    if Q6_I6*SQ6 > 0:

        print("Dirección de Q6: AZ")

    else:
        print("Dirección de Q6: ZA")
    #Q7
    if Q7_I7*SQ7 > 0:

        print("Dirección de Q7: UE")

    else:
        print("Dirección de Q7: EU")
    #Q8
    if Q8_I8*SQ8 > 0:

        print("Dirección de Q8: UJ")

    else:
        print("Dirección de Q8: JU")

    #CÁLCULO DE HGL
    print("Considerando el punto de alimentación como la altura = 0 m")
    print()

    #CÁLCULO DE PREESIONES

    #PESO ESPECIFICO
    y=991*9.81

    #ALTURAS DE CADA PUNTO

    A=0
    B = 0
    C = -13
    D = -13
    E = -13
    F = -13
    G = 12
    H = 12
    I = -5
    J = -13
    K = -13
    L = -13
    M = -29
    N = -29
    O = -13
    P = -13
    Q = -26
    R = -26
    S = -26
    T = -26
    U = -13
    Z = -13
    V = -13
    X = -13
    Y = -13
    W = -13
    J = -13

    #LONGITUDES DE CADA SECCIÓN DE TUBERÍA

    AB = 25
    BC = 13
    CD = 14
    DE = 22
    EF = 8
    FG = 12
    GH = 33
    HI = 52
    IJ = 8
    JK = 7
    KL = 50
    LM = 16
    MN = 73
    NO = 16
    OP = 25
    PQ = 13
    QR = 14
    RS = 25
    ST = 19
    TU = 13
    UZ = 22
    UV = 10
    VX = 8.5
    XY = 15
    YW = 8.5
    WE = 19
    ZA = 13
    UJ = 33

    #CALCULOS DE Kde cada sección

    KAB = fT1 * (AB / ID1) * (1 / (2 * g * A1 ** 2))
    KBC = fT1 * (BC / ID1) * (1 / (2 * g * A1 ** 2))+(8*fT1)* (1 / (2 * g * A1 ** 2))
    KCD = fT1 * (CD / ID1) * (1 / (2 * g * A1 ** 2))
    KDE = fT1 * (DE / ID1) * (1 / (2 * g * A1 ** 2))

    KEF = fT2 * (EF / ID2) * (1 / (2 * g * A2 ** 2))
    KFG = fT2 * (FG / ID2) * (1 / (2 * g * A2 ** 2))
    KGH = fT2 * (GH / ID2) * (1 / (2 * g * A2 ** 2))
    KHI = fT2 * (HI / ID2) * (1 / (2 * g * A2 ** 2))
    KIJ = fT2 * (IJ / ID2) * (1 / (2 * g * A2 ** 2))

    KJK = fT3 * (JK / ID3) * (1 / (2 * g * A3 ** 2))
    KKL = fT3 * (KL / ID3) * (1 / (2 * g * A3 ** 2))
    KLM = fT3 * (LM / ID3) * (1 / (2 * g * A3 ** 2))

    KMN = fT4 * (MN / ID4) * (1 / (2 * g * A4 ** 2))
    KNO = fT4 * (NO / ID4) * (1 / (2 * g * A4 ** 2))
    KOP = fT4 * (OP / ID4) * (1 / (2 * g * A4 ** 2))
    KPQ = fT4 * (PQ / ID4) * (1 / (2 * g * A4 ** 2))
    KQR = fT4 * (QR / ID4) * (1 / (2 * g * A4 ** 2))
    KRS = fT4 * (RS / ID4) * (1 / (2 * g * A4 ** 2))
    KST = fT4 * (ST / ID4) * (1 / (2 * g * A4 ** 2))+(8*fT4)* (1 / (2 * g * A4 ** 2))
    KTU = fT4 * (TU / ID4) * (1 / (2 * g * A4 ** 2))

    KUZ = fT5 * (UZ / ID5) * (1 / (2 * g * A5 ** 2))+(8*fT5)* (1 / (2 * g * A5 ** 2))

    KUV = fT7 * (UV / ID7) * (1 / (2 * g * A7 ** 2))
    KVX = fT7 * (VX / ID7) * (1 / (2 * g * A7 ** 2))
    KXY = fT7 * (XY / ID7) * (1 / (2 * g * A7 ** 2))
    KYW = fT7 * (YW / ID7) * (1 / (2 * g * A7 ** 2))
    KWE = fT7 * (WE / ID7) * (1 / (2 * g * A7 ** 2))

    KZA = fT6 * (ZA / ID6) * (1 / (2 * g * A6 ** 2))

    KUJ = fT8 * (UJ / ID8) * (1 / (2 * g * A8 ** 2))+(8*fT8)* (1 / (2 * g * A8 ** 2))

    #CALCULO DE hL de cada sección

    hLAB=KAB*(abs(Q1_I1))**2
    hLBC=KBC*(abs(Q1_I1))**2
    hLCD=KCD*(abs(Q1_I1))**2
    hLDE=KDE*(abs(Q1_I1))**2

    hLEF=KEF*(abs(Q2_I2))**2
    hLFG=KFG*(abs(Q2_I2))**2
    hLGH=KGH*(abs(Q2_I2))**2
    hLHI=KHI*(abs(Q2_I2))**2
    hLIJ=KIJ*(abs(Q2_I2))**2

    hLJK=KJK*(abs(Q3_I3))**2
    hLKL=KKL*(abs(Q3_I3))**2
    hLLM=KLM*(abs(Q3_I3))**2

    hLMN=KMN*(abs(Q4_I4))**2
    hLNO=KNO*(abs(Q4_I4))**2
    hLOP=KOP*(abs(Q4_I4))**2
    hLPQ=KPQ*(abs(Q4_I4))**2
    hLQR=KQR*(abs(Q4_I4))**2
    hLRS=KRS*(abs(Q4_I4))**2
    hLST=KST*(abs(Q4_I4))**2
    hLTU=KTU*(abs(Q4_I4))**2

    hLUZ=KUZ*(abs(Q5_I5))**2

    hLUV=KUV*(abs(Q7_I7))**2
    hLVX=KVX*(abs(Q7_I7))**2
    hLXY=KXY*(abs(Q7_I7))**2
    hLYW=KYW*(abs(Q7_I7))**2
    hLWE=KWE*(abs(Q7_I7))**2

    hLZA=KZA*(abs(Q6_I6))**2

    hLUJ=KUJ*(abs(Q8_I8))**2

    #KCODOS

    KC1 = Codo1*kcodo*fT1 * (1 / (2 * g * A1 ** 2))
    KC2 = Codo2*kcodo*fT2 * (1 / (2 * g * A2 ** 2))
    KC3 = Codo3*kcodo*fT3 * (1 / (2 * g * A3 ** 2))
    KC4 = Codo4*kcodo*fT4 * (1 / (2 * g * A4 ** 2))
    KC5 = Codo5*kcodo*fT5 * (1 / (2 * g * A5 ** 2))
    KC6 = Codo6*kcodo*fT6 * (1 / (2 * g * A6 ** 2))
    KC7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2))
    KC8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2))

    #hLCODOS

    hLC1=KC1*(abs(Q1_I1)**2)
    hLC2=KC2*(abs(Q2_I2)**2)
    hLC3=KC3*(abs(Q3_I3)**2)
    hLC4=KC4*(abs(Q4_I4)**2)
    hLC5=KC5*(abs(Q5_I5)**2)
    hLC6=KC6*(abs(Q6_I6)**2)
    hLC7=KC7*(abs(Q7_I7)**2)
    hLC8=KC8*(abs(Q8_I8)**2)

    #PRESIONESSSSSS
    PA=(HGL*y)-A

    #PAE
    if Q1_I1*SQ1 > 0:
        #PE=P2
        PB = ((PA / y) + A - B - (hLAB+1/3*hLC1)) * y
        PC = ((PB / y) + B - C - (hLBC+1/3*hLC1)) * y
        PD = ((PC / y) + C - D - (hLCD+1/3*hLC1)) * y
        PE = ((PD / y) + D - E - (hLDE)) * y

    else:# PE=P1
        PB = ((PA / y) + A - B + (hLAB + 1 / 3 * hLC1)) * y
        PC = ((PB / y) + B - C + (hLBC + 1 / 3 * hLC1)) * y
        PD = ((PC / y) + C - D + (hLCD + 1 / 3 * hLC1)) * y
        PE = ((PD / y) + D - E + (hLDE)) * y

    #PEJ
    if Q2_I2*SQ2 > 0:
        #PJ=P2
        PF = ((PE / y) + E - F - (hLEF+1/4*hLC2)) * y
        PG = ((PF / y) + F - G - (hLFG+1/4*hLC2)) * y
        PH = ((PG / y) + G - H - (hLGH+1/4*hLC2)) * y
        PI = ((PH / y) + H - I - (hLHI+1/4*hLC2)) * y
        PJ = ((PI / y) + I - J - (hLIJ)) * y

    else:# PJ=P1
        PF = ((PE / y) + E - F + (hLEF + 1 / 4 * hLC2)) * y
        PG = ((PF / y) + F - G + (hLFG + 1 / 4 * hLC2)) * y
        PH = ((PG / y) + G - H + (hLGH + 1 / 4 * hLC2)) * y
        PI = ((PH / y) + H - I + (hLHI + 1 / 4 * hLC2)) * y
        PJ = ((PI / y) + I - J + (hLIJ)) * y

    #PJM
    if Q3_I3*SQ3 > 0:
        #PM=P2
        PK = ((PJ / y) + J - K - (hLJK+1/2*hLC3)) * y
        PL = ((PK / y) + K - L - (hLKL+1/2*hLC3)) * y
        PM = ((PL / y) + L - M - (hLLM)) * y

    else:# PM=P1
        PK = ((PJ / y) + J - K + (hLJK + 1 / 2 * hLC3)) * y
        PL = ((PK / y) + K - L + (hLKL + 1 / 2 * hLC3)) * y
        PM = ((PL / y) + L - M + (hLLM)) * y

    #PMU
    if Q4_I4*SQ4 > 0:
        #PU=P1
        PN = ((PM / y) + M - N + (hLMN + 1 / 7 * hLC4)) * y
        PO = ((PN / y) + N - O + (hLNO + 1 / 7 * hLC4)) * y
        PP = ((PO / y) + O - P + (hLOP + 1 / 7 * hLC4)) * y
        PQ = ((PP / y) + P - Q + (hLPQ + 1 / 7 * hLC4)) * y
        PR = ((PQ / y) + Q - R + (hLQR + 1 / 7 * hLC4)) * y
        PS = ((PR / y) + R - S + (hLRS + 1 / 7 * hLC4)) * y
        PT = ((PS / y) + S - T + (hLST + 1 / 7 * hLC4)) * y
        PU = ((PT / y) + T - U + (hLTU)) * y

    else:# PU=P2
        PN = ((PM / y) + M - N - (hLMN + 1 / 7 * hLC4)) * y
        PO = ((PN / y) + N - O - (hLNO + 1 / 7 * hLC4)) * y
        PP = ((PO / y) + O - P - (hLOP + 1 / 7 * hLC4)) * y
        PQ = ((PP / y) + P - Q - (hLPQ + 1 / 7 * hLC4)) * y
        PR = ((PQ / y) + Q - R - (hLQR + 1 / 7 * hLC4)) * y
        PS = ((PR / y) + R - S - (hLRS + 1 / 7 * hLC4)) * y
        PT = ((PS / y) + S - T - (hLST + 1 / 7 * hLC4)) * y
        PU = ((PT / y) + T - U - (hLTU)) * y

    #PUZ
    if Q5_I5*SQ5 > 0:
        #PZ=P1
        PZ = ((PU / y) + U - Z + (hLUZ)) * y

    else:# PU=P2
        PZ = ((PU / y) + U - Z - (hLUZ)) * y

    #PUE
    if Q7_I7*SQ7 > 0:
        #PU=P1
        PV =  ((PU / y) + U - V - (hLUV + 1 / 4 * hLC7)) * y
        PX =  ((PV / y) + V - X - (hLVX + 1 / 4 * hLC7)) * y
        PY =  ((PX / y) + X - Y - (hLXY + 1 / 4 * hLC7)) * y
        PW =  ((PY / y) + Y - W - (hLYW + 1 / 4 * hLC7)) * y
        PE2 = ((PW / y) + W - E - (hLWE)) * y

    else:# PU=P2
        PV = ((PU / y) + U - V +  (hLUV + 1 / 4 * hLC7)) * y
        PX = ((PV / y) + V - X +  (hLVX + 1 / 4 * hLC7)) * y
        PY = ((PX / y) + X - Y +  (hLXY + 1 / 4 * hLC7)) * y
        PW = ((PY / y) + Y - W +  (hLYW + 1 / 4 * hLC7)) * y
        PE2 = ((PW / y) + W - E + (hLWE)) * y

    #PZA
    if Q6_I6*SQ6 > 0:
        #PZ=P2
        PZ2 = ((PA / y) + A - Z - (hLZA)) * y

    else:# PZ=P1
        PZ2 = ((PA / y) + A - Z + (hLZA)) * y

    #PUJ
    if Q8_I8*SQ8 > 0:
        #PJ=P2
        PU2 = ((PJ / y) + U - J + (hLUJ)) * y

    else:# PU=P2
        PU2 = ((PJ / y) + U - J - (hLUJ)) * y

    # CONVERSION A PSI

    print("PA=",PA/6894.76)
    print("PAB=",PB/6894.76)
    print("PBC=",PC/6894.76)
    print("PCD=",PD/6894.76)
    print()

    print("PEF=",PF/6894.76)
    print("PFG=",PG/6894.76)
    print("PGH=",PH/6894.76)
    print("PHI=",PI/6894.76)
    print("PIJ=",PJ/6894.76)
    print()

    print("PJK=",PK/6894.76)
    print("PKL=",PL/6894.76)
    print("PLM=",PM/6894.76)
    print()

    print("PMN=",PN/6894.76)
    print("PNO=",PO/6894.76)
    print("POP=",PP/6894.76)
    print("PPQ=",PQ/6894.76)
    print("PQR=",PR/6894.76)
    print("PRS=",PS/6894.76)
    print("PST=",PT/6894.76)
    print("PTU=",PU/6894.76)
    print()

    print("PUZ=",PZ/6894.76)
    print()


    print("PUV=",PV/6894.76)
    print("PVX=",PX/6894.76)
    print("PXY=",PY/6894.76)
    print("PYW=",PW/6894.76)
    print("PWE=",PE2/6894.76)
    print()

    print("PZA=",PZ2/6894.76)
    print()
    print("PUJ=",PU2/6894.76)
    print()

    #CALCULO DE HGL

    HGLB=(PB/y)+B
    HGLC=(PC/y)+C
    HGLD=(PD/y)+D
    HGLE=(PE/y)+E
    HGLF=(PF/y)+F
    HGLG=(PG/y)+G
    HGLH=(PH/y)+H
    HGLI=(PI/y)+I
    HGLJ=(PJ/y)+J
    HGLK=(PK/y)+K
    HGLL=(PL/y)+L
    HGLM=(PM/y)+M
    HGLN=(PN/y)+N
    HGLO=(PO/y)+O
    HGLP=(PP/y)+P
    HGLQ=(PQ/y)+Q
    HGLR=(PR/y)+R
    HGLS=(PS/y)+S
    HGLT=(PT/y)+T
    HGLU=(PU/y)+U
    HGLZ=(PZ/y)+Z
    HGLV=(PV/y)+V
    HGLX=(PX/y)+X
    HGLY=(PY/y)+Y
    HGLW=(PW/y)+W
    HGLE2=(PE2/y)+E
    HGLZ2=(PZ2/y)+Z
    HGLU2=(PU2/y)+U

    print(HGLB)
    print(HGLC)
    print(HGLD)
    print(HGLE)
    print(HGLF)
    print(HGLG)
    print(HGLH)
    print(HGLI)
    print(HGLJ)
    print(HGLK)
    print(HGLL)
    print(HGLM)
    print(HGLN)
    print(HGLO)
    print(HGLP)
    print(HGLQ)
    print(HGLR)
    print(HGLS)
    print(HGLT)
    print(HGLU)
    print(HGLZ)
    print(HGLV)
    print(HGLX)
    print(HGLY)
    print(HGLW)
    print(HGLE2)
    print(HGLZ2)
    print(HGLU2)


            
