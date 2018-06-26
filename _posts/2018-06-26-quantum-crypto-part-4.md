---
layout: post
toc: true
---

This is the last in the Quantum Cryptography series of posts. This post
covers the limitations of current methods and contemplates
possible avenues of evolution for the technology.

Limitations
===========

Distance
--------

Most QKD systems today rely on optical transmission of photons, either
via telecommunications fiber or free space. Both media pose technical
challenges in terms of attenuation and preserving polarization that must
be overcome if global QKD is to become a reality. The primary form of
noise in photonic transmissions is loss over distances {%cite Sangouard2011%}.
Currently, the best systems known span distances of between 100 and
140km {%cite Dixon2008; @Yuan2007a%}. Classical communications work around the
problem of attenuation by using repeaters, something that is difficult
to emulate in the quantum regime due to the no-cloning theorem. A
working quantum repeater would require matter quantum memory
{%cite Sangouard2011; @Duan2001%}, and might even be more difficult than the
task of developing a universal quantum computer, due to the constraints
involved (in particular, the quantum memories in question must satisfy
DiVincenzo's five criteria for universal quantum computers, as well as
his additional (harder) criterion. {%cite DiVincenzo2000%}). However, the
forefront of research today suggests alternate formulations of quantum
repeaters that do away with the requirement for quantum memories and may
provide a feasible way to extend the range of QKD {%cite Azuma2015%}.

Speed
-----

Current QKD systems are limited in key transfer rate by a multitude of
factors; the sifting process, transmission errors, detector
inefficiencies, attenuation, additionally key bits sacrificed to privacy
amplification, as well as other influences all combine to reduce the
number of secure viable key bits transmitted in a QKD link. The
transmission rate is intricately tied to the range of the system;
increased range decreases the probability that a qubit reaches the
destination receiver, and attenuation along the way may mean that
detection probability is lowered even if the destination is reached. The
rate also depends on the details of the system used; certain approaches
offer higher rates than others. The experimental SECOQC project
{%cite Peev2009%} recommended a baseline key transmission rate of 1kbit/s over
a 25km link, which was exceeded handily by some systems used in the
project, with even higher rates at shorter distances, as high as 50
kbits/s over an 80m free space link {%cite Peev2009%}. In fact, rates as high
as 1.02 Mbit/s have been seen at distances of 20km using fiber links
{%cite Dixon2008%}. In comparison to traditional communications
infrastructure, such rates are almost laughably small, which means that
QKD is likely to be used only for the highest security applications in
the near future. However, advances in high-speed single photon detectors
{%cite Yuan2007%} promise, among others, promise far higher rates in years to
come.

Cost
----

A significant obstacle to the widespread adoption of QKD systems is the
high cost of setting up and maintaining the equipment required for their
use. Here, the use of telecommunications fiber, as well as the reliance
on classical communications technologies for certain parts of the
protocols mitigate some of the investment, as existing infrastructure
can be reused. On the other hand, specialized equipment for the
generation of entangled pairs, for instance, or the modulation of weak
light pulses, require capital investments that are many orders of
magnitude higher than traditional cryptographic systems. The emergence
of a number of companies in the QKD space (ID Quantique, MagiQ
Technologies, Swiss Quantum, Battelle, etc.) are a promising indicator
that demand for such systems is healthy in environments where security
is of paramount importance, and the prevalent mood is that mass
production and economies of scale, coupled with technological advances
in the manufacture of the components required (detectors, especially),
will eventually bring the cost of QKD systems down to a manageable
amount. Furthermore, QKD systems are often much cheaper than the
alternative in many high security environments, where the prevalent
method of key distribution is the use of couriers to physically exchange
random key material, with a much lower security guarantee.

Future
======

Possible adoption trajectories
------------------------------

