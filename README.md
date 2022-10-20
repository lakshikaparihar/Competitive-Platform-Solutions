
# How to Contribute 

 1. Fork this Repository
 
 2. Clone the Repository in your local machine
```
$ git clone "https://www.github.com/{Username}/Competitive-Platform-Solutions"
```

 3. Choose the Platform and Language and solve it (Please ensure your solution should pass all the Test cases)
 
 4. Paste the Code into a new file and name it in the following format : Problem_Name.[extension of the language] (Make sure name of your file matches with the name mentioned in the url)

 5. Place your source code file in the respective folder(if there is no folder of your coding_platform or domain then go ahead and create it).If you have added a folder update the readme.md file

 6. add and commit the changes in your Repository
 ```
 $ git add <filename>
 ```
 ```
 $ git commit -m "(Your Name and File added)"
```

 7. push the changes to your repository
 ```
 $ git push -u origin branchname
 ```

 8. Generate a pull request (Make sure to add problem name in the title and url in the description)

# Synchronize forked repository with upstream repository

 1. Add this repository as an upstream repository
 ```
 $ git remote add upstream https://github.com/lakshika1064/HackerRank-Solutions
 ```
 2. Fetch all the changes from the repository
 ```
 $ git fetch upstream
 ```
 3. Make sure you are on your working branch
 
 ```
 $ git checkout master
 ```
 4.  Merge the changes from upstream into your local machine
 
```
$ git merge upstream/master
```
 5. Now your local branch is synced with the upstream branch . Push the changes in your forked repository
 ```
 $ git push -f origin master
 ```

# License 

MIT




