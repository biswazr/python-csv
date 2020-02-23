#! /bin/bash

for f in Ligand_*.pdbqt; do
    b=`basename $f .pdbqt`
    echo Processing ligand $b
    mkdir -p $b
    /home/aduri/bibhu/autodock_vina_1_1_2_linux_x86/bin/vina --config conf.txt --ligand $f --out ${b}/out.pdbqt --log ${b}/log.txt
    rm $b.pdbqt
done
