from django.shortcuts import render


def automatas(request):
    # Render  administracion.html
    if request.method == 'GET':
        gato='1'

        return render(request, "automatas.html", {'gato': gato,})



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
                aprobado = 3
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



def grafico_afnd(request):
    # Render  administracion.html
    if request.method == 'GET':
        gato='1'

        return render(request, "afnd.html", {'gato': gato,})
    elif request.method == 'POST':
        try:
            inicio = request.POST['inicio']
            dato=1
        except:
            dato=2
        palabra = len(request.POST['palabra'])
        caminos = request.POST['caminos']
        camino_actual = request.POST['camino_actual']
        palabra_final = request.POST['palabra']
        posicion_palabra = int(request.POST['posicion_palabra'])
        posicion_circulo = int(request.POST['posicion_circulo'])
        if posicion_palabra==palabra:
            if caminos=='2' and camino_actual=='1':
                camino_actualizado='2'
                aprobado = 3
                posicion_palabra=0
                posicion_circulo_final = 1
                return render(request, "1afnd.html", {'palabra': palabra_final,
                                                      'posicion_palabra': posicion_palabra,
                                                      'aprobado': aprobado,
                                                      'caminos': caminos,
                                                      'camino_actual': camino_actualizado,
                                                      'posicion_circulo': posicion_circulo_final, })
            else:
                aprobado = 4
                posicion_circulo_final = posicion_circulo
                renderizado=str(posicion_circulo)+'afnd.html'
                return render(request, renderizado, {'palabra': palabra_final,
                                                      'posicion_palabra': posicion_palabra,
                                                      'aprobado': aprobado,
                                                      'caminos': caminos,
                                                      'camino_actual': camino_actual,
                                                      'posicion_circulo': posicion_circulo_final, })
        letra = int(str(request.POST['palabra'])[posicion_palabra])
        posicion_palabra_final=posicion_palabra+1


        if dato==1:
            if palabra_final[0]=='0':
                caminos='2'
                camino_actual='1'
            else:
                caminos='1'
                camino_actual = '1'
            posicion_circulo_final=1
            if palabra != posicion_palabra_final:
                aprobado = 3
            else:
                aprobado = 3
            return render(request, "1afnd.html", {'palabra': palabra_final,
                                            'posicion_palabra': posicion_palabra,
                                            'aprobado': aprobado,
                                            'caminos': caminos,
                                            'camino_actual': camino_actual,
                                            'posicion_circulo': posicion_circulo_final, })


        if posicion_circulo==1:
            if letra==0:
                if camino_actual=='1':
                    caminos = '2'
                    posicion_circulo_final = 2
                    if palabra != posicion_palabra_final:
                        aprobado = 3
                    else:
                        aprobado = 2
                    return render(request, "2afnd.html", {'palabra': palabra_final,
                                                      'posicion_palabra': posicion_palabra_final,
                                                      'aprobado': aprobado,
                                                      'caminos': caminos,
                                                      'camino_actual': camino_actual,
                                                      'posicion_circulo': posicion_circulo_final, })
                else:
                    posicion_circulo_final = 3
                    if palabra != posicion_palabra_final:
                        aprobado = 3
                    else:
                        aprobado = 1
                    return render(request, "3afnd.html", {'palabra': palabra_final,
                                                          'posicion_palabra': posicion_palabra_final,
                                                          'aprobado': aprobado,
                                                          'caminos': caminos,
                                                          'camino_actual': camino_actual,
                                                          'posicion_circulo': posicion_circulo_final, })

            elif letra==1:
                posicion_circulo_final = 3
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 1
                return render(request, "3afnd.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                'caminos': caminos,
                                                'camino_actual': camino_actual,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==2:
                posicion_circulo_final = 1
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "1afnd.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                'caminos': caminos,
                                                'camino_actual': camino_actual,
                                                  'posicion_circulo': posicion_circulo_final, })
        elif posicion_circulo==2:
            if letra==1 or letra==2:
                posicion_circulo_final=2
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "2afnd.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                      'caminos': caminos,
                                                      'camino_actual': camino_actual,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==0:
                posicion_circulo_final = 3
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 1
                return render(request, "3afnd.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                      'caminos': caminos,
                                                      'camino_actual': camino_actual,
                                                  'posicion_circulo': posicion_circulo_final, })
        elif posicion_circulo==3:
            if letra==0:
                posicion_circulo_final=3
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 1
                return render(request, "3afnd.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'caminos': caminos,
                                                  'camino_actual': camino_actual,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==1 or letra==2:
                posicion_circulo_final = 3
                posicion_palabra_final=palabra
                aprobado=2
                return render(request, "3afnd.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                      'caminos': caminos,
                                                      'camino_actual': camino_actual,
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



def grafico_afndlamda(request):
    # Render  administracion.html
    if request.method == 'GET':
        gato='1'

        return render(request, "afndlamda.html", {'gato': gato, })
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
                aprobado = 3
            return render(request, "1afndlamda.html", {'palabra': palabra_final,
                                            'posicion_palabra': posicion_palabra,
                                            'aprobado': aprobado,
                                            'posicion_circulo': posicion_circulo_final, })

        if posicion_circulo==1:
            if letra==1 :
                posicion_circulo_final = 3
                posicion_palabra_final=palabra
                aprobado=2
                return render(request, "1afndlamda.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==2:
                posicion_circulo_final=1
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "1afndlamda.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==0:
                posicion_circulo_final = 2
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "2afndlamda.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
        elif posicion_circulo==2:
            if letra==1:
                posicion_circulo_final=3
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 1
                return render(request, "3afndlamda.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==0:
                posicion_circulo_final = 2
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "2afndlamda.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
            elif letra==2:
                posicion_circulo_final = 1
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "1afndlamda.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
        elif posicion_circulo==3:
            if letra==1 or letra==2 or letra==0:
                posicion_circulo_final=3
                if palabra != posicion_palabra_final:
                    aprobado = 3
                else:
                    aprobado = 2
                return render(request, "3afndlamda.html", {'palabra': palabra_final,
                                                  'posicion_palabra': posicion_palabra_final,
                                                  'aprobado': aprobado,
                                                  'posicion_circulo': posicion_circulo_final, })
