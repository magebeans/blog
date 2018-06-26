---
layout: post
---

This is the second in the Quantum Cryptography series of posts. This post
covers some of the theoretical underpinnings of QC, including some of
the earliest protocols and a metric for the error rate of
a quantum channel.

The BB84 Protocol {%cite Bennett1984%}  {#the-bb84-protocol}
---------------------------------

The BB84 protocol is widely accepted as the first quantum cryptography
protocol published. Its name comes from the initials of the authors of
the paper that first explained it (Bennett and Brassard), concatenated
with the year (1984) that the paper was published in. The protocol
relies on two fundamental tenets of quantum theory for its security; the
uncertainty theorem and the no-cloning theorem. The uncertainty theorem
extended from conjugate variables to conjugate bases implies that only
one bit of information to be derived from measurement on a single qubit
{%cite Wiesner1983%}. More concretely, consider a qubit that has one of the
four following possible values:

$$\begin{array}{l l l l}
    \text{Bit 0:} & \ket{\psi_0} &= \ket{0} & \\
    \text{Bit 1:} & \ket{\psi_1} &= \ket{1} & \\
    \text{Bit 0:} & \ket{\psi_2} &= \ket{-} &= \frac{1}{\sqrt{2}}(\ket{0}-\ket{1}) \\
    \text{Bit 1:} & \ket{\psi_3} &= \ket{+} &= \frac{1}{\sqrt{2}}(\ket{0}+\ket{1}) \\
\end{array}$$

The true value of the qubit takes four possibilities, which means that
at least two bits of information are required to distinguish between the
possible values. First, a choice of basis must be made between the
computational basis $\left(\ket{0}, \ket{1}\right)$ vs. the Hadamard basis
$\left(\ket{+},\ket{-}\right)$. The second bit comes from a measurement made in the
correct basis which then tells us which of the basis states the qubit is
in. Suppose we take a qubit that is in the computational basis and
measure it in the Hadamard basis. Since the two bases are conjugate
{%cite Wiesner1983%}, the result we get will be completely random; we
$\ket{0}$ half the time and $\ket{1}$ the other half. The same holds
true if we take a qubit in the Hadamard basis and measure it in the
computational basis. Therefore, choosing the wrong basis for measurement
completely destroys the information held by the qubit. This introduces
another possibility by which the information held by a qubit could be
extracted; we simply clone the qubit, and perform a measurement in the
computational basis on one copy, and a measurement in the Hadamard basis
on the other copy. This is impossible thanks to the no-cloning theorem,
and completes the intuition behind the foundations of the security of
the BB84 protocol.

Alice begins by generating two random bit strings of length $n$, $a$ and
$b$. $a$ will form the basis for the shared secret, while $b$ will
decide which base to use in order to encode the current bit in $a$. We
index the strings from left to right in the binary representation, so
that $a_1$ is the leftmost bit in the representation of $a$. Now, Alice
sets up her machinery so as to enable her to transmit one of the four
qubits below:

$$\begin{array}{l l l l}
    \text{Bit 0:} & \ket{\psi_0} &= \ket{0} & \\
    \text{Bit 1:} & \ket{\psi_1} &= \ket{1} & \\
    \text{Bit 0:} & \ket{\psi_2} &= \ket{-} &= \frac{1}{\sqrt{2}}(\ket{0}-\ket{1}) \\
    \text{Bit 1:} & \ket{\psi_3} &= \ket{+} &= \frac{1}{\sqrt{2}}(\ket{0}+\ket{1}) \\
\end{array}$$

For every index $i$ beginning at $1$ and ending at $n$, Alice transmits
the first basis vector if $a_i$ is zero and the second basis vector
otherwise. Furthermore, she transmits in the computational basis if
$b_i$ is zero and the Hadamard basis if $b_i$ is one. Put together, the
numbers formed by the bits $b_ia_i$ are precisely the index of the qubit
to use to encode the secret. An example transmission, with a random
short $a$ and $b$, along with the corresponding series of qubits is
shown below:

$$\begin{aligned}
    & b = 0110101 \\
    & a = 1011010 \\
    & \psi_1\psi_2\psi_3\psi_1\psi_2\psi_1\psi_2\end{aligned}$$

Bob, on the other end of the transmission, generates his own random bit
string $c$ of length $n$. As he receives Alice's $i'th$ transmission, he
measures it in the computational basis if $c_i$ is zero and the Hadamard
basis otherwise. In this manner, he destroys the information in the
qubit roughly half the time while accurately recovering it the other
half of the time. The amount of information Bob recovers is further
limited by transmission errors or inefficiencies in his detector.

The next phase of the protocol occurs on a public communications channel
that protects against active eavesdropping. As the name implies, the
channel is completely open to passive eavesdropping, implying that the
adversary Eve knows everything that is sent over the public channel.
However, we assume that it is impossible for an adversary to insert
arbitrary messages or modify existing messages on the channel. To see
that this assumption is reasonable, consider the case where the public
channel is a medium such as a newspaper, and the information conveyed is
simply present in the form of an advertisement in the classifieds
section addressed to the receiver. For every qubit that is not lost in
transmission, Bob reports, over the public channel, the base used to
measure the value of that qubit. Alice replies with a confirmation every
time Bob reports the correct base, and a refutation when he does not.
Both Alice and Bob now know which qubits were transmitted accurately and
thus end up with a shared secret consisting of exactly those bits. Since
both Alice and Bob choose the qubit basis independently and at random,
there is a fifty percent chance that they choose the same basis for
qubit $i$, and so, ignoring transmission errors, about half the qubits
transmitted are correctly received by Bob, yielding a secret of length
about $n/2$. This process is known as sifting, and the generated key is
commonly called a sifted key, owing to obvious parallels between the
physical process of sifting physical mixtures to extract useful
components.

Bennett and Brassard suggest sacrificing a third of the derived key bits
in order to guarantee security against eavesdropping in the following
manner: Alice and Bob publicly compare a third of the derived key bits,
keeping the remaining bits as valid key material only if they all agree.
To see why this works, consider the scenario with an eavesdropper
intercepting all of the $n$ qubits sent. Suppose Alice and Bob agree on
the basis used for $m$ out of the $n$ qubits sent. For each of the $m$
qubits, either Eve chose the wrong basis in which to intercept that
qubit, or she chose the correct basis. If she chose the correct basis,
both Alice and Bob's value for the qubit's state will agree. If she
chose the wrong basis, her first measurement destroyed the state of the
sent qubit, which means that the qubit she sent Bob has a random value
in the wrong basis. Since Bob used the same basis as Alice to measure
it, he used a basis conjugate to the basis Eve used, which means that
the value he measures is also random, and therefore matches Alice's
value with probability $1/2$. Since Eve has $1/2$ probability of
choosing the right basis, the probability of both Alice and Bob agreeing
on the value of an arbitrary qubit from the $m$ they chose the same
basis for, is:

$$\frac{1}{2} + \frac{1}{2} \times \frac{1}{2} = 3/4$$

Here, the first term accounts for Eve choosing the correct basis while
the second term accounts for the times Bob randomly gets the correct
value even after Eve chooses the wrong basis. However, Eve only has
information about the key if she guesses the basis correctly and if Bob
measures the basis correctly (she doesn't know the value of the qubit if
she guesses incorrectly, and the qubit isn't used in the key if Bob
guesses incorrectly), which happens $1/4$ of the time. Therefore,
intercepting $n$ qubits gives Eve at most $n/4$ bits of information
about the key, while disrupting $1/4$ of the bits Alice and Bob agree
on, which is to say that Alice and Bob have different valued key bits
for $1/4$ of the bits that Bob used the same basis as Alice did, as a
result of eavesdropping. Therefore, for each derived key bit, the
probability that tampering goes undetected is $3/4$, which means that
comparing a third of the key bits gives you a probability of $P_f$ that
Eve succeeds in going undetected, where

$$P_f = (3/4)^{c/3}$$

Alice and Bob can choose $n$ and the fraction of $m$ to sacrifice to be
as large as required to satisfy an upper bound for the probability that
Eve gets away with eavesdropping undetected.

In the general case, if Eve intercepts a fraction $\lambda$ of
transmitted qubits, the probability of one of the $m$ key qubits being
incorrect is $\lambda / 4$, where the factor $\lambda$ is the
probability of the chosen qubit to be intercepted, and $1/4$ is the
probability that Alice's and Bob's values for the qubit don't match,
given that it is intercepted by $Eve$. Therefore, if a fraction $\eta$
of the key bits are sacrificed to check for eavesdropping, the
probability of a false negative (where eavesdropping goes undetected) is
simply $P_f'$, where

$$P_f' = (1-\lambda/4)^{\eta m}$$

Given that all goes well, at the end of the transmission, Alice and Bob
share a secret key of length $(1-\eta)m$ which can be used to
symmetrically encrypt further communications, e.g. using a one time pad.
This assumes that there are is no noise in the transmission. The case of
noisy transmissions can be analyzed using Quantum Error Correction
Codes, and yields a similar security guarantee. This high level overview
of the protocol shows how Alice and Bob can come to share some classical
information with a high degree of correlation. Accounting for
transmission errors and the fact that Eve obtains some information about
the shared secret, we see that this transmission is not perfect. The
work of Bennett, Brassard and Robert ({%cite Bennett1988%}) outlines a process
they term Privacy Amplification, whereby classical discussion on the
public channel can be used to reduce the amount of information Eve has
about the shared secret, as well as to correct transmission errors. It
is this process that completes the key distribution, leaving Alice and
Bob with a perfectly correlated key with a high probability and reducing
the information leaked to Eve by an arbitrary amount.

### SARG04 {%cite Scarani2002%} {#sarg04}

The preceding discussion of the BB84 protocol has focused on the single
photon picture. Single photon production and detection for quantum key
distribution remain technologically difficult, although it is the focus
of several ongoing research efforts with varying degrees of success,
with InGaAs based avalanche photodiodes being at the forefront
{%cite Comandar2014%}. Most practical implementations of BB84 use weak laser
pulses in which Alice has encoded the bit to be sent, which introduces
the possibility of circumventing the guarantee provided by the
no-cloning theorem; Eve simply diverts some of the photons while
allowing the rest to proceed to Bob. Such an attack is known as a
photon-number splitting attack (PNS). If we consider an Eve to be
constrained only by the laws of physics, it is possible for her to store
the diverted photons in a quantum memory construct and wait until the
sifting phase, when Alice and Bob reveal the used bases, to measure the
stored photons in the correct base, obtaining full information about
them and precluding any process by which Bob and Alice can distill
completely secret keys. Moreover, Eve does not introduce any detectable
errors in this manner, resulting in insidiously successful leakage of
information.

The extreme weakness of the protocol against this attack is due to the
orthogonality of paired states into which the bits are encoded; if Eve
knows the basis used, all she has to do is perform the appropriate
measurement to distinguish between the states, and therefore obtain the
transmitted bit. Intuitively, this can be circumvented by using
non-orthogonal states. Although the states are not orthogonal, one can
construct a measurement that distinguishes between the two states, with
the caveat that an inconclusive measurement is sometimes obtained. In
effect, a greater portion of the transmitted qubits must be satisfied
during sifting. For concreteness, a simple such protocol (from the
original paper by Scarani et al.) is outlined here.

Alice randomly sends one of the four states $\ket{\pm x}$ or
$\ket{\pm z}$ to Bob, who randomly measures either in the $x$ basis
using $\sigma_x$ or the $z$ basis using $\sigma_z$. In this protocol,
successful transmission of $\ket{\pm x}$ corresponds to a 0, while
successful transmission of a $\ket{\pm z}$ corresponds to a 1. During
the sifting procedure, instead of revealing the bases, Alice announces
one of the four pairs of non-orthogonal states out of every possible
combination of sent photons, $\{\ket{\pm x}\} \times \{\ket{\pm z}\}$,
where the product is the cartesian product over the possible states.
This has the effect of limiting the possible valid measurements Bob can
make in the following manner: Suppose Alice announces
$\ket{+x}, \ket{+z}$. If Bob measured $\sigma_x$ and obtains the result
+1, he must discard the qubit, as such a result would have been possible
by measurement using $\sigma_z$ as well. Similarly, if he measures +1
using $\sigma_z$, he must discard the qubit, as it would have been
possible to obtain the same measurement using $\sigma_x$, and therefore
he cannot distinguish between the two possibilities. However, if he
measures $\sigma_z$ and obtains a result -1, he knows that the qubit
sent must have been in the state $\sigma_x$, as it would have been
impossible to obtain -1 using the $\sigma_z$ measurement, given that
Alice announces that she sent either $\ket{+x}$ or $\ket{+z}$.
Therefore, such a measurement allows Bob to keep the qubit, and add a
classical bit 1 to his sifted key. By symmetry, this leaves Bob with a
fourth of the raw key material after sifting, compared to the $1/2$
fraction obtained in classical BB84.

![](/assets/quantum/compare.png)
{%cite Jeong2014%} A comparison of secret key rate for BB84 (red) vs. SARG04
(blue)

However, this results in a protocol that protects from PNS attacks by
significantly reducing the amount of information that Eve can obtain
about diverted photons. Scarani's original paper {%cite Scarani2002%} provides
a proof of this fact, calculating the information that Eve obtains in a
storage attack to be about $0.4$ bits per pulse at an attenuation rate
that allows her to keep one photon out of every pulse, compared to
complete leakage of information in the case of a storage attack on BB84.

Quantum Bit Error Rate {%cite Gisin2002%} {#quantum-bit-error-rate}
-----------------------------------

A variety of environmental factors make it so that not all of the
photons transmitted by Alice are detected correctly by Bob. In practice,
some measure of reliability is required in order to characterize the
degree of losses induced by the environment. The quantum bit error rate
(QBER) provides this measure. It is defined, quite simply, as the ratio
of wrong bits to the total number of bits received, and is normally on
the order of a few percent. Note that this definition strictly only
applies to the BB84 protocol, and must be modified slightly for other
protocols.

$$\text{QBER} = \frac{N_{wrong}}{N_{right}+N_{wrong}} = \frac{R_{error}}{R_{sift}+R_{error}} \approx \frac{R_{error}}{R_{sift}}$$

Clearly, the sifted rate is half the raw rate at which Bob detects
incoming photons, corresponding to the approximately one-half likelihood
that Alice and Bob pick compatible bases. The raw rate has four major
contributions; the pulse rate $f$, the mean number of photons per pulse,
$\mu$, the probability $t_{link}$ of the photons arriving at the
analyzer, and the probability $\eta$ of the photon being detected,
giving us that:

$$R_{sift} = \frac{1}{2}R_{raw} = \frac{1}{2}f\mu t_{link}\eta$$

Certain phase-coding setups introduce an additional factor $q$,
typically $1$ or $\frac{1}{2}$, which accounts for non-interfering path
combinations, which results in the following modification:

$$R_{sift} = \frac{1}{2}qf\mu t_{link}\eta$$

Analyzing the error rate yields three contributions; photons that end up
in the wrong detector due to imperfections in the interferometer,
detector dark counts resulting from environmental light that is not
adequately filtered out, and uncorrelated photons due to imperfect
photon sources.

The first, $R_{opt}$, is simply the sifted-key rate multiplied by the
probability that the photon goes to the wrong detector, $p_{opt}$. This
is clear, as the photon must have been transmitted successfully in order
for it to reach a detector, which is essentially the same as the
condition required for it to be part of the sifted key.

$$R_{opt} = p_{opt} R_{sift}$$

The second, $R_{det}$, is independent of the bit rate, and only
contributes to the error rate if the dark count occurs during the time
when a photon is expected. Furthermore, the dark count occurs half the
time when Alice and Bob choose incompatible bases (in which case it does
not contribute to the error, as the corresponding detection is
eliminated during sifting) and an additional 50% chance of occurring in
the correct detector. If $p_{dark}$ is the probability of registering a
dark count per time window, we have the following expression:

$$R_{det} = \frac{1}{2} \frac{1}{2} f p_{dark}$$

The third factor arises due to imperfect photon sources, where two
photons in different pairs arrive in the same time window, but not
necessarily in the same state. This is only relevant in systems using
entangled photons. If $p_{acc}$ is the probability of finding a second
photon within the time window belonging to a different pair than the
first photon detected, where the factors of $\frac{1}{2}$ are due to the
same reasons outlined before.

$$R_{acc} = \frac{1}{2} \frac{1}{2} p_{acc} f t_{link} \eta$$

Therefore, the QBER is simply the ratio from earlier, with the
respective rates expanded into their separate contributions:

$$\begin{aligned}
    QBER &= \frac{R_{error}}{R_{sift}}  \\
    &= \frac{R_{opt} + R_{det} + R_{acc}}{R_{sift}} \\
    &= p_{opt} + \frac{p_{dark}}{t_{link}\eta2q\mu} + \frac{p_{acc}}{2p\mu} \\
    &= QBER_{opt} + QBER_{det} + QBER_{acc}\end{aligned}$$

The first contribution is entirely distance independent, and measures
the quality of the optical set up used. Different QC setups have
differing contributions and corresponding countermeasures to improve
$QBER_{opt}$, and this measure provides a single tool to evaluate the
quality of the optical set up alone.

The second contribution is distance dependent, increasing with distance
as the probability of a photon arriving at the detector $t_{link}$ goes
down with increasing distance while the dark-count rate does not
fluctuate significantly. Therefore, issues with range are solely a
function of detector noise; better detectors allow for QC over much
higher distances.

It is possible to calculate the maximum range of a QC system given these
parameters, where greater distances result in intolerably high values of
the QBER. Gisin{%cite Gisin2002%} finds the maximum range to be about 100km,
practical maxima being closer to 50km owing to a variety of factors.

Bibiliography
--------
{% bibliography --cited %}
