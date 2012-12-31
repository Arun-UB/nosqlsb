set terminal canvas
set output "/home/ubuntu/project/templates/throughput.html"

set style fill solid 1.00 border 0
set style histogram
set style data histogram
set style histogram cluster gap 1

set xlabel "DB Packages"
set ylabel "Throughtput (ops/sec)"
plot file using 2:xticlabels(1) title "Throughput" linecolor rgb "#0000FF"

