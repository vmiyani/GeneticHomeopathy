from PIL import Image

img = Image.open('/Users/vikasm/.gemini/antigravity/brain/9063df35-66a1-411b-8412-c14b96b03527/media__1775510177400.jpg')
print("Original size:", img.size)

img = img.convert("RGBA")
datas = img.getdata()

# Cleanly remove white background with anti-aliasing approximation
newdata = []
for item in datas:
    brightness = sum(item[0:3]) / 3
    if brightness > 250:
        newdata.append((255, 255, 255, 0)) # Fully transparent
    elif brightness > 220:
        alpha = int((250 - brightness) / 30 * 255)
        newdata.append((item[0], item[1], item[2], alpha))
    else:
        newdata.append(item)

img.putdata(newdata)

# The cursive text is bleeding in because 60% crop was too low. The text starts around 55%.
# Let's crop it tightly to 52% of the image.
crop_y = int(img.size[1] * 0.52)
tree_img = img.crop((0, 0, img.size[0], crop_y))

# Trim the transparent borders to get actual bounding box of the icon
bbox = tree_img.getbbox()
if bbox:
    tree_img = tree_img.crop(bbox)

tree_img.save('/Users/vikasm/Work/GeneticHomeopathy/assets/images/logo-icon.png')
print("Cropped tree image saved over logo-icon.png")
