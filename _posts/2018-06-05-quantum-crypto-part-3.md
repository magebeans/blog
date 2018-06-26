---
layout: post
toc: true
---

This is the third in the Quantum Cryptography series of posts. This post
covers some of the experiments undertaken in the field already.

The practical utility of a functional system of quantum key distribution
(QKD) is exceedingly high. It is perhaps too early to envision a future
where all secure transmissions occur over quantum channels, although
rapid progress is being made in pursuit of such a lofty goal.
Traditional QKD is distance limited, and can only proceed over a single
physical channel (either free space or telecommunications fiber, but not
at the same time in series due to issues with frequency propagation and
modulation {%cite Elliott2005%}). Furthermore, fiber cuts or intensive
eavesdropping result in denial of service, rendering a single link
effectively useless. However, a QKD network bypasses many of these
limitations to a surprising degree, in comparison to standalone QKD
systems. This section outlines some of the results that have been
obtained in recent years pertaining to the establishment and maintenance
of QKD networks.

Quantum Networks
----------------

QKD is fundamentally limited by the nature of the links possible between
devices; barring exotic protocols that are the subject of ongoing
research, almost all QKD protocols deal with point to point distribution
of keys, with the goal of establishing a shared secret between a pair of
users. This means that a transition to a networked distribution process,
where more than two users are involved, is relatively difficult, and
must be accomplished through additional protocols layered over the
fundamental choice of QKD protocol. {%cite Alleaume2014%} characterizes
quantum networks in the following ways:

1.  Optically switched quantum networks: In such networks, some optical
    operation (switching, multiplexing, beam-splitting, etc.) can be
    used to extend a network to multiple users. This can be done in two
    ways; passive switching, whereby a single beam of photons may be
    split into multiple, weaker beams, by randomly splitting single
    photons {%cite Townsend1994%}, or active switching, where two nodes of the
    network can be connected through a single quantum link by
    appropriately switching connections at other nodes so as to route
    the transmission correctly. Both methods effectively extend the
    quantum channel from one node to another with no interruption, and
    therefore carries no trust requirement on individual nodes; the same
    eavesdropping guarantees that secure single pair quantum
    transmissions are true for switched quantum channels, as the result
    is effectively a single, uninterrupted quantum channel that extends
    across multiple nodes {%cite Alleaume2014%}. Note, however, that this does
    not physically extend the range of the network, due to optical
    losses which effectively reduce the maximum range of the network.

2.  "Full" quantum networks: A true quantum network would need to use
    quantum repeaters to overcome signal losses over long distances,
    removing the requirement that intermediate nodes be trusted, much in
    the same manner as optically switched quantum networks. However,
    quantum repeaters involve quantum memory and elaborate quantum
    operations that are currently outside the scope of physical
    realization, although the quantum memory requirement is being
    challenged, for instance, by {%cite Azuma2015%}. An alternative would be
    to use quantum relays, which are simpler, as they do not require
    quantum memory to implement. However, current technological
    limitations make quantum relays impractical for arbitrary range
    extensions.

3.  Trusted Repeater QKD networks: This technique leverages classical
    memory to store local keys on every node, allowing for secure
    transmission of information between nodes using the local keys
    (using a One Time Pad). The local keys are replenished using QKD and
    are used for both unconditionally secure encryption and
    authentication. For global key transmission, the global key is sent,
    hop, by hop, along a series of nodes starting from the source and
    ending at the destination node. At each hop, the global key is
    encrypted and authenticated using the local key for that link,
    guaranteeing security as long as the intermediate nodes are trusted.
    Details of the security of this network architecture are in
    {%cite Salvail2010%}.

    ![](/assets/quantum/trusted_repeater_node_path.png)
    *{%cite Alleaume2014%} "Hop-by-hop" transmission of the global key along a path in the network, encrypting/decrypting using local keys at each step. Each colored link represents an identical key pair shared between two neighbouring nodes that is used to encrypt messages between the nodes*

It is important to note that the networks under consideration are
primarily for the purpose of key distribution. Any other communications
between the nodes is immaterial, and could be performed on any channel.
In order to simplify treatment and formulation of security guarantees,
the key distribution function of the network is entirely decoupled from
any other functions it may have. Only distribution is analyzed, under
the rationale that secure key distribution leads to provable information
theoretic communication using a one time pad.

