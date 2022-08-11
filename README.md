# ContestBot

This is a bot for writing Codeforces and Atcoder contests. It fetches testcases for the contest required and we can test our solution. The project is based on python and bash scripts.



# Setup/Installation
```bash
INSTALLATION_PATH="<directory_path_where_you_want_to_clone>"; # also the dir where you will write solution
cd $INSTALLATION_PATH
git clone https://github.com/sgunti137/ContestBot.git
cd ContestBot
# install the py packages required - Beautifulsoup
```

# Creating Problem Folders
```bash
./start.sh cf <contest-id> # command to start Codeforces contest
./start.sh at <contest-id> # command to start Atcoder contest
# For contest -> https://codeforces.com/contest/1713, the contest-id is '1713'
# For contest -> https://atcoder.jp/contests/abc264, the contest-id is 'abc264'
```

# Testing your solution
```bash
./test.sh A #if you want to test A/sol.cpp
# this will run your code on downloaded test cases
# and print to console your output vs expected output, and also the if the test cases are passed or failed. 
```
