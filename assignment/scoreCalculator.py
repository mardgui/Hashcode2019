filein = open("a_example.txt")
fileout = open("example.out")
nbSlides = int(fileout.readline().replace("\n", ""))
nbPics = int(filein.readline().replace("\n", ""))

photosDesc = {}
cpt = 0
for i in filein:
	line = i.replace("\n", "").split(" ")
	photosDesc[cpt] = line[2:]
	cpt += 1
print(photosDesc)

cpt = 0
prevTags = []
tags = []
totalScore = 0

for i in fileout:
	prevTags = tags
	tags = []
	common = 0
	different1 = 0
	different2 = 0

	line = i.replace("\n", "").split(" ")
	tags.append(photosDesc[int(line[0])])
	if len(line) > 1:
		tags.append(photosDesc[int(line[1])])

	if cpt == 0:
		cpt += 1
		continue

	for x in tags:
		for y in x:
			for z in prevTags:
				if y in z:
					common += 1
				else:
					different1 += 1

	for x in prevTags:
		for y in x:
			for z in tags:
				if y not in z:
					different2 += 1

	totalScore += min(common, different1, different2)

print(totalScore)
