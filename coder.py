from PIL import Image
import numpy as np

end = 255
locate = [(123, 231, 132), (50, 200, 90)]
change = 3

def open_image(path):
    return Image.open(path).convert("RGB")


def image_to_data(img):
    pix = np.array(img)
    return pix.reshape(-1, 3)


def encode(text, path):
    data = list(text.encode("utf-8")) + [end]

    img = open_image(path)
    pix = image_to_data(img)
    width, height = img.size

    capacity_bytes = width * height * 2
    if len(data) > capacity_bytes:
        print(f"❌ Текст завеликий! Можна вмістити максимум {capacity_bytes} символів.")
        return

    bit_parts = []
    for byte in data:
        bit_parts.append((byte >> 0) & 0b11)
        bit_parts.append((byte >> 2) & 0b11)
        bit_parts.append((byte >> 4) & 0b11)
        bit_parts.append((byte >> 6) & 0b11)
    
    bit_parts_iter = iter(bit_parts)

    colors = iter(pix)
    new_img = Image.new("RGB", (width * 2, height * 2))
    pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            try:
                basik = tuple(map(int, next(colors)))
            except StopIteration:
                basik = (0, 0, 0)

            pixels[x*2, y*2] = basik

            for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                r_base, g_base, b_base = basik
                new_r, new_g, new_b = r_base, g_base, b_base

                try:
                    part_r = next(bit_parts_iter)
                    new_r = (r_base + part_r) % 256
                except StopIteration:
                    part_r = 0
                    
                try:
                    part_g = next(bit_parts_iter)
                    new_g = (g_base + part_g) % 256
                except StopIteration:
                    part_g = 0

                try:
                    part_b = next(bit_parts_iter)
                    new_b = (b_base + part_b) % 256
                except StopIteration:
                    part_b = 0

                pixels[x*2 + dx, y*2 + dy] = (new_r, new_g, new_b)

    pixels[0, new_img.height - 1] = locate[0]
    pixels[1, new_img.height - 1] = locate[1]

    new_img.save("encoded.png")
    print("✅ Текст закодовано у encoded.png")


def decode(path):
    img = open_image(path)
    pixels = img.load()
    width, height = img.size

    if pixels[0, height - 1] != locate[0] or pixels[1, height - 1] != locate[1]:
        print("❌ У цьому зображенні немає зашифрованого тексту.")
        return

    decoded_bit_parts = []
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            base_r, base_g, base_b = pixels[x, y]

            for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                modified_r, modified_g, modified_b = pixels[x+dx, y+dy]

                part_r = (modified_r - base_r + 256) % 256
                part_g = (modified_g - base_g + 256) % 256
                part_b = (modified_b - base_b + 256) % 256
                
                decoded_bit_parts.append(part_r % 4)
                decoded_bit_parts.append(part_g % 4)
                decoded_bit_parts.append(part_b % 4)

    decoded_bytes = []
    current_byte = 0
    bit_count = 0
    
    for part in decoded_bit_parts:
        current_byte |= (part << bit_count)
        bit_count += 2
        if bit_count == 8:
            if current_byte == end:
                break
            decoded_bytes.append(current_byte)
            current_byte = 0
            bit_count = 0
        elif bit_count > 8:
            break

    text = bytes(decoded_bytes).decode("utf-8", errors="ignore")
    print("✅ Розкодований текст:\n", text)
    return


if __name__ == "__main__":
    mode = input("Вибери режим (e - encode, d - decode): ").strip().lower()
    path = input("Шлях до картинки: ").strip()

    if mode == "e":
        img = open_image(path)
        width, height = img.size
        capacity = width * height * 2
        print(f"ℹ️ У це зображення можна зашифрувати до {capacity} символів.")
        text = input("Текст: ")
        encode(text, path)

    elif mode == "d":
        decode(path)

    else:
        print("❌ Невідомий режим!")