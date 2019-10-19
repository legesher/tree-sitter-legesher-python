<img src="/lib/images/README-EggPeggy.png" align="center"/>
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)


<h1 align="center">Legesher's Tree-Sitter-Python</h1>
<blockquote align="center">💻 Code in Python 🐍using your native written ✏️language.</blockquote>
<p align="center">Programming with <b>Legesher</b>'s dev tools empowers any developer to create without losing the art of innovation 💡, creativity 🎨, or collaboration 🤝 in translation. </p>

<!-- DEVELOPMENT BADGES -->
<p align="center" style="margin-bottom: 5px; margin-top: 5px;">
    <a href="https://travis-ci.com/legesher/tree-sitter-legesher-python">
        <img src="https://img.shields.io/travis/com/legesher/tree-sitter-legesher-python?style=flat-square&labelColor=black&logo=travis&logoColor=white" alt="macOS Build Status"></a>
    <a href="https://ci.appveyor.com/project/madiedgar/tree-sitter-legesher-python">
        <img src="https://img.shields.io/appveyor/ci/madiedgar/tree-sitter-legesher-python?style=flat-square&labelColor=black&logo=appveyor&logoColor=white" alt="Windows Build Status"></a>
    <a href="https://david-dm.org/legesher/tree-sitter-legesher-python">
        <img src="https://img.shields.io/david/legesher/tree-sitter-legesher-python?style=flat-square&labelColor=black" alt="David Dependency Status"></a>
    <a href="http://makeapullrequest.com">
        <img src="https://img.shields.io/badge/pull_requests-welcome-brightgreen.svg?style=flat-square&labelColor=black" alt="Pull Requests Welcome"></a>
    <a href="https://github.com/legesher/tree-sitter-legesher-python/issues?q=is%3Aopen+is%3Aissue+label%3A%22Good+First+Issue%22">
        <img src="https://img.shields.io/badge/first--timers--only-friendly-success.svg?style=flat-square&labelColor=black" alt="First Timers Only"></a>
