Math website project
====================

The "problem"
-------------

I have a vision of a better way of writing mathematical papers than currently exists.
LaTeX is currently the standard for writing mathematics, but it's so *static* and *flat*.
.. I need to think of a better way of putting it than "flat"


In what ways is it static?
Well, LaTeX was designed with the goal of rendering documents for print publication, and it's currently not possible to include interactive elements within a PDF (besides simple forms and links).
But what if you wanted to expand or collapse a proof (or all proofs in the document)?
What if you wanted to collapse or expand parts of proofs?
What if you wanted to include an interactive figure?

What do I mean by LaTeX being flat?
What I am getting at is that LaTeX does not preserve the syntax of formulas nor the data behind plots.
For example, (F + G)(xy) could mean "multiply (F + G) by xy" or "xy is the argument of function (F + G)".
LaTeX does not preserve the symantic difference between these two, but something like Content-MathML does.
While an ambiguity like this might seem harmless in a mathematical paper where the reader inuitively knows the difference, in an interactive environment it creates difficulties for the computer trying to keep track of things.

As another example of this, often when I am writing a paper I find myself unwittingly switching from using A, B, C... for my arbitrary sets to using X, Y, Z...
Of course this seems like nitpicking, b
ut there is a better way.
Why not instantiate new sets in the code like "set1 = NewSet()" and have the software figure out how to render the symbols for the arbitrary sets?
You could even make it configurable.

As for plotting, one of my biggest pet peeves with LaTeX is that it can't (at least easily) label plot axes itself; the result is every plot in my document has labels that are different fonts and font sizes.
I've always wished there was a way to put the labels in separately so they're all the same size and font as the document's text.
This might be asking a lot, but I wish there was a way to JUST send the data along with the tex file, and have it generate the plots on the fly, as opposed to having to keep track of dozens of png files.

The "solution"
--------------

I think a solution to these problems is possible and doesn't exist yet.
I think when you break the problem down, solutions to the sub-problems already exist, but no one has put it together yet.

The main things I want from this software are:

* **Interactivity**: I think this needs to be a web project.
  Interactivity is everywhere with web technologies.

* **Content-awareness**: This is where Content-MathML comes in.
  If we wrote our equations using Content-MathML, this part is already solved.

* **Cross-referencing**: This project NEEDS to have cross-referencing support that is at least as good as LaTeX's.
  I think LaTeX's cross-referencing could be improved by having things like theorems, proofs, sections, chapters, important formulae, etc. be *objects* in some object-oriented environment.

* **Ease of use**: I absolutely LOVE typing equations in LyX, and I hate typing them in plain LaTeX.
  I've been playing around with Content-MathML and I think having to remember all of these tags is annoying.
  I don't know how to get around this though; you could write shorthands for them, but then you have to know all the shorthands.

(Brainstorming)
---------------

* I want to get some practice using coq or some other proof assistant thing.
  I think experiencing that would help guide this project

* I'm actually thinking maybe I could use Python to do this.
  I could create classes for each of the tags in the Content-MathML specification, and maybe streamline it with operator overloading.
  This actually seems like an AWESOME idea!
  Basically, you would write python scripts that can output to MathML+HTML *or* LaTeX!
  I could also use templating to divvy up the content more; like if you want to have your text content be separate from the python that ties it all together!
  The cool thing about this is that it lets you have the power of python while you're writing your document ;)
