set terminal png
set output "/home/akarsh/throughput.png"

set style fill solid 1.00 border 0
set style histogram
set style data histogram
set style histogram cluster gap 1

set xlabel "DB Packages"
set ylabel "Throughtput (ops/sec)"
set title "Throughput of NoSQL DB Packages"
plot file using 2:xticlabels(1) title "Throughput" linecolor rgb "#0000FF"

