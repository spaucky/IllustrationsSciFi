from pinscrape import pinscrape

keywords_art = ['plant art drawing','plant art','plant art work','floral art','botanical painting','nature art','nature artwork','whimsical plants']
keywords_scientific = ['plant scientific illustration','scientific illustration plants','plant diagram','diagram plants','botanical drawing','floral scientific illustration','botanical line drawing','plant anatomy','botanical illustration','botanical floral illustration']
keywords_art_img_num = [0] * len(keywords_art)
keywords_scientific_img_num = [0] * len(keywords_scientific)

for i in range(len(keywords_art)):
    plant_art = pinscrape.scraper.scrape(keywords_art[i], "PlantArt", max_images=1000)
    keywords_art_img_num[i] = len(plant_art['url_list'])

for j in range(len(keywords_scientific)):
    plant_scientific = pinscrape.scraper.scrape(keywords_scientific[i], "PlantScientific", max_images=1000)
    keywords_scientific_img_num[i] = len(plant_scientific['url_list'])

total_plant_art = sum(keywords_art_img_num)
total_scientific_art = sum(keywords_scientific_img_num)

print('Total artistic plant drawings: ' + str(total_plant_art))
print('Total plant scientific illustrations: ' + str(total_scientific_art))