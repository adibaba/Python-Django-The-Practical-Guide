# Python Django - The Practical Guide

[Course notes](https://github.com/adibaba/Python-Django-The-Practical-Guide#readme)

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


#### .gitignore

- [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/blob/19b4ddb61ee83a6f36b7d285f6a7b4ae813eecd2/.gitignore)
- [A collection of .gitignore templates](https://github.com/github/gitignore)
  - [VisualStudioCode](https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore)
  - [Python](https://github.com/github/gitignore/blob/main/Python.gitignore)


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


#### Visual Studio Code: Format HTML Settings

- [Code](https://github.com/adibaba/Python-Django-The-Practical-Guide/commit/b1e1a5e7ac38a107f78117b99c6651c338f9eed5)
- Show all commands: [Ctrl] + [Shift] + [P]
	- *Preferences: Open Workspace Settings (JSON)* creates `.vscode/settings.json`
- Format document: [Shift] + [Alt] + [F]
