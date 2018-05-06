import msgGUI
import mensajeria

def saca(lista):
     listan = []
     for i in lista:
         listan.append(i[1])
         return listan

def remove(cadena):
    cadena1 = ""
    for i in cadena:
        if i != "b" :
            cadena1+= i
    return cadena1
def elimina_el_primero(string):
    l = ""
    for i in range(0,len(string)):
        if i > 0:
            l += string[i]
    return l
def elimina(x,l):
    while x in l:
        l.remove(x)
    return l
def binario(numero):
    numero1 = ""
    numero2 = ""
    numero1 = bin(numero)
    if len(numero1) == 8:
        numero2 = "0" + numero1
    elif len(numero1) == 9:
        numero2 = numero1
    elif len(numero1) == 10:
        numero2 = elimina_el_primero(numero1)
    return numero2

def string_a_binario(s):
    lista0 = []
    for i in s:
        lista0.append(i)
    lista1 = []
    for j in lista0:
        lista1.append(ord(j))
    lista2 = []
    for k in lista1:
        lista2.append(remove(binario(k)))
    concatenar = ""
    for h in lista2:
        concatenar += h
    return concatenar
def binario_a_string(s):
    lista0 = []
    lista1 = []
    lista2 = []
    texto = ""
    k = 0
    h = 8
    for i in range(0,len(s)-1):
        lista0.append(s[k:h])
        k += 8
        h += 8
    lista1 = elimina('',lista0)
    for j in lista1:
        lista2.append(int(j,2))
    for k in lista2:
        texto += chr(k)
    return texto

def OTP(msg,clave):
    codificacion = ""
    if len(msg) == len(clave):
        for i in range(0,len(msg)-1):
            if msg[i] == clave[i]:
                codificacion += "0"
            else:
                codificacion += "1"
    elif len(msg) < len(clave):
        for i in range(0,len(msg)-1):
            if msg[i] == clave[i]:
                codificacion += "0"
            else:
                codificacion += "1"
    else:
        gui.alerta("Máximo de caracteres:45, eliminar caracteres")
    return codificacion
            
    
def ordenar(lista_de_listas):
	for pasada in range(1,len(lista_de_listas)-1):
		for i in range(0,len(lista_de_listas)-pasada):
			if lista_de_listas[i][1] > lista_de_listas[i+1][1]:
				aux = lista_de_listas[i]
				lista_de_listas[i] = lista_de_listas[i+1]
				lista_de_listas[i+1] = aux
	return lista_de_listas

def quitar_repetidos(lista):
     lista1= []
     for i in lista:
          if lista.count(i) == 1:
               lista1.append(i)
     return lista1
                  

def tarea(gui):
    
    #INICIO TAREA
    
    gui.cambiar_titulo('Mensajea2')
    
    mail = "haalfaro@puc.cl"
    clave = "110101011010001011001110000000100111100001100001001010001111001011000010001111101100010011001011011111001000000000011010110001011101101111001010011010111010110100011111011001001100101000110000100100000011001110101010000101111001010000010101010110000010111000001010111110110110101101110101010100001001010110101110100111001000110101000111011100001111011101111001"

    if mensajeria.conectar(mail, clave):
        gui.alerta('Te has conectado correctamente al servidor!')
    else:
        gui.alerta('Imposible conectar con el servidor de mensajería') 

    while True:
        boton = gui.esperar_click()
        if boton == 0:
            gui.borrar_mensajes()
            mensajes_ver = []
            enviadosbin = mensajeria.mensajes_enviados()
            recibidosbin = mensajeria.mensajes_recibidos()
            mensajesbin = enviadosbin + recibidosbin
            mensajesbin2 = quitar_repetidos(mensajesbin)
            mensajesbin3 = ordenar(mensajesbin2)
            for datos in mensajesbin2:
                if datos in enviadosbin:
                    string = "de " + mail + " para: " + datos[0] + " - " + binario_a_string(OTP(datos[2],clave))
                    mensajes_ver.append(string)
                if datos in recibidosbin:
                    string = "de " + datos[0] + " para: " + mail + " - " + binario_a_string(OTP(datos[2],clave))
                    mensajes_ver.append(string) 
            for i in mensajes_ver:
                gui.poner_mensaje_al_principio(i)
                      
        elif boton == 1:#buscar
            buscado = gui.busqueda()
            gui.borrar_mensajes()
            gui.pantalla_mensajes()
            mensajes_ver = []
            enviadosbin = mensajeria.mensajes_enviados()
            recibidosbin = mensajeria.mensajes_recibidos()
            mensajesbin = enviadosbin + recibidosbin
            mensajesbin2 = quitar_repetidos(mensajesbin)
            mensajesbin3 = ordenar(mensajesbin2)
            for datos in mensajesbin3:
                if datos in enviadosbin and buscado:
                    string = "de " + mail + " para: " + datos[0] + " - " + binario_a_string(OTP(datos[2],clave))
                    mensajes_ver.append(string)
                if datos in recibidosbin and buscado:
                    string = "de " + datos[0] + " para: " + mail + " - " + binario_a_string(OTP(datos[2],clave))
                    mensajes_ver.append(string)
            for mensaje_completo in mensajes_ver:
                if buscado in mensaje_completo:
                    gui.poner_mensaje_al_principio(mensaje_completo)
            gui.alerta("Para volver a los mensajes usar boton de actualizar")

                    
            

        elif boton == 2:#redactar mensaje
            gui.pantalla_redactar()
           
        elif boton == 4:
            mensaje_a_enviar = gui.mensaje_redactado()
            mensaje_bin = string_a_binario(mensaje_a_enviar)
            mensaje_cod = OTP(mensaje_bin,clave)
            destino = gui.destinatario()
            if "@puc.cl" in destino:
                envio = mensajeria.enviar_mensaje(destino,mensaje_cod)
                if envio:
                    gui.alerta("Mensaje enviado correctamente")
                    gui.borrar_mensaje_redactado()
                    gui.borrar_destinatario()
                    
                else:
                    gui.alerta("Mensaje no enviado")
                    gui.borrar_mensaje_redactado()
                    gui.borrar_destinatario()
            else:
                gui.alerta("mensaje no válido, arreglelo e intente de nuevo")

                        
        elif boton == 3:#mostrar mensajes
            gui.pantalla_mensajes()                
                    
    #FIN TAREA  
app = msgGUI.Application(None)
app.cargar_programa(tarea)
app.iniciar()

5
