set terminal png
set output "/home/akarsh/avg_latency.png"

set style fill solid 1.00 border 0
set style histogram
set style data histogram
set style histogram cluster gap 1

set xlabel "DB Packages"
set ylabel "Avergae Latency (usec)"
set title "Average Latency"
plot file using 2:xticlabels(1) title "Average Latency" linecolor rgb "#0000FF"

