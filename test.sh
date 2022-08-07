cd $1
g++ -std=c++17 sol.cpp -o main || { echo "$problem/sol.cpp failed to build. Check for errors."; exit 1; }

echo Compiled successfully...
echo
infiles=(`ls inp*.txt`)

for ((i=0; i<${#infiles[@]}; i++)); do
  ./main < inp$i.txt > yout$i.txt 
done

cd ..
./diff.sh $1
cd ..