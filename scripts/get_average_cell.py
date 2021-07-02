import sys
import numpy as np
from ipi.utils.io import read_file_raw

def get_average_structure(trajfilename, reffilename):
  """
  Reads an i-pi trajectory file, averages
  the the cell, and rescales a reference structure
  with the average cell structure.
	"""

  ext = trajfilename.split(".")[-1]
  prefix = ".".join(trajfilename.split(".")[0:-1])

  filename = open(trajfilename)
  iframe = 0

  avg_h = np.zeros((3,3))

  while True:
      try:
        frame_dict = read_file_raw("xyz", filename)
      except:

        frame_dict = read_file_raw("xyz", open(reffilename))
        q =  frame_dict["data"]
        h =  frame_dict["cell"]
        c =  frame_dict["comment"]
        n =  frame_dict["names"]

        nat = int(len(q) / 3)
        q = q.reshape((nat, 3))
        ih = np.linalg.inv(h)
        qs = np.dot(q, ih)

        h = avg_h / iframe
        q = np.dot(qs, h)
        print nat
        print "# CELL(H): %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f " % (h[0,0], h[0,1], h[0,2], h[1,0], h[1,1], h[1,2], h[2,0], h[2,1], h[2,2]), " ".join([ic for ic in c.split(" ") if "{" in ic ]),
        for i in range(nat):
          print "%s %10.5f %10.5f %10.5f " % (n[i], q[i][0], q[i][1], q[i][2])
        break

      h = frame_dict["cell"]
      avg_h += h 
      iframe += 1

args = sys.argv[1:]
get_average_structure(args[0], args[1])

