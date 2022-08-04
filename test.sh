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

testsMatched=$true

for ((i=0; i<${#mainoutfiles[@]}; i++)); do
  diff -w ${mainoutfiles[i]} ${yourfiles[i]} > differ.txt
  content=$(<differ.txt)
  if content
  then 
    testsMatched=$false
    echo 'Testcase' + i + ' Failed' 
  fi
done

cd ..