cd $1
g++ -std=c++17 sol.cpp -o main || { echo "$problem/sol.cpp failed to build. Check for errors."; exit 1; }

echo Compiled successfully...

infiles=(`ls inp*.txt`)

for ((i=0; i<${#infiles[@]}; i++)); do
  ./main < inp$i.txt > yout$i.txt 
done

mainoutfiles=(`ls out*.txt`)
yourfiles=(`ls yout*.txt`)

len=${#mainoutfiles[@]}

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# code to compare the output files

cd ..