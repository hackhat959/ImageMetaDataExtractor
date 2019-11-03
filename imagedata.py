import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def getMetaData(imgname, out):
    try:
        #Empty Dict
        metaData = {}

        imgFile = Image.open(imgname)
        print ("Getting meta data...")
        info = imgFile._getexif()
        if info:
            print ("found meta data!")
            for (tag, value) in info.items():
                tagname = TAGS.get(tag, tag)
                metaData[tagname] = value
                if not out:
                    print (tagname, value)

            if out:
                print ("Outputting to file...")
                with open(out, 'w') as f:
                    for (tagname, value) in metaData.items():
                        f.write(str(tagname)+"\t"+\
                            str(value)+"\n")
        
    except:
        print ("Failed")

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("img", help="Image Name ")
    parser.add_argument("--output","-o", help="dump data to txt.")
    args = parser.parse_args()
    if args.img:
        getMetaData(args.img, args.output)
    else:
        print (parser.usage)

if __name__ == '__main__':
    Main()



import argparse

parser = argparse.ArgumentParser()
parser.add_argument("lat", help="Latitude values in D,M,S")
parser.add_argument("lon", help="Longitude values in D,M,S")
args = parser.parse_args()

if args.lat and args.lon:
    lat = args.lat.split(',')
    lon = args.lon.split(',')

    dlat = int(lat[0]) + (int(lat[1])/60.0) + (int(lat[2])/3600.0)
    dlon = int(lon[0]) + (int(lon[1])/60.0) + (int(lon[2])/3600.0)

    print (dlat, dlon)

else:
    print (parser.usage)

