## Quick Terminal Command

Git Tree Files

```
git ls-tree -r HEAD --name-only | tree --fromfile
```

Git LFS Setup

```
sudo apt update && sudo apt install -y git-lfs
git lfs install
git lfs install
```

Git LFS migration for hero vid

```
git lfs migrate import --everything --include="/static/videos/hero.mp4"
```
