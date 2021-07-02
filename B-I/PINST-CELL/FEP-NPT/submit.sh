#!/bin/bash 
# ----- SLURM JOB SUBMIT SCRIPT -----
#SBATCH --export=ALL
#SBATCH --error=slurm.%J.err
#SBATCH --output=slurm.%J.out
#SBATCH --exclusive
################ CHANGE this section  (begin) ##########################
# -- job info --
#SBATCH --account=s1000
#SBATCH --job-name=PINST-CELL-B-I-NPT
#SBATCH --time=24:00:00
#SBATCH --partition=normal
# -- number of nodes --
#SBATCH --nodes=1               # of nodes            (default =  1)
#SBATCH --ntasks-per-node=1     # of MPI tasks/node   (default = 12)
#SBATCH --cpus-per-task=12      # of OMP threads/task (default =  1)
#SBATCH --ntasks-per-core=1     # HT (default = 1, HyperThreads = 2)
#SBATCH --constraint=gpu
# -- the program and input file (basename) --

module unload daint-mc
module load daint-gpu
module load GSL/2.5-CrayCCE-19.10

source ~/.bashrc

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

ipi=/users/kvenkat/source/i-pi-vk/bin/i-pi
lmp=/users/kvenkat/source/lammps/src/lmp_serial

rm /tmp/ipi_*

HOST=$(hostname)

if [ -f "RESTART" ]; then
${ipi} RESTART > log.i-pi &
else
${ipi} input.xml > log.i-pi &
fi

sleep 30;

for x in {1..1}
do
${lmp} < in.lmp > /dev/null &
done

wait

