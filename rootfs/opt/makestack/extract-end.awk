BEGIN{
active=0;
}

/M140.*S0/{
active=1;
}

/M104.*S0/{
active=1;
}

active==1{
print;
}