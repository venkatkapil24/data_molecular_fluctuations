# Copies the hessian.
cp ../HARM/simulation.phonons.hess hessian.data
echo " #" Copies the hessian

# Copies the initial structure and the LAMMPS data file.
cp ../HARM/init.* .
awk '(NF == 4){print $2, $3, $4}' init.xyz > ref.data
echo " #" Copies the initial configuration 

# Replaces the v_ref in input.xml
vref=`tail -1 ../HARM/simulation.out | awk '{print $2}'`
sed -i "s/v_reference>.*</v_reference> ${vref} </" input.xml
echo " #" Replaces v_ref 

# Replaces the v_ref in input.xml
hsize=`wc -l hessian.data | awk '{print $1-1}'`
sed -i "s/shape=.* mode=/shape='(${hsize},${hsize})' mode=/" input.xml
echo " #" Replaces the size of the Hessian 

i="0"
while read l; do
        ((i=i + 1))

        mkdir ${l}
        echo " #" ${i} Creating directory ${l} and copying i-PI and LAMMPS inputs

        cp input.xml ${l}/input.xml
        cp in*.lmp ${l}/
        cp submit.sh ${l}/

        L1=`echo ${l} | awk '{print $1 + 1e-6}'`
        L2=`echo ${l} | awk '{print 1 - ($1 + 1e-6)}'`

        sed -i "s/xxxixxx/${i}/g" ${l}/submit.sh
        sed -i "s/xxxixxx/${i}/g" ${l}/in-1.lmp
        sed -i "s/xxxixxx/${i}/g" ${l}/in-2.lmp
        sed -i "s/xxxixxx/${i}/g" ${l}/input.xml
        sed -i "s/xxxL1xxx/${L1}/g" ${l}/input.xml
        sed -i "s/xxxL2xxx/${L2}/g" ${l}/input.xml

done < LAMBDAS

