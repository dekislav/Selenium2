#convertng the buggy jpg to binary string
def image_bin(image_path):
    with open("buggy.jpg", "rb") as image:
        binary_string = image.read()
    return binary_string

image_path = "buggy.jpg"
binary_string = image_bin("buggy.jpg")
print(binary_string)
with open("binary_image.bin", "wb") as binary_file:
    binary_file.write(binary_string)
print(f"Binary image saved to: {image_path}")
