import pyautogui
from time import *
from PyPDF2 import *

def esperar_imagem_aparecer(imagem, timeout=30):
    start_time = time()

    while time() - start_time < timeout:
        try:
        
            posicao = pyautogui.locateOnScreen(imagem)

            if posicao is not None:
                return posicao

        except pyautogui.ImageNotFoundException:
    
            sleep(1)

    return None

nome_arquivo = pyautogui.prompt(text='Copie e cole o nome do arquivo aqui!')

if(nome_arquivo == None):
    pyautogui.alert(text='Operação cancelada!')
else:
    password = pyautogui.password(text='Digita a senha do token', mask='*')
    if(password == None or password != '1234'):
        pyautogui.alert(text='Operação cancelada!')
    else:

        pdf_files = open('C:\\Users\\iago.vieira\\Documents\\documentos a assinar\\' + nome_arquivo + ".pdf", '+rb')
        dados_do_pdf = PdfReader(pdf_files)
        
        for i in range(len(dados_do_pdf.pages)):
            if(i == 0):
                pyautogui.click(36,735, duration=0.5)
                pyautogui.click(133,93, duration=0.5)
                pyautogui.write('serpro')
                pyautogui.click(147,233, duration=0.5)

                try:
                    posicao_button_assinar = esperar_imagem_aparecer('image.png')

                    if posicao_button_assinar is not None:
                        pyautogui.click(posicao_button_assinar)
                        sleep(1.5)
                        pyautogui.doubleClick(501,217, duration=0.5)
                        pyautogui.click(428,219, duration=0.5)
                        pyautogui.click(976,518, duration=0.5)
                        pyautogui.click(1029,343, duration=4)
                        sleep(2)
                        pyautogui.drag(0,200, duration=0.5)
                        pyautogui.click(764,525, duration=0.5)
                        pyautogui.click(745,690, duration=0.5)

                        try:
                            posicao_button_jessica = esperar_imagem_aparecer('jessica.png')
                            if posicao_button_jessica is not None:
                                pyautogui.click(posicao_button_jessica)
                                pyautogui.click(956,508, duration=0.5)
                                pyautogui.click(672,343, duration=0.5)
                                sleep(0.5)
                                pyautogui.write('1234')
                                pyautogui.press('enter')
                                pdf_files.close()
                                sleep(1)
                                pyautogui.click(654,406, duration=0.1)
                                sleep(1)
                                pyautogui.click(700,405, duration=0.1)
                            else:
                                print("A imagem não foi encontrada dentro do tempo limite.")
                        except pyautogui.FailSafeException:
                            print("Operação interrompida devido à ativação do fail-safe (movimento do mouse para o canto superior esquerdo).")
                        except Exception as e:
                            print(f"Erro: {e}")
                    
                    else:
                        print("A imagem não foi encontrada dentro do tempo limite.")
                except pyautogui.FailSafeException:
                    print("Operação interrompida devido à ativação do fail-safe (movimento do mouse para o canto superior esquerdo).")
                except Exception as e:
                    print(f"Erro: {e}")
            else:
                pyautogui.click(36,735, duration=0.5)
                pyautogui.click(133,93, duration=0.5)
                pyautogui.write('serpro')
                pyautogui.click(147,233, duration=0.5)

                try:
                    posicao_button_assinar = esperar_imagem_aparecer('image.png')

                    if posicao_button_assinar is not None:
                        pyautogui.click(posicao_button_assinar)
                        sleep(1.5)
                        pyautogui.doubleClick(501,217, duration=0.5)
                        pyautogui.click(428,219, duration=0.5)
                        pyautogui.click(976,518, duration=0.5)
                        pyautogui.click(1029,343, duration=4)
                        sleep(2)
                        pyautogui.drag(0,200, duration=0.5)
                        for next in range(i):
                            pyautogui.click(626,647, duration=0.2)
                        pyautogui.click(764,525, duration=0.5)
                        pyautogui.click(745,690, duration=0.5)

                        try:
                            posicao_button_jessica = esperar_imagem_aparecer('jessica.png')
                            if posicao_button_jessica is not None:
                                pyautogui.click(posicao_button_jessica)
                                pyautogui.click(956,508, duration=0.5)
                                pyautogui.click(672,343, duration=0.5)
                                sleep(1)
                                pyautogui.write('1234')
                                pyautogui.press('enter')
                                sleep(1)
                                pyautogui.click(654,406, duration=0.1)
                                sleep(1)
                                pyautogui.click(700,405, duration=0.1)
                            else:
                                print("A imagem não foi encontrada dentro do tempo limite.")
                        except pyautogui.FailSafeException:
                            print("Operação interrompida devido à ativação do fail-safe (movimento do mouse para o canto superior esquerdo).")
                        except Exception as e:
                            print(f"Erro: {e}")
                    
                    else:
                        print("A imagem não foi encontrada dentro do tempo limite.")
                except pyautogui.FailSafeException:
                    print("Operação interrompida devido à ativação do fail-safe (movimento do mouse para o canto superior esquerdo).")
                except Exception as e:
                    print(f"Erro: {e}")
