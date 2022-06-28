import cv2

logo = cv2.imread('logo-if.jpg')
img = cv2.imread('ifma-caxias.jpg')


logo = cv2.resize(logo,(200,100), interpolation=cv2.INTER_AREA)

#obtem quantidade de linhas e colunas
rows, cols = logo.shape[0:2]
#corta a imagem no tammanho da logo
img_crop = img[0:rows, 0:cols]

#Operações
gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(gray,125, 255,cv2.THRESH_BINARY_INV)

#logo sem fundo
logo_tr = cv2.bitwise_and(logo,logo,mask=mask_inv)
#imagem com espaço vazio
img_null = cv2.bitwise_and(img_crop, img_crop,mask = cv2.bitwise_not(mask_inv))
#soma a imagem vazia com a logo sem fundo e adiciona na imagem original
result = cv2.add(img_null, logo_tr)
img[0:rows, 0:cols] = result

cv2.imshow('Original',logo)
cv2.imshow('Mask Inv',logo_tr)
cv2.imshow('NULL',img_null)
cv2.imshow('Com logo',img)

cv2.imwrite('ifmalogo.png', img)
cv2.imwrite('masklogo.png', mask_inv)




cv2.waitKey(0)
cv2.destroyAllWindows()