</p>
<!-- SUPPORT BADGES -->
<p align="center" style="margin-bottom: 5px;>
    <a href="https://github.com/legesher/tree-sitter-legesher-python" alt="Repository">
        <img src="https://img.shields.io/badge/Tree_Sitter_Legesher_Python-0.15.2-f58977.svg?style=flat-square&labelColor=black&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNTAxLjE3IDUwMS4xNyI+PGRlZnM+PGNsaXBQYXRoIGlkPSJjbGlwLXBhdGgiPjxlbGxpcHNlIGN4PSIxNzUuMjMiIGN5PSIyNTAuMTMiIHJ4PSIzNS45OCIgcnk9IjQxLjg5IiBmaWxsPSJub25lIi8+PC9jbGlwUGF0aD48Y2xpcFBhdGggaWQ9ImNsaXAtcGF0aC0yIj48ZWxsaXBzZSBjeD0iMzI0LjIiIGN5PSIyNTAuMTMiIHJ4PSIzNS45OCIgcnk9IjQxLjg5IiBmaWxsPSJub25lIi8+PC9jbGlwUGF0aD48L2RlZnM+PHRpdGxlPlBlZ2d5LUhlYWRzaG90QWxwaGE8L3RpdGxlPjxnIHN0eWxlPSJpc29sYXRpb246aXNvbGF0ZSI+PGcgaWQ9IkxheWVyXzEiIGRhdGEtbmFtZT0iTGF5ZXIgMSI+PHBhdGggZD0iTTE2Mi40OCwzNjRjNzYuODgsNTEuNjUsMzYuNywyNTMuNDYsMjAxLDI1Mi4wOHM3Ni44My05NS4xLDc2LjgzLTk1LjEtMTksNDYuNjctNjguNywxMy41OC03MC0xNDUtNDEuMDktMTY0LjRTMTYyLjQ4LDM2NCwxNjIuNDgsMzY0WiIgZmlsbD0iI2ZmODk3NiIvPjxwYXRoIGQ9Ik0zMjIuNjEsNDU2YzEsMy42NSwyLjA5LDYuMTYsMy4zOSw3LjY5LTEyLjQ0LTQwLTEyLjIxLTgyLjMyLDQuNTYtOTMuNTcsMTQuODUtMTAtMjkuNzYtMTEuMzEtNzYuNzMtMTAuMjhsLTEwLjQyLDUuODYtMywyOS44M1MzMDkuMTUsNDA0LjUxLDMyMi42MSw0NTZaIiBmaWxsPSIjZjQ4ODc3IiBvcGFjaXR5PSIwLjUiIHN0eWxlPSJtaXgtYmxlbmQtbW9kZTptdWx0aXBseSIvPjxjaXJjbGUgY3g9IjI1MC41NSIgY3k9IjI1Ni45MSIgcj0iMTM4LjYyIiBmaWxsPSIjZmY4OTc2Ii8+PGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAtcGF0aCkiPjxlbGxpcHNlIGN4PSIxNzUuMjMiIGN5PSIyNTAuMTMiIHJ4PSIzNS45OCIgcnk9IjQxLjg5IiBmaWxsPSIjZmZmIi8+PGVsbGlwc2UgY3g9IjE4NS4zNyIgY3k9IjI0OS4xNCIgcng9IjMzLjAxIiByeT0iMzguNDMiIGZpbGw9IiMyNjI2MjYiLz48L2c+PGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAtcGF0aC0yKSI+PGVsbGlwc2UgY3g9IjMyNC4yIiBjeT0iMjUwLjEzIiByeD0iMzUuOTgiIHJ5PSI0MS44OSIgZmlsbD0iI2ZmZiIvPjxlbGxpcHNlIGN4PSIzMTQuMDYiIGN5PSIyNDkuMTQiIHJ4PSIzMy4wMSIgcnk9IjM4LjQzIiBmaWxsPSIjMjYyNjI2Ii8+PC9nPjxwb2x5Z29uIHBvaW50cz0iMTQwLjUzIDI4NC45NCAzNjAuMjggMjg0Ljk0IDMyMi4yMyAzMTYuMDIgMTY3LjkyIDMxOS4yMSAxNDAuNTMgMjg0Ljk0IiBmaWxsPSIjZmY4OTc2Ii8+PHBhdGggZD0iTTE5Ni4zNCwyNzMuN3MyMi4zMy0yNC45Miw1NS0yNC45Miw1My4yNCwyNC45Miw1My4yNCwyNC45Mi0xMiw1Ni40Mi01NC4xLDU2LjQyUzE5Ni4zNCwyNzMuNywxOTYuMzQsMjczLjdaIiBmaWxsPSIjZmJjNDk5Ii8+PHBhdGggZD0iTTE5Ni4zNCwyNzMuN3MyMi4zMy0yNC45Miw1NS0yNC45Miw1My4yNCwyNC45Miw1My4yNCwyNC45Mi0xMiwyOS43LTU0LjEsMjkuN1MxOTYuMzQsMjczLjcsMTk2LjM0LDI3My43WiIgZmlsbD0iI2ZkZTRkMyIvPjxwb2x5Z29uIHBvaW50cz0iMTQ0LjEgMjMzLjg3IDE2Ni4yOCAyNDcuNzQgMTQyLjUxIDI2MC4wMiAxNDQuMSAyMzMuODciIGZpbGw9IiNmZmYiLz48cG9seWdvbiBwb2ludHM9IjM1NS4zMyAyMzMuODcgMzMzLjE0IDI0Ny43NCAzNTYuOTEgMjYwLjAyIDM1NS4zMyAyMzMuODciIGZpbGw9IiNmZmYiLz48cGF0aCBkPSJNMjExLjEsMTIzLjgyczQ1LTIzLDU5LjY5LTIzLDEwLjQ3LDIzLDEwLjQ3LDIzWiIgZmlsbD0iI2ZmODk3NiIvPjxwYXRoIGQ9Ik0zNTIuMzYsMTE0LjY0YTkuNDMsOS40MywwLDAsMSw0LjE1LTE1Ljg5YzYuNDctMS42MSwxNi4xMi0uNzEsMzAuMDgsNy40NiwxOSwxMS4xMSwxOS4zMSwyNy4wNiwxNi4zLDM4LjM2LTEuODMsNi44OS0xMC41Niw5LjEtMTUuNjYsNC4xMloiIGZpbGw9IiMyNjI2MjYiLz48cGF0aCBkPSJNMTU0LjM5LDExNC42NGE5LjQzLDkuNDMsMCwwLDAtNC4xNS0xNS44OWMtNi40Ny0xLjYxLTE2LjEyLS43MS0zMC4wOCw3LjQ2LTE5LDExLjExLTE5LjMxLDI3LjA2LTE2LjMsMzguMzYsMS44Myw2Ljg5LDEwLjU2LDkuMSwxNS42Niw0LjEyWiIgZmlsbD0iIzI2MjYyNiIvPjwvZz48L2c+PC9zdmc+" /></a>
    <a href="https://github.com/legesher/tree-sitter-legesher-python/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/legesher/tree-sitter-legesher-python?style=flat-square&color=f58977&labelColor=black" /></a>
    <a href="https://streamlabs.com/withmadico/tip" alt="Backers on Github">
        <img src="https://img.shields.io/badge/sponsors-4-black?style=flat-square&color=f58977&labelColor=black" /></a>
    <a href="https://instagram.com/withmadico" alt="Sponsors on Github">
        <img src="https://img.shields.io/badge/sponsor-@withmadico-black?style=flat-square&color=f58977&labelColor=black" /></a>

