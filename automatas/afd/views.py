from django.shortcuts import render

def grafico(request):
    # Render  administracion.html
    if request.method == 'GET':
        gato='1'

        return render(request, "index.html", {'gato': gato,})
    elif request.method == 'POST':
        try:
            inicio = request.POST['inicio']
            dato=1
        except:
            dato=2
        palabra = len(request.POST['palabra'])
        palabra_final = request.POST['palabra']
        posicion_palabra = int(request.POST['posicion_palabra'])
        posicion_circulo = int(request.POST['posicion_circulo'])
        letra = int(str(request.POST['palabra'])[posicion_palabra])
        posicion_palabra_final=posicion_palabra+1


        if dato==1:
            posicion_circulo_final=1
            if palabra != posicion_palabra_final:
                aprobado = 3
            else:
                aprobado = 2
            return render(request, "1.html", {'palabra': palabra_final,
                                            'posicion_palabra': posicion_palabra,
                                            'aprobado': aprobado,
                                            'posicion_circulo': posicion_circulo_final, })

        if posicion_circulo==1:
            if letra==1:
                posicion_circulo_final=3
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "3.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==0:
                posicion_circulo_final = 2
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "2.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
        elif posicion_circulo==2:
            if letra==1:
                posicion_circulo_final=4
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 1
                return render(request, "4.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==0:
                posicion_circulo_final = 2
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "2.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
        elif posicion_circulo==3:
            if letra==1:
                posicion_circulo_final=3
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "3.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==0:
                posicion_circulo_final = 4
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 1
                return render(request, "4.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
        elif posicion_circulo==4:
            if letra==1:
                posicion_circulo_final=2
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "2.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==0:
                posicion_circulo_final = 1
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "1.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })