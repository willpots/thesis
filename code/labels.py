import shapefile
import ogr


def get_label(row):
  lat, lng = row[3], row[4]
  # 0 to 36
  newlng = round((lng + 180) / 10)
  # 0 to 18
  newlat = round((lat + 90) / 10)
  return str(int(newlat))+"_"+str(int(newlng))

def majority_label(labels):
  counts = {}
  for label in labels:
    if label in counts:
      counts[label] += 1
    else:
      counts[label] = 1
  max_label = None
  max_value = -1
  for label in counts:
    if counts[label] > max_value:
      max_value = counts[label]
      max_label = label
  return max_label, max_value

def fips_label(row):
  return row[8]
# Code from http://stackoverflow.com/questions/7861196/check-if-a-geopoint-with-latitude-and-longitude-is-within-a-shapefile
def state_label(row):
  lat, lng = row[3], row[4]
  drv = ogr.GetDriverByName('ESRI Shapefile') #We will load a shape file
  ds_in = drv.Open("states/states.shp")    #Get the contents of the shape file
  lyr_in = ds_in.GetLayer(0)    #Get the shape file's first layer
  idx = lyr_in.GetLayerDefn().GetFieldIndex("STATEFP")

  geo_ref = lyr_in.GetSpatialRef()
  point_ref=ogr.osr.SpatialReference()
  point_ref.ImportFromEPSG(4236)
  ctran=ogr.osr.CoordinateTransformation(point_ref,geo_ref)

  def check(lon, lat):
    #Transform incoming longitude/latitude to the shapefile's projection
    [lon,lat,z]=ctran.TransformPoint(lon,lat)

    #Create a point
    pt = ogr.Geometry(ogr.wkbPoint)
    pt.SetPoint_2D(0, lon, lat)

    #Set up a spatial filter such that the only features we see when we
    #loop through "lyr_in" are those which overlap the point defined above
    lyr_in.SetSpatialFilter(pt)

    #Loop through the overlapped features and display the field of interest
    if(len(lyr_in)):
      for feat_in in lyr_in:
        return feat_in.GetFieldAsString(idx)
    else:
      return -1

  #Take command-line input and do all this
  return check(float(lng),float(lat))
  #check(-95,47)