</p>
<!-- SOCIAL BADGES -->
<p align="center">
    <a href="https://github.com/legesher">
        <img src="https://img.shields.io/badge/-Contribute-black?style=flat-square&logo=github&logoColor=7ed2e7"
            alt="Contribute on Github"></a>
    <a href="https://twitch.tv/withmadico">
        <img src="https://img.shields.io/badge/-Watch-black?style=flat-square&logo=twitch&logoColor=7ed2e7"
            alt="Watch on Twitch"></a>
    <a href="https://discord.gg/DkVjVDP">
        <img src="https://img.shields.io/badge/-Chat-black?style=flat-square&logo=discord&logoColor=7ed2e7"
            alt="chat on Discord"></a>
    <a href="https://www.instagram.com/legesher/">
        <img src="https://img.shields.io/badge/-Connect-black?style=flat-square&logo=instagram&logoColor=7ed2e7"
            alt="follow on Instagram"></a>
    <a href="https://twitter.com/intent/follow?screen_name=legesherio">
        <img src="https://img.shields.io/badge/-Tweet-black?style=flat-square&logo=twitter&logoColor=7ed2e7"
            alt="follow on Twitter"></a>
    <a href="https://medium.com/@legesher">
        <img src="https://img.shields.io/badge/-Read-black?style=flat-square&logo=medium&logoColor=7ed2e7"
            alt="Read on Medium"></a>
    <a href="https://legesher.io">
        <img src="https://img.shields.io/badge/-Subscribe-black?style=flat-square&logo=mailchimp&logoColor=7ed2e7"
            alt="Subscribe on Mailchimp"></a>    
</p>
<!-- SOCIAL MEDIA -->

# Introduction