The DARPA Quantum Network {%cite Elliott2005%} {#the-darpa-quantum-network}
----------------------------------------

The DARPA Quantum Network consists of 6 nodes operating through
telecommunications fiber between Harvard University, Boston University,
and BBN Technologies in Cambridge, and has been in continuous operation
since 2004. It is considered the first quantum cryptography network and
the first QKD systems operating continuously over a metropolitan area.

### Systems

The network uses four different kinds of hardware systems:

1.  BBN Mark 2 Weak-Coherent System: The core system transmits phase
    modulated photons over telecommunications fiber, using a Mach
    Zehnder interferometer to randomly modulate 1550nm laser pulses to
    one of four phases, thereby encoding both a basis and a value. The
    modulated pulses are augmented by bright pulses multiplexed over the
    same fiber to provide timing and framing information. On the
    receiving end, another interferometer randomly set to one of two
    phases performs demodulation, followed by by routing to one of two
    cooled InGaAs detectors.

2.  BBN/BU Mark 1 Entangled System: A BB84-based system utilizing
    polarization-entangled photon pairs that are transmitted over
    telecommunications fiber. The basis value pairs needed for
    transmission are encoded by polarization modulation, with random
    basis selection performed by a beam splitter in a purely passive
    fashion. Phase modulation is carried out using an external source of
    randomness that drives carefully tuned interferometers. A key aspect
    of the system is the incorporation of polarization controls in order
    to mitigate the polarization scrambling effect of telecommunications
    fiber. Errors are caused by significant attenuation resulting from
    the interferometers and beam-splitters used, as well as the fiber
    itself. Detector dark count introduces additional errors in the form
    of spurious detection events, all of which contribute to an increase
    in the Quantum Bit Error Rate of the system.

3.  NIST Freespace System {%cite Bienfang2004%}: Four vertical-cavity
    surface-emitting lasers (VCELs) are used to produce 250 picosecond
    pulses with a high extinction ratio, providing the quantum sources
    for the system. The pulses are then attenuated and coupled to
    freespace optics, where they are collimated and lineary polarized
    either vertically or in the $\pi/4$ direction, after which they are
    shaped to fill the output aperture of the transmission telescope. At
    the receiving end, an identical telescope receives the beam, passing
    it through a non-polarizing beam-splitting cube that performs a
    random choice of polarization basis, and then a polarizing
    beam-splitting cube that measures the value of the polarization
    through a fiber-couple detection box.

4.  QinetiQ Freespace System {%cite Tapster2005%}: A BB84-based four-laser
    faint-pulse transmission system is used to create the four
    alternative polarization states, generating pulses at a rate of
    10MHz. On the receiving side, measurement is performed automatically
    using avalanche photodiodes (APDs), after which software mechanisms
    perform sifting, error correction and privacy amplification to
    generate a secure key. The key characteristics of the system are
    compactness and portability, providing a final key exchange rate of
    about 1kbit/s at a range of 40m.

### Operation

At a high level, the systems used in the network perform the following
basic functions in order to arrive at a shared key:

1.  Sifting: Reconciliation of the raw secret bit streams as described
    in the section on the BB84 protocol. This removes errors resulting
    from failed detection (due to transmission losses, photons lost to
    eavesdropping without replacement, or detector inefficiencies),
    wrong basis choice (where Bob does in fact detect the transmitted
    photon, but randomly selected the wrong basis in which to measure
    it), or multiple detection events (where multiple detectors fire on
    Bob's end, as a result of which Bob cannot determine whether the
    symbol transmitted is a one or a zero, and therefore must discard
    it). This is done by public communication, after which only both
    parties end up with highly correlated "sifted" bits. The DARPA
    network implements both classic and SARG04 sifting.

2.  Error Detection and Correction: Elimination of bits damaged during
    transmission, which is an inherently probabilistic process that
    reveals information to an eavesdropper Eve. The end result is that
    both parties end up with identical copies of a secret bit string
    with high probability, about which an eavesdropper Eve has some
    information. The QBER may also be estimated in this stage. The DARPA
    network implements a modification of the Cascade protocol as well a
    Forward Error Correction technique called Niagra {%cite Pearson2004%} that
    is designed by BBN. The Niagra protocol offers reduced
    communications overhead, error correction delay, and CPU usage, at
    the expense of a small decrease in coding efficiency.
    {%cite Elliott2005%}.

3.  Entropy estimation: An accurate estimate of the amount of entropy in
    the sifted bits, beyond what Eve might have information about, is a
    necessary input to the privacy amplification step, and so is crucial
    for the security of a QKD system. The DARPA network implements four
    measures of this entropy, the details of which may be found in
    {%cite Elliott2005%}.

4.  Privacy Amplification: As detailed in previous sections, this allows
    Alice and Bob to reduce the amount of information gleaned by Eve
    about their shared bits to some low acceptable level. The DARPA
    network uses a linear hash function over the Galois Field $GF[2^n]$
    (corresponding to polynomials with coefficient $0$ or $1$ and degree
    less than $n$), where $n$ is the number of error-corrected bits in a
    transmission. The QKD node that initiates amplification selects the
    number of bits $m$ of the resulting hash, the primitive polynomial
    of the field, a multiplier $n$ and an $m$ bit polynomial to add to
    the product. Each side now has the information required to construct
    the hash, which is truncated to $m$ bits and used to perform privacy
    amplification.

5.  Authentication: In this phase, Alice and Bob assure each other that
    they are really exchanging information with each other, and not with
    Eve, with high probability. The DARPA network uses the existing
    authentication mechanisms of the Internet security architecture to
    perform authentication. This relies on pre-shared secret keys,
    although extensions using Universal Hashing are possible, which
    allow continuous authentication using secret bits derived from
    continuous QKD.

### Conclusion

The DARPA network represented a huge step forward in the implementation
of quantum networks, showing that it is viable to conduct QKD in a
reliable, practically autonomous fashion over a relatively widespread
geographic area. The consolidation of multiple QKD technologies and the
close partnership between government agencies, research institutions,
and industry were a promising forerunner of the kind of progress to
expect in future years, and the promises made by the success of this
endeavor have been borne out in the subsequent proliferation of QKD
implementations, notably the SECOQC {%cite Peev2009%} project.

QKD secured bank transfer {%cite Fedrizzi2005%} {#qkd-secured-bank-transfer}
-----------------------------------------

One of the most widely touted applications for a practical QKD system is
securing financial transfers. The first step in this direction was taken
in 2004, when researchers set up the first real-world application of an
entangled-state quantum cryptography protocol based on BB84. The
generated keys were used to secure an online wire transfer from the
Vienna City Hall to the headquarters of Bank-Austria Creditanstalt.

Keeping in mind the theoretical vulnerability of pulse-based BB84
implementations to photon number splitting (PNS) attacks, the system in
question used entangled photon pairs {%cite Ekert1991%}, in a modification of
the BB84. In such a system, the information to be transferred was stored
in correlations between the results of measurements on the individual
photons of the pair. Furthermore, the randomness of the generated key in
such a system arises from the quantum randomness of the measurement
itself, and does not rely on an external source of randomness, as
attenuated laser pulse systems do.

The photon source was a compact device based on type-II spontaneous
parametric down-conversion, which produces entangled pairs with
orthogonal polarizations. The produced pair was then split up, with one
photon being sent to Alice directly, and the other sent to Bob through
1.45km of optical fiber specially installed through the Viennese sewer
system. The associated computations for key distillation were carried
out on a dedicated QKD hardware device {%cite Lieger2004%}. Classical
communication was carried out over a TCP/IP connection through an
Ethernet bridge. The average QBER over the entire run time of the
experiment was less than 8%, of which 2.6% came from detection
imperfections and 1.2% came from imperfect production of the entangled
states, neither of which can be exploited by an eavesdropper and hence
can be excluded from the QBER factor in the calculations required for
privacy amplification. The resulting system had a raw transmission rate
of 80 bits/s after error correction and privacy amplification, which is
impressive for a first-use demo, but has been superseded by newer
technologies, as will be discussed in later sections.

The experiment carried out here marks an important milestone in the
practical development of QKD, demonstrating the viability of real-time
quantum cryptography systems in a realistic environment. The success of
this work clearly foreshadows the later successes of quantum
cryptography, such as its use in the Geneva elections of 2007, discussed
later, and the increasingly ambitious projects involving the
establishment of QKD networks seen in later years.

Geneva Elections
----------------

The 2007 Geneva elections saw the first commercial use of quantum
cryptography, where ID Quantique's (IDQ) Cerberis system was used to
secure the transmission of vote counts from the central ballot-counting
station to the government data center {%cite Messmer07%}. The version of
Cerberis used consisted of quantum key servers on both ends for key
generation, as well as a gigabit Ethernet link that carried the
encrypted transmissions {%cite Peck2007%}. The keys generated by the quantum
link were used to transmit a 256-bit AES key, which was then used to
provide secure point-to-point communication between the counting station
and the data center by encrypting all messages between the two centers.
As an additional security guarantee, both the AES key and the quantum
key were renewed upto 60 times an hour in both directions {%cite IDQ10%}.

Secure Communications based on Quantum Cryptography {%cite Peev2009%} {#secure-communications-based-on-quantum-cryptography}
---------------------------------------------------------------

Between 2004 and 2008, 41 European research and industrial organizations
worked together with the goal of producing a scalable system of QKD with
an average link length of about 25km, demonstrating the practical
utility of the technologies developed so far that are capable of
supporting secure quantum transmissions, under a project titled Secure
Communications based on Quantum Cryptography (SECOQC). The highlight of
this work consists in the systematic development of a design that allows
unrestricted scalability and interoperability of QKD technologies. The
development of an internal communications standard (titled the Q3P)
communications interface was instrumental, allowing QKD devices to
communicate seamlessly with higher network layers. The entire
infrastructure of the project is based around a single modular design
utilizing the trusted repeater network paradigm.

### Overview

Each node in the SECOQC architecture is built as the composition of two
modules, denoting a separation of concerns. A single node has many
functions; it must manage QKD keys generated over QKD links, ensure
encryption and decryption services for key transport across links,
communicate with other devices in a classical manner, manage keys
internally, and provide other cryptographic services (for key
distillation and privacy amplification, for instance). Given this, the
responsibilities of the node are split between the two modules, called
the *node module* and the *QKD device*. The node module performs the
network functions required, facilitating classical communications,
providing cryptography services, managing keys, etc.). It interfaces
with the QKD module to obtain the local QKD key that it then uses to
communicate securely with other nodes on the network. The QKD device has
the sole responsibility of communication over the quantum channel,
followed by key distillation and storing it in the classical node
module. This design allows for the use of arbitrary QKD devices, as long
as they adhere to a common interface detailed by the project, which
means that the network can be scaled up easily through the addition of a
variety of QKD devices. Another factor in the easy scaling of the
network is the fact that the number of keys that must be stored
increases linearly with the network size, as opposed to quadratically.
This is because, in the network graph, only neighbouring nodes need to
store link keys corresponding to the edge connecting them, as opposed to
every pair of nodes having to store keys in other network topologies.

The SECOQC network itself consists of six nodes connected by eight
quantum links, with deployment taking place in 2008 and a public
demonstration taking place during a QKD conference in October, 2008. The
demo involved a one-time pad encrypted telephone communication, a secure
video conference involving all deployed nodes, and a number of rerouting
experiments. In line with the focus of SECOQC's work, the various
transmissions that were part of the demo took place, strictly speaking,
over classical channels. The keys used to secure these channels were
derived using the QKD network, fulfilling the objective of the project
to create a robust, extensible quantum distribution network.

### Systems

Six different QKD systems were prototyped in Vienna as part of the
project:

1.  Three upgraded 'Cerberis' systems from the Swiss company id
    Quantique, which are plug and play pairs that can be used to set up
    a QKD link. This system employs phase coding to carry out the BB84
    protocol and the SARG {%cite Makoto2006%} protocol (a modification of BB84
    that is ideal for weak Poissonian sources). Multiple results testify
    to high reliability of id Quantique systems, which was used for
    ballot counting in the Swiss national elections of 2007, and have
    been used for the same purpose in each election in the Geneva
    canton. The performance of the upgraded system over a distance of
    25km equated to a secret key rate of 1kbit/s.

2.  One-way weak coherent pulse system with decoy states (Tosh) using a
    phase-encoding QKD system with two interferometers, stabilized by
    pulses that are time multiplexed with the quantum signals. The
    protocol implemented is a weak coherent pulse (WCP) decoy state +
    vacuum state BB84 variant, the details of which can be found in
    {%cite Hwang2002%}. The distinguishing feature is the use of decoy states
    in order to estimate expected signal pulse losses, followed by
    termination of the protocol if the estimated loss is much lower than
    the experimentally observed loss. This is a remediation technique
    for the photon-number-splitting attack against BB84, where an
    eavesdropper surreptitiously diverts some fraction of the
    transmitted photons. The key rate for a fiber length of 25km was
    found to be 5.7 kbit/s, almost six times higher than the required
    rate in the SECOQC specification. Furthermore, these rates are
    almost a hundredfold improvement over BB84 without decoy pulses
    {%cite Gobby2004%}.

3.  A coherent-one-way (COW) system that is an experimental realization
    of distributed phase reference protocols. The COW protocol is
    distantly related to the BB84 protocol, with the addition of a third
    basis (corresponding to time-of-arrival)) and using one of the
    original bases only to ensure coherence {%cite Lo2005%}. At a high level,
    Alice either sends pulses of weak coherent states or completely
    blocks the beam (corresponding to vacuum pulses). Bob then uses an
    interferometer and time-of-arrival measurements to distinguish
    between bit values and check the coherence of each pulse. The
    interferometer information provides indicates of eavesdropping.
    Further details may be found in {%cite Stucki2005%}.

4.  A polarization entanglement QKD system (Ent) that supports
    concurrent active stabilization of the optical elements for stable
    long-term automated operation. This system implements the BBM92
    {%cite Bennett1992%} protocol, and includes numerous active automated
    stabilization modules, allowing for completely autonomous startup
    and continued uninterrupted service. A reliable key rate of about 2
    kbit/s was observed for its operation during the SECOQC
    demonstration, and a more nuanced discussion of the system may be
    found in {%cite Treiber2009%}.

5.  A continuous variables (CV) system with Gaussian modulation, reverse
    reconciliation and homodyne detection of the coherent light pulses.
    The key information is stored in both quadratures of a coherent
    state of the electromagnetic field, which can then be measured using
    homodyne detection. The quadratures are simply the operators defined
    by $\hat{p} = \frac{1}{\sqrt{2}}(\hat{a}^\dagger + \hat{a})$ and
    $\hat{q} = \frac{1}{\sqrt{2}}(\hat{a}^\dagger - \hat{a})$, where
    $\hat{a}$ and $\hat{a}^\dagger$ are the annihilation and creation
    operators of the electromagnetic field. The process goes as follows;
    Alice generates coherent laser pulses that are split into a weak
    signal and a strong local oscillator (LO). The signal is then
    randomly modulated according to a centered Gaussian distribution in
    both quadratures. The LO and the signal are then time and
    polarization multiplexed and transmitted to Bob on the same physical
    optical fiber. At Bob's end, the two signals are combined and
    converted into an electric signal using a homodyne detector, where
    the term homodyne simply refers to the fact that the LO and the
    signal pulse are both derived from the same light source. The output
    signal is proportional to the quadrature of the signal, which
    depends on the phase difference between the LO and the signal. Bob
    randomly picks either no phase difference or a difference of $\pi/2$
    to select one of the two quadratures for measurement. Details of the
    protocol may be found in {%cite Andersen2010%}.

6.  A free space link, using the BB84 protocol with decoy states
    {%cite Hwang2002%} and polarization encoded laser pulses.

### Conclusion

The SECOQC network is a powerful testament to the progress made in the
practical implementation of QKD networks using the trusted repeater
paradigm. It serves as a landmark in paving the way for seamless
integration of QKD devices into higher level network layers through the
development of native protocols (Q3P, QKD-NL and QKD-TL) and by
exemplifying the performance, stability and robustness of a modular
architecture that separates QKD from classical networking functions. The
innovative core of the project can be boiled down to the concentration
of all QKD functions into a single node device, which makes it easy to
add links and grow the network when required, enhancing the scalability
properties of the network. Most importantly, the demonstration carried
out as part of the project shows that it is possible to perform every
day functions (telephony and video conferencing, for instance) in a
secure manner, building off of the inherent security of the QKD
paradigm.

Bibliography
=========
{% bibliography --cited %}
