### Initialization

#### Create branch 

 ```sh
$BRANCH="section-3-code"

git clone https://github.com/adibaba/Python-Django-The-Practical-Guide.git $BRANCH
cd $BRANCH

git switch --orphan $BRANCH

# edited this file
git add *
git commit -m "new branch"
git push --set-upstream origin $BRANCH
```
