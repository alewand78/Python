echo "Hello, World!" 
gpio mode 0 out 
gpio mode 2 out

for (( x=0; x<=9; x++ ))  
  do  
  gpio write 0 1  
  gpio write 2 1
  sleep 1         
  gpio write 0 0  
  gpio write 2 0
  sleep 1         

done              