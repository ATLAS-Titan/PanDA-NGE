#!/bin/bash
module load boost
module load fftw
module load cudatoolkit
module use --append /lustre/atlas/world-shared/bip103/modules
module load openmpi/STATIC
module load gcc
module use --append /lustre/atlas/world-shared/csc230/openmpi/modules/
module load openmpi/2017_05_04_539f71d
$2/gmx_mpi mdrun -ntomp 1 -nb cpu -s topol.tpr -c out.gro
cd ..
mkdir -p $1/$RP_SESSION_ID ; mv $RP_UNIT_ID $1/$RP_SESSION_ID
