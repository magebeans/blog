---
layout: post
---

Now that we've got the meat of the algorithm out of the way, we can move on to more interesting fare; applications of the LLL algorithm in what I think are somewhat breathtaking results. First, the motivating problem we starting this whole wild goose chase with:

## Expressing algebraic numbers
We return to our motivating problem; finding a polynomial with rational coefficients such that one of its roots is a given number. Consider $$ r = 0.222521 $$, which is just $$ \cos \left( \frac{3\pi}{7} \right) $$ rounded down to a few decimal places. Given the involvement of scary trigonometry, it seems unlikely that we would be able to find a nice polynomial  such that $r$ is a root of it. However, suppose we take the lattice in $$ \mathbb{R}^5 $$ spanned by the following vectors:

$$ \left\{ \left[1, 0, 0, 0, 1000000r^3 \right], \left[0, 1, 0, 0, 1000000r^2 \right], \\
\left[0, 0, 1, 0, 1000000r \right], \left[0, 0, 0, 1, 1000000 \right] \right\} $$

If we could find the shortest basis vector in this lattice, it would be some integer combination of the above, of the form $$ \left[a, b, c, d, 1000000(ar^3 + br^2 + cr + d) \right] $$, with relatively small coefficients $$a,b,c,d$$ and $$ ar^3 + br^2 + cr + d $$ even smaller (close to zero). Applying LLL, the lattice reduction algorithm that the rest of this post will talk about, we find that the shortest basis vector is $$ 
[8,-4,-4,1,0] $$, which represents the equation $$ 8x^3 - 4x^2 - 4x + 1 $$, one of whose roots is, indeed $$  \cos \left( \frac{3\pi}{7} \right) $$. Interestingly enough, the other roots of the cubic found happen to be $$   \cos \left( \frac{5\pi}{7} \right) $$ and $$ \cos \left( \frac{\pi}{7} \right) $$. We can verify that plugging in $$ \cos(\frac{3\pi}{7})  $$ into this polynomial does in fact, result in zero through the use of arcane trigonometric identities and some sweat-inducing algebraic manipulation, left as an exercise to the reader. It struck me as kind of magical, the first time I encountered this trick, that you could start with this truncated approximation of a weird-looking irrational number and find a nice, well-behaved polynomial that goes to zero when you plug the original (untruncated) number in.
