import numpy as np
import sys
import ase
import ase.io as aio

def make_lammps_data(filename):
    """
    Reads a self respecting file type and creates a LAMMPS data file which specifies cell, masses and atoms.
    """
    a = aio.read(filename)

    species = a.arrays['numbers']
    unique_species, i_unique_species  = np.unique(species,  return_index=True)
    scaled_positions= a.get_scaled_positions()
    cell = a.get_cell_lengths_and_angles()
    
    a = ase.Atoms(species, scaled_positions=scaled_positions, cell=cell)

    masses = a.get_masses()
    positions = a.get_positions()

    lammps_indices = species.copy()
    for ii in range(len(unique_species)):
        lammps_indices[species == unique_species[ii]] = ii + 1

    ((hxx, hxy, hxz), (hyx, hyy, hyz) , (hzx, hzy, hzz)) = a.get_cell().T
    #print (a.get_cell())
    #print (venkat)


    print("LAMMPS data file generated get_lammps_data.py [VK]")
    print( "")
    print( len(species), "atoms")
    print( len(unique_species), "atom types")
    print( "")
    print( "0.0", hxx, "xlo xhi")
    print( "0.0", hyy, "ylo yhi")
    print( "0.0", hzz, "zlo zhi")
    print( hxy, hxz, hyz, "xy xz yz")
    print( "")
    print( "Masses")
    print( "")
    for ii in range(len(unique_species)):
        print( lammps_indices[i_unique_species[ii]], masses[i_unique_species[ii]])
    print( "")
    print( "Atoms")
    print( "")
    for ii in range(len(species)):
        print ("%5d %5d %s" % (ii + 1, lammps_indices[ii], "  ".join(map(str, positions[ii]))) )
    print("")

make_lammps_data(sys.argv[1:][-1])