The types of environments best suited for the balance of security and
cost offered by QKD networks are controlled, high-value organizations
that require extremely strong security guarantees over long periods of
time. QKD, combined with one-time pad encryption, offers *unconditional
security*, as defined by Diffie and Hellman {%cite Diffie1976%}, which
protects secrets from any form of cryptanalysis, no manner how
computationally or mathematically advanced. Compare this with the
vulnerability of traditional encryption schemes to expanding
computational power over time; leaps in the amount of processing power
possessed by novel systems reduce the complexity of a brute force attack
on, say, 256-bit AES to the point where ciphertexts from today, stored
by an adversary until such time in the future as computational power has
reached the point where it is feasible to perform cryptanalysis on such
ciphertexts, maybe decrypted in the future. Only the one-time pad offers
any guarantee against such attacks, and only QKD has the potential to
distribute keys for use in the one-time pad in a relatively efficient,
scalable manner. Therefore, sensible predictions about the adoption of
QKD must begin with environments such as government organizations,
financial institutions, global military organizations, among others. It
is possible that QKD technology may follow a trajectory not too
different from that of the internet; beginning as the sole province of
research institutions and government-funded projects, and then gradually
expanding to encompass businesses and industry, eventually reaching a
sort of threshold where widespread mass adoption becomes possible, and
the dream of provably secure communication for all becomes true.

Satellite-based QKD
-------------------

One of the most attractive proposals for a global QKD system leverages
free space transmissions between ground and satellite systems for key
exchange. Development in this area is well underway. A research effort
from 2002 demonstrated secure key exchange over a free space link at
23.4km {%cite Kurtsiefer2002%}, with the attenuation results obtained
indicating that near earth key exchange (at a range of 500-1,000km)
should be possible in the near future. It has been almost 13 years since
this result, and the proposal made by that paper seems achievable at
present. A collaboration between industry partners and the Canadian
Space agency over a mission called QEYSSat (Quantum Encryption and
Science Satellite) is underway, proposing the use of a microsatellite
located in low earth orbit at about 600km carrying an optical receiver
with 40cm aperture as the main optical instrument. The group has
conducted studies of transmission losses in such regimes, successfully
operating a system at upto 60dB losses {%cite Meyer-Scott2011%}, even in the
face of strong turbulence, countered with careful post-processing
{%cite Erven2012%}. Ensuring the robust and reliable operation of such a
service remains a goal for the future, paving the way for optical links
to low earth satellites that may eventually form the basis for a global
system of QKD. Further applications of satellite QKD could be in the
secure distribution of keys for satellite remote access and for secure
inter-satellite links {%cite PerdiguesArmengol2008%}.

![](/assets/quantum/satellite.png)
*{%cite Jennewein2014%} An artist's rendering of QKD via a trusted satellite node*

The Quantum Internet {%cite Kimble2008%} {#the-quantum-internet}
----------------------------------

One of the key results of research into quantum cryptography is the
maturation of technologies that allow for the creation of purely quantum
links between systems, transporting quantum states between
geographically separated sites with high fidelity, maintaining important
quantum properties like entanglement. Carrying out this idea to its
logical conclusion leads to the idea of a quantum internet, whereby a
network of computational nodes linked by quantum channels would be
empowered to perform computational tasks beyond classical physics. For
instance, Preskill's notion of quantum software {%cite Preskill1999%}, used to
describe difficult-to-create quantum states that perform useful quantum
computations, would find a distribution mechanism in such a quantum
internet. Perhaps most dazzling is the exponential increase in state
space that would be produced by full quantum connectivity between nodes
of such a network; a fully quantum network of $n$ nodes each with $k$
quantum bits would have a state space on the order of $2^{kn}$, whereas
such a network that utilized only classical connections would have a
state space of significantly lower dimension, on the order of $n2^k$.
However, fully realizing such a system would require overcoming rather
large technical difficulties in local quantum processing, quantum
repeaters, and error-corrected quantum teleportation, as well as
advances in quantum memory. Theoretically, the developments required
would signal a shift in focus from concentrating on highly specialized
components (say, systems comprising of single electrons trapped in
crystals) to more complex dynamical quantum systems composed of many
such building blocks.

Bibliography
=========
{% bibliography --cited %}
