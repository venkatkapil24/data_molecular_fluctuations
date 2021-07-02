nat=`head -1 ../GEOP/simulation.pos_0.xyz | awk '{print $1+2}'`
tail -${nat} ../GEOP/simulation.pos_0.xyz 
