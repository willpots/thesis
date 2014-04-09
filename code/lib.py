class BoundingBox():

  def __init__(self,lat1,lng1,lat2,lng2):
    if lat1 > lat2:
      self.max_lat = lat1
      self.min_lat = lat2
    else:
      self.max_lat = lat2
      self.min_lat = lat1
    if lng1 > lng2:
      self.max_lng = lng1
      self.min_lng = lng2
    else:
      self.max_lng = lng2
      self.min_lng = lng1


  def contains(self, lat, lng):
    if lat < self.max_lat and lat > self.min_lat and lng < self.max_lng and lng > self.min_lng:
      return true
    else:
      return false


# class Database():

#   def __init__(self, filename):
#     self.conn = sqlite3.connect(filename)


#   def select(self, bounding_box=None):

# class Dataset():
#   def __init__(self, cursor):
#     self.data = 