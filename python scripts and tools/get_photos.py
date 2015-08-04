import urllib2

"""
This script was only created to extract a several
photos, in jpg format, from an internal website.
It was a very quick script I made only for the
purpose decribe before.
"""

web_not_found = 0
web_found = 0

for num_photo in range(7277, 7630):
    web_page = r'http://ntpnoapps0301.corp.codetel.com.do/intranet/Fotos_premio_al_logro_2010/content/images/large/IMG_' + str(num_photo) + '.jpg'
    print 'Opening ' + web_page
    archive_name = 'IMG_' + str(num_photo) + '.jpg'
    try:
        url = urllib2.urlopen(r'http://ntpnoapps0301.corp.codetel.com.do/intranet/Fotos_premio_al_logro_2010/content/images/large/IMG_' + str(num_photo) + '.jpg')
        web_found += 1
    except Exception, e:
        web_not_found += 1
        continue
    fp = open(r'C:\\Documents and Settings\\Roberto Zapata\\My Documents\\ISC\\Premios al logro 2010\\' + archive_name, 'wb')
    fp.write(url.read())
    fp.close()
    url.close()



print "Stats"
print "Web pages found ", str(web_found)
print "Web pages not found ", str(web_not_found)

                          
                         

