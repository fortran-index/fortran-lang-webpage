# Mini-book Tutorials on fortran-lang.org

This guide will cover how to write mini-book tutorials for the [Learn](https://fortran-lang.org/learn)
section of <https://fortran-lang.org>.

See [contributing guidelines](contributing) for general guidance on contributing to <https://fortran-lang.org>.

## 0. Mini-book formats

Mini-books are designed to be mostly self-contained tutorials on a particular feature of the Fortran language.

There are two types of mini-book format:

- **Single-page:** all content is written within a single markdown file and displayed
  on a single webpage;

- **Multi-page:** tutorial content is written across multiple markdown files and displayed
  as a collection of webpages.

The choice of book type depends on the length of your content and how you intend to structure it.

Consider the table of contents that will be produced:

- Single-page books have **one level** of navigation: a link for each heading in the tutorial in inpage-toc (toc on the right hand side of the page).

- Multi-page books have **two levels** of navigation: a link for each heading in the tutorial in inpage-toc (toc on the right hand side of the page) and sidebar-toc (toc on the left hand side of the page showing different pages in directory).

Single-page mini-books are simpler to produce and should be used for brief topics or short tutorials that will
eventually be subsumed into a more-comprehensive multi-page book.

Multi-page books are recommended for more-comprehensive tutorials that can be structured with one subtopic per page.

The rest of this guide is split into two sections, one each for the single-page and multi-page book types.

## 1. Single-page mini-book

The steps required for publishing a single-page mini-book are:

- Create a new markdown document in the `./learn` directory

- Write your tutorial content

- Add an entry to [data/learning.yml][learning_yml] for your new mini-book

- Open a pull request

### 1.1 Writing your mini-book in markdown

For single-page mini-books your tutorial will be entirely contained within a single markdown document.

First create a new markdown document in the `./learn/{{name_of_minibook}}/` directory with the `.md` file extension
and a short name that concisely describes the topic of your tutorial, _e.g._ `./learn/{{name_of_minibook}}/file_io.md`.

Open your new markdown file and append an entry in the toc of `learn.md` in the following format:

```
:::{toctree}
:hidden:

learn/quickstart/index
learn/best_practices/index
learn/os_setup/index
learn/building_programs/index
learn/intrinsics/index
learn/{{book-filename}}
:::
```

Replace `{{book-filename}}` with the filename of your markdown file
but **excluding the `.md` extension**. There should also be no trailing slash.

**Example:** header

```
:::{toctree}
:hidden:

learn/quickstart/index
learn/best_practices/index
learn/os_setup/index
learn/building_programs/index
learn/intrinsics/index
learn/file_io
:::
```

**NOT:** `permalink: /learn/file_io.md`

**NOT:** `permalink: /learn/file_io/`

You can now fill the rest of the file with your tutorial content written in markdown;
see [Kramdown syntax](https://kramdown.gettalong.org/syntax.html) for documentation on
the markdown implementation.

### 1.2 Structuring your mini-book with headings

You should use headings to break-up your single-page mini-book into a logical structure.
Each heading will show up in the hyperlinked table-of-contents.

In markdown, headings can be written as:

```markdown
# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6
```

**Note:** make sure to include a blank line before your heading.

### 1.3 Add your mini-book to the Learn page

To add your new mini-book to the _Learn_ page, you need to add a new entry
in the [data/learning.yml][learning_yml] datafile.

Open this file and create a new entry under the `books:` field in the following format:

```yaml
- title: {{book-title}}
  description: {{book-description}}
  category: {{book-category}}
  link: /learn/{{book-filename}}
```

The `title` field is what will be displayed on the _Learn_ page for your mini-book
and should generally be the same as the `title` field in your markdown file, but this isn't required.

The contents of the `description` field is also displayed on the _Learn_ page
and should briefly summarise the contents of your mini-book tutorial.

The `category` field should match one of the categories listed at the top of the data file (under
the `categories:` field) and is used to group tutorials on the Learn page.

The `link` field should exactly match the `permalink` field in your markdown document.

**Example:** `learning.yml` book entry

```yaml
- title: File input and output
  description: A tutorial on reading and writing files in Fortran
  category: Getting started
  link: /learn/file/file_io
```

Save the modified `learning.yml` data file and run fortran_package.py and rebuild the website on your local machine to check the results.
If successful, a new link should appear on the \_Learn* page with the title of your new mini-book.

Once you have completed your mini-book and added an entry to the `learning.yml` data file, open a pull request
at <https://github.com/fortran-lang/webpage> (see [CONTRIBUTING][contributing_md]).

## 2. Multi-page mini-books

The steps required for publishing a multi-page mini-book are:

- Create a new folder in the `./learn/` directory

- Create an `index.md` file in your new folder

- Write your tutorial content in markdown files in your new folder

- Add an entry to [data/learning.yml][learning_yml] for your new mini-book

- Open a pull request

### 2.1 Create a new folder for your mini-book

Create a new folder in the `./learn/` directory with a short name that concisely describes the topic of your tutorial, _e.g._ `./learn/coarrays/`.
All pages of your mini-book will be contained within this folder.

The first page of your mini-book should be called `index.md`, so create a new markdown file in
your mini-book folder called `index.md`, and add a toc in the following format in all the markdown files:

```
:::{toctree}
:hidden:

file1
file2
:::
```

**There should be no trailing slash.**

**Example:** toc for `index.md`

```
:::{toctree}
:hidden:

learn/quickstart/index
learn/best_practices/index
learn/os_setup/index
learn/building_programs/index
learn/intrinsics/index
:::
```

**NOT:** `permalink: /learn/coarrays/`


you should populate the remainder of `index.md` with an introduction to your mini-book tutorial which may include: a summary of the concepts covered; any prerequisites; and any references to other related mini-books or useful third-party resources.

### 2.2 Add pages to your mini-book

For each new page in your mini-book, create a new markdown file in your mini-book folder.

As with single-page mini-books, you should use headings to break-up each
page into a logical structure.
Each heading on the current page will show up in the inpage table-of-contents.

### 2.3 Add your mini-book to the Learn page

To add your new mini-book to the _Learn_ page, you need to add a new entry
in the [data/learning.yml][learning_yml] datafile.

Open this file and create a new entry under the `books:` field in the following format:

```yaml
- title: {{book-title}}
  description: {{book-description}}
  category: {{book-category}}
  link: /learn/{{book-folder}}
  pages:
    - link: /learn/{{book-folder}}/{{page1-filename}}
    - link: /learn/{{book-folder}}/{{page2-filename}}
    - link: /learn/{{book-folder}}/{{page3-filename}}
```

The `title` field is what will be displayed on the _Learn_ page for your mini-book
and should generally be the same as the `title` field in your `index.md` markdown file, but this isn't required.

The contents of the `description` field is also displayed on the _Learn_ page
and should briefly summarise the contents of your mini-book tutorial.

The `category` field should match one of the categories listed at the top of the data file (under
the `categories:` field) and is used to group tutorials on the Learn page.

The top-level `link` field should exactly match the `permalink` field in your `index.md` file.

Each `link` field under `pages` should exactly match the `permalink` field in each of your subsequent mini-book pages.

**Example:** `learning.yml` book entry

```yaml
- title: Parallel programming with Coarrays
  description: A tutorial on parallel programming using coarrays
  category: Parallel programming
  link: /learn/coarrays
  pages:
    - link: /learn/coarrays/background
    - link: /learn/coarrays/codimension
    - link: /learn/coarrays/examples
```

Save the modified `learning.yml` data file and run fortran*package.py and rebuild the website on your local machine to check the results.
If successful, a new link should appear on the \_Learn* page with the title of your new mini-book.

Once you have completed your mini-book and added an entry to the `learning.yml` data file, open a pull request
at <https://github.com/fortran-lang/fortran-lang.org> (see [CONTRIBUTING][contributing_md]).

[learning_yml]: https://github.com/fortran-lang/webpage/blob/main/data/learning.yml
[contributing_md]: https://github.com/fortran-lang/webpage/blob/main/CONTRIBUTING.md
