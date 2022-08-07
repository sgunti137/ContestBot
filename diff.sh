cd $1

mainoutfiles=(`ls out*.txt`)
yourfiles=(`ls yout*.txt`)

len=${#mainoutfiles[@]}

for((i=0; i<$len; i++)) do
    echo 'Running on testcase '$(($i+1))':'
    echo '-------------------'
    echo 'Output:'
    cat ${yourfiles[i]}
    echo '-------------------'
    echo 'Expected:'
    cat ${mainoutfiles[i]}
    echo '-------------------'
    diff -w ${yourfiles[i]} ${mainoutfiles[i]} && echo -e "\033[32mTest Passed!\033[m" || echo -e "\033[31mTest Failed!\033[m"
    echo
done

cd ..