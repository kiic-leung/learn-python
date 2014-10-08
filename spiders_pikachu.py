import urllib2
import urllib
import re

def spiders():
    image_number = 0
    
    for page_number in range(1,9):
        
        site_url = "http://500px.com/search?exclude_nude=true&page="+str(page_number)+"&q=pikachu&type=photos"
        print site_url
        html = urllib2.urlopen(site_url).read()
        
        image_reg_string = r'src="(.*?\.jpg)" '   
        img_reg = re.compile(image_reg_string)
        
        image_list = re.findall(img_reg,html) # find all images that match RE 
                
        for image_url in image_list:
            urllib.urlretrieve(image_url,'picture_%s.jpg' %image_number) # download the teledata
            print "Download %s images" %image_number
            image_number += 1

    print "END"
    
if __name__ == "__main__":
    spiders()
