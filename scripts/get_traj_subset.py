import sys
import numpy as np
from ipi.utils.io import read_file_raw

def get_average_structure(trajfilename, stride):
  """
  Reads an i-pi trajectory file, and prints out
  the structure every $stride steps.
	"""

  ext = trajfilename.split(".")[-1]
  prefix = ".".join(trajfilename.split(".")[0:-1])

  filename = open(trajfilename)
  iframe = 0

  stride = int(stride)

  while True:
        frame_dict = read_file_raw("xyz", filename)

        if iframe % stride != 0 or iframe == 0:
          iframe +=1 
          continue

        q =  frame_dict["data"]
        h =  frame_dict["cell"]
        c =  frame_dict["comment"]
        n =  frame_dict["names"]

        nat = int(len(q) / 3)
        q = q.reshape((nat, 3))

        print nat
        print "# CELL(H): %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f " % (h[0,0], h[0,1], h[0,2], h[1,0], h[1,1], h[1,2], h[2,0], h[2,1], h[2,2]), " ".join([ic for ic in c.split(" ") if "{" in ic ]),
        for i in range(nat):
          print "%s %10.5f %10.5f %10.5f " % (n[i], q[i][0], q[i][1], q[i][2])

        iframe += 1

args = sys.argv[1:]
get_average_structure(args[0], args[1])

