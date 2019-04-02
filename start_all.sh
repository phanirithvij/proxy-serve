for port in {8000..8009} # {20000..20099}
do
    python3 -m http.server $port &
done

for port in {8010..8019} # {20101..20200}
do
    python3 -m http.server $port &
done
