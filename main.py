import cv2
import pylibdmtx.pylibdmtx as dmtx

def scan_dmatrix(source):
    # Carregue a imagem do datamatrix
    img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)

    # Defina as coordenadas (superior, esquerda, inferior, direita)
    coordenadas = (2170, 2279, 2170 + 1178, 2279 + 1178)  # EPP
    # coordenadas = (1382, 2197, 1382 + 178, 2197 + 178)  # ECU

    # Corte a imagem
    img_cortada = img[coordenadas[1]:coordenadas[3], coordenadas[0]:coordenadas[2]]

    # Decodifique o datamatrix
    data = dmtx.decode(img_cortada)

    # Imprima o conteúdo do datamatrix
    result = data[0].data.decode()
    return result

# print(scan_dmatrix("epp.jpg"))