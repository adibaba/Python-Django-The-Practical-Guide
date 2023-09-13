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

[Changes](https://github.com/adibaba/Python-Django-The-Practical-Guide/commit/596fdfd0f8664e57d07eca093a84f028caf7dbb0) and
  [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/596fdfd0f8664e57d07eca093a84f028caf7dbb0)

#### Create project

 ```sh
python -m django startproject project

# edited this file
git add *
git commit -m "new project"
git push
```

[Changes](https://github.com/adibaba/Python-Django-The-Practical-Guide/commit/ef77ebb6c74a59607012b426345381a8e51e2836) and
  [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/ef77ebb6c74a59607012b426345381a8e51e2836)

#### Create app

 ```sh
cd project
python manage.py startapp app
cd ..

# edited this file
git add *
git commit -m "new app"
git push
```

[Changes](https://github.com/adibaba/Python-Django-The-Practical-Guide/commit/4916ace266c6d419d675087b303e075d42d81195) and
  [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/tree/4916ace266c6d419d675087b303e075d42d81195)

#### .gitignore

- https://github.com/github/gitignore
- https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
- https://github.com/github/gitignore/blob/main/Python.gitignore

