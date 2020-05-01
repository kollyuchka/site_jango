function abs(x) {
if(x<0) return(-x);
return(x);
}

BEGIN{
active=0;
if(LAYER_START==0) active=2;
print "; extraction from LAYER_START=" LAYER_START \
  " to LAYER_STOP=" LAYER_STOP
}

/G1.*Z/{
z=gensub("G1.*Z([0-9.]+).*","\\1","g");
if(abs(z-LAYER_START)<0.1 && active==0) active=1;
if(abs(z-LAYER_STOP)<0.1) {
 print "; " $0 "; Layer extraction ends here!"
 exit(0);
 }
}

active==1{
# remove extrude commands until extruder length is reset
if($0 ~ /G92.*E0$/) {
 print;
 active=2;
 next;
 }
if($0 ~ /G1.*E.*/) {
 next;
 }
print;
}

active==2{
print;
}