<img src="/lib/images/README-EggPeggy.png" align="center"/>

<h1 align="center">蛋壳之Tree-Sitter-Python</h1>
<blockquote align="center">💻 使用母语学会Python🐍编码✏️。</blockquote>
<p align="center"><b>蛋壳</b>之程式设计主要解决来自各地计算机的语言障碍，并且能保持有创意的心态去发挥所长。 </p>

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
    <!-- <a href="https://github.com/legesher/tree-sitter-legesher-python/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/legesher/tree-sitter-legesher-python?style=flat-square&color=f58977&labelColor=black" /></a> -->
    <a href="#the-community" alt="All Contributors">
        <img src="https://img.shields.io/badge/all_contributors-11-black?style=flat-square&color=f58977&labelColor=black" /></a>
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

*其他语言版本: [English](README.md), [简体中文](README.zh-cn.md).*

# 简介

**`tree-sitter-legesher-python`** 🌳 是个可以跟tree-sitter互换的python编码语言，Atom会是我们常用的软件。[`language-legesher-python`](https://github.com/legesher/language-legesher-python) NPM包能允许你使用不同的编码语言。

_📢 查看是否有你的母语在我们软件里[Legesher translation repository](https://github.com/legesher/legesher-translations)！若没，我们愿意为你添加上去！

# 快速开始

跟着一下的步骤来使用"tree-sitter-legesher-python"：

**1️⃣ 下载 Atom (编码编辑软件)**  
这个链接[Atom.io](https://atom.io/)是下载最新版本的。

**2️⃣ 更新Atom设置**  
当下载完毕，开启Atom软件。点击option在头上的菜单，并且点击Settings > Preferences，设置的屏幕会展现在软件里。

**3️⃣ 关上 Atom's `language-python`**  
寻找Packages的选项。寻找'language-python'并点击'Disable'。

**4️⃣ 下载蛋壳 `language-legesher-python`**  
点击'Install'选项，下载'language-legesher-python'包。（注意！！：在搜索栏隔壁，确保你是在Packages的选择而不是Themes。<br/>
<ins>*在这个步骤有问题，请到[我们的discord查看](https://discord.com/invite/DkVjVDP)，在频道 '#language-legesher-python'*</ins>

**5️⃣ 开启蛋壳 `language-legesher-python`**  
去会你的Packages选项，确保'language-legesher-python'是否已经开启。

**6️⃣ 编个简单的 "Hello World" 程序用你的编码语言**  
尝试用Python在蛋壳的翻译知识库里吧！编码编辑软件的句法会有根据的。

```python
def main():
    print "Hello World"
```

# 贡献

❤️蛋壳的发展是靠来自各地的计算机与非计算机有所贡献的，把蛋壳软件继续往全球推广。

还没贡献前，请确保你有以蛋壳之[贡献指南手册](https://github.com/legesher/legesher/blob/master/CONTRIBUTING.md)与[语言惯例](https://github.com/legesher/legesher/blob/master/LANGUAGE_CONVENTIONS.md)。身为一位蛋壳的会员，你应去遵守我们的[行为守则](https://github.com/legesher/legesher/blob/master/CODE_OF_CONDUCT.md)。

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

- [Python 2 Grammar](https://docs.python.org/2/reference/grammar.html)
- [Python 3 Grammar](https://docs.python.org/3/reference/grammar.html)
- [Tree Sitter](https://github.com/tree-sitter/tree-sitter)

# Legesher Projects

Legesher Developer Tools might be useful to you if:

- you are a non-native english speaker
- you are new to programming
- you work on a team with non-native english speakers
- you are a developer

| Project                                                                                  | Purpose                                                                                                   |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [`tree-sitter-legesher-python`](https://github.com/legesher/tree-sitter-legesher-python) | Tree-sitter python grammar used by text editors allowing Legesher's languages to be implemented           |
| [`language-legesher-python`](https://github.com/legesher/language-legesher-python)       | Atom's programming language binding to allow syntax highlighting, code folding etc. to a specific grammar |
| [`legesher-translations`](https://github.com/legesher/legesher-translations)             | Host and API of all the language translations for written languages for code keywords / concepts          |
| [`legesher-dot-io`](https://github.com/legesher/legesher-dot-io)                         | Legesher's public [website](https://legesher.io)                                                          |
| [`legesher-docs`](https://github.com/legesher/legesher-docs)                             | Legesher's documentation hub. Will be transitioning to a documentation host soon.                         |
| [`legesher`](https://github.com/legesher/legesher)                                       | Git integration to collaborate with code and others in other languages                                    |
| [`legesher-pride`](https://github.com/legesher/legesher-pride)                           | A non-programmer's dream to contributing to open source by sharing what they know and learning what's new |

## The Community

A message from our founder:

> It is truly a blessing to be surrounded by a community of passionate, driven individuals who love sharing their gifts to creating better products together. Your contribution means the world to me, and keeps me motivated to continue creating. This wouldn't be possible without you. From the bottom of my heart, THANK YOU!

Meet our [community](https://github.com/legesher/legesher/tree/master/community) (full of contributors, backers, sponsors, and supporters) that give a little piece of their heart to this project. Thank you so much. ([emoji key](https://allcontributors.org/docs/en/emoji-key))

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://withmadi.co"><img src="https://avatars0.githubusercontent.com/u/7844510?v=4" width="100px;" alt="Madison (Pfaff) Edgar"/><br /><sub><b>Madison (Pfaff) Edgar</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/commits?author=madiedgar" title="Code">💻</a> <a href="https://github.com/legesher/tree-sitter-legesher-python/issues?q=author%3Amadiedgar" title="Bug reports">🐛</a> <a href="#projectManagement-madiedgar" title="Project Management">📆</a></td>
    <td align="center"><a href="https://github.com/wescran"><img src="https://avatars2.githubusercontent.com/u/36459418?v=4" width="100px;" alt="Wesley Cranston"/><br /><sub><b>Wesley Cranston</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/commits?author=wescran" title="Code">💻</a> <a href="#marketing-wescran" title="Marketing - People who help in marketing the repo/project">💌</a></td>
    <td align="center"><a href="https://github.com/dolphincodes"><img src="https://avatars0.githubusercontent.com/u/31311145?v=4" width="100px;" alt="dolphincodes"/><br /><sub><b>dolphincodes</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/commits?author=dolphincodes" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/LeonardoFurtado"><img src="https://avatars3.githubusercontent.com/u/22118060?v=4" width="100px;" alt="Leonardo Furtado"/><br /><sub><b>Leonardo Furtado</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/commits?author=LeonardoFurtado" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Eshan-Agarwal"><img src="https://avatars0.githubusercontent.com/u/47007275?v=4" width="100px;" alt="Eshan Agarwal"/><br /><sub><b>Eshan Agarwal</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/commits?author=Eshan-Agarwal" title="Documentation">📖</a></td>
    <td align="center"><a href="http://mythreya.dev"><img src="https://avatars1.githubusercontent.com/u/26112391?v=4" width="100px;" alt="Mythreya Kuricheti"/><br /><sub><b>Mythreya Kuricheti</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/issues?q=author%3AMythreyaK" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/jonathan-alvaro"><img src="https://avatars2.githubusercontent.com/u/13015661?v=4" width="100px;" alt="Jonathan Alvaro"/><br /><sub><b>Jonathan Alvaro</b></sub></a><br /><a href="#marketing-jonathan-alvaro" title="Marketing - People who help in marketing the repo/project">💌</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/zeesh-ali"><img src="https://avatars1.githubusercontent.com/u/26367273?v=4" width="100px;" alt="Zeeshan Ali"/><br /><sub><b>Zeeshan Ali</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/commits?author=zeesh-ali" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/andres-posadas"><img src="https://avatars2.githubusercontent.com/u/50717533?v=4" width="100px;" alt="andres-posadas"/><br /><sub><b>andres-posadas</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/commits?author=andres-posadas" title="Documentation">📖</a></td>
    <td align="center"><a href="https://blenderbell.artstation.com/"><img src="https://avatars3.githubusercontent.com/u/32410407?v=4" width="100px;" alt="calra123"/><br /><sub><b>calra123</b></sub></a><br /><a href="https://github.com/legesher/tree-sitter-legesher-python/commits?author=calra123" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/AjaiDubey"><img src="https://avatars3.githubusercontent.com/u/44136561?v=4" width="100px;" alt="Ajai Dubey"/><br /><sub><b>Ajai Dubey</b></sub></a><br /><a href="#ideas-AjaiDubey" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

_This project follows the [all-contributors](https://allcontributors.org/) specification. Contributions of any kind are welcome and recognized. ✨_
