# OEIS funfacts

> Some funfacts about OEIS.

This program/website tells you some fun facts about OEIS.
View the up-to-date version at [https://benwiederhake.github.io/oeis-funfacts/](https://benwiederhake.github.io/oeis-funfacts/).

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Background](#background)
- [TODOs](#todos)
- [NOTDOs](#notdos)
- [License](#license)
- [Contribute](#contribute)

## Install

You only need some Python3 installed somewhere.

## Usage

FIXME: Download from OEIS

Just use it! No dependencies, and it's short enough.

The result will be written to `index.html`, which you can then publish/view/whatever.

## Background

I [came
across](https://www.reddit.com/r/AskReddit/comments/hg1uax/what_is_your_favorite_paradox/fw1m948/)
a blog post claiming that
[11630 was the First Uninteresting Number in June 2009](http://www.njohnston.ca/2009/06/11630-is-the-first-uninteresting-number/).
There are even some updates about how it it increased to 12407 in November 2009 and later to 14228 in November 2013.
So naturally I wondered what the current lowest uninteresting number is.

Note that this is not a paradox, as the blog post confirms:

> Update \[June 13, 2009\]: I got word back via e-mail today that this sequence didn't make the cut. So there you have it — these numbers truly are uninteresting.

;-)

### Data source

I'm pleased that OEIS makes a simple version of its database readily available at [https://oeis.org/stripped.gz](https://oeis.org/stripped.gz).
This file sometimes contains only a few terms, but usually still the first few "interesting" terms. ;-)

Curiously, the "how many terms" part is difficult to quantify, as there are some [sequences with only one term](https://oeis.org/A058445),
and also a sequence with [377 terms](https://oeis.org/A266330).

Also, all meta-information (author, context, formula, references, etc) is omitted, except the A number.

All this together means that `stripped.gz` is a handy about-40MB file that is a pleasure to work with.

## TODOs

These are the things I'd like to do next:
* Show it to some people
* Maybe find even more interesting things to analyze in this data?

## NOTDOs

Here are some things this project will definitely not support:
* Graphing. I could only find Sloane's Gap, and promptly remembered [Numberphile's video on it](https://www.youtube.com/watch?v=_YysNM2JoFo).
* Automation outside of my own devices. I don't know how OEIS's bandwidth, and hence intend to update the website about once a month, at most.

## License

- All files written by me or by the program are available under CC0.
- The font "Astloch" is available under the [SIL Open Font License](https://www.1001fonts.com/astloch-font.html#license).
- The data on the rendered webpage is available under the [Creative Commons Attribution Non-Commercial 3.0 license](http://creativecommons.org/licenses/by-nc/3.0/), with attribution to [The Online Encyclopedia of Integer Sequences](https://oeis.org/), because it contains derivative work from the ["stripped.gz"](https://oeis.org/stripped.gz) by OEIS.
- The favicon is from [icon-library.com](http://icon-library.com/icon/bored-icon-4.html) under the CC0. Irritatingly they also claim that it is "Free for personal use only, Attribution required", which contradicts the CC0 claim. Whatever, I'm fine in both cases.

To put it simply: If you ain't makin' money from it, you can do whatever you want. If you *do* make
money from it, change the favico, and OEIS might want a share. (And I wouldn't mind a box of cereal, or whatever.
I would be more interested in how the hell you monetized it, though.)

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/oeis-funfacts/issues/new) or submit PRs.
