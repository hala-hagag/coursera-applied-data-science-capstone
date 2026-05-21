# How to push this folder to your GitHub repo

Open Terminal on your Mac, then copy-paste these blocks one at a time.

## 1. Go to the capstone folder

Drag the `capstone` folder from Finder onto your Desktop first so the path is easy.
Then in Terminal:

```bash
cd ~/Desktop/capstone
```

(If you kept it somewhere else, adjust the path.)

## 2. Initialise git and connect to your GitHub repo

```bash
git init
git branch -M main
git remote add origin git@github.com:hala-hagag/coursera-applied-data-science-capstone.git
```

If you don't have SSH set up, use HTTPS instead:

```bash
git remote add origin https://github.com/hala-hagag/coursera-applied-data-science-capstone.git
```

## 3. Stage, commit, push

```bash
git add .
git commit -m "Add Falcon 9 capstone — notebooks, dashboard, report"
git push -u origin main
```

When `git push` asks for credentials with the HTTPS remote:
- Username: `hala-hagag`
- Password: paste a **GitHub Personal Access Token** (not your normal password). Create one at https://github.com/settings/tokens — give it the `repo` scope.

## 4. Verify

Refresh `https://github.com/hala-hagag/coursera-applied-data-science-capstone` — you should see:

```
data/          notebooks/         images/
Data_Science_Capstone_Project_Report.pdf
Data_Science_Capstone_Project_Report.pptx
README.md      requirements.txt
```

That's it.

## Troubleshooting

| Error | Fix |
|---|---|
| `Permission denied (publickey)` | You're using SSH but haven't set up a key. Switch remote to HTTPS: `git remote set-url origin https://github.com/hala-hagag/coursera-applied-data-science-capstone.git` |
| `remote: Support for password authentication was removed` | GitHub no longer accepts passwords over HTTPS. Use a Personal Access Token as the password (step 3). |
| `! [rejected] main -> main (fetch first)` | The repo isn't empty. Run `git pull origin main --allow-unrelated-histories`, then `git push`. |
