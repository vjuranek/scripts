BEGIN {
    shrd_c = 0
    shrd_d = 0
    priv_c = 0
    priv_d = 0
}

/Shared_Clean/ { shrd_c = shrd_c + $2 }
/Shared_Dirty/ { shrd_d = shrd_d + $2 }
/Private_Clean/ { priv_c = priv_c + $2 }
/Private_Dirty/ { priv_d = priv_d + $2 }

END {
    printf "Shared clean mem = %d kB\n", shrd_c
    printf "Shared dirty mem = %d kB\n", shrd_d
    printf "Private clean mem = %d kB\n", priv_c
    printf "Private dirty mem = %d kB\n", priv_d
    printf "----------------------------\n"
    printf "Shared total mem = %d kB\n", shrd_c + shrd_d
    printf "Private total mem = %d kB\n", priv_c + priv_d
    printf "Total mem = %d kB\n", shrd_c + shrd_d + priv_c + priv_d
}