**`tree-sitter-legesher-python`** 🌳 is the written language interchangeable version of the tree-sitter grammar for the python language used by text editors such as **Atom**. This npm package is used by [`language-legesher-python`](https://github.com/legesher/language-legesher-python) to enable you to code in the language you natively use.

_📢 Check if your native language is available in the [Legesher translation repository](https://github.com/legesher/legesher-translations)! If not, we'd love your help to add it!!_

# Getting Started
In order to use the `tree-sitter-legesher-python` grammar to code, you will need to follow the following steps:

**1️⃣ Download Atom (a text editor)**  
Head on over to [Atom.io](https://atom.io/) to download the latest version of the text editor.

**2️⃣ Update Preferences**  
Once installed on your local computer, open the _Atom_ application. In the options in the top menu bar, navigate to Atom's Settings _Atom > Preferences..._ . A settings window should pop up in your editor.

**3️⃣ Disable Atom's `language-python`**  
Continue by clicking the _Packages_ section. Here, you'll see a number of items: _Installed Packages_, _Community Packages_, _Core Packages_, _Development Packages_, _Git Packages_. Using the search bar, type `language-python` to find the _Core Package_ currently installed on your text editor. Click _Disable_.

**4️⃣ Download Legesher's `language-legesher-python`**  
Now, head to the _Install_ section to install a new package to your text editor (make sure that the _Packages_ button is selected instead of the _Themes_). Type `language-legesher-python` in the search bar to find Legesher's package, and click _Install_.

**5️⃣ Enable Legesher's `language-legesher-python`**  
Sometimes you'll have to enable a newly installed package by clicking the _Enable_ button in the package when it is within the _Packages_ section of the settings.

**6️⃣ Write A "Hello World" Program In Your Language**  
Now, you can start coding in Python using any written language currently available within Legesher's translation library! The syntax highlighting should match as if you were coding Python in English!

``` python
def main():
    print "Hello World"
```

# Contributing
❤️Legesher relies on the passionate members of its community (both developer and non-developer alike) to keep delivering impactful tools to people all over the world.

Before contributing, be sure to consult Legesher's [contribution guidelines](https://github.com/legesher/legesher/blob/master/CONTRIBUTING.md) and [language conventions](https://github.com/legesher/legesher/blob/master/.github/language-conventions.md). As a member of our community, you must abide by our [Code Of Conduct](https://github.com/legesher/legesher/blob/master/CODE_OF_CONDUCT.md).

## Installation
**1️⃣ Fork the legesher/tree-sitter-legesher-python repository**  
Follow these instructions on [how to fork a repository](https://help.github.com/en/articles/fork-a-repo)

**2️⃣ Cloning the repository**  
Once you have set up your fork of the `legesher/tree-sitter-legesher-python` repository, you'll want to clone it to your local machine. This is so you can make and test all of your personal edits before adding it to the master version of `legesher/tree-sitter-legesher-python`.

Navigate to the location on your computer where you want to host your code. Once in the appropriate folder, run the following command to clone the repository to your local machine.

```
git clone git@github.com:your-username/tree-sitter-legesher-python.git
```

**3️⃣ Bootstrapping the repository**  
You'll then want to navigate within the folder that was just created that contains all of the content of the forked repository. There you'll want to run the installation script to get the updated version of all the dependencies.

```
cd tree-sitter-legesher-python  
npm install
```

## Development
We love your desire to give back, and want to make the process as welcoming to newcomers and experts as possible. We're working on developing more intuitive tutorials for individuals of all skill levels and expertise, so if you think the community would value from being walked through the steps you're going through please share! ❤️

### Test Changes
When you start making changes to the code on your local branch, you'll need to test those changes. Before your code can be accepted into the master branch, it will have to pass all of the tests within `/examples/*`. To check the updates made to the grammar, run the following commands:

**1️⃣ Save Current Changes**  
When you get to a point when you want to test the functionality of the code, make sure all your changes are saved. ❗They don't necessarily have to be _committed_ changes in order to test them.

**2️⃣ Generate the updated tree-sitter parser**  
You'll need to generate a new tree-sitter grammar whenever you make changes in this repository. Running this command will usually update files within the `/src/*` folder.

```
tree-sitter generate
```

**3️⃣ Configure the grammar**  
This command makes sure the binding information for the grammar is properly set up and configured.  

```
node-gyp configure
```

**4️⃣ Build the grammar**
Using the newly configured bindings, we can now build the new grammar with your changes.
```
node-gyp build
```

**5️⃣ Test changes**  
To make sure that the grammar is properly updated, run the tests. If you add elements that do not have tests to prove whether they work correctly or not, please include them in your pull request.
```
tree-sitter test
```

### References
This repository is a forked extension of [tree-sitter's](http://tree-sitter.github.io) `tree-sitter-python`. This package works alongside the _language_ repository [`language-legesher-python`](https://github.com/legesher/language-legesher-python). These two repositories work closely together, so it may be useful to touch up on both repositories' documentation.

**The Python Language**
* [Python 2 Grammar](https://docs.python.org/2/reference/grammar.html)
* [Python 3 Grammar](https://docs.python.org/3/reference/grammar.html)
* [Tree Sitter](https://github.com/tree-sitter/tree-sitter)

# Legesher Projects
Legesher Developer Tools might be useful to you if:
- you are a non-native english speaker
- you are new to programming
- you work on a team with non-native english speakers
- you are a developer

| Project | Purpose |
|---------|---------|
| [`tree-sitter-legesher-python`](https://github.com/legesher/tree-sitter-legesher-python) | Tree-sitter python grammar used by text editors allowing Legesher's languages to be implemented |
| [`language-legesher-python`](https://github.com/legesher/language-legesher-python) | Atom's programming language binding to allow syntax highlighting, code folding etc. to a specific grammar |
| [`legesher-translations`](https://github.com/legesher/legesher-translations) |  Host and API of all the language translations for written languages for code keywords / concepts |
| [`legesher-dot-io`](https://github.com/legesher/legesher-dot-io) | Legesher's public [website](https://legesher.io) |
| [`legesher-docs`](https://github.com/legesher/legesher-docs) | Legesher's documentation hub. Will be transitioning to a documentation host soon. |
| [`legesher`](https://github.com/legesher/legesher) | Git integration to collaborate with code and others in other languages |
| [`legesher-pride`](https://github.com/legesher/legesher-pride) | A non-programmer's dream to contributing to open source by sharing what they know and learning what's new |
## The Community
A message from our founder:
>It is truly a blessing to be surrounded by a community of passionate, driven individuals who love sharing their gifts to creating better products together. Your contribution means the world to me, and keeps me motivated to continue creating. This wouldn't be possible without you. From the bottom of my heart, THANK YOU!

Meet our [community](https://github.com/legesher/legesher/tree/master/community) (full of contributors, backers, sponsors, and supporters) that give a little piece of their heart to this project. Thank you so much.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://withmadi.co"><img src="https://avatars0.githubusercontent.com/u/7844510?v=4" width="100px;" alt="Madison (Pfaff) Edgar"/><br /><sub><b>Madison (Pfaff) Edgar</b></sub></a><br /><a href="https://github.com/madiedgar/tree-sitter-legesher-python/commits?author=madiedgar" title="Code">💻</a> <a href="https://github.com/madiedgar/tree-sitter-legesher-python/issues?q=author%3Amadiedgar" title="Bug reports">🐛</a> <a href="#projectManagement-madiedgar" title="Project Management">📆</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!