set terminal png
set output "/home/akarsh/runtime.png"

set style fill solid 1.00 border 0
set style histogram
set style data histogram
set style histogram cluster gap 1

set xlabel "DB Packages"
set ylabel "Runtime (msec)"
set title "Runtime of NoSQL Benchmark Workload"
plot file using 2:xticlabels(1) title "Runtime" linecolor rgb "#0000FF"

