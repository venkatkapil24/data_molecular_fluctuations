This directory contains the following subdirectories:

codes:
Contains a copy of the i-PI code used to run the simulations.

scripts:
Contains the scripts used for preparing inputs for free energy calculations.

structures:
Contains the starting crystal structures of the different polymorphs of benzene, succinic acid, and glycine.

dft_input_files:
Contains sample FHI-AIMS and Quantum Espresso inputs for the different polymorphs of benzene, succinic acid, and glycine. To perform analogous simulations for different configurations, the atomic positions, numbers of atoms, and k-point grids must be adapted accordingly. Note that the k-point grids used are stored in the Materials Cloud archive.

B-I:
Contains the inputs for running path integral free energy calculations for form I of benzene and an analysis script for calculating free energies, which can be used as templates for running and analysing simulations for all other polymorphs.

potentials:
Contains the files describing the N2P2 neural network potential for benzene at PBE-TS and PBE0-MBD levels of theory.
