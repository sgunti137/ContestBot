if [ "$1" == "cf" ];
then
    py CodeforcesSampleGenerator.py $2
elif [ "$1" == "at" ];
then
    py AtcoderSampleGenerator.py $2
else
    echo "supported platforms are Codeforces('cf') and Atcoder('at')"
fi