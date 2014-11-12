---
layout: post
---

Fractals
--------
Fractals are incredibly cool. You know you're in for a treat when fractional
dimensions are a (meaningful) thing and things like shapes that enclose a
finite area with an infinite perimeter actually exist. A lot of fractals are
mathematically tractable, which usually means pretty pictures. This post is
basically about pretty pictures.

Hilbert Curves
--------------
The particular fractal I've been playing with was first described by David Hilbert,
an illustrious man whose name prepends a veritable litany of mathematical concepts.
The curve itself is a continuous fractal space-filling curve - it has no breaks,
it is self-similar, and it fills space. 

Why is it useful? Locality. Take the 2 dimensional Hilbert curve, for instance. Two points
that are nearby on the curve (measuring distance along the curve) will also be
nearby in 2-D space. That is, for two points $$ A(x_1,y_1) $$ and $$ B(x_2,y_2) $$ that are
distances $$ d_1 $$ and $$ d_2 $$ along the curve, respectively, if $$ d_2-d_1 $$ is a small number,
the Euclidean distance between the points A,B - $$ \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2} $$ will
also be relatively small. Of course, the converse is not always true - there will
always be points that are nearby in 2-D space that, when mapped onto the curve,
are relatively far away. This is inevitable when mapping from a high-dimensional
space to a lower dimensional space. However, the Hilbert curve minimizes the number
of such pairs, which is nice.

RGB Space
---------
How do we represent color? As a 3-tuple of values indicating the intensity of
each of the primary colors - red, green, and blue. The color of each pixel in
an image is determined by the relative values of the red, green, and blue in it -
represented as a number between 0 and 255. So, for example, the tuple (0,0,0)
represents the color black - the complete absence of each of the primary colors.
The tuple (255,255,255) represents the color white - each primary color is maxed
out. The tuple (255,0,0) represents pure red, (0,255,0) pure green, and (0,0,255)
pure blue. Intermediate values represent various mixtures of the three primary colors.
You get the idea. 

Vanilla RGB
-----------
Now, I'd like to create an image with every single RGB color ever. This is nothing
new - tens of hundreds of people have done it before in ways ranging from 
utterly fantastically creative to tear-inducingly boring, and I'm only doing
this because it's intensely cool and the act of writing code that makes pretty
pictures is pretty satisfying. The first idea that pops up is to write a simple
nested for loop that matches every possible 3-tuple with element values between 0 and 255
to a 2-D coordinate, and draw the resulting image. It's boring, yes, but it's
easy to write, and runs quickly. Here's the result:

![vanillargb](https://cloud.githubusercontent.com/assets/1315728/4998116/52ac4820-69a3-11e4-9874-77f3bb00d603.png)

You can see how terrible the banding is - there is a green to blue transition across
the picture, with bands of pixels transitioning from "pure" green-blue colors
to redder variants. It's a pretty picture alright, just not as pretty as can be.

![greenvanillargb](https://cloud.githubusercontent.com/assets/1315728/4999191/18ad0410-69ae-11e4-9124-43f57cfeb014.png)

You can try changing up the order of the coordinates to vary the pictures. I've
done just that here, and you can see how the bands now transition across blue
and green, respectively.

Curving through space
---------------------
You're probably wondering what that whole spiel about fractals and Hilbert curves
at the beginning of the post was about, if all I'm going to be doing is talk
about colorspaces and pictures. Here's where it becomes important. In the
Vanilla version, I'd assigned 2-D coordinates to a point in RGB space more
or less arbitrarily - I flattened the 3-D coordinates into a single index, so
the point $$ (r,g,b) \rightarrow 256 \times 256 \times r + 256 \times g + b $$, 
and then unpacked that value into 2-D coordinates, so that the index i would map 
to the coordinates $$ ((i \div 4096) \mod 4096, i \mod 4096) $$.

This worked because I could treat the (r,g,b) tuple as a 3-digit base 256 number,
and also as a 2-digit base 4096 number, and $$ 256 \times 256 \times 256 = 4096 \times 4096 $$.
However, converting indices into 2-D coordinates in a more interesting manner results in way cooler
pictures. If, instead of unpacking the index as above, you treat the index as
distance along a Hilbert curve in two dimensions, you can map points in RGB space
to points along this curve. Here are the resulting pictures:

![vanillargbhilbert2](https://cloud.githubusercontent.com/assets/1315728/4999185/0ff1ac90-69ae-11e4-8e52-16ca163a3c92.png)


3: The final dimension
----------------------
Now that you've seen the prettifying power of Hilbert curves, it is time to use
Hilbert curves one last time to make the ultimate in color visualization techniques.
Recall the original "nice" property of Hilbert curves - locality. We'd like to
create an image that has smoother transitions into colors than the ones we made
above. The solution is simple - we change the index function. Instead of indexing
RGB space as though each point represents a 3 digit number is base 256, we determine
the index of the point by finding the distance of that point along the Hilbert curve
in 3-D that passes through all of RGB space.

We then use this index as the distance of the point along a 2-dimensional Hilbert
curve to determine the coordinate of the point on the image that we are creating,
and assign that point to the RGB color corresponding to that index.

Here are the results:

![Hilbertrgb](https://cloud.githubusercontent.com/assets/1315728/4989633/4b87920c-6949-11e4-9684-6ab5d75757a4.png)

Now THAT is pretty pretty.

More
----
The [Wikipedia](http://en.wikipedia.org/wiki/Hilbert_curve) page is a pretty good reference
for general information about Hilbert curves.

If you're interested in the math behind the conversion between Hilbert indices and
coordinates for the n-dimensional curve, [this paper](https://www.cs.dal.ca/sites/default/files/technical_reports/CS-2006-07.pdf) is pretty helpful.


