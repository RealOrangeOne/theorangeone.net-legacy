---
title: My Dotfiles
template: projects
slug: dotfiles
repo: https://github.com/RealOrangeOne/dotfiles/
summary: How I set up my machines just the way I like them!
---

### What are dotfiles?
Dotfiles are a way for people to store their settings and preferences to make setting up a new computer that much easier. They can usually be found in a persons VCS profile.

### Taking dotfiles 1 step further
I use both my laptop and work machines almost every day, and want them to be setup in an almost identical way, despite the fact that 1 runs Ubuntu, and the other runs Arch. The main things I needed synced over were my `.bashrc` file and my atom config.

## How I did it
Originally, I used my owncloud server to sync all my dotfiles between my computer, and then used symlinks to split out the relevant files into the relevant locations.

This worked brilliantly, config files were automatically synced as soon as I made a change. This was especially great for my `.bashrc` file! The main problem was with atom packages, I had to manually store what files were installed, then manually install them on the other machine from the saved file. This was made easier by `apm` allowing me to list them and automatically save them in a file, but it wasn't perfect.

Eventually, after looking into possible solutions, I came across the [`Sync settings`](https://atom.io/packages/sync-settings) package, which seemed to be the answer to my prayers! It saved all my config data for atom into a gist, which I could then backup and restore too from within the application. It also warned me when my local data was out of date from the remote, and prompt me to download the updated data.
