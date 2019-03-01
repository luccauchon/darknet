: "${VAL_GPU?GPU to use.}": "${BACKUPDIR?directory for weights.}": "${OUTPUTFILE?result file.}" 

for value in {100..1000..100}
do    
  echo $value    
  ./darknet -i $VAL_GPU detector recall data/odema.data cfg/yolo-voc.2.odema.cfg $BACKUPDIR/yolo-voc_$value.weights &>> $OUTPUTFILE
done

for value in {1000..60000..1000}
do
  echo $value
  ./darknet -i $VAL_GPU detector recall data/odema.data cfg/yolo-voc.2.odema.cfg $BACKUPDIR/yolo-voc_$value.weights &>> $OUTPUTFILE
done

