# al-folio

A simple and clean [Jekyll](https://jekyllrb.com/) theme for academics.

Originally, **al-folio** was based on the [\*folio theme](https://github.com/bogoli/-folio) (published by [Lia Bogoev](http://liabogoev.com) and under the MIT license).
Since then, it got a full re-write of the styles and many additional cool features.
The emphasis is on whitespace, transparency, and academic usage: [theme demo](https://alshedivat.github.io/al-folio/).

## Getting started

### Testing in local

Assuming you have [Ruby](https://www.ruby-lang.org/en/downloads/) and [Bundler](https://bundler.io/) installed on your system (*hint: for ease of managing ruby gems, consider using [rbenv](https://github.com/rbenv/rbenv)*), first fork the theme from `github.com:alshedivat/al-folio` to `github.com:<your-username>/<your-repo-name>` and do the following:

```bash
$ bundle exec jekyll serve
```
After your are done commit your changes to branch **source** and deploy to branch **master**

```bash
$ git status
$ git diff *
$ git add .
$ git commit -m
$ git push origin source
$ ./bin/deploy --user
```
# Updating a Gem without modifying the Gemfile

Sometimes some security issues arise and it's necessary to update a dependency.

```bash
$ bundle update name_to_update
```

In case that you want to update every gem:

```bash
$ bundle update
```

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
