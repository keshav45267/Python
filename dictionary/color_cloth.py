# program to print the color and cloth item in wardrobe
# red shirt, blue shirt

wardrobe = {"shirt":["red","blue","white"],
			 "jeans":["blue","black"]}
print('Color\t Item')
for cloth in wardrobe:
	for color in wardrobe[cloth]:
		print("{} \t {}".format(color,cloth))