from pylab import *
import imageio as im


def show_img(image, img_title=""):
    """
    Old and poorly-written function for displaying images.
    Need to provide images:
    * peppers_mono.png
    * znak4.png (with smaller resolution than peppers_mono.png)

    Prosta funkcja do wyswietlania obrazu.
    img - obraz do wyswilab2_zad1etlenia,
    monochromatyczny, z wartosciami pikseli z przedzialu [0.0, 1.0] lub
    calkowitymi z przedzialu [0, 255]
    imgTitle - tytul obrazu; opcjonalny, wartosc domyslna: '' (tekst pusty)
    """
    figure()
    axis("off")
    title(img_title)
    vmax = 1.0  # domyslnie - obrazy float
    if "int" in str(image.dtype):  # ale jesli obrazy int, to zakres do 255
        vmax = 255.0
    imshow(image, cmap=cm.gray, vmin=0, vmax=vmax)


def main():

    # wczytanie obrazow funkcja imread
    img = im.imread("peppers_mono.png")
    symb = im.imread("znak4.png")

    # wyswietlenie formatow danych, obrazow i rozdzielczosci
    print("Img:", img.dtype)
    print("Znak:", symb.dtype)
    show_img(img, "Obraz wyjsciowy")
    show_img(symb, "Znak")
    print("Wymiary obrazu oryginalnego", img.shape[0], " na ", img.shape[1])
    print("Wymiary znaku oryginalnego:", symb.shape[0], " na ", symb.shape[1])

    # przetworzenie znaku na wektor i dodanie iteratora po tym wektorze
    symb_heigth = symb.shape[0]
    symb_width = symb.shape[1]
    symb = reshape(symb, -1)
    bytes_in_symb = len(symb)
    index = 0

    # wyzerowanie LSB w calym obrazie
    img_out = img & 0xFE

    # osadzanie znaku
    for img_row in range(0, int(img.shape[0] / 4)):  # range(0, 128)
        for img_col in range(0, int(img.shape[1] / 4)):
            for row in range(
                4 * img_row, 4 * img_row + 4
            ):  # obraz-host podzielony na blok 4 x 4
                for col in range(4 * img_col, 4 * img_col + 4):
                    if (
                        index > bytes_in_symb - 1
                    ):  # jesli "skonczyl sie" wstawiany symbol, to zaczynamy go od nowa
                        index = 0
                    if symb[index] == 0xFF:  # jesli kolejny bit w wektorze jest "bialy"
                        img_out[
                            row, col
                        ] |= 0x01  # ustawienie LSB na 1 dla piksela [row, col]
            index += 1
    show_img(img_out, "Obraz ze znakiem")

    # odczytanie znaku
    how_many_copies = img.shape[0] * img.shape[1] / bytes_in_symb / 16
    symb_read = symb & 0x0
    symb_copies = np.empty((int(bytes_in_symb), int(how_many_copies)), dtype=int)
    index = 0
    block_of_16 = 0
    copy = 0
    for img_row in range(0, int(img_out.shape[0] / 4)):
        for img_col in range(0, int(img_out.shape[1] / 4)):
            for row in range(4 * img_row, 4 * img_row + 4):
                for col in range(4 * img_col, 4 * img_col + 4):
                    if (
                        img_out[row, col] & 0x01
                    ):  # wyciagniecie sredniej wartosci z bloku 16 bitow
                        block_of_16 += 1

            if (
                block_of_16 / 16
            ) > 0.5:  # sprawdzenie czy w bloku wystapilo wiecej 0 czy 1
                symb_copies[index, copy] = 0xFF
            else:
                symb_copies[index, copy] = 0

            block_of_16 = 0
            index += 1
            if index > bytes_in_symb - 1:
                index = 0
                copy += 1

    # wyciagnienie sredniej ze wszystkich kopii obrazu ukrytego
    for index in range(0, bytes_in_symb):
        if sum(symb_copies[index]) > 128 * how_many_copies:
            number = 0xFF
        else:
            number = 0

        symb_read[index] = number

    # wyswietlenie odczytanego znaku
    symb_read = reshape(symb_read, (symb_width, symb_width))
    show_img(symb_read, "Znak odczytany")
    imsave("Znak odczytany.png", symb_read, format="png", cmap=cm.gray)
    show()


if __name__ == "__main__":
    main()
