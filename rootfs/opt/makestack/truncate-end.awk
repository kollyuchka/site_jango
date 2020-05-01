BEGIN{
active=1;
}

/M140.*S0/{
exit(0);
}

/M104.*S0/{
exit(0);
}

active==1{
print;
}