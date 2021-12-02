import cv2

#Menentukan file path gambar
filepath = 'belajar_opencv\\images\\popcat.jpg'
#Membaca gambar
image = cv2.imread(filepath)
#Menampilkan gambar
cv2.imshow("Gambar popcat.jpg", image)
cv2.waitKey(0)
#Menyimpan gambar
output = 'belajar_opencv\\hasil\\popcat_simpan.jpg'
cv2.imwrite(output, image)
print("Gambar berhasil disimpan di {}" .format(output))
