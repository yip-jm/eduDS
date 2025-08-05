![](images/1c59b7f92cbab22dba5af70f0064b51d078c9b3b74985d8378f450cb15e8bc62.jpg)

![](images/ffdc982f0cd40141923444bb5b9db59bf9ce835756087ab44f9c2a979d84ffe8.jpg)

![](images/5ef4a7478525a51eaa708ca9610dc2e64e79211fd010363d4a4d6b02f8797c47.jpg)

All rights reserved. No part of this book may be reproduced in any form by any electronic or mechanical means (including photocopying, recording, or information storage and retrieval) without permission in writing from the publisher.

This book was set in $\mathrm { I A T } _ { \mathrm { E } } \mathrm { X }$ by the author. Printed and bound in the United States of America.

Library of Congress Cataloging-in-Publication Data

Names: Fokkink, Wan, 1965- author   
Title: Distributed algorithms $:$ an intuitive approach / Wan Fokkink   
Description: Third edition | Cambridge, MA $:$ The MIT Press, [2025] |   
Includes bibliographical references and index   
Identifiers: LCCN 2017031164 | ISBN 9780262037662 (hardcover $:$ alk. paper)   
Subjects: LCSH: Distributed algorithms–Textbooks   
Classification: LCC QA76.58 .F647 2018 | DDC 004/.36–dc23   
LC record available at https://lccn.loc.gov/2017031164

# Contents

Preface . . . . xi   
1 Introduction . . . . .   
2 Preliminaries 3   
2.1 Mathematical Notions . . 3   
2.2 Message Passing . 5   
2.3 Shared Memory . . . 10   
2.4 Exercises 13

# 3 Snapshots . 15

3.1 Chandy-Lamport Algorithm . 16   
3.2 Lai-Yang Algorithm 17   
3.3 Peterson-Kearns Checkpointing and Rollback Recovery Algorithm 18   
3.4 Exercises 21

# 4 Waves 23

4.1 Traversal Algorithms 23   
4.2 Tree Algorithm 27   
4.3 Echo Algorithm . . 28   
4.4 Exercises 29

# 5 Deadlock Detection . . . . . 31

5.1 Wait-for Graphs . . 31   
5.2 Bracha-Toueg Algorithm 32   
5.3 Exercises 39

# 6 Termination Detection . 41

6.1 Dijkstra-Scholten Algorithm 42   
6.2 Rana’s Algorithm 43   
6.3 Safra’s Algorithm 45   
6.4 Weight Throwing . . 46   
6.5 Fault-Tolerant Weight Throwing . 47   
6.6 Exercises 49

# 7 Garbage Collection . . . 53

7.1 Reference Counting . . 53   
7.2 Garbage Collection Implies Termination Detection 56   
7.3 Tracing . . 57   
7.4 Exercises 57

# 8 Routing . . . . 59

8.1 Chandy-Misra Algorithm . 59   
8.2 Merlin-Segall Algorithm 61   
8.3 Toueg’s Algorithm . . 64   
8.4 Frederickson’s Algorithm . 66   
8.5 Packet Switching . 70   
8.6 Routing on the Internet . . 72   
8.7 Exercises 73

# 9 Election . . . . 77

9.1 Election in Rings . . 77   
9.2 Tree Election Algorithm . . . 81   
9.3 Echo Algorithm with Extinction 82   
9.4 Minimum Spanning Trees 83   
9.5 Exercises 88

# 10 Anonymous Networks . . . 91

10.1 Impossibility of Election in Anonymous Rings . 91   
10.2 Probabilistic Algorithms . 92   
10.3 Itai-Rodeh Election Algorithm for Rings 93   
10.4 Echo Algorithm with Extinction for Anonymous Networks . 95   
10.5 Computing the Size of an Anonymous Ring Is Impossible 96   
10.6 Itai-Rodeh Ring Size Algorithm 97   
10.7 Election in IEEE 1394 99   
10.8 Exercises 100

# 11 Synchronous Networks 103

11.1 Awerbuch’s Synchronizer . 103   
11.2 Bounded Delay Networks with Local Clocks 106   
11.3 Election in Anonymous Rings with Bounded Expected Delay 108   
11.4 Exercises 110

# 12 Consensus with Crash Failures . . . .

12.1 Impossibility of 1-Crash Consensus 112   
12.2 Bracha-Toueg Crash Consensus Algorithm 113   
12.3 Failure Detectors . 115   
12.4 Consensus with a Weakly Accurate Failure Detector 116   
12.5 Chandra-Toueg Algorithm 116   
12.6 Consensus for Shared Memory 119   
12.7 Exercises 122

# 13 Consensus with Byzantine Failures . . . 125

13.1 Bracha-Toueg Byzantine Consensus Algorithm . 125   
13.2 Mahaney-Schneider Synchronizer . 129   
13.3 Lamport-Shostak-Pease Broadcast Algorithm . 131   
13.4 Lamport-Shostak-Pease Authentication Algorithm . 134   
13.5 Exercises 136

# 14 Mutual Exclusion . 139

14.1 Ricart-Agrawala Algorithm 140   
14.2 Raymond’s Algorithm 141   
14.3 Agrawal–El Abbadi Algorithm 144   
14.4 Peterson’s Algorithm 146   
14.5 Bakery Algorithm 149   
14.6 Fischer’s Algorithm 151   
14.7 Test-and-Test-and-Set Lock . 152   
14.8 Queue Locks 153   
14.9 Exercises 157

# 15 Barriers . . 161

15.1 Sense-Reversing Barrier 161   
15.2 Combining Tree Barrier 162   
15.3 Tournament Barrier . . 165   
15.4 Dissemination Barrier . 167   
15.5 Exercises 169

# 16 Distributed Transactions . . . 171

16.1 Serialization . 172   
16.2 Two- and Three-Phase Commit Protocols 176   
16.3 Transactional Memory 177   
16.4 Exercises 180

# 17 Self-Stabilization . . . 183

17.1 Dijkstra’s Token Ring for Mutual Exclusion 183   
17.2 Arora-Gouda Spanning Tree Algorithm 186   
17.3 Afek-Kutten-Yung Spanning Tree Algorithm 189   
17.4 Exercises 191

# 18 Dynamic Networks . . . . . . . 193

18.1 Chord Ring . . 193   
18.2 AODV Routing Protocol. . 197   
18.3 Vasudevan-Kurose-Towsley Election Algorithm 200   
18.4 Walter-Welch-Vaidya Mutual Exclusion Algorithm 201   
18.5 Cao-Singhal Checkpointing Algorithm . 203   
18.6 Exercises 206

# 19 Security . . . 209

19.1 Basic Techniques . . 210   
19.2 Kerberos Authentication Protocol . 213   
19.3 Diffie-Hellman Key Exchange Protocol 215   
19.4 Quantum Cryptography 216   
19.5 Merkle Signature Scheme . 220   
19.6 Blockchains . 226   
19.7 Exercises 230

# 20 Online Scheduling . . . 235

20.1 Jobs . . 235   
20.2 Schedulers . 236   
20.3 Resource Access Control . 241   
20.4 Exercises 243

# A Appendix: Pseudocode Descriptions . 245

A.1 Chandy-Lamport Snapshot Algorithm 246   
A.2 Lai-Yang Snapshot Algorithm 246   
A.3 Cidon’s Depth-First Search Algorithm 247   
A.4 Tree Algorithm 248   
A.5 Echo Algorithm . . 249   
A.6 Shavit-Francez Termination Detection Algorithm 250   
A.7 Rana’s Termination Detection Algorithm 251   
A.8 Safra’s Termination Detection Algorithm . 252   
A.9 Weight-Throwing Termination Detection Algorithm 253   
A.10 Chandy-Misra Routing Algorithm . 254   
A.11 Merlin-Segall Routing Algorithm 254   
A.12 Toueg’s Routing Algorithm 255   
A.13 Frederickson’s Breadth-First Search Algorithm . 257   
A.14 Dolev-Klawe-Rodeh Election Algorithm 259   
A.15 Gallager-Humblet-Spira Minimum Spanning Tree Algorithm 260   
A.16 IEEE 1394 Election Algorithm 263   
A.17 Awerbuch’s Synchronizer . 264   
A.18 Ricart-Agrawala Mutual Exclusion Algorithm 265   
A.19 Raymond’s Mutual Exclusion Algorithm 266   
A.20 Agrawal–El Abbadi Mutual Exclusion Algorithm 267   
A.21 MCS Queue Lock . 269   
A.22 CLH Queue Lock with Timeouts . 270   
A.23 Afek-Kutten-Yung Spanning Tree Algorithm 271

References . . . . . 275 ndex . . . 281

# Preface

This textbook is meant to be used in a course on distributed algorithms for senior-level undergraduate or graduate students in computer science or software engineering and as a quick reference for researchers in the field. On the one hand it focuses on fundamental and instructive algorithms and results in distributed computing, while on the other hand it aims to exhibit the versatility of distributed and parallel computer systems. The distributed algorithms treated in this book are largely “classics” that were selected mainly because they are instructive with regard to the algorithmic design of distributed systems or shed light on key issues in distributed computing and concurrent programming. The book also discusses topics that are the focus of exciting new developments, notably transactional memory, P2P networks, blockchains, and quantum cryptography.

There are two very different ways to structure a course on algorithms. One way is to discuss algorithms and their analysis in great detail. The advantage of this approach is that students may gain deep insight into the algorithms and at the same time acquire experience in mathematical reasoning regarding their correctness and performance. Another way is to discuss algorithms and their correctness in an informal manner, and let students get acquainted with an algorithm from different angles by means of examples and exercises, without a need to understand the intricacies of the corresponding model and its underlying assumptions. Mathematical argumentations, which can be a stumbling block for many students, are thus avoided. An additional advantage is that a large number of algorithms can be discussed within a relatively short time, providing students with many different views on, and solutions to, challenges in distributed computing. In 10 years of teaching about distributed algorithms, I have converged on the latter approach, most of all because the students in my lectures tend to have hands-on experience and practical interests with regard to distributed systems. As a result, the learning objective of my course has been algorithmic thought rather than proofs and logic.

This book provides a Cook’s tour of distributed algorithms. This phrase, meaning a rapid but extensive survey, refers to Thomas Cook, the visionary tour operator (and not the great explorer James Cook). Accordingly, this book is intended to be a travel guide through the world of distributed algorithms. A notable difference from other books in this area is that it does not emphasize correctness proofs. Algorithms are explained by means of brief, informal descriptions, illuminating examples, and exercises. The exercises have been carefully selected to make students well acquainted with the intricacies of distributed algorithms. Proof sketches, arguing the correctness of an algorithm or explaining the idea behind a fundamental result, are presented at a somewhat superficial level.

A thorough correctness proof, of course, is important in order to understand an algorithm in full detail. My research area is automated correctness proofs of distributed algorithms and communication protocols, and I have written two textbooks devoted to this topic. In the current textbook, however, intuition prevails. Readers who want to get a more detailed description of distributed algorithms in this book are recommended to consult the original papers, mentioned in the bibliographical notes at the end of each chapter. Moreover, pseudocode descriptions of a considerable number of algorithms are provided as an appendix.

Wan Fokkink Amsterdam, April 2025

# Introduction

In this age of the Internet, wide and local area networks, and multicore laptops, the importance of distributed and parallel computing is evident. The fact that you have opened this book suggests that no further explanation is needed to convince you of this point. The majority of modern-day system designers, system programmers, and ICT support staff must have a good understanding of distributed and concurrent programming. This, however, is easier said than done. The main aim of this book is to provide students with an algorithmic frame of mind, so that they can recognize and solve fundamental problems in distributed computing.

The two main communication paradigms for distributed systems are message passing, where the compute nodes in a physically distributed computer network send messages to each other via channels, and shared memory, in which different execution threads in a parallel computation can read and write to the same memory locations. Both communication paradigms are addressed in this book.

An algorithm is a step-by-step procedure to solve a particular problem on a computer. To become a skilled programmer, it is essential to have good insight into algorithms. Every computer science degree program offers one or more courses on basic algorithms, typically for searching and sorting, pattern recognition, and finding shortest paths in graphs. There, students learn how to detect such subproblems within their computer programs and solve them effectively. Moreover, they are trained to think algorithmically, to reason about the correctness of algorithms, and to perform a simple complexity analysis.

Distributed computing is very different from and considerably more complex than a uniprocessor setting, because executions at the different compute nodes in a distributed system are interleaved. When different nodes can concurrently perform events, these events can in principle happen in any order. For example, mutual exclusion becomes an issue: it may be necessary to avoid that two nodes concurrently decide to start writing on the same part of the memory. Distributed systems moreover are inherently nondeterministic: running an algorithm twice from the same initial configuration may yield different results. For instance, a so-called race condition can occur if two messages are traveling to the same node in the network, where different behavior may occur depending on which of the messages reaches its destination first. Furthermore, the number of reachable configurations of a distributed system tends to grow exponentially relative to its number of nodes.

Another important distinction between distributed and uniprocessor computing is the fact that the compute nodes in a distributed system in general do not have up-to-date knowledge of the global configuration of the system. They are aware of their own local state, but not always of the local states at other nodes or the messages in transit. For example, termination detection becomes an issue. It must be determined that all nodes in the system have become passive, and even if this is the case, there may still be a message in transit that will make the receiving node active again.

This book offers a wide range of basic algorithms for key challenges in distributed systems, such as termination detection, routing in a distributed network, coping with a crash of a compute node, or letting the nodes in a distributed network together build a snapshot of a global system configuration. It offers a bird’s-eye view on such pivotal issues from many different angles, as well as hand-waving correctness arguments and back-of-the-envelope complexity calculations.

# Preliminaries

We start with some general mathematical notions and notations in section 2.1. Sections 2.2 and 2.3 contain preliminaries that are specific to the two different communication frameworks for distributed systems: message passing and shared memory.

# 2.1 Mathematical Notions

This section presents some basic definitions regarding sets, complexity measures for algorithms, and special operations on numbers.

# Sets and Orders

As usual, $S _ { 1 } \cup S _ { 2 } , S _ { 1 } \cap S _ { 2 } , S _ { 1 } \setminus S _ { 2 }$ , and $S _ { 1 } \subseteq S _ { 2 }$ denote set union, intersection, difference, and inclusion, respectively; $s \in S$ means that $s$ is an element of the set $s$ . Equality is expressed by $s _ { 1 } = s _ { 2 }$ ; it holds if $s _ { 1 }$ and $s _ { 2 }$ denote the same element. The sets of natural and real numbers are denoted by $\mathbb { N }$ and $\mathbb { R }$ . The Booleans consist of the elements true and false. A set may be written as $\{ \cdots \} $ , where to the left of | the possible elements in the set are described, and to the right the property that they should satisfy is identified. For example, $\{ n \in \mathbb { N } \mid n > 5 \}$ represents the set of natural numbers greater than 5. The empty set is denoted by $\varnothing$ . For any finite set $s$ , $| S |$ denotes its number of elements.

A (strict) order on a set $s$ is a binary relation $<$ between elements of $s$ that is irreflexive, asymmetric, and transitive, meaning that for all $s , s ^ { \prime } , s ^ { \prime \prime } \in S \colon s < s$ does not hold; if $s < s ^ { \prime }$ , then $s ^ { \prime } < s$ does not hold; and if $s < s ^ { \prime }$ and $s ^ { \prime } < s ^ { \prime \prime }$ , then $s < s ^ { \prime \prime }$ , , <. An order is total if for any distinct $s , s ^ { \prime } \in S$ either $s < s ^ { \prime }$ or $s ^ { \prime } < s$ ; otherwise < < <the order is called partial. Given two sets $S _ { 1 }$ and $S _ { 2 }$ with orders $< _ { 1 }$ ,and $< _ { 2 }$ < <, respectively, the lexicographical order $<$ on pairs from $S _ { 1 } \times S _ { 2 }$ is defined by $\left( s _ { 1 } , s _ { 2 } \right) < \left( s _ { 1 } ^ { \prime } , s _ { 2 } ^ { \prime } \right)$ < if either $s _ { 1 } < _ { 1 } s _ { 1 } ^ { \prime }$ , or $s _ { 1 } = s _ { 1 } ^ { \prime }$ and $s _ { 2 } < _ { 2 } \ : s _ { 2 } ^ { \prime }$ . If $< _ { 1 }$ and $< _ { 2 }$ < , < , <are total orders, then so is the corresponding lexicographical order $<$ .

# Complexity Measures

Complexity measures state how resource consumption of an algorithm (in terms of messages, time, or space) grows in relation to input size. We are not interested in the precise utilization of resources on a given network, as this may depend, for instance, on the underlying hardware, but in how quickly resource consumption grows if the input size increases in a linear fashion. Different executions of an algorithm usually give rise to a different utilization of resources. We consider worst-case complexity, which provides an upper bound on the considered resource consumption for all executions, and average-case complexity, which gives the average resource consumption over all executions. For example, if an algorithm has a worst-case message complexity of $O ( n ^ { 2 } )$ , then for an input of size $n$ , the algorithm in the worst case takes in the order of $n ^ { 2 }$ messages, give or take a constant factor.

Let $f , g : \mathbb { N } \to \mathbb { R } _ { > 0 }$ , meaning that the functions $f$ and $g$ map natural numbers to positive real numbers. We write $f \in O ( g )$ if $f$ >is bounded from above by $g$ , multiplied by some positive constant:

$$
f \in O ( g ) { \mathrm { ~ i f , ~ f o r ~ s o m e ~ } } c \in \mathbb { R } _ { > 0 } , f ( n ) \leq c \cdot g ( n ) { \mathrm { ~ f o r ~ a l l ~ } } n \in \mathbb { N }
$$

Likewise, $f \in { \mathcal { Q } } ( g )$ means that $f$ is bounded by $g$ from below, multiplied by some positive constant:

$$
f \in \Omega ( g ) { \mathrm { ~ i f , ~ f o r ~ s o m e ~ } } c \in \mathbb { R } _ { > 0 } , f ( n ) \geq c \cdot g ( n ) { \mathrm { ~ f o r ~ a l l ~ } } n \in \mathbb { N } .
$$

Finally, $f \in \theta ( g )$ means that $f$ is bounded by $g$ from above as well as below:

$$
f \in \theta ( g ) { \mathrm { ~ i f ~ } } f \in O ( g ) { \mathrm { ~ a n d ~ } } f \in \Omega ( g ) .
$$

So if an algorithm has, say, a worst-case message complexity of $\textstyle \Theta ( n ^ { 2 } )$ , then this upper bound is sharp.

Example 2.1 Let $a , b \in \mathbb { R } _ { > 0 }$ .

– $n ^ { a } \in O ( n ^ { b } )$ if $a \leq b$ . – $n ^ { a } \in O ( b ^ { n } )$ if $b > 1$ . – $\log _ { a } n \in O ( n ^ { b } )$ > for all $^ { a , b }$

Divide-and-conquer algorithms, which recursively divide a problem into smaller subproblems until they are simple enough to be solved directly, typically have a logarithm in their time complexity. The reason is that dividing a problem of input size $2 ^ { k }$ into subproblems of size 1 takes $k$ steps, and $k = \log _ { 2 } 2 ^ { k }$ .

One can write $O ( \log n )$ instead of $O ( \log _ { a } n )$ . By definition, $\log _ { a } a ^ { n } = n$ , which implies $a ^ { \log _ { a } n } = n$ . So

$$
a ^ { \log _ { a } b \cdot \log _ { b } n } = b ^ { \log _ { b } n } = n .
$$

Therefore, $\log _ { a } b \cdot \log _ { b } n = \log _ { a } n$ . So $\log _ { b } n \in O ( \log _ { a } n )$ for all $a , b \in \mathbb { R } _ { > 0 }$ .

, >Resource consumption of an execution of a distributed algorithm can be measured in several ways:

Message complexity: the total number of messages exchanged.   
Bit complexity: the total number of bits exchanged.   
Time complexity: the amount of time required to complete the execution.   
Space complexity: the total amount of space needed for the processes.

In the context of the message-passing framework, we focus mostly on message complexity. Bit complexity is interesting only when messages can be very long. In the analysis of time complexity, we assume that internal computation steps at a process take no time and that a message is received at most one time unit after it is sent. In the context of the shared-memory framework, we focus on time and space complexity.

While determining a complexity measure, we will sometimes use the notations $\lfloor a \rfloor$ and $\lceil a \rceil$ with $a \in \mathbb { R } _ { > 0 }$ , meaning the largest integer $k$ such that $k \leq a$ and the smallest integer $\ell$ such that $\ell \geq a$ , respectively.

The integer domain modulo a positive natural number $n$ ℓ, denoted by $\mathbb { Z } / n \mathbb { Z }$ ℓ, is represented by the elements $\{ 0 , . . . , n - 1 \}$ . Each integer $k$ has a representative modulo $n$ /, denoted by $k$ mod $n$ , which is the unique $\ell \in$ $\{ 0 , . . . , n - 1 \}$ such that $k - \ell$ is divisible by $n$ . In other words, $k$ mod $n$ is the remainder if $k$ is divided by $n$ ℓ. This means that when counting upward modulo $n$ , integer values are wrapped around when $n$ is reached: $n$ mod $n$ is represented by 0, $( n + 1 )$ mod $n$ by 1, and so on. Addition and multiplication on integers carry over to modulo arithmetic in a straightforward fashion: $( j \bmod n ) + ( k \bmod n ) = ( j + k )$ mod $n$ and $\left( j { \bmod { n } } \right) \cdot \left( k { \bmod { n } } \right) =$ $\left( \boldsymbol { j } \cdot \boldsymbol { k } \right)$ mod $n$ .

# 2.2 Message Passing

In a message-passing framework, a distributed system consists of a finite network (or graph) of $N$ processes (or nodes), which are denoted by $p , q , r .$ . Each process in the network carries a unique ID. The processes in the , ,network are connected by channels (or edges), through which they can send messages to each other, which are denoted by m. A channel between processes $p$ and $q$ is denoted by $p q$ . There is at most one channel from one process to another, and a process does not have a channel to itself. Sometimes a process may want to communicate a message to itself, but clearly no channel is needed for this. We use $E$ and $D$ to denote the number of channels and the diameter of the network, respectively.

A process can record its own state and the messages it sends and receives; processes do not share memory or a global clock. Each process knows only its (direct) neighbors in the network. The topology of the network is assumed to be strongly connected, meaning that there is a path from each process to every other process.

Communication in the network is asynchronous, meaning that sending and receiving a message are distinct events at the sending and receiving process, respectively. The delay of a message in a channel is arbitrary but finite. We assume that communication protocols are being used to avoid having messages garbled, duplicated, or lost. Such a protocol defines a set of rules for how data is transmitted through the network. Channels need not be FIFO (first-in, first-out), which means that messages can overtake each other. To mimic a FIFO channel, a simple protocol suffices, which typically provides a sequence number to each message. (Special care is required if these numbers overflow, meaning that they go outside the available range of integers.) However, for the purposes of this book, it is important to study the fully asynchronous nature of distributed algorithms, which comes to light in a setting with non-FIFO channels. Moreover, most algorithms we will consider do not require FIFO channels, and enforcing them comes with a performance penalty.

In a directed network, messages can travel only in one direction through a unidirectional channel. In an undirected network, channels are bidirectional, meaning that messages can travel either way. If the network is directed, then a channel $p q$ is directed from $p$ to $q$ . Bidirectional channels are for instance required for distributed algorithms that use an acknowledgment scheme. Acyclic networks, in which there is no cycle of distinct channels, will always be undirected, since otherwise the network would not be strongly connected. A network topology is called complete if there is a bidirectional channel (or, equivalently, there are two unidirectional channels in both directions) between each pair of different processes.

A spanning tree of an undirected network is a connected, acyclic graph that consists of all the nodes and a subset of the edges in the network. The edges of the spanning tree are called tree edges, and all other edges are called frond edges. Often the edges in a spanning tree are given a direction to obtain a sink tree, in which all paths lead to the same node, called the root; each unidirectional edge leads from a child to its parent. A leaf is a node without children in the tree. A descendant of a process $p$ is either a child of $p$ or a descendant of a child of $p$ .

At some places, we will deviate from the assumptions mentioned so far and move to, for instance, synchronous communication in which the sending and receiving of the same message form one atomic step; unreliable processes or channels; FIFO channels; processes without a unique ID; or processes with a probabilistic specification instead of a deterministic one. Such deviations will be stated explicitly.

# Transition Systems

A distributed algorithm, which runs on a distributed system, provides (usually deterministic) specifications for the individual processes. The global state of a distributed algorithm, called a configuration, evolves by means of transitions. The overall behavior of distributed algorithms running on a distributed system is captured by a transition system, which consists of

a set $\mathcal { C }$ of configurations, a binary transition relation $ \mathbf { o n } \mathcal { C }$ , and a set ${ \mathcal { S } } \subseteq { \mathcal { C } }$ of initial configurations.

The underlying idea is that every run of a distributed algorithm starts in an initial configuration, and each of its transitions adheres to the transition relation. A configuration $\gamma$ is terminal if it has no outgoing transition: $\gamma  \delta$ for no $\delta \in \mathcal { C }$ γ. An execution of a distributed algorithm is a sequence $\gamma _ { 0 } \gamma _ { 1 } \gamma _ { 2 } \cdots$ of configurations that γ δ δis either infinite or ends in a terminal configuration $\gamma _ { k }$ , such that

• $\gamma _ { 0 } \in \mathcal { I }$ , and • $\gamma _ { i }  \gamma _ { i + 1 }$ for all $i \geq 0$ (and in the case of a finite execution, $i < k$ ).

A configuration $\delta$ is reachable if it is part of an execution: there is a $\gamma _ { 0 } \in \mathcal { I }$ and a sequence $\gamma _ { 0 } \gamma _ { 1 } \cdots \gamma _ { k }$ with $\gamma _ { i }  \gamma _ { i + 1 }$ for all $0 \leq i < k$ and $\gamma _ { k } = \delta$ .

# States and Events

The configuration of a distributed system consists of the local states of its processes and the messages in transit. A state of a process typically consists of the values of the local variables at this process. A transition between configurations of a distributed system is associated with an event (or, in the case of synchronous communication, two events) at one (or two) of its processes. A process can perform internal, send, and receive events. An internal event influences only the state at the process where the event is performed. Typical internal events are reading or writing to a local variable. Assignment of a new value to a variable is written as $\gets$ ; for example, $n \gets n + 1$ means that the value of variable $n$ , representing a natural number, is increased by 1. A send event, in principle, gives rise to a corresponding receive event of the same message at another process. It is assumed that two different events never happen at the same moment in real time (with the exception of synchronous communication).

A process is an initiator if its first event is an internal or send event; that is, an initiator can start performing events without input from another process. An algorithm is centralized if there is exactly one initiator. A decentralized algorithm can have multiple initiators.

# Assertions

An assertion is predicated on the configurations of an algorithm. That is, in each configuration, the assertion is either true or false. For example, $x > 1$ asserts that the variable $x$ is greater than one, which may hold in some but not all configurations.

An assertion is a safety property if it is supposed to be true in each reachable configuration of the algorithm. A safety property typically expresses that something bad will never happen. Informal examples of safety properties are:

You can always count on me. – Never will a deadlock occur. Each message reaches its destination within one second after it is sent.

Phrased differently, the first example states that it is never the case that you cannot count on me, and the third example states that never a message fails to reach its destination within one second.

In general, it is undecidable whether a given configuration is reachable. An assertion $P$ is an invariant if • $P ( \gamma )$ for all $\gamma \in \mathcal { I }$ , and • if $\gamma  \delta$ and $P ( \gamma )$ , then $P ( \delta )$ .

In other words, an invariant is true in all initial configurations and is preserved by all transitions. Clearly, each invariant is a safety property. Note that checking whether an assertion is an invariant does not involve reachability, so such a proof can focus on local transitions. The price to pay is that an invariant must also hold for unreachable configurations, although in principle we are only interested in the reachable ones.

An assertion is a liveness property if it expresses that each execution contains a configuration in which the assertion holds. A liveness property typically expresses that something good will eventually happen but provides no time bound on how long this may take. Informal examples of liveness properties are:

What goes up, must come down.   
The program always eventually terminates.   
Each message eventually reaches its destination.

The third informal safety and liveness properties show that the difference between these notions can be subtle. One could say that the safety property regards the foreseeable future and the liveness property the unforeseeable future.

A liveness property sometimes holds only with respect to the fair executions of an algorithm. For example, consider a simple algorithm that consists of flipping a coin until the result is tails. Since there is an infinite execution in which the outcome of every coin flip is heads, the liveness property that eventually the outcome will be tails does not hold. However, if the coin is fair, this infinite execution has zero chance of happening; infinitely often we flip the coin with the possible outcome tails, but never is the outcome tails. We say that an execution is fair if every event that can happen in infinitely many configurations in the execution is performed infinitely often during the execution. The infinite execution in which the outcome of every coin flip is heads is not fair. Note that any finite execution is trivially fair.

# Causal Order

In each configuration of an asynchronous distributed system, events that can occur at different processes are always independent, meaning that they can happen in any order. The causal order $\prec$ is a binary relation on events in a given execution such that $a \prec b$ if and only if $a$ must happen before $^ b$ . That is, the events in the execution cannot be reordered in such a way that $a$ happens after $^ b$ . The causal order for an execution is the smallest relation such that

• if $a$ and $^ b$ are events at the same process and $a$ occurs before $^ b$ , then $a \prec b$ , • if $a$ is a send and $^ b$ the corresponding receive event, then $a \prec b$ , and • if $a \prec b$ and $b \prec c$ , then $a \prec c$ .

The first two clauses define direct causal order relations between events, and the third clause takes the transitive closure. The causal order relation is irreflexive: $a \prec a$ never holds. We write $a \preceq b$ if either $a \prec b$ or $a = b$ . Distinct events in an execution that are not causally related are called concurrent. An important challenge in the design of distributed systems is to cope with concurrency (for example, to avoid race conditions).

A permutation of concurrent events in an execution does not affect the result of the execution. These permutations together form a computation. All executions of a computation start in the same configuration, and if they are finite, they all end in the same terminal configuration. In general, we will consider computations rather than executions.

Example 2.2 Consider an execution abc. If $a \prec b$ is the only causal relationship, then the executions abc, acb, and cab form one computation.

# Logical Clocks

A common physical clock, which approximates the global real time, is in general difficult to maintain by the separate processes in a distributed system. For many applications, however, we are not interested in the precise moments in time at which events occur but only in the ordering of these occurrences in time. A logical clock $C$ maps occurrences of events in a computation to a partially ordered set such that

$$
a \prec b \Rightarrow c ( a ) < C ( b ) .
$$

Lamport’s clock $L C$ assigns to each event $a$ the length $k$ of a longest causality chain $a _ { 1 } \prec \dots \prec a _ { k } = a$ in the computation. Clearly, $a \prec b$ implies $L C ( a ) < L C ( b )$ , because $a _ { 1 } \prec \dots \prec a _ { k } \prec b$ . So Lamport’s clock is a <logical clock. The clock values that Lamport’s clock assigns to events can be computed at runtime, so that these values can be employed during the execution. Consider an event $a$ , and let $k$ be the clock value of the previous event at the same process $k = 0$ if there is no such previous event). The value of $L C ( a )$ is determined at runtime as follows:

• If $a$ is an internal or send event, then $L C ( a ) = k + 1$ .   
• If $a$ is a receive event and $^ b$ the send event corresponding to $a$ , then $L C ( a ) = \operatorname* { m a x } \{ k , L C ( b ) \} + 1$ .

To perform the latter case, each message must include the clock value of its send event.

Example 2.3 Consider the following sequences of events at processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ .

$$
\begin{array} { r } { \begin{array} { r c l } { p _ { 0 } : } & { a } & { s _ { 1 } ~ r _ { 3 } ~ b } \\ { p _ { 1 } : } & { c } & { r _ { 2 } ~ s _ { 3 } } \\ { p _ { 2 } : } & { r _ { 1 } ~ d } & { s _ { 2 } ~ e } \end{array} } \end{array}
$$

Here $s _ { i }$ and $r _ { i }$ are corresponding send and receive events for $i = 1 , 2 , 3$ , while $a , b , c , d , e$ are internal events.   
Lamport’s clock provides these events with the following values.

$$
\begin{array} { l l l l l } { { p _ { 0 } : } } & { { 1 } } & { { 2 } } & { { 8 } } & { { 9 } } \\ { { p _ { 1 } : } } & { { 1 } } & { { 6 } } & { { 7 } } & { { } } \\ { { p _ { 2 } : } } & { { 3 } } & { { 4 } } & { { 5 } } & { { 6 } } \end{array}
$$

Since the values of Lamport’s clock are in the totally ordered set of natural numbers, there is an ordering relation between the clock values of each pair of events, even if they are concurrent. Sometimes it is convenient to use a logical clock for which this is not the case. The vector clock VC maps each event in a computation to a unique value such that

$$
a \prec b \Leftrightarrow V C ( a ) < V C ( b ) .
$$

Let the network consist of processes $p _ { 0 } , . . . , p _ { N - 1 }$ . The vector clock assigns to events in a computation values in $\mathbb { N } ^ { N }$ , . . . ,, whereby this set is provided with a partial order defined by

$$
\begin{array} { r } { ( k _ { 0 } , \ldots , k _ { N - 1 } ) \leq ( \ell _ { 0 } , \ldots , \ell _ { N - 1 } ) \Leftrightarrow k _ { i } \leq \ell _ { i } \mathrm { f o r } \mathrm { a l l } i = 0 , \ldots , N - 1 . } \end{array}
$$

We write $( k _ { 0 } , \ldots , k _ { N - 1 } ) < ( \ell _ { 0 } , \ldots , \ell _ { N - 1 } )$ if, moreover, these sequences are unequal to each other. (We note that , . . . , < ℓ , . . . , ℓin contrast to this partial order, the lexicographical order on $\mathbb { N } ^ { N }$ is total.)

The vector clock is defined as $V C ( a ) = \left( k _ { 0 } , \ldots , k _ { N - 1 } \right)$ , where each $k _ { i }$ for $i = 0 , . . . , N - 1$ is the length of a longest causality chain $a _ { 1 } ^ { i } \prec \dots \prec a _ { k _ { i } } ^ { i }$ , . . . ,of events at process $p _ { i }$ with $a _ { k _ { i } } ^ { i } \preceq a$ , . . . ,. On the one hand, $a \prec b$ implies $V C ( a ) < V C ( b ) .$ . This follows from the fact that $c \preceq a$ implies $c \prec b$ for each event $c$ . And at the process where $^ b$ <occurs, there is a longer causality chain for $^ b$ than for $a$ . Conversely, $V C ( a ) < V C ( b )$ implies $a \prec b$ . Consider the longest causality chain $a _ { 1 } ^ { i } \prec \dots \prec a _ { k } ^ { i } = a$ of events at the process $p _ { i }$ <where $a$ occurs. Then $V C ( a ) < V C ( b )$ implies that the ith coefficient of $V C ( b )$ is at least $k$ , and so $a \preceq b$ . Since clearly $a$ and $^ b$ <must be distinct events, $a \prec b$ . The vector clock can also be computed at runtime (see exercise 2.10).

Example 2.4 Consider the sequences of events at processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ from example 2.3. The vector clock provides these events with the following values.

$$
\begin{array} { r l } { p _ { 0 } : } & { { } \left( 1 \mathrm { ~ 0 ~ 0 } \right) } \\ { p _ { 1 } : } & { { } \left( 0 \mathrm { ~ 1 ~ 0 } \right) } \\ { p _ { 2 } : } & { { } \left( 2 \mathrm { ~ 0 ~ 1 } \right) } \end{array}
$$

# Basic and Control Algorithms

Several chapters will discuss distributed algorithms to provide some service or detect a certain property during the execution of another distributed algorithm. For instance, chapter 3 shows how processes can take a snapshot of a configuration in the ongoing computation, chapter 6 treats how processes can detect termination, and chapter 7 discusses garbage collection to reclaim memory occupied by inaccessible objects. Then the underlying distributed algorithm for which we are taking a snapshot, detecting termination, or collecting garbage is called the basic algorithm, while the distributed algorithm put on top for executing this specific task is called the control algorithm. We refer to a message of the basic or control algorithm as a basic message or control message, respectively.

# 2.3 Shared Memory

An alternative communication paradigm to message passing is shared memory, in which processes communicate with each other via shared variables in main memory. On the one hand there is a strong relation between the shared memory and message passing paradigms. Notably, in section 12.6 it will be shown that shared memory can be emulated by means of message passing, even if processes may crash. On the other hand they are fundamentally different, both in their concepts and in the design of distributed algorithms based on these two paradigms. A significant part of the second half of this book will be dedicated to shared memory.

In a shared-memory framework, a number of (hardware) processors communicate with main memory, and with the other processors, over a bus. The processes (or threads) are sequential programs that can run on a processor; at any time, at most one process is running on each processor. Processes communicate with each other, asynchronously, via shared variables in main memory, called registers (or fields). We distinguish single-reader registers, which are fields that can be read by only one process, and multi-reader registers, which can be read by all processes. Likewise, we distinguish single-writer and multi-writer registers.

Processors and main memory are snooping, meaning that they are listening for messages that are broadcast over the bus. A cache is a relatively small memory unit, local to a processor, that stores copies of data from main memory that may be frequently used. Access to main memory is slow compared to cache access. Changes to data values are therefore accumulated in the cache and written back to main memory when needed to make space in the cache, when another process wants the value, or at some memory barrier which enforces that writes are flushed to main memory. A cache consists of data blocks of fixed size called cache lines; copying data from and to main memory is performed at the level of cache lines. When a process takes a cache miss, meaning that it cannot find some data in its cache, the required data is fetched from main memory or provided by another processor.

![](images/544b53d083b078fe9cb49b7c2912015d9c00860aaf2dffeadf7f2e309e9b4c70.jpg)

In the presence of caches, synchronization primitives are typically needed to avoid in certain cases that processes read stale values from their cache, enforcing that they fetch fresh values from main memory instead. Notably, one can impose memory barriers or declare that for certain variables the reads and writes are always with regard to main memory (for example, in Java, such variables are declared volatile).

A cache coherence protocol maintains the consistency of the data in the local caches. If a process writes a value in a cache line, the cache coherence protocol makes sure that this same cache line in other caches is invalidated, so that the values in these lines become obsolete. For example, the MSI protocol identifies three possible states for a cache line:

• Modified: The line has been written to in the cache and must eventually be stored in main memory.   
• Shared: The line has not been written to in any cache and can be read.   
• Invalid: The line must be refreshed before it can be read.

When a process writes to a nonmodified cache line, this line becomes modified in the corresponding cache and is invalidated in all other caches. If a process reads a cache line that is modified in some other cache, then in both caches this line becomes shared. When a modified cache line becomes shared or invalid, it is flushed to main memory. Note that if a cache line is modified in some cache, then it can only occur as invalid in other caches.

An event at a process typically consists of one atomic read or write to a register. Read-modify-write operations, however, read a memory location and write a new value into it in one atomic step; this new value may be computed on the basis of the value returned by the read, without interruption by an event of another process. Atomicity is achieved through keeping a hardware lock on the bus from the moment the value is read until the moment the new value is written. Typical examples of read-modify-write operations are:

test-and-set, which writes true in a Boolean register and returns the previous value of the register. get-and-increment, which increases the value of an integer register by 1 and returns the previous value of the register. get-and-set(new), which writes the value new in a register and returns the previous value of the register. compare-and-s $\gimel t ( o l d , n e w )$ , which checks whether the value of the register equals old and, if so, over,writes it with the value new. A Boolean value is returned to signal whether the new value was actually written.

Read-modify-write operations tend to impose a memory barrier.

To avoid simultaneous use of a resource, such as a block of memory, mutual exclusion is of the essence in a shared-memory framework. A common way to achieve this is by means of software locks; to become privileged, one must obtain the lock, and at any time at most one process can hold the lock. The mutual exclusion algorithms for shared memory presented in chapter 14 are all based on this principle. In a setting with locks, we distinguish between two kinds of progress properties for mutual exclusion algorithms. Here it is assumed that no process holds a lock forever; in particular, that processes do not crash. Livelock-freeness means that some process trying to get a lock always eventually succeeds. Starvation-freeness means that every process trying to get a lock eventually succeeds. In particular, consider an algorithm in which some process infinitely often wants to obtain and release a certain lock. If in some execution this process obtains the lock only finitely often, then the algorithm is not starvation-free.

A disadvantage of locks is that they create a bottleneck, since many processes may concurrently be waiting to obtain a lock. Moreover, if a process holding a lock crashes, this may bring the execution of the entire system to a standstill. One can aim for stronger, nonblocking progress properties, where locks are disallowed. An algorithm is lock-free if, as long as it has not terminated, it is guaranteed that some process progresses (but it is allowed that some active, noncrashed process performs no events); it is wait-free if all active, noncrashed processes always progress. For example, consider an algorithm in which some process infinitely often performs the event $a$ . If in some execution this process does not crash and performs $a$ only finitely often, then the algorithm is not wait-free. Note that if a process crashes while holding a lock, then the lock-freeness (and therefore wait-freeness) property may be violated if the other processes wait in vain to get this lock. Therefore, this property precludes the use of locks.

A software crash is always a consequence of a hardware instruction; for example, a program counter may be set to an incorrect address. This means that processes do not crash during a read-modify-write operation. Therefore, in the absence of a hardware crash, the lock on the bus is always eventually released.

Locks and read-modify-write operations are usually furnished with automatic synchronization primitives: when a process acquires a lock or performs a read-modify-write operation, it invalidates its cache to ensure that fields are reread from main memory, and when it releases the lock, modified fields in its cache are written back to main memory.

Registers on which reads and writes are always distinct atomic events will be called atomic, to distinguish them from registers on which read-modify-write operations can be performed.

In practice, many processors allow out-of-order execution of read and write operations to increase performance. This means a processor may execute such operations in an order governed by the availability of input data to avoid delays, instead of the order declared by the program. In case of a multi-threaded program this can give rise to undesired behavior. If a programmer wants to disallow out-of-order execution with regard to certain read and write operations, this must be specified explicitly by placing memory barriers; operations before a memory barrier cannot be reordered behind operations after this memory barrier. In the algorithms for shared memory described in this book, we will take the liberty of disregarding out-of-order execution.

# Bibliographical notes

Lamport’s clock originates from [68].1 The vector clock was proposed independently in [41] and [79].

# 2.4 Exercises

Exercise 2.1 For each of the following functions $f$ and $g$ , say whether $f \in O ( g )$ and/or $g \in O ( f )$ .

(a) $f ( n ) = 5 n ^ { 2 } + 3 n + 7$ and $g ( n ) = n ^ { 3 }$ .   
(b) $\begin{array} { r } { f ( n ) = \sum _ { i = 1 } ^ { n } i } \end{array}$ and $g ( n ) = n ^ { 2 }$ .   
(c) $f ( n ) = n ^ { n }$ and $g ( n ) = n !$ .   
(d) $f ( n ) = n { \cdot } \log _ { 2 } n$ and $g ( n ) = n \cdot { \sqrt { \frac { n } { 2 } } }$ .   
(e) $f ( n ) = n + n { \cdot } \log _ { 2 } n$ and $g ( n ) = n { \cdot } { \sqrt { n } }$ .

Exercise 2.2 What is more general?

(a) An algorithm for directed or undirected networks.   
(b) A control algorithm for centralized or decentralized basic algorithms.

Exercise 2.3 Given a network with directed non-FIFO channels (in which messages are never lost or garbled). Explain how FIFO treatment of messages can be achieved by the processes in the network.

Exercise 2.4 [117] Give a transition system $s$ and an assertion $P$ such that $P$ is a safety property but not an invariant of $s$ .

Exercise 2.5 Define the union of $S _ { 1 } = ( \mathcal { C } ,  _ { 1 } , \mathcal { S } )$ and $S _ { 2 } = ( \mathcal { C } ,  _ { 2 } , \mathcal { S } )$ as $S = ( \mathcal { C } , \to _ { 1 } \cup \to _ { 2 } , \mathcal { I } )$

(a) [117] Prove that if $P$ is an invariant of $S _ { 1 }$ and $S _ { 2 }$ , then $P$ is an invariant of $s$ (b) Give an example where $P$ is a safety property of $S _ { 1 }$ and $S _ { 2 }$ but not of $s$ .

Exercise 2.6 Consider an execution abcd. Let $a \prec c$ and $b \prec d$ be the only causal relationships. Which executions are in the same computation as abcd?

Exercise 2.7 Consider the following sequences of events at processes $p _ { 0 } , p _ { 1 } , p _ { 2 }$ , and $p _ { 3 }$

$$
\begin{array} { l } { { p _ { 0 } : \begin{array} { l l l l } { { p _ { 1 } } } & { { s _ { 1 } } } & { { s _ { 2 } } } & { { r _ { 5 } } } \\ { { p _ { 1 } : } } & { { r _ { 2 } } } & { { s _ { 5 } } } \end{array} } } \\ { { p _ { 2 } : \begin{array} { l l l l } { { p _ { 1 } } } & { { a } } & { { s _ { 4 } } } & { { r _ { 3 } } } & { { r _ { 6 } } } \\ { { p _ { 3 } : } } & { { s _ { 3 } } } & { { r _ { 4 } } } & { { b } } & { { s _ { 6 } } } \end{array} } } \end{array}
$$

Here $s _ { i }$ and $r _ { i }$ are corresponding send and receive events for all $i$ , while $a$ and $^ b$ are internal events. Use Lamport’s logical clock to assign clock values to these events. Do the same for the vector clock.

Exercise 2.8 Give an example where $L C ( a ) < L C ( b )$ , while $a$ and $^ b$ are concurrent events.

# Exercise 2.9 [117]

(a) Define the causal order for events of a system execution with synchronous communication. (b) Adapt Lamport’s logical clock for such systems, and give a distributed algorithm for computing the clock at runtime.

Exercise 2.10 Give an algorithm to compute the vector clock at runtime.

Exercise 2.11 Propose two adaptations of the MSI cache coherence protocol, in both cases by introducing an additional state for cache lines.

(a) Reduce bus traffic when a process reads a certain variable and then writes to it in its cache, while the corresponding cache line occurs only as invalid in other caches.   
(b) Reduce the number of flushes to main memory in the case of a continuous stream of reads and writes by different processes to a certain variable.

Exercise 2.12 For each of the following approaches for handing a free lock to a waiting process, say whethe it is starvation-free.

(a) Randomly hand the lock to one of the waiting processes.   
(b) Processes that wait for the lock are placed in a FIFO (first-in, first-out) queue. Hand the lock to the process at the head of this queue (and remove it from the queue).   
(c) Hand the lock to the waiting process with the highest ID.

# Snapshots

A snapshot of an execution of a distributed algorithm is a configuration of this execution that consists of the local states of the processes and the messages in transit. Snapshots are useful to try to determine offline properties that will remain true as soon as they have become true, such as deadlock (see chapter 5), termination (see chapter 6), or being garbage (see chapter 7). Moreover, snapshots can be used for checkpointing to restart after a failure (see section 3.3) or for debugging.

In a centralized environment, the execution of a program can usually be interrupted at any moment to query the program state, consisting of the values of the program variables. In a distributed setting, this is not the case. Suppose a process that is involved in the execution of a distributed algorithm wants to take a snapshot of a configuration of the ongoing execution. Then it should ask all processes to take a snapshot of their states. Processes, moreover, need to compute channel states of messages that were in transit at the moment of the snapshot. The challenge is to develop a snapshot algorithm that works at runtime; that is, without freezing the execution of the basic algorithm for which the snapshot is taken. Messages of the basic and the snapshot algorithm are called basic and control messages, respectively.

A complication is that the processes take local snapshots and compute channel states at different moments in time. Therefore, care is needed to ensure that a snapshot represents a configuration of the ongoing execution. Actually, generally one cannot be certain that this configuration occurred during execution, because the order in which concurrent events took place may be unknown. However, a configuration of an execution in the same computation as the ongoing execution is good enough. Such a snapshot is called consistent. As said, one should be careful not to take an inconsistent snapshot. For instance, a process $p$ could take a local snapshot and then send a basic message $m$ to a process $q$ , where $q$ could either take a local snapshot after the receipt of $m$ or include $m$ in the state of the channel $p q$ . This would turn $m$ into an orphan message that was, with regard to the snapshot, not sent according to $p$ but was received or in transit according to $q$ . Likewise, $p$ could send a basic message $m$ before taking its local snapshot, while $q$ could receive $m$ after taking its local snapshot and exclude $m$ from the channel state of $p q$ . This would turn $m$ into a lost message that was, with regard to the snapshot, sent according to $p$ but neither received nor in transit according to $q$ . Such inconsistent snapshots clearly should be avoided.

An event is called presnapshot if it occurs at a process before the local snapshot at this process is taken; otherwise it is called postsnapshot. A snapshot is consistent if

(1) no postsnapshot event is causally before a presnapshot event, and   
(2) a basic message is included in a channel state if and only if the corresponding send event is presnapshot while the corresponding receive event is postsnapshot.

The first property guarantees that all presnapshot events can be placed before the postsnapshot events in the actual execution by means of permutations that do not violate the causal order. The second property guarantees that there are no lost messages. And the two properties together guarantee that there are no orphan messages. This implies that the snapshot determines a configuration of an execution that is in the same computation as the actual execution.

We discuss two decentralized snapshot algorithms for directed networks; the first one requires channels to be FIFO. In these algorithms, the individual processes record fragments of the snapshot; the subsequent phase of collecting these fragments to obtain a composite view is omitted here.

# 3.1 Chandy-Lamport Algorithm

The Chandy-Lamport snapshot algorithm requires that channels be FIFO. Any process that is designated to be an initiator can decide to take a local snapshot of its state. It then sends a control message ⟨marker⟩ through all its outgoing channels to let its neighbors take a snapshot also. When a process that has not yet taken a snapshot receives a $\langle \mathrm { \bf m a r k e r } \rangle$ message, it takes a local snapshot of its state and sends a $\langle \mathbf { m a r k e r } \rangle$ message through all its outgoing channels. A process $q$ computes as channel state for an incoming channel $p q$ the (basic) messages that it receives via $p q$ after taking its local snapshot and before receiving a ⟨marker⟩ message from $p$ . The Chandy-Lamport algorithm terminates at a process when it has received a $\langle \mathbf { m a r k e r } \rangle$ message through all its incoming channels.

Example 3.1 We consider one possible computation of the Chandy-Lamport algorithm on the directed network pictured here. First, process $p$ takes a local snapshot of its state (dark gray) and sends $\langle \mathrm { \bf m a r k e r } \rangle$ into its two outgoing channels $p q$ and $p r$ . Next, $p$ sends a basic message $m _ { 1 }$ to process $q$ and changes its state (to striped). Concurrently, process $r$ receives $\langle \mathrm { \bf m a r k e r } \rangle$ from $p$ and as a result sends $\langle \mathrm { \bf m a r k e r } \rangle$ into its outgoing channel $r p$ , takes a local snapshot of its state (white), and computes the channel state $\varnothing$ for its incoming channel $p r$ .

![](images/6aa471e60baef8cc952d50af023b62cecb79e3bc72098f2a77ea96b20ad7a2a6.jpg)

Next, $p$ receives $\langle \mathrm { \bf m a r k e r } \rangle$ from $r$ and as a result computes the channel state $\varnothing$ for its incoming channel $r p$ . Concurrently, $q$ sends a basic message $m _ { 2 }$ to $r$ . Next, $q$ receives $\langle \mathbf { m a r k e r } \rangle$ from $p$ and as a result sends $\langle \mathbf { m a r k e r } \rangle$ into its outgoing channel $q r$ , takes a local snapshot of its state (light gray), and computes the channel state $\varnothing$ for its incoming channel pq. Finally, $r$ receives $m _ { 2 }$ and next ⟨marker⟩ from $q$ , and as a result it computes the channel state $\{ m _ { 2 } \}$ for its incoming channel qr.

![](images/73dec4541159ff54df1cad92c875a2f4ecef034dfa532fb5b06bc748668e69a8.jpg)

We note that the computed snapshot (states: dark gray, light gray, white; channels: $\varnothing , \varnothing , \varnothing , \{ m _ { 2 } \} )$ is not a configuration of the actual execution. However, both the sending of $m _ { 1 }$ and the internal event at $p$ that changes its state from light gray to striped are not causally before the sending of $m _ { 2 }$ . Therefore, the snapshot determines a configuration of an execution in the same computation as the actual execution.

We argue that properties (1) and (2) of a consistent snapshot are satisfied. First, if an event $a$ is causally before a presnapshot event $^ b$ , then $a$ is also presnapshot. If $a$ and $^ b$ occur at the same process, then this is trivially the case. The interesting case is where $a$ is a send and $^ b$ is the corresponding receive event. Suppose $a$ occurs at process $p$ and $^ b$ occurs at process $q$ . Since $^ b$ is presnapshot, $q$ has not yet received a $\langle \mathbf { m a r k e r } \rangle$ message at the time it performs $^ b$ . Since channels are FIFO, this implies that $p$ has not yet sent a ⟨marker⟩ message to $q$ at the time it performs $a$ . Hence, $a$ is presnapshot. Second, a basic message is included in the channel state of $p q$ if and only if its send event at $p$ is presnapshot and its receive event at $q$ is postsnapshot. This is because $q$ includes in the channel state of $p q$ those basic messages $m$ that are received after $q$ ’s local snapshot and before the $\langle \mathrm { \bf m a r k e r } \rangle$ message through pq. Since channels are FIFO, the latter means exactly that the sending of $m$ is presnapshot at $p$ .

The Chandy-Lamport algorithm requires $E$ control messages, one per (unidirectional) channel, and it takes at most $O ( D )$ time units to complete a snapshot (under the assumption that each message travels for at most one time unit, see Section 2.1).

# 3.2 Lai-Yang Algorithm

The Lai-Yang snapshot algorithm does not require channels to be FIFO. Any initiator can decide to take a local snapshot of its state. As long as a process has not taken a local snapshot, it appends false to each outgoing basic message; after its local snapshot, it appends true to these messages. When a process that has not yet taken a local snapshot receives a message with the tag true, it takes a local snapshot of its state before receiving this message. A process $q$ computes as channel state of an incoming channel $p q$ the basic messages with the tag false that it receives through this channel after having taken its local snapshot.

There are two complications. First, if after its local snapshot an initiator would happen not to send any basic messages, other processes might never take a local snapshot. Second, how does a process know when it can stop waiting for basic messages with the tag false and compute the state of an incoming channel? Both issues are resolved by a special control message, which each process $p$ sends into all its outgoing channels $p q$ after having taken its local snapshot. This control message informs $q$ how many basic messages with the tag false $p$ has sent into the channel $p q$ . If $q$ has not yet taken a local snapshot, it takes one upon receiving this control message.

Example 3.2 Consider a network of two processes $p$ and $q$ , with non-FIFO channels $p q$ and $q p$ . We apply the Lai-Yang algorithm to take a snapshot.

Let $p$ send basic messages $\langle m _ { 1 } , f a l s e \rangle$ and $\left. m _ { 2 } , f a l s e \right.$ to $q$ . Then it takes a local snapshot of its state and sends a control message to $q$ ,, reporting that $p$ ,sent two basic messages with the tag false to $q$ . Next, $p$ sends basic messages $\langle m _ { 3 } , t r u e \rangle$ and $\langle m _ { 4 } , t r u e \rangle$ to $q$ . Let $\langle m _ { 3 } , t r u e \rangle$ arrive at $q$ first. Then $q$ takes a local snapshot of , ,its state and sends a control message to $p$ ,, reporting that $q$ did not send any basic message with the tag false to $p$ . Next, $q$ waits until the control message from $p$ , $\langle m _ { 1 } , f a l s e \rangle$ , and $\left. m _ { 2 } , f a l s e \right.$ have arrived and concludes that the channel state of $p q$ consists of $m _ { 1 }$ and $m _ { 2 }$ , ,. Thanks to the tag true, $q$ recognizes that $m _ { 3 }$ and $m _ { 4 }$ are not part of the channel state. When $p$ receives $q$ ’s control message, it concludes that the channel state of $q p$ is empty.

Similar to the Chandy-Lamport algorithm, we can argue that if an event $a$ is causally before a presnapshot event $^ b$ , then $a$ is also presnapshot. Again, the interesting case is where $a$ is a send and $^ b$ is the corresponding receive event. The fact that $^ b$ is presnapshot implies that the message sent by $a$ carries the tag false. Hence, $a$ is presnapshot. Furthermore, a basic message is included in the channel state of $p q$ if and only if its receive event at $q$ is postsnapshot and it carries the tag false, meaning that its send event at $p$ is presnapshot.

The Lai-Yang algorithm also requires $E$ control messages and takes at most $O ( D )$ time units to complete a snapshot.

# 3.3 Peterson-Kearns Checkpointing and Rollback Recovery Algorithm

Checkpointing and rollback recovery aim at coping with crash failures of processes in a network, meaning that they stop executing unexpectedly; this topic will be studied in depth in chapter 12. They decrease the impact of a crash, by avoiding that the interrupted execution must be restarted from an initial configuration. Instead it can be relaunched from an intermediate configuration of the execution that was stored in memory. This is particularly important for long-running applications.

It is still presumed that channels always function properly. Here we suppose that when a process crashes, another process will eventually continue its execution. It is assumed that each process owns a failure detector that eventually picks up on every crash failure. If an upper bound on network latency, meaning the time between when a message is sent and when it is received, is known, and each process sends a heartbeat message at regular time intervals, then a failure detector can be implemented using a timeout mechanism. Section 12.3 provides an in-depth treatment of such devices. It is, moreover, assumed that each process $p$ has stable storage at its disposal, meaning that this part of $p$ ’s local memory is preserved in a consistent state and remains accessible to the other processes even after $p$ has crashed. Without such special precautions, inconsistent memory could remain if $p$ crashes while performing a write operation. Stable storage can be implemented using two disks, where updates in memory on the first disk are faithfully copied to the second disk. If a crash happens during such a copying procedure, one can then return to the data on the first disk.

Each process periodically establishes a checkpoint by saving its state in stable storage. Moreover, it continuously tracks which basic messages it sent and received at which moments of its execution and logs this information in stable storage at each checkpoint. Checkpointing is performed sporadically because the use of stable storage makes this operation expensive.

In contrast to the snapshot algorithms discussed in the previous two sections, processes do not coordinate their checkpoints. The underlying idea is that crashes occur rarely, which makes it attractive to only incur message overhead directly after such a crash instead of periodically. The price to pay for this reduced message overhead is that after a crash a rollback must be performed, because the uncoordinated checkpoints in the different processes may give rise to orphan or lost messages. The checkpoints of the processes in stable storage serve as the basis for rollback recovery, determining a consistent snapshot, i.e., a configuration in the past, from which the execution can be restarted after a crash. Events at noncrashed processes must be rolled back if they are causally after an irrecoverably lost event at the crashed process, meaning this event happened after the last checkpoint of that process.

Example 3.3 The picture below shows the time line of events at three processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ with regard to some basic computation, where real time progresses from left to right.

![](images/21706d83ecb10402ac17fa98333e89972b840b33334aa8016d480f6030365534.jpg)

Process $p _ { 0 }$ receives $m _ { 1 }$ from $p _ { 1 }$ , saves a checkpoint, receives $m _ { 2 }$ from $p _ { 2 }$ , sends $m _ { 3 }$ to $p _ { 1 }$ , and crashes. After receiving $m _ { 3 } , p _ { 1 }$ sends $m _ { 4 }$ to $p _ { 2 }$ and $m _ { 5 }$ to $p _ { 0 }$ . The latter message reaches its destination after $p _ { 0 }$ has recovered from the crash.

When $p _ { 0 }$ recovers from its crash, its state is restored to its last checkpoint. The fact that $p _ { 0 }$ received $m _ { 2 }$ is irrecoverably lost. The resulting snapshot is inconsistent because $m _ { 2 }$ is a lost message and $m _ { 3 }$ an orphan message. To resolve the latter, $p _ { 1 }$ is rolled back to before the receipt of $m _ { 3 }$ . This, however, turns $m _ { 4 }$ and $m _ { 5 }$ into orphan messages. To resolve the former, $p _ { 2 }$ in turn is rolled back to before the receipt of $m _ { 4 }$ . Furthermore, $p _ { 2 }$ needs to physically resend $m _ { 2 }$ . Finally, after its recovery phase, $p _ { 0 }$ needs to recognize that $m _ { 5 }$ is an orphan message and discard it. This will be explained later.

The Peterson-Kearns checkpointing algorithm uses the logical vector clock to determine which basic events should be discarded in the rollback recovery. Each basic message contains the vector time of its send event, so that the vector time of the corresponding receive event can be determined; see the computation at runtime of Lamport’s logical clock in section 2.2 as well as exercise 2.10. Control events of the rollback procedure are not taken into account by the vector clock. The vector time of a process is the vector time of the last basic event it performed; initially it consists only of zeros. Each checkpoint is in stable storage paired with the vector time of its process at the moment it is taken. Moreover, in each checkpoint, send and receive events of basic messages are paired with their vector times.

After a crashed process $p _ { i }$ has restarted (i.e., its execution has been taken over by another process), it retrieves its last checkpoint from stable storage. Then $p _ { i }$ initiates a run of the rollback procedure at the other processes by flooding a control message through the network, carrying its index $i$ and the ith component $k _ { i }$ of the vector time $\left( k _ { 0 } , \ldots , k _ { N - 1 } \right)$ at $p _ { i }$ ’s last checkpoint. The rollback procedure discards those basic events causally after a basic event at $p _ { i }$ that was irrecoverably lost in the crash; that is, all basic events for which the ith coordinate of the vector time is greater than $k _ { i }$ . While a process is performing the rollback procedure, its basic computation is stalled. Immediately after this procedure, the process saves a checkpoint. Basic messages that arrive during a restart or rollback recovery are buffered and treated after completing this procedure.

When $p _ { i }$ ’s control message arrives at a $p _ { j }$ , that process checks whether the ith coordinate of its current vector time is greater than $k _ { i }$ . If it is, then a basic event at $p _ { i }$ that is causally before basic events at $p _ { j }$ was lost in the crash. In that case, $p _ { j }$ restarts at its last checkpoint for which the ith coordinate of the vector time is not greater than $k _ { i }$ . From there, it reconstructs events according to its basic algorithm up to (but not including) its first event at which the ith coordinate of the vector time is greater than $k _ { i }$ . Basic messages that were received by $p _ { j }$ beyond this point and for which the ith coordinate of the vector time of the corresponding send event is not greater than $k _ { i }$ are kept, since discarding them would needlessly turn them into lost messages; they can be clustered right after the point where the reconstruction at $p _ { j }$ has halted. On the other hand, received basic messages for which the ith coordinate of the vector time of the corresponding send event is greater than $k _ { i }$ are discarded, since keeping them would turn them into orphan messages.

An orphaned message, for which the corresponding send event was rolled back, may reach its destination after completion of the recovery phase. This is remedied by maintaining a sequence number, which initially is zero at all processes. At each new recovery phase, all processes increase their sequence number by 1. They keep in stable storage the old sequence number paired with $\left( k _ { i } , i \right)$ . The sequence number of the sender is attached to basic messages, so that such orphan messages can be recognized and discarded by their receivers. Such a message carries an old sequence number associated with a time stamp $\left( k _ { i } , i \right)$ , while the ith coordinate of the vector time of its send event is greater than $k _ { i }$ .

To avoid that basic messages reaching $p _ { i }$ between its last checkpoint and its recovery from the crash are lost, $p _ { i }$ informs each other process $q$ which basic messages $p _ { i }$ received from $q$ between the previous recovery of a crash by $p _ { i }$ (if any) and $p _ { i }$ ’s last checkpoint. Each process $q$ physically resends to $p _ { i }$ those basic messages that may have been lost in the crash (again carrying the old sequence number). If the first installment of such a basic message is still in transit after the time of recovery, then $p _ { i }$ will recognize from the vector time of the send event that it receives this message twice, so that the second instance of the message will be discarded.

Example 3.4 We apply the Peterson-Kearns algorithm in the scenario given in example 3.3. Let the sequence number initially be 0; all basic messages carry this number. After $p _ { 0 }$ has crashed, it restarts from its last checkpoint with sequence number 1. Let the checkpoint carry vector time $\left( k _ { 0 } , k _ { 1 } , k _ { 2 } \right)$ . Then $p _ { 0 }$ sends control messages to $p _ { 1 }$ and $p _ { 2 }$ , containing the vector time component $k _ { 0 }$ , ,, its index 0, and sequence number 1. Upon receipt of this message, $p _ { 1 }$ and $p _ { 2 }$ start a run of the rollback procedure with sequence number 1; they store $k _ { 0 }$ paired with index 0 and sequence number 1. Because of the receipts of $m _ { 3 }$ and $m _ { 4 }$ , the vector times at $p _ { 1 }$ and $p _ { 2 }$ carry a value greater than $k _ { 0 }$ at index 0. So both processes restart at their last checkpoint (not shown in the picture) and reconstruct events. These replays halt right before the receipts of $m _ { 3 }$ and $m _ { 4 }$ , respectively. Message $m _ { 2 }$ is physically resent by $p _ { 2 }$ (with sequence number 0) because it was not received by $p _ { 0 }$ before its last checkpoint. When $m _ { 5 }$ reaches $p _ { 0 }$ , it is discarded as an orphan message, because its sequence number is 0, while the vector time of its send event carries a value greater than $k _ { 0 }$ at index 0.

The Peterson-Kearns algorithm cannot cope with multiple concurrent crashes. If crashes are rare and a recovery phase takes little time, it is reasonable to neglect the possibility of a crash during a recovery phase.

# Bibliographical notes

The Chandy-Lamport algorithm originates from [23].2 The Lai-Yang algorithm comes from [65]; the special control message was suggested in [79]. The Peterson-Kearns algorithm stems from [97]. An implementation of stable storage was proposed in [72].

# 3.4 Exercises

Exercise 3.1 Argue that a consistent snapshot, meaning one that satisfies properties (1) and (2), rules out orphan messages.

Exercise 3.2 Show by an example that the Chandy-Lamport algorithm is flawed if channels are non-FIFO.

Exercise 3.3 Consider an undirected circle of three processes $p , q$ , and $r$ (with non-FIFO channels). The LaiYang algorithm is applied to take a snapshot. First, $p$ sends basic messages $m _ { 1 }$ and $m _ { 2 }$ to $q$ and $r$ , respectively. Then it takes a local snapshot of its state, and sends piggybacked basic messages $\langle m _ { 3 } , t r u e \rangle$ and $\langle m _ { 4 } , t r u e \rangle$ to $q$ and $r$ , respectively. Let $\langle m _ { 3 } , t r u e \rangle$ arrive at $q$ first, so before $m _ { 1 }$ ,. On the other hand, let $m _ { 2 }$ arrive at $r$ first, so before $\langle m _ { 4 } , t r u e \rangle$ . Explain in detail how the snapshot is completed.

Exercise 3.4 Give an example in which the Lai-Yang algorithm computes a snapshot that is not a configuration of the ongoing execution.

Exercise 3.5 Adapt the Lai-Yang algorithm so that it supports multiple subsequent snapshots.

Exercise 3.6 Propose an adaptation of the Lai-Yang algorithm in which the channel states of the snapshot are always empty. (Your solution may affect the basic computation.)

Exercise 3.7 Give a snapshot algorithm for undirected networks with non-FIFO channels that, instead of adding control information to basic messages, uses

• marker messages, tagged with the number of basic messages sent into a channel before the marker message,   
acknowledgments, and   
• temporary (local) freezing of the basic execution.

Exercise 3.8 Consider the application of the Peterson-Kearns algorithm described in example 3.4. Adapt the basic computation depicted in example 3.3 in such a way that process $p _ { 0 }$ receives message $m _ { 2 }$ twice.

Exercise 3.9 Suppose sequence numbers were omitted from the Peterson-Kearns algorithm. What would go wrong in example 3.4?

Exercise 3.10 The picture below shows the time line of events at three processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ with regard to some basic computation. (Basic message $m _ { 8 }$ is sent after $p _ { 0 }$ has resumed its execution.)

![](images/9fc7cc4a34ac4a638907ab913fc830b9dbc8222a9cb11808a522ab99fb99388b.jpg)

Explain in detail how the processes roll back to a consistent snapshot using the Peterson-Kearns algorithm.

Exercise 3.11 Explain why in the Peterson-Kearns algorithm, a received message is an orphan message if and only if it carries an old sequence number, associated with some time stamp $\left( k _ { i } , i \right)$ , and its send event has a vector time of which the ith coordinate is greater than $k _ { i }$ .

Exercise 3.12 Give an example where in the Peterson-Kearns algorithm a process must retrieve from one of its checkpoints a basic message it needs to resend to the crashed process.

Exercise 3.13 In the original Peterson-Kearns algorithm, processes only resend basic messages to the crashed process if their send events have vector times not smaller than the vector time of the last checkpoint at the crashed process. Give an example to show that this approach can lead to lost messages, even if channels are FIFO (which is an assumption made for the original Peterson-Kearns algorithm).

Exercise 3.14 Give an example of a computation in which the Peterson-Kearns algorithm would roll back a certain event if Lamport’s clock were used, but this event is not rolled back with the vector clock.

Exercise 3.15 How would sequence numbers in the Peterson-Kearns algorithm need to be enhanced to cope with concurrent crashes?

# Waves

In distributed computing, a process often needs to gather information from all other processes in the network. This process then typically sends a request through the network, which incites the other processes to reply with the required information. Notable examples are termination detection (see chapter 6), routing (see chapter 8), and election of a leader in the network (see chapter 9).

This procedure is formalized in the notion of a wave algorithm, in which each computation, called a wave, satisfies the following three properties:

• It is finite.   
. It contains one or more decide events.   
. For each decide event $a$ and process $p$ , $b \prec a$ for some event $^ b$ at $p$ .

A decide event can for instance be that the network has terminated or who will be the leader in the network. The idea behind wave algorithms is that each computation produces one or more decisions, in which all processes have a say. An important characteristic of a wave algorithm is that it does not complete if any process $p$ refuses to take part in its execution, because no event at $p$ in the wave would be causally before the decide event.

Often a wave is initiated by one process, and in the end one decide event happens, at its initiator. If there can be concurrent calls of a wave algorithm, initiated by different processes, then usually for each wave the messages are marked with the ID of its initiator. In such a setting, if a wave does not complete, because a process refuses to take part, then typically another wave will complete successfully later on. Examples are Rana’s termination detection algorithm (see section 6.2) and the echo algorithm with extinction for election (see section 9.3).

# 4.1 Traversal Algorithms

A traversal algorithm is a centralized wave algorithm in which the initiator sends a token through the network. After visiting all other processes, the token returns to the initiator, which then makes a decision. A typical example of a traversal algorithm is the ring algorithm, in which the token makes one trip around the ring.

Traversal algorithms can be used to build a spanning tree of the network, with the initiator as the root. Each noninitiator has as its parent the process from which it received the token for the first time.

# Tarry’s Algorithm

Tarry’s algorithm is a traversal algorithm for undirected networks. It is based on the following two rules:

1 A process never forwards the token through the same channel twice.   
.2 A noninitiator only forwards the token to its parent if there is no other option.

By applying these two rules, the token travels through each channel twice and finally ends up at the initiator.

Example 4.1 We apply Tarry’s algorithm to the following network; $p _ { 0 }$ is the initiator.

![](images/860095ec8f3e8608881fc9be3f4832de577d065dec2961873d761cd3edd9c421.jpg)

The network is undirected (and unweighted); arrows and numbers mark the consecutive steps of one possible path of the token. Solid arrows establish a parent-child relation (in the opposite direction) in the resulting spanning tree. So the resulting spanning tree of this execution is

![](images/c4310de02bf5051d5624aca59a31b1d7ac5fbe3387b6581f6a4eed94662588ae.jpg)

Tree edges are solid, whereas frond edges are dashed.

We argue that in Tarry’s algorithm the token traverses each channel twice, once in each direction, and finally ends up at the initiator. By rule 1, the token is never sent through the same channel in the same direction twice. Each time a noninitiator $p$ holds the token, it has received the token one more time than it has sent the token to a neighbor, meaning that there is still a channel into which $p$ has not yet sent the token. So, in accordance with rule 1, $p$ can send the token into this channel. Hence, when Tarry’s algorithm terminates, the token must be at the initiator. Suppose, toward a contradiction, that at the moment of termination some channel $p q$ has not been traversed by the token in both directions; let $p$ be the earliest visited process for which such a channel exists. The fact that the token started and finished at the initiator implies that the token has traversed all channels of the initiator in both directions. So $p$ is a noninitiator. Since by assumption all channels of the parent of $p$ have been traversed in both directions, $p$ has sent the token to its parent. So, by rule

2, $p$ must have sent the token into all its channels. Since $p$ has sent and received the token an equal number of times, it must have received the token through all its channels. To conclude, the token has traversed pq in both directions, contradicting our assumption. Hence, the token must have traversed all channels in both directions.

Tarry’s algorithm requires $2 E$ messages (two messages per channel, one in either direction), and it takes at most $2 E$ time units to terminate.

# Depth-First Search

In a depth-first search, starting from the initiator, whenever possible, the token is forwarded to a process that has not yet held the token. If a process holding the token has no unvisited neighbor, then it sends the token back to its parent, being the process from which it received the token for the first time. Depth-first search has a wide range of applications. It can for instance be the cornerstone for computing the strongly connected components in a distributed network that itself is not strongly connected.

The spanning tree in example 4.1 is not a depth-first search tree; that is, it cannot be the result of a depthfirst search. Because in a depth-first search, processes $s$ and $t$ would never both have $p$ as their parent. In general, a spanning tree is the result of a depth-first search if all frond edges connect a process with one of its descendants in the spanning tree (unlike the frond edge between $s$ and $t$ ).

A depth-first search is obtained by adding one more rule to Tarry’s algorithm:

3 When a process receives the token, it immediately sends it back through the same channel if this is allowed by rules 1 and 2.

Example 4.2 Consider the same network as in example 4.1; $p _ { 0 }$ is again the initiator. In the following picture one possible depth-first search is charted out.

![](images/7f8cf508ad0e9c00fc25b57f8465ff4731579a90f979ace3e01c261fbe9f6d2f.jpg)

In example 4.1, when $p _ { 0 }$ receives the token from $q$ , it forwards it to $s .$ . However, here $p _ { 0 }$ is forced to send the token back to $q$ immediately because of rule 3.

Depth-first search is a special case of Tarry’s algorithm, so it also takes $2 E$ messages, and at most $2 E$ time units to terminate.

Sending the token back and forth through a frond edge, such as in steps 3 and 4 and steps 9 and 10 in example 4.2, constitutes a loss of time. One obvious way to avoid this is by including the IDs of visited processes in the token, so that a process can determine which neighbors have already seen the token. Since the token then travels back and forth only through the $N - 1$ tree edges, the message complexity is reduced from $2 E$ to $2 N - 2$ messages, and similarly the time complexity is reduced to at most $2 N - 2$ time units. The drawback, however, is that the bit complexity goes up from $O ( 1 )$ to $O ( N { \cdot } \log N )$ (assuming that ${ \cal O } ( \log N )$ bits are needed to represent the ID of a process).

An alternative is to let a process $p$ that holds the token for the first time inform its neighbors (except the process that sent the token to $p$ and the process to which $p$ will send the token) that it has seen the token. In Awerbuch’s depth-first search algorithm, $p$ waits for acknowledgments from all those neighbors before forwarding the token, to ensure that they cannot receive the token before $p$ ’s information message. A process marks a channel as a frond edge as soon as it has received an information message through this channel and has received the token through another channel. A process never forwards the token through a frond edge. The worst-case message complexity goes up to $4 E$ because frond edges carry two information messages and two acknowledgments, while tree edges carry two tokens and possibly one information and acknowledgment pair. Also, the worst-case time complexity goes up, to $4 N - 2$ time units, because tree edges carry two tokens, and each process may wait at most two time units for acknowledgments to return.

Cidon’s depth-first search algorithm improves on Awerbuch’s algorithm by abolishing the wait for acknowledgments. A process $p$ forwards the token without delay and records to which process forward ${ \bf \chi } _ { p } ^ { \prime }$ it forwarded the token last. If $p$ receives the token back from a process $q \neq f o r w a r d _ { p }$ , it dismisses the token and marks the channel $p q$ as a frond edge. No further action from $p$ is required, because $q$ will eventually receive the information message from $p$ . Then in turn $q$ marks the channel $p q$ as a frond edge and continues to forward the token to another process (if possible).

Example 4.3 In the following undirected network, with $p _ { 0 }$ as initiator, one possible computation of Cidon’s depth-first search is depicted.

![](images/2c2bd007a8697bd77f4bbe8fda476274fc30694cb6297889195733788261720b.jpg)

The token is forwarded by $r$ through the frond edge $p _ { 0 } r$ before the information message from $p _ { 0 }$ reaches $r$ . When the information message from $p _ { 0 }$ arrives, $r$ continues to forward the token to $s$ . The information message from $p _ { 0 }$ reaches $s$ before the token does, so $s$ does not send the token to $p _ { 0 }$ .

If in Cidon’s algorithm processes keep track of their children, then it is essential to clearly distinguish tokens sent to nonparents from tokens sent to parents (see exercise 4.5).

In Cidon’s algorithm, frond edges may carry two information messages and two tokens (see exercise 4.3), so the worst-case message complexity is still $4 E$ . But the worst-case time complexity reduces to $2 N - 2$ time units, because at least once per time unit the token is forwarded through a tree edge, and the $N - 1$ tree edges each carry two tokens.

# 4.2 Tree Algorithm

The tree algorithm is a decentralized wave algorithm for undirected, acyclic networks. A process $p$ waits until it has received messages from all its neighbors except one. Then $p$ makes that neighbor its parent and sends a message to it. When $p$ receives a message from its parent, it decides. Always exactly two processes in the network decide, and these two processes consider each other their parent. Note that initially only the processes with a single neighbor can send a message.

Example 4.4 We consider one possible computation of the tree algorithm on the following network.

![](images/a156b5fd3a7640534a50a9cc52eb86d434404c735403fb697132cea7d962c078.jpg)

$p$ and $q$ both send a message to $r$ and make $r$ their parent. Likewise, $t$ and $u$ both send a message to $s$ and make $s$ their parent.   
When the messages from $t$ and $u$ have arrived, $s$ sends a message to $r$ and makes $r$ its parent.   
When the messages from $q$ and $s$ have arrived, $r$ sends a message to $p$ and makes $p$ its parent.   
When $p$ ’s message has arrived, $r$ decides. Likewise, when $r$ ’s message has arrived, $p$ decides.

The parent-child relations in the terminal configuration are as follows.

![](images/ea482e59e64de8352896e90bae9466dded4f49729f64d0bf0c629d1b470bc84a.jpg)

We argue that in each execution of the tree algorithm, exactly two processes decide. As each process sends at most one message, each execution reaches a terminal configuration $\gamma$ . Suppose, toward a contradiction, that in $\gamma$ a process $p$ has not sent any message, meaning that it did not receive a message through two of its γchannels, say $q p$ and $r p$ . Since $\gamma$ is terminal, $q$ did not send a message to $p$ , which implies it did not receive γa message through two of its channels, $p q$ and say sq. This argument can be repeated with $s$ instead of $q$ , and so forth. Repeating this argument over and over again, inevitably we eventually establish a cycle of processes that did not receive a message through two of their channels. This contradicts the assumption that the network topology is acyclic. So in $\gamma$ each process has sent a message, which adds up to $N$ messages in total. Since γprocesses send a message into the only channel through which they have not yet received a message, clearly each channel carries at least one message. An acyclic network has $N - 1$ channels, so exactly one channel carries two messages. Only the two processes $t$ and $u$ connected by this channel decide. All events, except for the reception of $t$ ’s message and the decision at $u$ , are causally before the decision at $t$ , and likewise for the decision at $u$ .

The tree algorithm is incorrect for networks that contain a cycle, because in that case the algorithm does not terminate. For instance, consider a ring of three processes. Since each process has two neighbors, it will wait for a message from one of its neighbors. Hence, all three processes wait for input, meaning that no event ever happens.

The tree algorithm takes at most $\frac { D } { 2 }$ time units to terminate if $D > 1$ (see exercise 4.9).

# 4.3 Echo Algorithm

The echo algorithm is a centralized wave algorithm for undirected networks, which underlies several of the distributed algorithms presented in the following chapters. It is in a sense a parallel version of Tarry’s traversal algorithm.

The initiator starts by sending a message to all its neighbors. Intuitively, these messages are forwarded in all directions and bounce back from the corners of the network toward the initiator. This is achieved as follows. When a noninitiator receives a message for the first time, it makes the sender its parent and sends a message to all its neighbors except its parent. When a noninitiator has received messages from all its neighbors, it sends a message to its parent. Finally, when the initiator has received messages from all its neighbors, it decides.

Example 4.5 We consider one possible computation of the echo algorithm on the following network, in which $p _ { 0 }$ is the initiator.

![](images/a4f704e8c92795e06e00fae93b0610954f982f7f1b9769e7ad43a7fd1cbaff68.jpg)

$p _ { 0 }$ sends messages to $q , s ,$ , and $t$ .   
$p _ { 0 }$ ’s message arrives at $q$ , which makes $p _ { 0 }$ its parent and sends messages to $r , s ,$ , and $t$ .   
$q$ ’s message arrives at $t$ , which makes $q$ its parent and sends messages to $p _ { 0 }$ and $s$ .   
$q$ ’s message arrives at $r$ , which makes $q$ its parent. Since $r$ has no other neighbors, it sends a message to its parent $q$ straightaway.   
$p _ { 0 }$ ’s message arrives at $s$ , which makes $p _ { 0 }$ its parent and sends messages to $q$ and $t$ .   
$p _ { 0 }$ ’s and $s$ ’s messages arrive at $t$ , which sends a message to its parent $q$ .   
$r$ ’s, $s$ ’s, and $t ^ { : }$ ’s messages arrive at $q$ , which sends a message to its parent $p _ { 0 }$ .   
$q$ ’s and $t$ ’s messages arrive at $s$ , which sends a message to its parent $p _ { 0 }$ .   
$q$ ’s, s’s, and $t ^ { \prime }$ ’s messages arrive at $p _ { 0 }$ , which decides.

The resulting spanning tree is as follows.

![](images/9c0b309fea8bd5c36b1433f937e467341c10fde9a05324be3b0e1a5f1ea07f1c.jpg)

We argue that the echo algorithm is a wave algorithm. Since messages are flooded through the network, a spanning tree is constructed that covers the entire network. Clearly, each process eventually sends a message to its neighbors except its parent. We argue by induction on the size of the network that each noninitiator eventually sends a message to its parent. Consider a leaf $p$ in the spanning tree. Eventually, $p$ will receive a message from all its neighbors (as only the channel to its parent is a tree edge) and send a message to its parent. When this message arrives, we can consider the network without $p$ , in which by induction each noninitiator eventually sends a message to its parent. We conclude that, through each channel, one message travels either way. So eventually the initiator receives a message from all its neighbors and decides. All messages are causally before this decision.

In total, the echo algorithm takes $2 E$ messages, and it takes at most $2 N - 2$ time units to terminate.

# Bibliographical notes

Tarry’s algorithm stems from [115]. The first distributed depth-first search algorithm was presented in [28].   
Awerbuch’s algorithm originates from [9]; Cidon’s algorithm was proposed independently in [66] and in [30].   
The echo algorithm stems from [25]; the presentation here is based on an optimized version from [105].

# 4.4 Exercises

Exercise 4.1 Describe in detail a computation of Tarry’s algorithm on a complete undirected network of four processes in which a spanning tree is constructed that is not a depth-first search tree.

Exercise 4.2 Give an example of a computation of Awerbuch’s algorithm in which an information message and a token are communicated through the same tree edge.

Exercise 4.3 Give a computation of Cidon’s algorithm on the undirected network below, with initiator $p _ { 0 }$ , in which two information messages and two tokens are exchanged through the channel that connects $p _ { 0 }$ and $q$ .

![](images/9b4d0dcc647376a2182c312f08f647c131902c6f370ce3b39ada3524b5c26e87.jpg)

Exercise 4.4 [87] Consider a complete undirected network withcomputation of Cidon’s algorithm on this network that consists $N \geq 3$ and  (i.e $\begin{array} { r } { E = \frac { N \cdot ( N - 1 ) } { 2 } } \end{array}$ ges). Give a) messages. $4 E - 2 N + 1$ $2 N ^ { 2 } - 4 N + 1 \rangle$

Exercise 4.5 (a) [122] Give a computation of Cidon’s algorithm on an undirected ring of three processes in which at the end the initiator $p _ { 0 }$ considers neighbor $q$ its child while $q$ does not consider $p _ { 0 }$ its parent. (b) Explain how Cidon’s algorithm can be adapted to avoid this problem (without adding messages or delays).

Exercise 4.6 Explain how the tree algorithm can compute the size of an acyclic undirected network.

Exercise 4.7 Extend the tree algorithm so that a spanning tree is computed.

Exercise 4.8 Consider a computation of the tree algorithm on the undirected network below.

![](images/709cd2f7c87599b5638c4c949a50f830b53811dd78d021724f23f26e5a6a3426.jpg)

Let (only) process $q$ initiate a run of the Lai-Yang snapshot algorithm, just after receiving its first wave message. Show how the snapshot is computed, whereby the wave message from $q$ to its parent overtakes the control message from $q$ to its parent.

Exercise 4.9 Explain how the tree algorithm can be extended with a phase in which the decision is communicated to all processes. Furthermore, argue that the tree algorithm takes at most $D$ time units to terminate, if the time needed to communicate the decision to all processes is taken into account.

Exercise 4.10 Compute the vector clock values of the events in an computation of the echo algorithm on an undirected ring of three processes, in which a spanning tree of depth 2 is constructed.

Exercise 4.11 Consider an undirected network of $N > 3$ processes $p _ { 0 } , . . . , p _ { N - 1 }$ , where $p _ { 1 } , . . . , p _ { N - 1 }$ form a ring and $p _ { 0 }$ > , . . . , , . . . ,has a channel to all other processes. Give a computation of the echo algorithm on this network, with $p _ { 0 }$ as initiator, that takes (arbitrarily close to) $N + 1$ time units to complete.

Exercise 4.12 Argue that the echo algorithm takes at most $2 N - 2$ time units to terminate.

Exercise 4.13 [117] Suppose you want to use the echo algorithm in a network where duplication of messages may occur. Which modification to the algorithm should be made?

Exercise 4.14 [117] Let each process initially carry a random integer value. Adapt the echo algorithm to compute the sum of these integer values. Explain why your algorithm is correct.

# Deadlock Detection

A process may have to wait to perform events until some other processes send or (in a synchronous setting) are ready to receive input, or until some resources have become available. A deadlock occurs if a group of processes is doomed to wait forever. This happens if each of these processes is waiting until some other process in the group either sends a message or releases a resource. The first type of deadlock is called a communication deadlock, while the second type is called a resource deadlock.

Deadlock detection is a fundamental problem in distributed computing that is of great practical importance, since a deadlock stops a distributed system from completing its task. A deadlock can be very hard to uncover, because it requires determining a cyclic dependency within a running system. For this purpose, the global configuration of the distributed system is regularly examined by the individual processes to detect whether a deadlock has occurred. That is, snapshots are taken of the global configuration of the system, and these are examined for cycles. If a deadlock is detected, the basic algorithm may be rolled back (see section 3.3) and processes may be restarted in order to remove the detected deadlock. Here we focus only on the detection of deadlocks.

# 5.1 Wait-for Graphs

A wait-for graph depicts dependencies between processes and resources. A node in a wait-for graph can represent either a process or a resource. Both communication and resource deadlocks can be captured by what are called $N$ -out-of- $M$ requests, where $N \leq M$ . For example, if a process is waiting for one message from a group of $M$ processes, then $N = 1$ ; or, if a database transaction first needs to lock $M$ data files, then $N = M$ .

A nonblocked node $u$ in a wait-for graph can issue an $N$ -out-of- $M$ request, meaning that it sends a request to $M$ other nodes and becomes blocked until $N$ of these requests have been granted. In the wait-for graph, a unidirectional edge is drawn from $u$ to each of the $M$ nodes to which $u$ issues the $N _ { ☉ }$ -out-of- $M$ request. Only nonblocked nodes can grant a request. Every time a node $\nu$ grants $u$ ’s request, the edge uv can be removed from the wait-for graph. When $N$ requests have been granted, $u$ becomes unblocked and informs the remaining $M - N$ nodes that $u$ ’s request can be dismissed; accordingly, these $M - N$ outgoing edges of $u$ are removed from the wait-for graph.

The following example shows how a wait-for graph can be used to model communication dependencies.

Example 5.1 Suppose process $p$ must wait for a message from process $q$ . In the wait-for graph, $p$ sends a request to $q$ ; as a result, the edge $p q$ is created and $p$ becomes blocked. When $q$ sends a message to $p$ , the request from $p$ is granted. Then the edge $p q$ is removed from the wait-for graph, and $p$ becomes unblocked.

The following example shows how a wait-for graph can be used to model resource dependencies.

Example 5.2 Suppose two different processes $p$ and $q$ want to claim a resource, while at any time only one process can own the resource.

Nodes $u$ and $\nu$ , representing $p$ and $q$ , respectively, send a request to node $w$ , representing the resource. As a result, in the wait-for graph, edges uw and $\nu w$ are created.   
The resource is free, and $w$ sends a grant to, say, $u$ , so that $p$ can claim the resource. In the wait-for graph, the edge uw is removed.   
The resource must be released by $p$ before $q$ can claim it. Therefore, $w$ sends a request to $u$ , creating the edge wu in the wait-for graph.   
After $p$ releases the resource, $u$ grants the request from $w$ . Then the edge wu is removed from the wait-for   
graph.   
Now $w$ can grant the request from $\nu$ , so $q$ can claim the resource. In the wait-for graph, the edge wv is created and the edge vw is removed.

In wait-for graphs, an $M$ -out-of- $M$ request with $M > 1$ (also called an AND request) is drawn with an arc through the $M$ edges, while a 1-out-of- $M$ >request (also called an OR request) is drawn without an arc. For example, for $M = 3$ ,

![](images/4dce795a2097c5e82c76a7000d6da41ac154fc69c64d068c6692b9c830e79f57.jpg)

The examples in this chapter do not contain any $N$ -out-of- $M$ requests with $1 < N < M$ .

# 5.2 Bracha-Toueg Algorithm

To try to detect a deadlock with regard to an ongoing execution of a basic algorithm, first a snapshot can be taken of the corresponding wait-for graph. A process that suspects it is deadlocked starts a Lai-Yang snapshot to compute the wait-for graph (see section 3.2). To distinguish between subsequent snapshots, snapshots (and their control messages) are tagged with a sequence number. Each node $u$ takes a local snapshot to determine the requests it sent or received that were not yet granted or dismissed, taking into account the request, grant, and dismiss messages in the channel states of its incoming edges. Then it computes two sets of nodes:

• $O u t _ { u }$ : the nodes to which $u$ has sent requests that have not yet been granted or dismissed.   
• $I n _ { u }$ : the nodes from which $u$ has received requests that have not yet been granted or dismissed.

The following analysis on the computed wait-for graph, which cleans out the graph as much as possible, may reveal deadlocks:

• Nonblocked nodes in the wait-for graph can grant requests. When a request has been granted, the corresponding edge in the wait-for graph is removed. When a node $u$ with an outstanding $N$ -out-of- $M$ request has received $N$ grants, $u$ becomes unblocked. The remaining $M - N$ outgoing edges of $u$ in the wait-for graph are removed.

When no more grants are possible, nodes that are still blocked in the wait-for graph are deadlocked in the snapshot of the basic algorithm.

We consider two examples. Granted requests are drawn as dashed arrows (they are no longer part of th wait-for graph).

Example 5.3 The next wait-for graph contains three 2-out-of-2 requests. Blocked nodes are colored gray.

![](images/e172e0598af6256a104d716ce56add5029b74c38518b181487ce1251cf1f22ae.jpg)

The unblocked node $x$ grants the three incoming requests. After that, the three other nodes remain blocked, so no other requests can be granted. Hence, these three nodes are deadlocked.

Example 5.4 The next wait-for graph contains two 2-out-of-2 requests and one 1-out-of-2 request.

![](images/d7d5a3eb302a263974f4055cfe39c28056248290ac35033b509e9329b38a4071.jpg)

The unblocked node $x$ grants the three incoming requests. As a result, node $w$ becomes unblocked; it dismisses its remaining request to $\nu$ and grants the incoming request from $u$ . Next, node $u$ becomes unblocked; it grants the last pending request in the graph.

![](images/b246ea1b677c3e1e7c77ec0ddc3eac9ad4fad232593b3a51dc255555a6c64090.jpg)

Finally, all nodes have become unblocked, so no nodes are found to be deadlocked.

Let the basic algorithm run on an undirected network, and suppose a wait-for graph has been computed. The centralized Bracha-Toueg deadlock detection algorithm provides a distributed method to perform the analysis whereby the wait-for graph is cleaned out to try to find deadlocks. To distinguish between invocations of the algorithm by different initiators, all control messages are tagged with the ID of the corresponding initiator. The nodes in the wait-for graph start to resolve grants, in the manner described earlier. Initially, requestsv is the number of grants node $\nu$ requires to become unblocked in the wait-for graph. When requestsv is or becomes 0, $\nu$ sends grant messages to all nodes in $I n _ { \nu }$ . When $\nu$ receives a grant message, requestsv $\gets$ $r e q u e s t s _ { \nu } - 1$ . If after termination of this deadlock detection run request $\mathfrak { s } _ { u } > 0$ at the initiator $u$ , then it is deadlocked in the basic algorithm.

A key question is how to determine that deadlock detection has terminated. In principle, nodes could apply a termination detection algorithm from chapter 6. However, the Bracha-Toueg algorithm is designed in such a way that termination detection comes for free. We now explain in detail how the nodes choreograph cleaning out the wait-for graph. Initially, notifiedv $=$ false and freev $=$ false at all nodes $\nu$ ; these two variables ensure that $\nu$ executes at most once the routines $N o t i f y _ { \nu }$ and $G r a n t _ { \nu }$ , respectively, given in the pseudocode that follows. The initiator $u$ of deadlock detection starts the resolution of grants throughout the wait-for graph by executing $N o t i f y _ { u }$ . It consists of sending a notify message into all outgoing edges, and executing $G r a n t _ { u }$ if $r e q u e s t s _ { u } = 0$ . Noninitiators $\nu$ that receive a notify message for the first time execute $N o t i f y _ { \nu }$ . Moreover, nodes $\nu$ that are or become unblocked, meaning that $r e q u e s t s _ { \nu } = 0$ , grant all pending requests by executing Grantv. The pseudocode for the procedure Notifyv is as follows.

notified $_ { \nu } \gets t r u e$ ;   
send $\langle \mathbf { n o t i f y } \rangle$ to all $w \in O u t _ { \nu }$ ;   
if requests $, = 0$ and $f r e e _ { \nu } =$ false then perform procedure $G r a n t _ { \nu }$ ;   
end if   
await $\langle \mathbf { d o n e } \rangle$ from all $w \in O u t _ { \nu }$ ;

And the pseudocode for the procedure Grantv is the following.

$f r e e _ { \nu } \gets t r u e$ ;   
send $\langle \bf g r a n t \rangle$ to all $w \in I n _ { u }$ ;   
await $\langle \mathbf { a c k } \rangle$ from all $w \in I n _ { u }$ ;

Note that since $G r a n t _ { \nu }$ is a subcall of $N o t i f y _ { \nu }$ , waiting for ack messages postpones the sending of done messages. The done (and ack) messages are used for termination detection. That is, when the initiator $u$ has received a done from all nodes in $O u t _ { u }$ , it checks the value of $f r e e _ { u }$ . If it is still false, $u$ concludes that it is deadlocked.

While a node is awaiting done or ack messages, it can process incoming notify and grant messages When a node $\nu$ receives a notify message from a neighbor $w$ , it does the following.

if notified $=$ false then perform procedure Notifyv;   
end if   
send $\langle \mathbf { d o n e } \rangle$ to $w$ ;

When a node $\nu$ receives a grant message from a neighbor $w$ , it does the following.

if requestsv $> 0$ then $r e q u e s t s _ { \nu } \gets r e q u e s t s _ { \nu } - 1$ ; if requests $_ { \nu } = 0$ and $f r e e _ { \nu } =$ false then perform procedure $G r a n t _ { \nu }$ ; end if   
end if   
send $\langle \mathbf { a c k } \rangle$ to $w$ ;

Note that if $\nu$ receives a notify message and notifie $\mathbf { \nabla } \cdot d _ { \nu } = t r u e$ (meaning that $\nu$ already executed Notifyv), or a grant message and the assignment request $s _ { \nu } \gets r e q u e s t s _ { \nu } - 1$ does not set requestsv from 1 to 0 (meaning that $\nu$ does not become unblocked by the grant message), then $\nu$ immediately sends back a done or ack message, respectively.

Example 5.5 Suppose the following wait-for graph, consisting of one 2-out-of-2 request and two 1-outof-1 requests, has been computed in a snapshot. Initially, request $\mathrm { s } _ { u } = 2$ , requests $\mathbf { \Phi } _ { \nu } = r e q u e s t s _ { w } = 1$ , and requests $_ x = 0$ .

![](images/d255746316bbad3de589c169ed652acee264d650f78fe96612240fd221362411.jpg)

We consider one possible computation of the Bracha-Toueg algorithm.

Initiator $u$ starts by sending a notify to $\nu$ and $x _ { \ast }$ , and must now await a done from both $\nu$ and $x$ before it can examine reques $ { \boldsymbol } { { \mathrm { \Sigma } } } _ { S _ { u } }$ to see whether it is deadlocked.

![](images/f6a91a8eb5468d7b94fce90c613a18fa3b50c96ad4afca1408edca684150c454.jpg)

The notify from $u$ is received at $\nu$ , which sends a notify to $w$ and must await a done from $w$ before it can send a done back to $u$ . Concurrently, the notify from $u$ is received at $x .$ , which sends a grant to $u$ and $w$ , because requests $_ x = 0$ , and must await an ack from both $u$ and $w$ before it can send a done back to $u$ .

![](images/fcb7a54c5e95754b2d14e0d9f00447caca31f2dfc5a66eb94108ac175c82133b.jpg)

The notify from $\nu$ is received at $w$ , which sends a notify to $x$ and must await a done from $x$ before it can send a done to $\nu$ . Concurrently, the grant from $x$ is received at $u$ , which sends an ack back to $x$ immediately, because the grant decreases requestsu from 2 to 1. Next, the grant from $x$ is received at $w$ , which sends a grant to $\nu$ , because requestsw decreases from 1 to 0, and must await an ack from $\nu$ before it can send an ack back to $x$ .

![](images/4d7046038c1e0ff2ffd419e2bac935057699e244bc5b6d2bf6ce5ed490f2fda3.jpg)  
⟨grant⟩

The notify from $w$ is received at $x$ , which sends a done back to $w$ immediately. Next, the ack from $u$ is received at $x _ { \ast }$ , so that $x$ only needs an ack from $w$ in order to send a done to $u$ . Concurrently, the grant from $w$ is received at $\nu$ , which sends a grant to $u$ , because requestsv decreases from 1 to 0, and must await an ack from $u$ before it can send an ack back to $w$ .

awaits ⟨ack⟩ from $w$

![](images/8ed08c8afada32165b477ed6cb21b37adbe730d77c9a86adcc2ecd09301c983a.jpg)

– The done from $x$ is received at $w$ , which can now send a done to $\nu$ . Concurrently, the grant from $\nu$ is received at $u$ , which decreases requestsu from 1 to 0 and sends an ack back to $\nu$ immediately, because there are no requests for $u$ to grant.

awaits $\langle \mathbf { d o n e } \rangle$ from v, x awaits ⟨ack⟩ from $w$ awaits ⟨ack⟩ from $\nu$

![](images/aa56521d27f3c71c59408b83c5d04be1dc2a43719582caaa426a08a2687e2f29.jpg)  
awaits $\langle \mathbf { d o n e } \rangle$ awaits $\langle \mathbf { a c k } \rangle$   
⟨done⟩

![](images/f3e930b67e0348514b2ae217174f1315397fb5dbcc6a81a0b2b7b0befcb39c24.jpg)  
awaits ⟨done⟩ from $x$ awaits ⟨ack⟩ from v

The done from $w$ is received at $\nu$ , which can now send a done to u. Next, the ack from $u$ is received at $\nu$ which can now send an ack to $w$ .

awaits $\langle \mathbf { d o n e } \rangle$ awaits ⟨ack⟩ from $w$ awaits ⟨ack⟩ from $\nu$

– The done from $\nu$ is received at $u$ , which now only awaits a done from $x$ before it can examine requestsu to see whether it is deadlocked. Concurrently, the ack from $\nu$ is received at $w$ , which can now send an ack to $x$ .

awaits $\langle \mathbf { d o n e } \rangle$ from x $\langle \mathbf { a c k } \rangle$ from $w$

![](images/ec32098f468185d95669a6f02958b1d509e5fbdba3fca1b97f6dca16efaa3f58.jpg)

– The ack from $w$ is received at $x$ , which can now send a done to $u$ – The done from $x$ is received at $u$ , which now examines requestsu, finds that its value is 0, and concludes that it is not deadlocked.

![](images/9d69e47e5bff198976fa126cf638d4e272b65f5342791cb062d21e940789f6bf.jpg)

We argue that when the initiator completes its Notify call, the Bracha-Toueg algorithm has terminated. The idea is that we can distinguish between two types of trees. First, by assuming that each node receiving a notify message for the first time makes the sender its parent, we obtain a tree $T$ rooted in the initiator. The notify/done messages construct $T$ and travel through (part of) the network similar to the echo algorithm (see section 4.3). Second, by assuming that each node receiving a grant message that sets requests to 0 makes the sender its parent, we obtain disjoint trees $T _ { \nu }$ (that may overlap with $T$ ), each rooted in a node $\nu$ where from the start $r e q u e s t s _ { \nu } = 0$ . Again, the grant/ack messages construct $T _ { \nu }$ and travel through the network similar to the echo algorithm. A noninitiator $\nu$ that is the root of a tree $T _ { \nu }$ only sends a done to its parent in $T$ when all grant messages sent by nodes in $T _ { \nu }$ have been acknowledged. This implies that when the initiator completes its Notify call, not only all notify messages but also all grant messages in the network have been acknowledged.

We argue that the Bracha-Toueg algorithm is deadlock-free. That is, the initiator will eventually complete its Notify call. Replying with a done (to a notify) or ack (to a grant) is delayed by a node $u$ only if it is executing $G r a n t _ { u }$ because requestsu is 0 (in case of a done) or has been made 0 by the grant (in case of an ack), and $u$ is awaiting ack messages. There cannot be a cycle of nodes that sent a grant to the next node and must wait before sending an ack to the previous node in the cycle, because such a cycle would always contain a node $\nu$ for which requestsv was not set to 0 by a grant from a node in this cycle. This implies that some node will always be able to respond to a pending notify or grant.

As noted, if after resolving the wait-for graph the initiator remains blocked, then it is deadlocked in the snapshot. Because the Bracha-Toueg algorithm cleans out the part of the wait-for graph that is reachable from the initiator as much as possible. So if the initiator remains blocked, this means that in the ongoing execution of the basic algorithm it is part of a cycle of nodes waiting for each other.

In the case of a communication deadlock (see example 5.1), the other direction also holds: if the initiator is deadlocked in the ongoing execution of the basic algorithm when the snapshot is taken, then it will remain blocked in the wait-for graph. In the case of resource deadlock, this only holds if resource requests are granted nondeterministically (see exercise 5.10). Because, as shown in example 5.2, modeling resource deadlock means that removing one edge (in the example, wu) may automatically produce another edge (in the example, wv). The Bracha-Toueg approach to resolving edges in wait-for graphs does not take into account this automatic creation of edges.

# Bibliographical notes

The Bracha-Toueg deadlock detection algorithm originates from [17].

# 5.3 Exercises

Exercise 5.1 Draw the wait-for graph for the initial configuration of the tree algorithm, applied to an undirected cycle of three nodes.

Exercise 5.2 Give one possible computation of the Bracha-Toueg algorithm on the wait-for graph in example 5.5, with $\nu$ as initiator.

Exercise 5.3 Let node $u$ initiate a deadlock detection run in which the following wait-for graph is computed.

![](images/7b331f232c56759f3e37e38b0cb66bda2d451f5ac2e381a772af998553474ee9.jpg)

Give one possible computation of the Bracha-Toueg algorithm on this wait-for graph.

Exercise 5.4 Let node $u$ initiate a deadlock detection run in which the wait-for graph from the previous exercise is computed, with the only difference that $w$ is waiting for a 2-out-of-3 (instead of a 1-out-of-3) request. Give one possible computation of the Bracha-Toueg algorithm.

Exercise 5.5 Suppose node $u$ sends a request to node $\nu$ , then dismisses this request, and next sends another request to $\nu$ . Let the dismiss message reach $\nu$ first, then the second request, and finally the first request. How should $\nu$ process these three messages?

Exercise 5.6 Suppose that in a run of the Bracha-Toueg algorithm, some notify, done, grant, or ack message is in transit. Explain why the initiator of this run has then not yet checked whether its free field is true.

Exercise 5.7 In the Bracha-Toueg algorithm, are grant messages sent by the initiator relevant? If so, give an example that shows this. If not, explain why they are irrelevant.

Exercise 5.8 In the Bracha-Toueg algorithm, can also noninitiators, after having received a done from the neigbors to which they sent a notify, see from their free field whether they are deadlocked?

Exercise 5.9 Give a computation on a wait-for graph in which $f r e e _ { u }$ remains false for some node $u$ after running the Bracha-Toueg algorithm, while $u$ is not deadlocked in the basic algorithm.

Exercise 5.10 Suppose the order in which resource requests are granted is predetermined. Give an example of a snapshot with a resource deadlock that is not discovered by the Bracha-Toueg algorithm. Show, moreover, that if the selection of which resource request is granted is performed in a nondeterministic fashion, then the deadlock in your example may be avoided.

# Termination Detection

This chapter deals with the problem of detecting termination of a computation. While a deadlock, in which some processes are doomed to wait forever, is always undesirable, termination is generally a desirable situation. An execution of a distributed algorithm is terminated if all processes are passive and no (basic) messages are in transit. Termination detection is a fundamental and challenging problem in distributed computing because no process has complete knowledge of the global configuration of the network. Moreover, a passive process may be reactivated by a message from another process, and the absence of messages in the network must be established. Termination detection is important in e.g. diffusing computations (section 8.1), self-stabilization (chapter 17), and workpools (chapter 20).

The basic algorithm is the algorithm for which termination is being detected, and the control algorithm is the termination detection algorithm employed for this task. The control algorithm consists of two phases: termination detection and announcement. The announcement part, called Announce, is straightforward; we focus on the termination detection part. Ideally, this does not require freezing the basic execution.

From the viewpoint of the control algorithm, a simple description of the process states in the basic algorithm suffices. A process is said to be passive if the only basic event it can perform is a receive event, upon which it will always become active. A process is active if it is not passive. So initially the initiators of the basic algorithm are active and the noninitiators are passive. The control algorithm is, moreover, interested in send and receive events, to determine whether there are basic messages under way. As for internal events, it is only interested in those that change a process state from active to passive. So the abstract view of the control algorithm on states of processes with regard to the basic algorithm is as follows.

![](images/c3fa50ff39e41c9d8924fcac56eb038baa229a33617bc68fd9636dfd957f6921.jpg)

Correctness of the termination detection problem means (1) if the execution terminates, this is eventually detected, and (2) when termination is detected, the execution indeed terminated at some point in the past.

We will consider termination detection techniques based on maintaining trees of active processes (section 6.1), waves tagged with logical clock values (section 6.2), token-based traversal (section 6.3), and dividing a fixed amount of weight between the active processes and basic messages in transit (sections 6.4 and 6.5).

# 6.1 Dijkstra-Scholten Algorithm

The Dijkstra-Scholten algorithm is a termination detection algorithm for centralized basic algorithms on undirected networks. The idea is to build a tree, rooted in the initiator of the basic algorithm, that contains all active processes, and passive ones that have active descendants in the tree. If a basic message from a process $p$ makes a process $q$ active, then $q$ becomes a child of $p$ in the tree. A process can quit the tree only if it is passive and has no children left in the tree. In that case, it informs its parent that it is no longer a child. Termination is detected by the initiator when the tree has disappeared.

To be more precise, initially the tree $T$ consists of only the initiator. Each process $p$ maintains a child counter $c c _ { p }$ that estimates from above (1) its number of children in $T$ and (2) the number of basic messages $p$ sent that are still in transit. Initially, this counter is zero at all processes. The control algorithm works as follows. When a process $p$ sends a basic message $m$ , it increases $c c _ { p }$ by 1. When the message arrives at its destination $q$ , either $q$ joins $T$ with parent $p$ if $q$ was not yet in $T$ , or otherwise $q$ sends an acknowledgment to $p$ that it is not a new child. Upon receiving an acknowledgment, $p$ decreases $c c _ { p }$ by 1. When a process in $T$ is passive and its counter is zero, it quits $T$ . When a noninitiator quits $T$ , it sends an acknowledgment to its parent that it is no longer its child. Finally, when the initiator quits $T$ , it calls Announce.

Example 6.1 We consider one possible computation of a basic algorithm supplied with the Dijkstra-Scholten algorithm on an undirected ring of three processes $p _ { 0 } , q$ , and $r$ .

At the start, the initiator $p _ { 0 }$ sends basic messages to $q$ and $r$ ; it sets $c c _ { p _ { 0 } }$ to 2. Upon receipt of these messages, $q$ and $r$ both become active and join $T$ with parent $p _ { 0 }$ .   
$q$ sends a basic message to $r$ ; it sets $c c _ { q }$ to 1. Upon receipt of this message, $r$ sends back an acknowledgment, so $q$ decreases $c c _ { q }$ to 0.   
$p _ { 0 }$ becomes passive. (Since $c c _ { p _ { 0 } } = 2$ , $p$ remains in $T$ .)   
$r$ becomes passive. Since $c c _ { r } = 0$ , $r$ sends an acknowledgment to its parent $p _ { 0 }$ , so $p _ { 0 }$ decreases $c c _ { p _ { 0 } }$ to 1. $q$ sends a basic message to $r$ ; it sets $c c _ { q }$ to 1.   
$q$ becomes passive. (Since $c c _ { q } = 1$ , it remains in $T$ .)   
Note that all three processes are now passive, but there is still a basic message traveling from $q$ to $r$ . Upon receipt of this message, $r$ becomes active again and joins $T$ with parent $q$ .   
$r$ becomes passive. Since $c c _ { r } = 0$ , $r$ sends an acknowledgment to its parent $q$ , so $q$ decreases $c c _ { q }$ to 0. Since $q$ is passive and $c c _ { q } = 0$ , $q$ sends an acknowledgment to its parent $p _ { 0 }$ , so $p _ { 0 }$ decreases $c c _ { p _ { 0 } }$ to 0. Since $p _ { 0 }$ is passive and $c c _ { p _ { 0 } } = 0$ , $p _ { 0 }$ calls Announce.

When all processes have become passive and all basic messages have been acknowledged, clearly the tree $T$ will eventually disappear, after which the initiator will call Announce. Conversely, active processes and processes that sent a basic message that is still in transit are guaranteed to be in $T$ , which implies that the initiator will only call Announce when the basic algorithm has terminated.

The Shavit-Francez algorithm generalizes the Dijkstra-Scholten algorithm to decentralized basic algorithms. The idea is to maintain not one tree but a forest of disjoint trees, one for each initiator. Initially, each initiator constitutes a tree in the forest. A process can only join a tree if it is not yet in a tree in the forest. For the rest, the algorithm proceeds exactly as the Dijkstra-Scholten algorithm. The only distinction is that when an initiator detects that its tree has disappeared, it cannot immediately call Announce. Instead, the initiator starts a wave, tagged with its ID, in which only processes that are not in a tree participate. The decide event of such a wave calls Announce. If a wave does not complete, this is not a problem, because then another initiator for which the tree has not yet disappeared will start a subsequent wave. And a last tree to disappear is guaranteed to start a wave that will complete.

Example 6.2 We consider one possible computation of a basic algorithm supplied with the Shavit-Francez algorithm on an undirected ring of three processes $p , q$ , and $r$ .

At the start, the initiators $p$ and $q$ both send a basic message to $r$ ; they set $c c _ { p }$ and $c c _ { q }$ to 1. Next, $p$ and $q$ become passive.   
Upon receipt of the basic message from $p$ , $r$ becomes active and makes $p$ its parent. Next, $r$ receives the basic message from $q$ and sends back an acknowledgment, which causes $q$ to decrease $c c _ { q }$ to 0. Since $q$ became passive as the root of a tree and $c c _ { q } = 0$ , it starts a wave. This wave does not complete, because $p$ and $r$ refuse to participate.   
$r$ sends a basic message to $q$ ; it sets $c c _ { r }$ to 1. Next, $r$ becomes passive.   
Upon receipt of the basic message from $r$ , $q$ becomes active and makes $r$ its parent. Next, $q$ becomes passive and sends an acknowledgment to its parent $r$ , which causes $r$ to decrease $c c _ { r }$ to 0.   
Since $r$ is passive and $c c _ { r } = 0$ , it sends an acknowledgment to its parent $p$ , which causes $p$ to decrease $c c _ { p }$ to 0.   
Since $p$ became passive as the root of a tree and $c c _ { p } = 0$ , it starts a wave. This wave completes, so $p$ calls Announce.

# 6.2 Rana’s Algorithm

Rana’s algorithm detects termination of decentralized basic algorithms on undirected networks. It exploits waves that carry a logical clock value (cf. section 2.2). Each basic message is acknowledged, so that a process can determine whether each basic message it sent has reached its destination.

To understand Rana’s algorithm, it is helpful first to consider an incorrect termination detection algorithm, which uses waves without clock values. Let a process become quiet if (1) it is passive and (2) all the basic messages it sent have been acknowledged. Then it starts a wave, tagged with its ID. Only quiet processes take part in this wave. If a wave completes, its initiator calls Announce. Note that there can be multiple concurrent waves; each process must keep track of its state in each of these waves.

The problem with this termination detection algorithm is expressed by the following scenario. Let an active process $q$ that was not yet visited by some wave send a basic message to a quiet process $p$ that already took part in the wave, making $p$ active again. Next, $q$ receives $p$ ’s acknowledgment, becomes quiet, and takes part in the wave. Then the wave can complete while $p$ is active.

To avoid this scenario, processes maintain a logical time stamp, which initially is zero. As noted, each basic message is acknowledged, and a process becomes quiet if (1) it is passive and (2) all the basic messages it sent have been acknowledged. Then it starts a wave, tagged with its ID and its time stamp t. Upon receipt such a wave message pushes the time stamp of the receiver $p$ to the maximum of $p$ ’s current time stamp and t. Moreover, each acknowledgement carries the time stamp $t$ of its sender, and upon receipt pushes the time stamp of the receiver $q$ to the maximum of $q$ ’s current time stamp and $t + 1$ . Only quiet processes that have been quiet from some logical time $\leq t$ onward take part in this wave. If a wave completes, its initiator calls Announce.

Let us revisit the problematic scenario, but now for Rana’s algorithm. When $p$ is visited by the wave, its clock time becomes at least the time stamp of the wave. Therefore, the acknowledgment from $p$ sets $q$ ’s time stamp to beyond the time stamp of the wave. Hence, $q$ will refuse to take part in the wave.

Example 6.3 We consider one possible computation of a basic algorithm supplied with Rana’s algorithm, using logical time stamps, on an undirected ring of three processes $p , q$ , and $r$ .

Initially, $p , q$ , and $r$ all have logical time 0, and only $p$ is active. It sends basic messages $m _ { 1 }$ to $q$ and $m _ { 2 }$ to $r$ . The corresponding receive events of these messages make $q$ and $r$ active. Next, they send acknowledgments $\left. a _ { 1 } , 0 \right.$ and $\left. { a _ { 2 } , 0 } \right.$ , respectively, to $p$ .   
$p$ and $q$ , ,become passive. Moreover, $p$ receives both acknowledgments, setting its time to 1. Next, $p$ and $q$ both start a wave, tagged with 1 and 0, respectively. The wave of $p$ first visits $q$ , setting its time to $1 ; q$ takes part in the wave, because it is quiet from time 0 onward. The wave of $q$ first visits $r$ , which refuses to take part in the wave, because it is active.   
$r$ sends a basic message $m _ { 3 }$ to $q$ . Upon receipt of this message, $q$ becomes active and sends back an acknowledgment $\left. { a _ { 3 } , 1 } \right.$ . When $r$ receives this acknowledgment, its clock value becomes 2.   
$q$ and $r$ ,become passive. Next, $r$ refuses to take part in $p$ ’s wave, because $r$ is quiet from time 2 onward, while the wave is tagged with 1.   
$q$ and $r$ both start a wave, tagged with 1 and 2, respectively. The wave of $r$ completes, and $r$ calls Announce.

We argue that Rana’s algorithm is a correct termination detection algorithm. When the basic algorithm has terminated, Rana’s algorithm will eventually call Announce. Because each process eventually becomes quiet, when all the basic messages it sent have been acknowledged; and when a process becomes quiet, it starts a wave. Suppose a wave, tagged with some time stamp $t$ , does not complete. Then some process does not take part in the wave, which means that at some time $\geq t$ it is not quiet. When that process becomes quiet, it will start another wave, tagged with some $t ^ { \prime } \geq t$ . This implies that when all processes have become quiet, eventually some wave, carrying the largest time stamp among all waves, is guaranteed to complete.

Conversely, when Rana’s algorithm calls Announce, the basic algorithm has terminated. Let a wave complete. Suppose, toward a contradiction, that at that moment the basic algorithm has not terminated. Then some process is active, or some basic message is in transit. Since only quiet processes take part in a wave, such a situation can arise only if a quiet process $p$ was first visited by the wave and then made active again by a basic message $m$ from a process $q$ that was not yet visited by the wave. Note that $q$ can take part in the wave only after it has received an acknowledgment for $m$ from $p$ . Let the wave be tagged with time stamp $t$ . When $p$ takes part in the wave, its logical time becomes at least t. So the acknowledgment from $p$ to $q$ sets the logical time of $q$ to a value greater than $t$ . However, this means that $q$ is not quiet from a logical time $\leq t$ , so it cannot take part in the wave. This contradicts the fact that the wave completes. So at the moment the wave completes, the basic algorithm must have terminated.

# 6.3 Safra’s Algorithm

Safra’s algorithm is a traversal-based termination detection algorithm. The initiator of the control algorithm sends out a token that visits every process in the network. A process can only forward the token when it is passive. When the token returns to the initiator, it is decided on the basis of information in the token whether the basic algorithm has terminated. If not, the token is sent out again. Although Safra’s algorithm is centralized, the basic algorithm can be decentralized. The network can be directed. Note that a traversal of the entire network is always feasible, owing to the fact that networks are assumed to be strongly connected.

There are two complications. First, it must be determined whether there are basic messages in transit. In the case of a directed network, there is no simple acknowledgment scheme for basic messages. The second complication is that a traversal of passive processes does not guarantee termination. A traversal-based algorithm can give rise to an execution similar to the counterexample to the flawed termination detection algorithm presented at the start of section 6.2. An active process $q$ may make a passive process $p$ that was already visited by the token active again, after which $q$ becomes passive and forwards the token.

To cope with these complications, in Safra’s algorithm, every process maintains a counter of type integer; initially it is zero. At each outgoing or incoming basic message, the counter is increased or decreased, respectively. During each round trip, the token carries the sum of the counters of the processes it has traversed.

At any time, the sum of the counters of all processes in the network is nonnegative, and it is zero if and only if no basic message is in transit. Still, the token may compute a negative sum for a round trip if a passive process $p$ that already forwarded the token receives a basic message, becomes active, and sends basic messages that are received by a process $q$ before this same token arrives. Note that then the receipt of these messages at $q$ is accounted for in the token, but not their sending at $p$ .

This scenario is dealt with by coloring processes black after receiving a basic message. Initially, all processes are white. When the initiator of the control algorithm becomes passive, it sends a white token, carrying sum value zero, and the initiator becomes white. A process that receives the token waits until it is passive and then adds its counter value to the sum value of the token. A white process leaves the color of the token unchanged. A black process colors the token black, while the process itself becomes white. The token will then remain black for the rest of the round trip. If the process is a noninitiator, it forwards the token. If it is the initiator, it checks whether the token is white and carries sum value zero. If so, then the initiator calls Announce; if not, then it sends out a white token again, carrying sum value zero.

Example 6.4 We consider one possible computation of a basic algorithm supplied with Safra’s algorithm on the following directed network.

![](images/86e50ea1a9c8568e9197090c24f58b5b1f415bf6c9371addaeb34a27285e3405.jpg)

Initially, the token is at the initiator $p _ { 0 }$ of the control algorithm, only $s$ is active, all processes are white with counter 0, and there are no messages in transit. First, $s$ sends a basic message $m$ to $q$ , setting the counter of $s$ to 1. Now $s$ becomes passive. The token travels around the network and returns to $p _ { 0 }$ , white with sum 1. Next, the token travels on from $p _ { 0 }$ via $q$ to $r$ , white with sum 0. The message $m$ travels to $q$ and back to $s$ , making them active and black, with counter 0. Now $s$ becomes passive and the token travels from $r$ via $s$ to $p _ { 0 }$ , black with sum 0. Note that $s$ becomes white. Finally, $q$ becomes passive, and after two more round trips of the token (one round trip is needed to color $q$ white), $p _ { 0 }$ calls Announce.

When there are no basic messages in transit, the counters of the processes sum to zero. When, moreover, all processes have become passive, the token will color them all white. So when the basic algorithm has terminated, the token will eventually return to the initiator colored white and with sum value zero, after which the initiator calls Announce. Conversely, suppose a token returns to the initiator colored white and with sum value zero. This token was only forwarded by processes while they were passive and white. The fact that the token is white implies that each receipt of a basic message that is included in the sum value of the token occurred during an earlier token round, so that the sending of this message is also included in this sum value. So, since the token has sum value zero, it follows that no basic messages are in transit and no process can be made active after the token’s visit. Hence, the basic algorithm has terminated.

An optimization of Safra’s algorithm does away with black tokens. Instead, when a black process $p$ holds the token, it dismisses the token. As soon as $p$ is passive, it becomes white and sends a fresh token, carrying sum value zero and tagged with $p$ ’s ID. Suppose the token completes the round trip, i.e., it reaches $p$ tagged with $p$ . As soon as $p$ is passive, it checks whether $p$ is white and the token’s sum value is zero. If so, $p$ calls Announce. Otherwise $p$ dismisses the token, becomes white, and sends a fresh token, as explained earlier.

# 6.4 Weight Throwing

In weight-throwing termination detection, for centralized basic algorithms on directed networks, the initiator is given a certain amount of weight. During a computation, this weight is divided among active processes and basic messages in transit. Crucially, the total amount of weight in the entire network must stay unchanged during the computation. Every time a basic message is sent, the sender transfers some (but not all) of its weight to the message. And every time a basic message is received, the receiver adds the weight in this message to its own weight. When a noninitiator becomes passive, it returns its weight to the initiator in a control message (with control messages via a sink tree rooted in the initiator). When the initiator is passive and has regained its original weight, it calls Announce.

Example 6.5 We consider one possible computation of a basic algorithm supplied with the weight-throwing algorithm on an undirected ring of three processes $p _ { 0 } , q$ , and $r$ .

At the start, the initiator $p _ { 0 }$ has weight 12. It sends basic messages to $q$ and $r$ , with weights 6 and 3, respectively, and reduces its own weight to 3. Upon receipt of these messages, $q$ and $r$ become active, with weights 6 and 3.   
$q$ sends a basic message to $r$ , with weight 3, and reduces its own weight to 3. Upon receipt of this message, $r$ increases its weight to 6. $p _ { 0 }$ becomes passive. (Since it has weight less than 12, it does not yet call Announce.)   
$r$ becomes passive and sends a control message to $p _ { 0 }$ , returning its weight 6. Upon receipt of this message, $p _ { 0 }$ increases its weight to 9.   
$q$ sends a basic message to $r$ , with weight 1 5, and reduces its own weight to 1 5.   
$q$ .becomes passive and sends a control message to $p _ { 0 }$ ., returning its weight 1 5. Upon receipt of this message, $p _ { 0 }$ increases its weight to 10 5.   
.Note that all three processes are now passive, but there is still a message traveling from $q$ to $r$ . Upon receipt of this message, $r$ becomes active again, with weight 1 5.   
$r$ becomes passive again. It sends a control message to $p _ { 0 }$ ., returning its weight 1 5. Upon receipt of this message, $p _ { 0 }$ increases its weight to 12. Since $p _ { 0 }$ is passive, it calls Announce.

When all processes have become passive and there are no basic messages in transit, clearly all weight will eventually be returned to the initiator, which will then call Announce. Conversely, since all active processes and basic messages carry some weight, it is guaranteed that the initiator detects termination only when all processes are passive and there are no basic messages in transit.

The Achilles’ heel of this simple and effective termination detection scheme is underflow: the weight at a process can become too small to be divided further. Three solutions have been proposed for this problem.

A first solution is that a process $p$ where underflow occurs gives itself extra weight. If $p$ is a noninitiator, it must send a control message to the initiator that more weight has been introduced in the system or else the initiator could call Announce prematurely. To avoid race conditions, $p$ must wait for an acknowledgment from the initiator before it can continue sending basic messages. Otherwise the initiator could regain its original weight before the control message from $p$ has reached it.

A second solution is that $p$ starts a weight-throwing termination detection subcall. Then $p$ only returns its weight to the initiator when it has become passive and its subcall has terminated. The weights originating from the initiator and from $p$ must be recorded separately at the processes as well as in the basic messages.

A third solution is that each process $p$ maintains its weight by a counter $c r e d i t _ { p }$ , where intuitively $p$ ’s weight is $2 ^ { - c r e d i t _ { p } }$ . Initially, credit $_ p _ { 0 } = 0$ at the initiator $p _ { 0 }$ and $c r e d i t _ { q } = \infty$ at all noninitiators $q$ . An (active) process $p$ that sends a basic message $m$ increases credit $\dot { p }$ by 1, indicating $p$ ’s weight is halved, and attaches this increased value of $c r e d i t _ { p }$ to $m$ , so that the other half of $p$ ’s weight is donated to $m$ . A passive process $q$ that receives a basic message with credit $k$ becomes active with $c r e d i t _ { q } = k$ . An active process that receives a basic message returns the weight in this message to the initiator when it becomes passive. As before, the initiator calls Announce when it has regained all weight and is passive. Weight returned to the initiator cannot be reused because at each active process the weight must be a power of two. But since weight is recorded in credit variables, which grow in a linear fashion with the number of basic messages, this is not a serious issue.

# 6.5 Fault-Tolerant Weight Throwing

As in section 3.3 on rollback recovery, we now turn our attention to the situation where processes may crash. Here this means they stop executing unexpectedly and never resume execution; this topic will be studied in depth in chapter 12. We adapt the weight-throwing algorithm such that it can cope with crash failures.

It is assumed the network topology is complete, so that strong connectedness is always preserved after crash failures. This assumption is commonly made when considering fault-tolerant distributed algorithms, as it allows one to abstract away from the possibility that the network may be divided into disconnected components that start behaving independently. In practice it is often sufficient to guarantee that if strong connectedness of the network is lost after a crash, it can always be reestablished, typically by creating a new channel. Furthermore, as in section 3.3, each process is assumed to own a failure detector that is complete and strongly accurate. This means that eventually it detects every crash failure and no process is ever falsely suspected of having crashed; see section 12.3 for an in-depth treatment of such devices.

Inevitably termination may be announced while a basic message sent by a crashed process is in transit. Therefore passive processes should never become active by the receipt of a basic message from a process they know has crashed. An execution of the basic algorithm has terminated if all alive processes are passive and for all basic messages in transit, the destination process either crashed or knows that the sender crashed.

The possibility of crash failures poses three serious problems to the weight-throwing algorithm. First, when a process crashes, this process or a basic message traveling to it may hold some weight, which can then no longer be recovered by the initiator $p _ { 0 }$ . To cope with this situation, when $p _ { 0 }$ detects a crash failure, it initiates a run of a snapshot algorithm to account for the weight still present at the live processes and basic messages in transit. We employ the Lai-Yang algorithm from section 3.2 for this purpose. Each live process $q$ reports the weight in its local snapshot to $p _ { 0 }$ , including the weights of basic messages in the states of its incoming channels rq for which $r$ is alive. The initiator $p _ { 0 }$ waits until every live process has reported its weight and then determines the total amount of weight in the network. If during a run of the snapshot algorithm $p _ { 0 }$ detects a new crash, it starts a new run of the snapshot algorithm. Either $p _ { 0 }$ must wait until the current run has completed or control messages of different runs of the snapshot algorithm must be distinguished by means of a sequence number. If a process $q$ has reported its local snapshot to $p _ { 0 }$ while knowing that another process $r$ crashed and later receives a basic message $m$ from $r$ , then $q$ must ignore $m$ if it is passive and must in any case discard the weight in $m$ . In the case of underflow, a process can attribute extra weight to itself just before reporting its local snapshot to $p _ { 0 }$ ; this extra weight is then taken into account in the snapshot.

The second problem is that, at the start of a snapshot, the initiator $p _ { 0 }$ may know that a process $r$ has crashed while a live noninitiator $q$ does not. Then $q$ may report its local snapshot to $p _ { 0 }$ and later send a basic message $m$ to $r$ . When eventually $q$ ’s failure detector reports that $r$ has crashed, $q$ cannot figure out whether the weight of $m$ has been lost. If the weight is indeed lost and no further crashes happen, $p _ { 0 }$ may never realize that the total amount of weight in the network has been reduced. To avoid this situation, $p _ { 0 }$ informs all live noninitiators during a snapshot which processes have crashed according to $p _ { 0 }$ ’s failure detector.

The third problem is that the initiator of the basic algorithm, which is responsible for announcing termination, may crash. Therefore, the processes in the network are enumerated: $p _ { 0 } , . . . , p _ { N - 1 }$ , with $p _ { 0 }$ the initiator of the basic algorithm. When a process $p _ { i + 1 }$ discovers that all processes $p _ { j }$ , . .with $j \le i$ have crashed, it becomes the leader, meaning that it takes responsibility for initiating snapshots, recovering the weight in the network, and announcing termination. (We note that this is not an election algorithm according to the definition that will be presented at the start of chapter 9, because processes do not have the same local election algorithm, as it depends on their process IDs.) Each process $q$ considers as leader the process with the smallest process ID that is still alive according to $q$ ’s failure detector. When $p _ { i + 1 }$ becomes the new leader, a crash has occurred, so $p _ { i + 1 }$ initiates a snapshot and thus gets an accurate view of the weight in the network.

Example 6.6 Let the fault-tolerant weight-throwing algorithm run on a network of three active processes $p _ { 0 }$ , $p _ { 1 }$ , and $p _ { 2 }$ . Suppose $p _ { 1 }$ sends a basic message $m _ { 1 }$ to $p _ { 0 }$ , while $p _ { 2 }$ crashes after sending a basic message $m _ { 2 }$ to $p _ { 1 }$ . When the failure detector of the initiator $p _ { 0 }$ detects this crash, $p _ { 0 }$ starts a snapshot by taking a local snapshot and sending a control message to $p _ { 1 }$ . When $p _ { 1 }$ receives this message, it takes a local snapshot, determines that the incoming channel from $p _ { 0 }$ is empty, and sends control messages to $p _ { 0 }$ and $p _ { 2 }$ . Next, the failure detector of $p _ { 1 }$ detects that $p _ { 2 }$ crashed, so $p _ { 1 }$ no longer waits for a control message from $p _ { 2 }$ , decides that the incoming channel from $p _ { 2 }$ is empty, and reports its own weight to $p _ { 0 }$ . Later $m _ { 2 }$ arrives at $p _ { 1 }$ , which discards the weight in this basic message. When $p _ { 0 }$ receives the control message from $p _ { 1 }$ , it determines that this incoming channel contains a basic message and it waits for $m _ { 1 }$ to arrive to determine the snapshot of this channel. Finally, $p _ { 0 }$ receives the local snapshot of $p _ { 1 }$ and determines as the total weight in the network the sum of the weights at $p _ { 0 }$ and $p _ { 1 }$ , which includes the weight in $m _ { 1 }$ .

# Bibliographical notes

The Dijkstra-Scholten algorithm originates from [36], and the Shavit-Francez algorithm comes from [107]. Rana’s algorithm stems from [100]. Safra’s algorithm was presented in [35]. Weight throwing was proposed independently in [78] and in [57], and its fault-tolerant variant in [121].

# 6.6 Exercises

Exercise 6.1 Let the Dijkstra-Scholten algorithm be employed to detect termination of some centralized basic algorithm on an acyclic undirected network of three processes $p _ { 0 } , q$ , and $r$ . Give a computation of the basic algorithm in which process $q$ has parent $p _ { 0 }$ in the Dijkstra-Scholten tree while $q$ was made active for the last time by $r$ .

Exercise 6.2 [117] How much time does the Dijkstra-Scholten algorithm need at most to call Announce after the basic algorithm has terminated?

Exercise 6.3 Give a computation of the Shavit-Francez algorithm with two initiators, in which one of the initiators becomes active again after having become passive, and both initiators concurrently call Announce.

Exercise 6.4 Consider the following computation of a decentralized basic algorithm on an undirected ring of three processes $p , q$ , and $r$ , with $p$ and $q$ initiators. Let $p$ send messages to $q$ and $r$ and become passive, while $q$ sends a message to $r _ { \cdot }$ . When $q$ receives $p$ ’s message, it also becomes passive. After receiving the messages first from $p$ and then from $q$ , $r$ sends a message to both $p$ and $q$ and becomes passive. After receiving the message from $r$ , $p$ and $q$ send a message to each other and after receiving these messages become passive.

Add the following termination detection algorithms on top of the basic algorithm, and in each case extend the basic computation with control messages to explain how termination is detected:

(a) The Shavit-Francez algorithm.   
(b) Rana’s algorithm.   
(c) Safra’s algorithm, with $p$ as initiator of this control algorithm.

Exercise 6.5 Let Rana’s algorithm be applied to an always terminating basic algorithm. Suppose process $p$ at some point sends a basic message. Argue that even if $p$ is the first process to become permanently passive, there is always a possibility that ultimately only $p$ will call Announce.

Exercise 6.6 Suppose that Rana’s algorithm is adapted as follows: only quiet processes that have been quiet from some logical time $< t$ (instead of $\leq t$ ) onward can take part in a wave tagged with time stamp $t$ . Give an <example of a finite computation for which termination would not be detected.

Exercise 6.7 Suppose that in Rana’s algorithm, processes can take part in a wave tagged with $t$ if they have been quiet from a time $\leq t + 1$ . Give an example to show that then termination could be detected prematurely.

Exercise 6.8 Give an example to show that, in Safra’s algorithm, coloring sending processes black (instead of receiving ones) is incorrect.

Exercise 6.9 [61] In Safra’s algorithm, certain basic messages do not need to color the receiver black. Only messages that are sent after a token visits the sender and that are received before this same token visits the receiver need to be taken into account. Propose an optimization of Safra’s algorithm based on this observation.

Exercise 6.10 [117] Safra’s algorithm can be viewed as a snapshot algorithm. During every tour of the token, each process takes a local snapshot when it handles the token. In the constructed snapshot, all processes are passive, because the token is handled only by passive processes. Explain how the token’s sum value and color (when the token arrives back at the initiator) capture the consistency and channel states of the snapshot. In particular, argue that the following two claims are true:

1. If the token is white, the snapshot is consistent.   
2. If, moreover, the token’s sum value is zero, the basic algorithm has terminated.

Exercise 6.11 Explain how the Lai-Yang snapshot algorithm can be employed for a centralized termination detection algorithm.

Exercise 6.12 Consider weight-throwing termination detection, where in the case of underflow at a process $p$ , it gives itself extra weight and informs the initiator. Give an example to show that if $p$ does not wait for an acknowledgment from the initiator, then the initiator could prematurely detect termination.

Exercise 6.13 Consider the weight-throwing termination detection algorithm with the counter $c r e d i t _ { p }$ for recording weight, to avoid underflow. Why does it make sense for an active process that receives a basic message to not return the weight in this message to the initiator immediately, but only after it has become passive?

Exercise 6.14 Propose an adaptation of the weight-throwing termination detection algorithm that works for decentralized basic algorithms.

Exercise 6.15 Explain why in a setting where processes can crash, the following two definitions when an execution of a basic algorithm has terminated are flawed.

(a) All alive processes are passive and no basic messages are in transit in the channels.   
(b) All alive processes are passive and the only basic messages in transit are from processes that have crashed.

Exercise 6.16 Consider fault-tolerant weight-throwing termination detection. Suppose a process $p$ reports its local snapshot to the leader while knowing another process $q$ has crashed, and later $p$ receives a basic message from $q$ . What could go wrong if $p$ added the weight in this message to its own weight?

Exercise 6.17 Consider fault-tolerant weight-throwing termination detection. Suppose processes $p$ and $q$ report their local snapshots to the leader, where $p$ knows that another process $r$ has crashed while $q$ does not. Explain why in this case the leader will start a new run of the snapshot algorithm.

Exercise 6.18 [61] Develop a fault-tolerant variant of Safra’s algorithm for complete networks, in the presence of a complete and strongly accurate failure detector. If a process crashes, its predecessor sends a backup token to its new successor, to avoid that the token may be lost. The counters at the processes and the sum in the token are split into $N$ parts for the different processes, to discard message counts for crashed processes.

# Garbage Collection

Each process is provided with memory to store, for instance, its local state. An object is the content of a certain memory range on a process. An object can contain references to other objects, possibly in the memory of other processes. A reference to an object name makes it possible to access this object remotely, instead of having to transmit the object across the network. A reference to a local object, which is located at the same process, is called a pointer, to distinguish it from a remote procedure call to an object located at another process. A message may contain references, if the sender desires the receiver to perform method calls to these objects. If multiple objects at a process $p$ hold references to the same remote object $o$ , $p$ still maintains only one $o$ -reference. Only when no object at $p$ has an $o$ -reference anymore, can $p$ delete its $o$ -reference.

A root object is mentioned in the main function of a process, while a nonroot object is supposed to be used, directly or indirectly, in method calls of root objects. An object needs to be kept in memory only if it is accessible by navigating from a root object. An object is garbage if it cannot be accessed from any root object. Garbage collection aims to automatically detect and reclaim inaccessible memory objects in order to free up memory space. This is of great practical importance to avoid that such garbage clogs up the available memory. Of course, it should not be allowed to create a reference or pointer to an object labeled as garbage.

The two main techniques for garbage collection are reference counting and tracing. Reference counting, discussed in section 7.1, counts the number of references to an object. Tracing, discussed in section 7.3, marks all objects reachable from the root objects. In section 7.2, it is shown there is a strong link between garbage collection and termination detection, which was discussed in the previous chapter.

# 7.1 Reference Counting

Reference counting is based on keeping track of the number of references to a nonroot object in memory; if it drops to zero and there are no pointers to the object, then the object is garbage.

An advantage of reference counting is that it can be easily performed at runtime, because counting can be done locally. A disadvantage is that cyclic garbage, meaning a cycle of references between garbage objects, is not detected. A separate technique must be added to try and detect such cycles. For instance, an object that is suspected of being part of cyclic garbage may be virtually deleted. That is, a separate set of trial reference counts is used to propagate the effects of this trial deletion: every outgoing link of the suspected object is trial deleted, and as a result the trial count at the destination object of the link is its current reference count minus 1; if as a result the trial count at an object becomes zero, it is also trial deleted, and so on. If in the end the trial count of the suspected object drops to zero, then this confirms that the object is garbage. In that case, it can be physically deleted.

The owner of an object $o$ , meaning the process where $o$ is located, can easily count the (local) pointers to $o$ . But, in a distributed setting, the challenge is to keep track of the number of (remote) $o$ -references during the execution of a (basic) distributed algorithm. We distinguish three operations in which processes build or delete a reference to an object $o$ :

Creation: The owner of $o$ sends an $o$ -pointer to another process.   
Duplication: A process that is not the owner of $o$ sends an $o$ -reference to another process.   
Deletion: An $o$ -reference is deleted because it has become obsolete.

Reference counting must take into account basic messages that duplicate a reference. Otherwise an object could be reclaimed prematurely if there are no pointers and references to it but a message is carrying a duplicated reference to this object. One solution is that a process wanting to duplicate a reference must first inform the object owner; the reference is duplicated only after the receipt of the owner’s acknowledgment. The drawback of this approach is high synchronization delays. We now discuss two different approaches to avoiding such delays.

# Indirect Reference Counting

One method to avoid having to inform the object owner when a reference is duplicated is to maintain a tree for each nonroot object, with the object at the root and the references to this object as the other nodes in the tree. Each reference keeps track of where it was duplicated or created from; that is, it stores its parent in the tree. The object and references are provided with a counter, estimating from above how many children they have in the tree: the counter at the object keeps track of how many references to the object have been created, while the counter at a reference keeps track of how many times the reference has been duplicated.

When a process receives a reference to a nonroot object but already holds a reference to or owns this object, it immediately sends back a decrement to decrease the counter at the sender. A deleted reference can be restored if a duplication or creation of this reference is received before its counter has become zero. Also in this case it immediately sends a decrement in reply. Hence a deleted reference that is still part of a tree does not switch to another tree.

When a duplicated (or created) reference has been deleted and its counter is zero, a decrement message is sent to the process from which it was duplicated (or to the object owner). When the counter of the nonroot object becomes zero and there are no pointers to it, the object can be reclaimed.

Example 7.1 We consider one possible computation with indirect reference counting on an undirected ring of three processes $p , q$ , and $r _ { \cdot }$ . Let $p$ hold one pointer to the nonroot object $o$ .

$p$ sends $o$ -references to $q$ and $r$ ; it sets its counter of created $o$ -references to 2. Upon receipt of these messages, $q$ and $r$ build an $o$ -reference.

$q$ sends an $o$ -reference to $r$ ; it increases its counter of duplicated $o$ -references to 1. Upon receipt of this message, $r$ sends back a decrement message to $q$ because it already holds an $o$ -reference. Upon receipt of this message, $q$ decreases its counter back to 0.   
$p$ deletes its $o$ -pointer. (Since its counter is 2, $o$ cannot yet be reclaimed by the garbage collector.) $r$ deletes its $o$ -reference. Since its counter is 0, $r$ sends a decrement message to $p$ , which causes $p$ to decrease its counter to 1.   
$q$ sends an $o$ -reference to $r$ ; it increases its counter to 1.   
$q$ deletes its $o$ -reference. (Since its counter is 1, $q$ does not yet send a decrement message to $p$ .) Note that there is no pointer or reference to $o$ , but there is still an $o$ -reference traveling from $q$ to $r$ . Upon receipt of this message, $r$ builds an $o$ -reference.   
$r$ deletes its $o$ -reference. Since its counter is 0, $r$ sends a decrement message to $q$ , which causes $q$ to decrease its counter to 0.   
Since $q$ holds no $o$ -reference and its counter is 0, it sends a decrement message to $p$ , which causes $p$ to decrease its counter to 0.   
Since $p$ holds no $o$ -pointer and its counter is 0, $o$ can be reclaimed by the garbage collector.

# Weighted Reference Counting

Another method to avoid having to inform the object owner when a reference is duplicated is to provide each nonroot object with a total weight. References are provided with a part of the weight of the object to which they refer. The object maintains a partial weight that was not yet handed out to references to the object. Initially, the partial weight of the object equals its total weight.

When a reference is created, the partial weight of the object is divided between the object and the reference. That is, the object owner gives some weight to the message responsible for creating this reference, and it deducts this weight from the partial weight of the object. When the message arrives at its destination, either the reference is created with the weight of the message, if the process does not yet hold a reference to this object, or otherwise the weight of the message is added to this reference. Likewise, when a reference is duplicated, the weight of the reference is divided between itself and the copy (except if the reference happens to be duplicated to the object owner, in which case the weight is subtracted from the total weight of the object). When a reference is deleted, the object owner is notified and the weight of the deleted reference is subtracted from the total weight of the object. When the total weight of the object becomes equal to its partial weight and there are no pointers to the object, it can be reclaimed.

Example 7.2 We consider one possible computation with weighted reference counting on an undirected ring of three processes $p , q$ , and $r$ . Let $p$ hold one pointer to the nonroot object $o$ , which has total and partial weights 12.

$p$ sends $o$ -references to $q$ and $r$ , with weights 6 and 3, respectively, and reduces the partial weight of $o$ to 3. Upon receipt of these messages, $q$ and $r$ build an $o$ -reference, with weights 6 and 3.   
$q$ sends an $o$ -reference to $r$ , with weight 3, and reduces the weight of its $o$ -reference to 3. Upon receipt of this message, $r$ increases the weight of its $o$ -reference to 6.   
$p$ deletes its $o$ -pointer. (Since the partial weight of $o$ is less than its total weight, $o$ cannot yet be reclaimed by the garbage collector.) $r$ deletes its $o$ -reference and sends a control message to $p$ with weight 6. Upon receipt of this message, $p$ decreases the total weight of $o$ to 6.   
$q$ sends an $o$ -reference to $r$ with weight 1 5 and decreases the weight of its $o$ -reference to 1 5. $q$ deletes its $o$ .-reference and sends a control message to $p$ .with weight 1 5. Upon receipt of this message, $p$ decreases the total weight of $o$ to 4 5.   
.Note that there is no pointer or reference to $o$ , but there is still an $o$ -reference traveling from $q$ to $r$ . Upon receipt of this message, $r$ builds an $o$ -reference with weight 1 5.   
$r$ deletes its $o$ -reference and sends a control message to $p$ .with weight 1 5. Upon receipt of this message, $p$ decreases the total weight of $o$ .to 3. Since the partial and total weights of $o$ are now equal, and $p$ holds no $o$ -pointer, $o$ can be reclaimed by the garbage collector.

Just as with weight-throwing termination detection, a drawback of weighted reference counting is the possibility of underflow: when the weight of a reference becomes too small to be divided further, it can no longer be duplicated. There are three possible solutions, similar to the solutions proposed for weight-throwing termination detection:

1. The reference increases its weight and tells the object owner to increase its total weight. An acknowledgment from the object owner to the reference is needed before it can be duplicated. 2. The process at which the underflow occurs creates an artificial object, with a reference to the original object. Duplicated references are then referenced to the artificial object, so that references to the original object become indirect. 3. Weights are of the form $2 ^ { - k }$ . A process attaches half its weight to a duplicated reference. A process that receives a reference it already holds, returns the weight of the received reference to the object owner.

# 7.2 Garbage Collection Implies Termination Detection

At first sight, garbage collection has little in common with termination detection, discussed in the previous chapter. Still, the garbage collection algorithms in the previous section may have reminded you of some of the termination detection algorithms discussed earlier. This is not a coincidence. It turns out that garbage collection algorithms can be transformed into (existing and new) termination detection algorithms. This works as follows. Given a basic algorithm, let each process $p$ host one artificial root object $O _ { p }$ . There is also a special nonroot object Z. Initially, only initiators $p$ hold a reference from $O _ { p }$ to $Z$ . Each basic message carries a duplication of the $Z$ -reference. When a process becomes passive, it deletes its $Z$ -reference. When a process becomes active, it is told to duplicate a $Z$ -reference, owing to the fact that all basic messages carry a $Z$ - reference.

The basic algorithm is terminated if and only if $Z$ is garbage. If all processes are passive and there are no messages in transit, then clearly there is no $Z$ -reference. And vice versa, if there is an active process or a message in transit, it holds (a duplication of) the $Z$ -reference.

This transformation turns indirect reference counting into Dijkstra-Scholten termination detection and weighted reference counting into a slight variation of weight-throwing termination detection (see exercise 7.5). Note that examples 7.1 and 7.2 are basically identical to examples 6.1 and 6.5, respectively, but in the context of garbage collection instead of termination detection.

# 7.3 Tracing

Tracing (also called mark-scan or mark-and-sweep) garbage collection consists of two phases. The first phase consists of a traversal of all accessible objects in memory, starting from the root objects; the accessible objects are marked. In the second phase, all unmarked objects are reclaimed.

An advantage of this approach, compared to reference counting, is that it detects all garbage, including cyclic garbage. Drawbacks of tracing are that it tends to require taking a snapshot of the channel states, to catch references in transit, and freezing the basic execution, since a global scan of all reachable memory objects is performed. In spite of this, tracing is more widely used than reference counting, since it has become the method of choice for garbage collection within the programming language Java. Key to this success has been the division of objects into two generations.

There are two standard ways to perform the second phase of tracing, in which unmarked objects are reclaimed:

• Mark-copy: Copy all marked objects to contiguous empty memory space.   
• Mark-compact: Compact all marked objects in the current memory space.

Copying is significantly faster than compaction, because marked objects are copied without changing the memory structure. However, in the long run, mark-copy leads to a fragmentation of the memory space, be cause objects have a fixed place, while mark-compact clearly resolves such fragmentation.

In practice, most objects either can be reclaimed shortly after their creation or stay accessible for a very long time. This observation is exploited by generational garbage collection, in which objects are divided into two generations. Garbage in the young generation is collected frequently using mark-copy, while garbage in the old generation is collected sporadically using mark-compact. A newly created object starts in the young generation. If it stays accessible for a certain amount of time (or for a certain number of garbage collection runs), it is moved from the young generation to the old generation.

# Bibliographical notes

The technique for detecting cyclic garbage that was mentioned at the start of this chapter originates from [124]. Indirect reference counting was put forward in [98], and weighted reference counting was proposed independently in [15] and [126]. The derivation of termination detection algorithms from garbage collection algorithms was observed in [118]. Generational garbage collection stems from [74].

# 7.4 Exercises

Exercise 7.1 Give an example of cyclic garbage where trial deletion of one object on this cycle will not lead to detection by reference counting that this object is garbage.

Exercise 7.2 Consider the following computation of a basic algorithm on an undirected ring of size 3, with processes $p , q$ , and $r$ , where $p$ owns an object $o$ . Initially, there is one $o$ -pointer. First, $p$ sends a message to $q$ and $r$ , both containing a created $o$ -reference. Next, $p$ deletes the $o$ -pointer. When the message from $p$ arrives, $q$ and $r$ create an $o$ -reference. Now $q$ and $r$ send messages to each other, both of which contain a duplicated $o$ -reference, and delete their $o$ -references. When these messages arrive, $q$ and $r$ create an $o$ -reference again. Finally, $q$ and $r$ delete their $o$ -references.

Explain for each of the following two garbage collection algorithms how it is detected that $o$ has become garbage:

(a) Indirect reference counting.   
(b) Weighted reference counting.

Exercise 7.3 In weighted reference counting, why is underflow much more likely to happen than overflow of a reference counter?

Exercise 7.4 Consider solution 1 for dealing with underflow in weighted reference counting. Give an example to show that if the process where the weight is increased would not wait for an acknowledgment from the object owner, then the object owner could prematurely mark the object as garbage.

Exercise 7.5 Employ the technique from section 7.2 to derive termination detection algorithms for centralized basic algorithms.

(a) Show that indirect reference counting gives rise to Dijkstra-Scholten termination detection.   
(b) [118] Show that weighted reference counting gives rise to a variation of weight-throwing termination detection in which the initiator cannot reuse weight that was returned to it. Also take into account solution 1 for underflow.

Exercise 7.6 [119] Argue that every termination detection algorithm can be turned into a tracing garbage collection algorithm, by treating each memory object as an individual process.

Exercise 7.7 Suppose tracing garbage collection is performed on a running distributed system. Let $O _ { 1 }$ and $O _ { 2 }$ be root objects, with only $O _ { 2 }$ holding a reference to nonroot object $o$ . First, $O _ { 1 }$ builds a reference to $o$ . Next, $O _ { 2 }$ deletes its reference to $o$ . Show how tracing garbage collection could wrongly label $o$ as garbage.

Exercise 7.8 [12, 110] Consider the following on-the-fly tracing garbage collection algorithm. Let all memory objects be white.

(1) Color all root objects black.   
(2) For all black objects, color the white objects to which they have a pointer or reference black.   
(3) If white objects were colored black in step (2), repeat this step; otherwise, collect the white objects as garbage and make all remaining objects white.

When the basic algorithm creates a new pointer or reference, the object to which it points is colored black.

(a) Explain why this algorithm will not label the object $o$ from the previous exercise as garbage.   
(b) [118] Employ the technique from section 7.2 to derive a termination detection algorithm from this garbage collection algorithm.   
(c) What is still the Achilles’ heel of this approach?

# Routing

When a process wants to send a message to another process in the network that is not a direct neighbor, the message needs to be routed through the network. Effective routing algorithms are of vital importance, especially for the Internet, but also for e.g. city logistics.

Each process $q$ maintains a routing table, which stores for each destination $p \neq q$ the distance of $q$ to $p$ as well as a neighbor $r$ of $q$ : each message with destination $p$ that arrives at $q$ is passed on to $r _ { \cdot }$ . In this way, routing tables at processes establish a route from $q$ to $p$ . We consider weighted networks,, in which each channel $p q$ is provided with a positive weight weight $( p q )$ from $\mathbb { R } _ { > 0 }$ . We discuss algorithms that route messages via shortest >paths, meaning that the sum of the weights of the traversed weighted channels is minimal.

# 8.1 Chandy-Misra Algorithm

The Chandy-Misra algorithm is a centralized routing algorithm (also called a single-source shortest-path algorithm) for undirected networks. It computes a sink tree consisting of shortest paths to the initiator.

Each process $p$ maintains values $d i s t _ { p }$ and parentp, where $d i s t _ { p }$ is the length of the shortest known path from $p$ to the initiator, and paren $\dot { p }$ is the process after $p$ on this path. Initially, the variable dist at the initiator has value 0, $d i s t _ { p } = \infty$ (that is, infinity) for each noninitiator $p$ , and paren $_ p = \perp$ (that is, undefined) for all processes $p$ .

The algorithm starts with messages $\langle \mathbf { d i s t } , 0 \rangle$ , which the initiator sends to all its neighbors, informing them ,that the initiator knows a path to itself of distance 0.

When a process $p$ receives a message $\langle \mathbf { d i s t } , d \rangle$ from a neighbor $q$ , it checks whether $d + w e i g h t ( p q ) <$ ${ d i s t } _ { p }$ . If this is the case, then $p$ ,has found a shorter path to the initiator via $q$ , so it changes $d i s t _ { p }$ into $d +$ weigh $\cdot ( p q )$ and parentp into $q$ , and communicates the improved estimate to all neighbors except $q$ in the form of a message $\langle \mathbf { d i s i } , d i s t _ { p } \rangle$ . If not, then $p$ simply dismisses the incoming message from $q$ .

,A termination detection algorithm needs to be used on the side. For instance, one could employ the Dijkstra-Scholten algorithm (see section 6.1).

Example 8.1 We consider the longest possible computation of the Chandy-Misra algorithm on the following network with initiator $p$ .

$$
\frac { 1 } { ( 1 ) } - \frac { 1 } { ( 2 ) } - \frac { 1 } { ( 3 ) }
$$

Initially, $d i s t _ { p } = 0$ and $d i s t _ { q } = d i s t _ { r } = d i s t _ { s } = d i s t _ { t } = \infty$ , while parent $= \bot$ at all five processes.

$p$ sends $\langle \mathbf { d i s t } , 0 \rangle$ to $q$ and $r$ . When $p$ ,’s message arrives at $q , d i s t _ { q } \gets \frac { 1 } { 2 }$ and $p a r e n t _ { q } \gets p$ , and $q$ sends $\big \langle \mathbf { d i s t } , \frac { 1 } { 2 } \big \rangle$ to $r$ . When $q$ ’s message arrives at $r , d i s t _ { r } \gets 1$ and paren $t _ { r } \gets q$ , and $r$ sends $\mathbf { \Psi } ( \mathbf { d i s t } , 1 \rangle$ to $p , s$ , and $t$ . $p$ dismisses $r$ ’s message. When $r$ ’s message arrives at $\mathrm { s } , d i s t _ { s } \gets \frac { 9 } { 8 }$ and paren ${ \bf \Phi } _ { s } \gets r$ , and $s$ sends $\bigl \langle \mathbf { d i s t } , \frac { 9 } { 8 } \bigr \rangle$ to $t$ . When $s ^ { \th }$ ’s message arrives at $t .$ , $d i s t _ { t } \gets \frac { 5 } { 4 }$ and paren $_ t  s$ , and $t$ sends $\langle \mathbf { d i s t } , _ { 4 } ^ { 5 } \rangle$ to $r$ . $r$ dismisses $t ^ { \prime }$ ’s message. When r’s message arrives at $t$ , $d i s t _ { t } \gets \frac { 9 } { 8 }$ and $p a r e n t _ { t } \gets r$ , and $t$ sends $\bigl \langle \bigl \langle \mathrm { d i s t } , \frac { 9 } { 8 } \bigr \rangle$ to $s$ . $s$ dismisses $t ^ { : }$ ’s message. When $p$ ’s message (finally) arrives at $r , d i s t _ { r } \gets \frac { 1 } { 2 }$ and paren ${ \bf \dot { \boldsymbol { r } } }  { \boldsymbol { p } }$ , and $r$ sends $\langle \mathbf { d i s t } , \frac { 1 } { 2 } \rangle$ to $q , s ,$ , and $t$ . $q$ dismisses $r$ ’s message. When $r ^ { \mathrm { : } }$ ’s message arrives at $s$ $s , d i s t _ { s } \gets \frac { 5 } { 8 }$ and paren ${ \bf \underline { { \theta } } } _ { s } \gets r$ , and $s$ sends $\langle \mathbf { d i s t } , \mathbf { \Pi } _ { 8 } ^ { 5 } \rangle$ to $t$ . When $s ^ { \th }$ ’s message arrives at $t .$ , $\begin{array} { r } { d i s t _ { t } \gets \frac { 3 } { 4 } } \end{array}$ and paren ${ \bf \Phi } _ { t } \gets s$ , and $t$ sends $\langle \mathbf { d i s t } , _ { 4 } ^ { 3 } \rangle$ to $r$ . $r$ dismisses $t ^ { \prime }$ ’s message. When $r$ ’s message arrives at t, $d i s t _ { t } \gets \frac { 5 } { 8 }$ and $p a r e n t _ { t } \gets r$ , and $t$ sends $\langle \mathbf { d i s t } , \mathbf { \Pi } _ { 8 } ^ { 5 } \rangle$ to $s$ . – $s$ dismisses $t$ ’s message.

We argue that the Chandy-Misra algorithm computes shortest paths toward the initiator. A safety property of the algorithm is that any process $p$ with $d i s t _ { p } < \infty$ has a shortest path to the initiator with weight at most ${ d i s t } _ { p }$ <. This follows from the facts that this property holds initially and it is an invariant: if $p$ receives a message $\langle \mathbf { d i s t } , d \rangle$ from a neighbor $q$ , then there is a path from $p$ via $q$ to the initiator with weight at most $d + w e i g h t ( p q )$ , so (even) if $p$ changes $d i s t _ { p }$ into $d + w e i g h t ( p q )$ , the property is preserved. For each process $p , d i s t _ { p }$ will eventually attain the weight of a shortest path from $p$ to the initiator, which we argue by induction on the number of channels in such a path. The base case, where $p$ is the initiator, is trivial, because then $d i s t _ { p }$ is 0 from the start. In the inductive case, let a shortest path from $p$ to the initiator start with the channel $p q$ . By induction, eventually $d i s t _ { q }$ will attain the weight of a shortest path from $q$ to the initiator; this path cannot go via $p$ , because channels carry positive weights. So $q$ will send $\langle \mathbf { d i s t } , d i s t _ { q } \rangle$ to $p$ , and upon receipt of this message, $d i s t _ { p }$ will equal the weight of a shortest path from $p$ ,to the initiator. Finally, if $p$ is a noninitiator, then a shortest path from $p$ to the initiator goes via parentp, because parentp is updated at each improvement of $d i s t _ { p }$ .

The worst-case message complexity of the Chandy-Misra algorithm is exponential, since there can be exponentially many different cycle-free paths from a process to the initiator, which may be discovered in decreasing order of weight (see exercise 8.4). In the case of minimum-hop paths in unweighted networks (in other words, each channel has weight 1), the worst-case message complexity of computing shortest paths to all processes in the network drops down to $O ( N ^ { 2 } { \cdot } E )$ . For each process $p$ , the algorithm requires at most $O ( N \cdot E )$ messages to compute all shortest paths to $p$ : the longest cycle-free path has at most length $N - 1$ , so each process sends at most $N - 1$ messages to its neighbors. In the case of minimum-hop paths, the sink tree forms what is called a breadth-first search tree.

# 8.2 Merlin-Segall Algorithm

The Merlin-Segall algorithm is a centralized algorithm to compute all shortest paths to the initiator. The underlying idea is to bring structure to the Chandy-Misra algorithm by letting it proceed in rounds. In each round, distance messages a la Chandy-Misra flow up and down the sink tree, similarly as in the echo algo- \` rithm, and distance values are updated. At the end of each round, the sink tree is restructured. It assumes that the initiator knows (an upper bound on) the network size $N$ .

Initially (after round 0), the variable dist at the initiator has value 0, $d i s t _ { p } = \infty$ for each noninitiator $p$ , and the parentp values form a sink tree with the initiator as root. Such a sink tree can be built by means of a centralized wave algorithm from chapter 4.

Each round $> 0$ is started by the initiator, which sends the message $\langle \mathbf { d i s t } , 0 \rangle$ to its neighbors to infor >them that the initiator has a shortest path to itself of length 0.

Let a noninitiator $p$ receive a message $\langle \mathbf { d i s t } , d \rangle$ from a neighbor $q$ .

• If $d + w e i g h t ( p q ) < d i s t _ { p }$ , then $d i s t _ { p } \gets d + w e i g h t ( p q )$ (and $p$ stores $q$ as the future value for $p a r e n t _ { p }$ ).   
• If $q = p a r e n t _ { p }$ <, then $p$ sends $\langle \mathbf { d i s t } , d i s t _ { p } \rangle$ to its neighbors, except $q$ .

When $p$ has received a message from all its neighbors in the current round, it sends $\langle \mathbf { d i s t } , d i s t _ { p } \rangle$ to parentp and moves to the next round. If $p$ updated $d i s t _ { p }$ in the last round, then $p$ updates $p a r e n t _ { p }$ to the neighbor whose message is responsible for the current value of $d i s t _ { p }$ . The initiator starts a new round after it has received a message from all its neighbors in the current round.

After round $n \geq 0$ , for each process $p$ with a shortest path to the initiator that consists of $\leq n$ channels, ${ d i s t } _ { p }$ and parentp have achieved their ultimate values. This is easy to see by induction on $n$ . The base case $n = 0$ is trivial, because at the initiator the variables dist and parent have values 0 and $\perp$ , respectively, from the start. Now consider the inductive case: a noninitiator $p$ with a shortest path of $\leq n + 1$ channels to the initiator. Let $p q$ be the first channel in such a path. Then process $q$ has a shortest path of $\leq n$ channels to the initiator. By the induction hypothesis, after round $n$ , $d i s t _ { q }$ has obtained its ultimate value. So in round $n + 1$ , $p$ receives the message $\langle \mathbf { d i s t } , d i s t _ { q } \rangle$ from $q$ . Therefore, $d i s t _ { p }$ and parentp have achieved their ultimate values at the end of round $n + 1$ ,. Since shortest paths consist of at most $N - 1$ channels, the Merlin-Segall algorithm can terminate after round $N - 1$ .

Example 8.2 We consider one possible computation of the Merlin-Segall algorithm on the following complete undirected network. The original sink tree, after round 0, consists of the channels $q r , r p _ { 0 }$ , and $s p _ { 0 }$ .

![](images/1de022ad7497628697e58e6e8f8a65c79723ff1179ac26dcf4285449dc771773.jpg)

The computation we consider determines the correct sink tree toward the initiator $p _ { 0 }$ only at the end of round 3, because (1) there is a shortest path of length 3, (2) we start with a sink tree that has nothing in common with the correct sink tree, and (3) in every round we let messages in the opposite direction of the sink tree travel very quickly, so that processes send messages to their neighbors early on.

The five pictures that follow show the progression of the computation in round 1. Process names and channel weights have been omitted from these pictures. Messages that are depicted with a solid arrowhead are toward a parent. In the first picture, $p _ { 0 }$ has sent out messages $\langle \mathbf { d i s t } , 0 \rangle$ . In the second picture, $r$ and $s$ have received this message from their parent $p _ { 0 }$ ,, computed distances 5 and 4, and sent $\langle \mathbf { d i s t } , 5 \rangle$ and $\langle \mathbf { d i s t } , 4 \rangle$ , respectively, to their other neighbors. In the third picture, $q$ has received $\langle \mathbf { d i s t } , 5 \rangle$ from its parent $r$ , computed distance 8, and sent $\langle \mathbf { d i s t } , 8 \rangle$ to its other neighbors. In the fourth picture, $s$ has received $\langle \mathbf { d i s t } , 8 \rangle$ from $q$ and $\langle \mathbf { d i s t } , 5 \rangle$ from $r$ , sent $\langle \mathbf { d i s t } , 4 \rangle$ to its parent $p _ { 0 }$ , and made $p _ { 0 }$ its parent (again); moreover, $q$ ,has received $\langle \mathbf { d i s t } , 0 \rangle$ from $p _ { 0 }$ and $\langle \mathbf { d i s t } , 4 \rangle$ from $s$ , computed an improved distance 1, sent $\mathbf { \Psi } ( \mathbf { d i s t } , 1 \rangle$ to its parent $r$ , and made $p _ { 0 }$ its new parent. In the fifth picture, $r$ has received $\mathbf { \Psi } ( \mathbf { d i s t } , 1 \rangle$ from $q$ and $\langle \mathbf { d i s t } , 4 \rangle$ from $s$ , computed an improved distance 4, sent $\langle \mathbf { d i s t } , 4 \rangle$ to its parent $p _ { 0 }$ , and made $q$ ,its new parent. When the three messages traveling toward $p _ { 0 }$ have reached their destinations, round 2 is started.

![](images/02b3b6253e0087c5285d7ee1785ff760bbb49f08633cef196fdda3e1f3d805a9.jpg)

The depictions of the two other rounds are given without further explanations, as they are similar to those of round 1. The five pictures that follow show the progression of the computation in round 2.

![](images/5aa5ee4d0e26eec93ba3fe26dbef1c88eaace974315b4880e0609e1a5e997edf.jpg)

Finally, the five pictures that follow show the progression of the computation in round 3.

![](images/a051fa1af11dd3e4e01e38fe5581d6e6a972972ce0065756bd1bdf9b23091d40.jpg)

Now the computation has terminated. In the terminal configuration, the correct shortest paths toward $p _ { 0 }$ have been computed, leading from $r$ to $s$ to $q$ to $p _ { 0 }$ .

The message complexity of the Merlin-Segall algorithm is $\Theta \big ( N ^ { 2 } { \cdot } E \big )$ . For every root, the algorithm requires $( N - 1 ) { \cdot } 2 E$ messages, since in each of the $N - 1$ Θ rounds, two messages travel through each channel.

The Merlin-Segall algorithm can be adapted to make it robust against topology changes. When a tree edge fails or a new channel becomes operational that is part of a shortest path, the adjacent processes send a special control message toward the initiator via the sink tree. In case of a failed tree edge, a new sink tree toward the initiator is constructed. If the special control message meets a failed tree edge, it is discarded. This is no problem, because the other side of this tree edge already sends a control message toward the initiator. When the initiator receives this control message, it starts a new set of $N$ rounds, with a higher number. This number is attached to the messages in this run of the algorithm.

# 8.3 Toueg’s Algorithm

Toueg’s algorithm is a decentralized algorithm for undirected networks that generalizes the well-known Floyd-Warshall algorithm to a distributed setting. It is an all-pairs shortest-path algorithm, meaning that it computes a shortest path between any pair of processes. The idea behind the Floyd-Warshall algorithm is to compute, for each set $s$ of processes, a distance function $d ^ { S } ( p , q )$ denoting the length of a shortest path between $p$ and $q$ with all intermediate processes in S . Its value is $\infty$ if there is no such path. The following equations hold for all processes $p , q$ :

$$
\begin{array} { l } { { d ^ { 5 } ( p , p ) = 0 . } } \\ { { d ^ { \emptyset } ( p , q ) = w e i g h t ( p q ) \mathrm { i f } p \neq q \mathrm { a n d t h e r e ~ i s ~ a ~ c h a n n e l } p q . } } \\ { { d ^ { \emptyset } ( p , q ) = \infty \mathrm { i f } p \neq q \mathrm { a n d t h e r e ~ i s ~ n o ~ c h a n n e l } p q . } } \\ { { d ^ { S \cup \{ r \} } ( p , q ) = \operatorname* { m i n } \{ d ^ { S } ( p , r ) + d ^ { S } ( r , q ) , d ^ { S } ( p , q ) \} \mathrm { f o r ~ e a c h } r \not \in S . } } \end{array}
$$

The first equation is obvious. For the second and third equations, note that if $S = \emptyset$ , then a path between two distinct processes $p$ and $q$ with all intermediate processes in $s$ can only consist of a channel between $p$ and $q$ . The fourth equation expresses that a shortest path between $p$ and $q$ with all intermediate processes in $S \cup \{ r \}$ either visits $r$ or does not; in the first case this path has length $d ^ { S } ( p , r ) + d ^ { S } ( r , q )$ , and in the second case it has length $d ^ { S } ( p , q )$ . Here, $\operatorname* { m i n } \{ \infty , a \} = a$ and $\infty + a = \infty$ for all $a \in \mathbb { R } _ { \geq 0 } \cup \{ \infty \}$ ,.

, ,The Floyd-Warshall algorithm starts with $S = \emptyset$ , in which case the first three equations completely define $d ^ { S }$ . As long as $s$ does not contain all processes, a pivot $r \not \in S$ is selected and $d ^ { S \bar { \cup } \{ r \} }$ is computed from $d ^ { S }$ using the fourth equation; then $r$ is added to $s$ . Finally, note that if $s$ contains all processes, then $d ^ { S }$ is the standard distance function.

Transferring this algorithm to a distributed setting gives rise to two complications. First, all processes must uniformly select the pivots in the same order. Therefore, we make the (strong) assumption that each process knows from the start the IDs of all processes in the network. Second, in each pivot round, the pivot $r$ must broadcast its routing table because a process $p$ may need to know $d ^ { S } ( r , q )$ in order to compute $d ^ { \bar { S } \cup \{ r \} } ( p , q )$ in view of the fourth equation.

In Toueg’s algorithm, each process $p$ starts with $S _ { p } = \emptyset$ and maintains values $d i s t _ { p } ( q )$ and parent $_ p ( q )$ for each process $q$ , where $d i s t _ { p } ( q )$ is the length of the shortest known path from $p$ to $q$ , and parent $\dot { \mathbf { \Omega } } _ { p } ( \dot { q } )$ is the process after $p$ on this path. Initially, $d i s t _ { p } ( p ) = 0$ and $p a r e n t _ { p } ( p ) = \perp$ , while for each $q \neq p$ , either $d i s t _ { p } ( q ) = w e i g h t ( p q )$ and paren $\dot { \mathbf { \eta } } _ { p } ( q ) = q$ if there is a channel $p q$ , or $d i s t _ { p } ( q ) = \infty$ and paren $t _ { p } ( q ) = \bot$ otherwise.

In each successive round, the same pivot $r$ is selected by all processes $p$ and added to the sets $S _ { p }$ . The pivot $r$ broadcasts its values $d i s t _ { r } ( q )$ for all processes $q$ . If parent $_ p ( r ) = \perp$ for a process $p \neq r$ in this pivot round, then $d i s t _ { p } ( r ) = \infty$ , so $d i s t _ { p } ( r ) + d i s t _ { r } ( q ) = \infty \geq d i s t _ { p } ( q )$ for all processes $q$ . Therefore, processes that are not in the sink tree toward $r$ do not need the routing table of $r$ . Hence, this sink tree can be used in the opposite direction to broadcast $d i s t _ { r }$ . To facilitate this use of $r$ ’s sink tree, in the $r$ -pivot round, each process $p$ sends $\langle \mathbf { r e q u e s t } , r \rangle$ to parent $_ p ( r )$ if it is not $\perp$ to let that process pass on the values $d i s t _ { r } ( q )$ to $p$ . Next, $p$ acts as follows:

If $p$ is not in the sink tree of $r$ , then $p$ immediately completes the $r$ -pivot round. Suppose $p$ is in the sink tree of $r$ (that is, $p a r e n t _ { p } ( r ) \neq \bot$ or $p = r ,$ ). If $p \neq r$ , then $p$ must first wait until it has received $d i s t _ { r }$ from $p a r e n t _ { p } ( r )$ . It forwards $d i s t _ { r }$ to those neighbors that send $\langle \mathbf { r e q u e s t } , r \rangle$ to $p$ . Moreover, for each process $q , p$ checks whether $d i s t _ { p } ( r ) + d i s t _ { r } ( q ) < d i s t _ { p } ( q )$ ,and, if so, performs $d i s t _ { p } ( q ) \gets d i s t _ { p } ( r ) + d i s t _ { r } ( q )$ and parent $\mathbf { \Psi } _ { p } ( q ) \gets p a r e n t _ { p } ( r )$ <. This completes the $r$ -pivot round.

Finally, $p$ either proceeds to the next pivot round, if $S _ { p }$ does not contain all processes, or terminates.

Example 8.3 We give a computation of Toueg’s algorithm on the following network, with pivot order $p q r s$ .

$$
\underbrace { \overbrace { \big < P } ^ { 4 } } _ { \begin{array} { l } { 1 } \\ { 2 } \end{array} } \underbrace { \overbrace { 4 } } _ { \begin{array} { l } { 1 } \\ { 2 } \end{array} }
$$

Initially, $d i s t _ { t } ( t ) = 0$ for all four processes $t$ , $d i s t _ { t } ( u ) = w e i g h t ( t u )$ if there is a channel $_ { t u }$ , and all other dist values are $\infty$ . And parent $\dot { \mathbf { \Omega } } _ { t } ( u ) = u$ if $t$ is a direct neighbor of $u$ , and all other parent values are $\perp$ .

In the $p$ -pivot round, $q$ and $s$ both send $\langle \mathbf { r e q u e s t } , p \rangle$ to $p$ . So the distance values of $p$ are sent to $q$ and $s$ , but not to $r _ { \cdot }$ , which is not yet in the sink tree of $p$ ,. As a result, $q$ and $s$ discover a path to each other via $p$ , so that $d i s t _ { q } ( s )$ and $d i s t _ { s } ( q )$ are set to 5, and parent $\mathbf { \chi } _ { q } ^ { \cdot } ( s )$ and parent $\mathbf { \sigma } _ { s } ( q )$ are set to $p$ .

In the $q$ -pivot round, $p , r _ { \mathrm { : } }$ , and $s$ send $\langle \mathbf { r e q u e s t } , q \rangle$ to $q , q$ , and $p$ , respectively. So the distance values of $q$ are sent to $p , r _ { : }$ and $s$ . As a result, $p$ and $r$ ,discover a path to each other via $q$ , so that $d i s t _ { p } ( r )$ and $d i s t _ { r } ( p )$ are set to 5, and $p a r e n t _ { p } ( r )$ and parent $_ r ( p )$ are set to $q$ .

In the $r$ -pivot round, $p , q$ , and $s$ send $\left. \mathbf { r e q u e s t } , r \right.$ to $q , r$ , and $r$ , respectively. So the distance values of $r$ are sent to $p , q$ , and $s$ . As a result, $q$ and $s$ ,discover a shorter path to each other via $r$ , so that $d i s t _ { q } ( s )$ and $d i s t _ { s } ( q )$ are set to 2, and paren $\mathbf { \chi } _ { q } ^ { \cdot } ( s )$ and parent $\mathbf { \Pi } _ { s } ^ { * } ( q )$ are set to $r$ .

In the $s$ -pivot round, $p , q$ , and $r$ send $\langle \mathbf { r e q u e s t } , s \rangle$ to $s , r ,$ , and $s$ , respectively. So the distance values of $s$ are sent to $p , q$ , and $r$ . As a result, $p$ and $r$ ,discover a shorter path to each other via $s$ , so that $d i s t _ { p } ( r )$ and $d i s t _ { r } ( p )$ are set to 2, and parent $_ p ( r )$ and parentr $. ( p )$ are set to $s$ . Moreover, $p$ and $q$ discover a shorter path to each other via $s$ , so that $d i s t _ { p } ( q )$ and $d i s t _ { q } ( p )$ are set to 3, paren $\dot { \mathbf { \zeta } } _ { p } ( q )$ to $s$ , and parent $\dot { \mathbf { \eta } } _ { q } ( p )$ to $r$ .

The worst-case message complexity of Toueg’s algorithm is $O ( N ^ { 2 } )$ , since there are $N$ pivot rounds, and each round takes at most $O ( N )$ messages to forward the distance values of the pivot through the sink tree.

By introducing negative counterparts of the request messages, which inform neighbors that no distance values for the current pivot round have to be forwarded, the need for processes to store distance values of pivots from past rounds indefinitely is avoided. This, however, has a negative impact on the message complexity (see exercise 8.11).

A drawback of Toueg’s algorithm (besides uniform selection of pivots) is that all distance values of a pivot are sent through the sink tree of the pivot, which gives rise to a high bit complexity. This overhead can be reduced as follows. When a process $p$ in the sink tree of the pivot $r$ receives the distance values of $r$ , it first performs for each process $q$ the check for whether $d i s t _ { p } ( r ) + d i s t _ { r } ( q ) < d i s t _ { p } ( q )$ . Now $p$ only needs to forward those values $d i s t _ { r } ( q )$ <for which this check yields a positive result (see exercise 8.13).

# 8.4 Frederickson’s Algorithm

We now discuss a centralized algorithm to compute a breadth-first search tree toward the initiator in an undirected (unweighted) network. We first consider a simple version of this algorithm, in which the processes at distance $n$ from the initiator are discovered in round $n$ .

Initially, after round 0, the variable dist at the initiator has value 0 $, d i s t _ { p } = \infty$ for each noninitiator $p$ , and $p a r e n t _ { p } = \bot$ for all processes $p$ . After each round $n \geq 0$ , the breadth-first search tree has been constructed up to depth $n$ : for each process $p$ at a distance $k \leq n$ from the initiator, $d i s t _ { p } = k$ , and $p$ knows which neighbors are at distance $k - 1$ ; and if $p$ is a noninitiator, then it has a parent in the sink tree toward the initiator.

We explain what happens in round $n + 1$ . It can be depicted as follows.

forward / reverse forward / reverse explore / reverse

![](images/efbbf1bbe377432eb65ca6792aa1f1a84f840d933db90a6d82faa7c0d02a4898.jpg)

At the start of the round, messages $\left. \mathbf { f o r w a r d } , n \right.$ travel down the tree, from the initiator to processes at depth $n$ . When a process $p$ at depth $n$ ,receives this message, it sends $\left. \mathbf { e x p l o r e } , n + 1 \right.$ to its neighbors that are not at depth $n - 1$ . When such a neighbor $q$ ,receives this message, it acts as follows, depending on whether $d i s t _ { q }$ is $\infty , n + 1$ , or $n$ :

• If $d i s t _ { q } = \infty$ , then $d i s t _ { q } \gets n + 1 , p a r e n t _ { q } \gets p$ , and $q$ sends back ⟨reverse true⟩, informing $p$ that $q$ is a child of $p$ .   
• If $d i s t _ { q } = n + 1$ , then $q$ stores that $p$ is at depth $n$ and sends back ⟨reverse false⟩, informing $p$ that $q$ is not a child of $p$ .

• If $d i s t _ { q } = n$ , then $q$ interprets $\left. \mathbf { e x p l o r e } , n + 1 \right.$ as a negative reply to the message $\left. \mathbf { e x p l o r e } , n + 1 \right.$ that $q$ sent (or will send) to $p$ .

A process $p$ at depth $n$ waits until all messages $\left. \mathbf { e x p l o r e } , n + 1 \right.$ have been answered with a ⟨reverse $_ - \rangle$ or $\left. \mathbf { e x p l o r e } , n + 1 \right.$ . Likewise, a noninitiator $p$ at a depth $< n$ waits until all messages $\left. \mathbf { f o r w a r d } , n \right.$ , have been ,answered with a $\left. \mathrm { \bf r e v e r s e } , _ { - } \right.$ . In both cases, $p$ sends $\langle \mathbf { r e v e r s e } , b \rangle$ to its parent, where $b = t r u e$ only if new ,processes were added to its subtree.

The initiator waits until all messages $\left. \mathbf { f o r w a r d } , n \right.$ (or, in round 1, $\left. \mathbf { e x p l o r e } , 1 \right.$ ) have been answered with a $\left. \mathrm { \bf r e v e r s e } , _ { - } \right.$ . If no new processes were added in round $n + 1$ , then the initiator terminates, and it may inform ,all other processes that the breadth-first search has terminated. Otherwise the initiator continues with round $n + 2$ ; processes in the tree only send a forward to children that reported new processes in round $n + 1$ .

The worst-case message complexity of this breadth-first search algorithm is $O ( N ^ { 2 } )$ . There are at most $N + 1$ rounds, and in each round tree edges carry at most one forward and one replying reverse, adding up to at most $2 ( N - 1 ) N$ messages. And, in total, channels carry one explore and one replying reverse or explore, adding up to $2 E$ messages. The worst-case time complexity is also $O ( N ^ { 2 } )$ : round $n$ is completed in at most $2 n$ time units, for $n = 1 , . . . , N$ , and $2 ( 1 + 2 + \cdots + N ) = N ( N + 1 )$ .

, . . . ,Frederickson’s algorithm is based on the observation that in the simple breadth-first search algorithm just described, forward messages need to travel up and down the tree often, since each round only discovers processes that are one level deeper than the ones discovered in the previous round, level meaning the distance to the initiator. Efficiency can be gained by exploring several levels in one round. However, explore messages then give a performance penalty because they may travel through the same channel multiple times in one round. Notably, if we abolished forward messages and used only explore messages to discover all processes in one round, we would be back at the Chandy-Misra algorithm, which we have seen is not efficient. Therefore, the number of levels explored in one round is included as a parameter $\ell$ . At the end, an optimal value for $\ell$ will be determined. In the simple breadth-first search algorithm, $\ell = 1$ .

ℓ ℓIn Frederickson’s algorithm, initially (after round 0) the variable dist at the initiator has value 0, $d i s t _ { p } = \infty$ for each noninitiator $p$ , and $p a r e n t _ { p } = \bot$ for all processes $p$ . After each round $n \geq 0$ , the breadth-first search tree has been constructed up to depth $\ell \cdot n$ : for each process $p$ at a distance $k \leq \ell \cdot n$ from the initiator, $d i s t _ { p } = k$ , and $p$ ℓknows which neighbors are at distance $k - 1$ ; and if $p$ ℓis a noninitiator, then it has a parent in the sink tree toward the initiator.

At the start of round $n + 1$ , messages $\langle \mathbf { f o r w a r d } , \ell \cdot n \rangle$ travel down the tree, from the initiator to processes at depth $\ell \cdot n$ . When a process at depth $\ell \cdot n$ , ℓreceives this message, it sends $\left. \mathbf { e x p l o r e } , \ell \cdot n + 1 \right.$ to its neighbors ℓthat are not at depth $\ell \cdot n - 1$ ℓ , ℓ. The parameter in this message is (possibly an overapproximation of) the depth ℓof the receiving process. This value is increased by 1 every time the explore message is forwarded. When this parameter becomes divisible by $\ell$ , the $\ell$ levels for the current round have been explored and $\langle \mathbf { r e v e r s e } , b \rangle$ ℓ ℓmessages bounce back toward the processes at level $\ell \cdot n$ .

ℓCompared to the simple breadth-first search algorithm, two complications occur. First, a process $q$ may receive a forward from a neighbor $p$ that is not its parent. This can happen if in the previous round $p$ temporarily was $q$ ’s parent but $q$ later selected another parent with a shorter path to the initiator and $p$ sent the forward to $q$ before being informed that $q$ is no longer its child (see exercise 8.16). Such a forward can simply be dismissed by $q$ , because $p$ will eventually receive $q$ ’s negative acknowledgment from the previous round. Second, a process may send multiple explores into the same channel, if its distance value is improved several times in a round. Therefore, a reverse in reply to an explore is supplied with a distance parameter, so that a process can distinguish which explore an incoming reverse is a reply to.

We now specify Frederickson’s algorithm in detail. Each process is supposed to know the value of $\ell$ . The algorithm is started by the initiator, which in round 1 sends $\left. \mathbf { e x p l o r e } , 1 \right.$ ℓ to its neighbors. Let a process $q$ receive a message $\left. \mathbf { e x p l o r e } , k \right.$ from a neighbor $p$ . We consider two cases:

• If $k < d i s t _ { q }$ , then $d i s t _ { q } \gets k$ and paren $t _ { q } \gets p$ . Again, we consider two cases:   
$^ *$ If $k$ <is not divisible by $\ell$ , then $q$ sends $\scriptstyle \left. \mathbf { e x p l o r e } , k + 1 \right.$ to its neighbors, except $p$ . Next, $q$ waits until it has received ⟨reverse $k + 1 , \ O _ { - } \rangle$ or $\langle \mathbf { e x p l o r e } , j \rangle$ ,with $j \in \left\{ k , k + 1 , k + 2 \right\}$ from all these neighbors. Then $q$ sends $\langle \mathrm { r e v e r s e } , k , b \rangle$ to $p$ ,, where $b = t r u e$ ,if and only if $q$ ,received a message $\langle \mathrm { r e v e r s e } , k + 1 , t r u e \rangle$ . , ,Only neighbors that reply with $\langle \mathrm { r e v e r s e } , k + 1 , t r u e \rangle$ are children of $q$ in the tree (unless $q$ , ,also receives a message $\left. \mathbf { e x p l o r e } , k \right.$ , , from such a neighbor, in which case the sender is not a child of $q$ ). If $q$ ,later receives a message $\langle \mathrm { e x p l o r e } , k ^ { \prime } \rangle$ with $k ^ { \prime } < k$ , then $q$ changes its distance to $k ^ { \prime }$ , makes the sender its parent, sends messages $\langle \mathbf { e x p l o r e } , k ^ { \prime } + 1 \rangle$ <, and waits for replies to these messages before sending $\langle \mathrm { r e v e r s e } , k ^ { \prime } , b \rangle$ to its new parent, where $b = t r u e$ if and only if $q$ received a message ⟨reverse $k ^ { \prime } + 1 , t r u e \rangle$ .   
$^ *$ If $k$ , ,is divisible by $\ell$ , then $q$ sends $\langle \mathrm { r e v e r s e } , k , t r u e \rangle$ to $p$ immediately.   
• If $k \geq d i s t _ { q }$ , then again we consider two cases:   
$^ *$ If $k > d i s t _ { q }$ or $k$ is not divisible by $\ell$ , then $q$ does not send a reply to $p$ . In this case, $q$ sent $\langle \mathbf { e x p l o r e } , d i s t _ { q } +$ $^ { 1 \rangle }$ >into the channel $q p$ ℓ ,, which already serves as a negative acknowledgment to the current incoming message.   
$^ *$ If $k = d i s t _ { q }$ and $k$ is divisible by $\ell$ , then $q$ sends $\langle \mathrm { r e v e r s e } , k , f a l s e \rangle$ to $p$ .

A process $p$ at depth $\ell \cdot n$ waits until all messages $\left. \mathbf { e x p l o r e } , \boldsymbol { \ell \cdot n } + 1 \right.$ have been answered with a reverse ℓor explore. Likewise, a noninitiator $p$ at a depth $< \ell \cdot n$ , ℓwaits until all messages $\langle \mathbf { f o r w a r d } , \ell \cdot n \rangle$ have been answered with a reverse. In both cases, $p$ sends $\langle \mathbf { r e v e r s e } , b \rangle$ to its parent, where $b =$ , ℓtrue only if new processes were added to its subtree.

The initiator waits until all messages $\langle \mathbf { f o r w a r d } , \ell \cdot n \rangle$ (or, in round 1, $\left. \mathbf { e x p l o r e } , 1 \right.$ ) have been answered , ℓwith a reverse. If no new processes were added in round $n + 1$ ,, then the initiator terminates and may inform all other processes that the breadth-first search has terminated. Otherwise the initiator continues with round $n + 2$ ; processes in the tree only send a forward to children that reported new processes in round $n + 1$ .

Example 8.4 We consider one possible computation of Frederickson’s algorithm on the following network with $p$ as initiator and $\ell = 3$ .

![](images/55e98909060334a404fc5542345f5c1f0952bdb1f516b1a78030abbf22c43930.jpg)

After round $0 , d i s t _ { p } = 0$ and the distance value of all other processes is $\infty$ ; nobody has a parent.

– Round 1 is started by $p$ , which sends ⟨explore $^ { 1 \rangle }$ to $q$ and $r$ .

$p$ ’s explore arrives at $\mathit { l } : d i s t _ { q } \gets 1$ , parentq ← p, and $q$ sends $\left. \mathbf { e x p l o r e } , 2 \right.$ to $r$ and $s$ .   
$q$ ’s explore arrives at $r \colon d i s t _ { r } \gets 2$ , paren $t _ { r } \gets q$ , and $r$ sends $\left. \mathbf { e x p l o r e } , 3 \right.$ to $p , s ,$ , and $t$ .   
$p$ receives and dismisses $r$ ’s explore.   
$r$ ’s explore arrives at $s \colon d i s t _ { s } \gets 3$ , $p a r e n t _ { s } \gets r$ , and $s$ sends ⟨reverse 3 true⟩ in reply.   
r’s explore arrives at $t \colon d i s t _ { t } \gets 3$ , $p a r e n t _ { t } \gets r$ , and $t$ sends $\langle \mathrm { r e v e r s e } , 3 , t r u e \rangle$ in reply.   
$p$ ’s explore arrives at $r \colon d i s t _ { r } \gets 1$ , $p a r e n t _ { r } \gets p$ , and $r$ sends $\left. \mathbf { e x p l o r e } , 2 \right.$ to $q , s ,$ , and $t$ .   
$r$ receives and dismisses the reverses from $s$ and $t$ .   
$q$ ’s explore arrives at $s \colon d i s t _ { s } \gets 2$ , $p a r e n t _ { s } \gets q$ , and $s$ sends $\left. \mathbf { e x p l o r e } , 3 \right.$ to $r , t ,$ , and $u$ .   
$r$ ’s explore arrives at $t \colon d i s t _ { t } \gets 2$ , and $t$ sends $\left. \mathbf { e x p l o r e } , 3 \right.$ to $s$ and $u$ .   
s’s explore arrives at u: $d i s t _ { u } \gets 3$ , $p a r e n t _ { u } \gets s$ , and $u$ ,sends back ⟨reverse 3 true⟩.   
t’s explore arrives at $u$ , which sends back ⟨reverse 3 false⟩.   
$r$ ’s and $t$ ’s explores and $u$ ’s reverse arrive at $s$ , ,, which sends ⟨reverse 2 true⟩ to $q$ .   
s’s explore and $u$ ’s reverse arrive at $t$ , which sends $\langle \mathrm { \bf r e v e r s e } , 2 , t r u e \rangle$ , , to $r$ .   
$r$ ’s explore and $s$ ’s reverse arrive at $q$ , ,, which sends ⟨reverse 1 true⟩ to $p$ .   
s’s explore and $t ^ { \prime }$ ’s reverse arrive at $r$ , ,, which sends ⟨reverse 1 true⟩ to $p$ .   
$q$ ’s and $r ^ { \mathrm { : } }$ ’s reverses arrive at $p$ , ,, which starts round 2. No further processes are discover after which the computation terminates.

The resulting spanning tree is as follows.

![](images/a3c1f048bc35520d6dcc7e08a1765b023025fa9157c5cbb3718e04d858e035ca.jpg)

The worst-case message complexity of Frederickson’s algorithm, where $\ell$ levels are explored in each round, is $O ( \frac { N ^ { 2 } } { \ell } + \ell \cdot E )$ . There are at most $\lceil \frac { N } { \ell } \rceil + 1$ ℓ rounds, and, in each round, tree edges carry at most one ℓ ℓ ℓforward and one replying reverse, adding up to at most 2· $\lceil \frac { N } { \ell } \rceil \cdot ( N - 1 )$ messages. And, in total, channels carry at most $2 \ell$ explores and $2 \ell$ ℓreplying reverses, and frond edges carry at most one spurious forward, adding ℓup to (fewer than) $( 4 \ell + 1 ) E$ messages. Note that $\frac { N ^ { 2 } } { \ell }$ decreases while $\ell \cdot E$ increases when $\ell$ is increased. An optimal value for $\ell$ ℓis determined by equating these two summands of the message complexity : N 2 = · E yields $\begin{array} { r } { \ell = \frac { N } { \sqrt { E } } } \end{array}$ ℓ. Since √ $\ell$ must be an integer value, we take $\begin{array} { r } { \ell = \lceil \frac { N } { \sqrt { E } } \rceil } \end{array}$ ℓ ℓ. The worst-case message complexity then becomes $O ( N { \cdot } \sqrt { E } )$ .

The worst-case time complexity of Frederickson’s algorithm is $O ( \frac { N ^ { 2 } } { \ell } )$ : round $n$ is completed in at most $2 \ell \cdot n$ time units, for $n = 0 , . . . , \lceil \frac { N } { \ell } \rceil$ , and $\begin{array} { r } { 2 \ell \cdot ( 1 + 2 + \cdots + \lceil \frac { N } { \ell } \rceil ) = \ell \cdot \lceil \frac { N } { \ell } \rceil \cdot \bar { ( \lceil \frac { N } { \ell } \rceil + 1 ) } } \end{array}$ . If we take $\begin{array} { r } { \ell = \lceil \frac { N } { \sqrt { E } } \rceil } \end{array}$ , then the worst-case message time complexity becomes $O ( N { \cdot } \sqrt { E } )$ .

Concluding, computing a breadth-first search tree toward each process in the network takes $O ( N ^ { 2 } { \cdot } \sqrt { E } )$ messages and time in the worst case.

# 8.5 Packet Switching

Consider a network for which routing tables have been computed, so that all processes know how data packets should be forwarded through the network toward their destinations. On their way, these packets are stored at a buffer slot of a process until that process is certain the packet has arrived safely and has been stored in the buffer of the next process on the packet’s route. When a packet reaches its destination, it is consumed; that is, removed from the network.

Even with cycle-free routing tables, a store-and-forward deadlock may occur when a group of packets are all waiting for the use of a buffer slot occupied by a packet in the group. A controller avoids such deadlocks by prescribing whether a new packet can be generated at a process and whether an existing packet can be forwarded to the next process, and possibly prescribing the buffer slot in which it is put. To avoid a trivial deadlock-free controller that disallows any generation of packets, it is generally required that generation of a new packet at a process with an empty buffer should always be allowed.

As noted, a process can eliminate a packet from its buffer only when it is sure the packet has arrived safely at the next process. For simplicity, we assume synchronous communication, which basically means that a process can send a packet only when the receiver is ready to receive it; that is, when it has a suitable buffer slot available. Thus, we abstract away from the communication overhead imposed by fruitless attempts to forward a packet.

# Destination and Hops-So-Far Controllers

Consider a directed network of processes $p _ { 0 } , . . . , p _ { N - 1 }$ , and let $T _ { i }$ be the sink tree (with respect to the routing tables) with root $p _ { i }$ for $i = 0 , \ldots , N - 1$ , . . . ,. We first discuss two simple controllers based on these sink trees.

, . . . ,In the destination controller, each process carries $N$ buffer slots, numbered from 0 to $N - 1$ . The ith buffe slots at the processes are used to mimic the sink tree $T _ { i }$ .

• When a packet with destination $p _ { i }$ is generated at a process $q$ , it is placed in the ith buffer slot of $q$ .   
• If qr is an edge in $T _ { i }$ , then a packet in the ith buffer slot of $q$ can be forwarded to the ith buffer slot of $r$ .

The destination controller is deadlock-free. This follows from the fact that, for each $i$ , since $T _ { i }$ is acyclic, a packet in the ith buffer slot of any process can always travel to its destination. The clear drawback of this controller is that it requires $N$ buffer slots per process, so it does not scale to large networks.

Let $K$ be the length of a longest path in any $T _ { i }$ . In the hops-so-far controller, each process carries $K + 1$ buffer slots, numbered from 0 to $K$ .

• When a packet is generated at a process $q$ , it is placed in the 0th buffer slot of $q$ . • If qr is an edge in some $T _ { i }$ , then, for any $j < K$ , a packet in the jth buffer slot of $q$ can be forwarded to the $( j + 1 ) \mathrm { t h }$ buffer slot of $r$ .

We argue that the hops-so-far controller is deadlock-free. It is easy to see, by induction on $j$ , that no packet can get stuck at a $( K - j )$ th buffer slot of any process, for $j = 0 , . . . , K$ . The base case $j = 0$ is trivial, because , . . . ,a packet in a Kth buffer slot is guaranteed to be at its destination and so can be consumed. Now consider the inductive case: a packet in a $( K - ( j + 1 ) )$ th buffer slot. By induction, packets in a $( K - j )$ th buffer slot can be forwarded to their destinations and consumed. Hence, a packet in a $( K - ( j + 1 ) ) \mathrm { t } \mathfrak { h }$ buffer slot can either be consumed or forwarded to a $( K - j )$ th buffer slot and from there to its destination, where it is consumed. The hops-so-far controller typically requires between $\frac { D } { 2 }$ and $D$ buffer slots per process. This is much better than for the destination controller but still not appealing for large networks.

# Acyclic Orientation Cover Controller

An acyclic orientation of an undirected network $G$ is an acyclic directed network obtained by directing the edges of $G$ in one of the two possible directions. Acyclic orientations $G _ { 0 } , \ldots , G _ { n - 1 }$ of $G$ form an acyclic orientation cover of a set $\mathcal { P }$ of paths in $G$ if each path in $\mathcal { P }$ , . . . ,is the concatenation of paths $P _ { 0 } , . . . , P _ { n - 1 }$ in $G _ { 0 } , \ldots , G _ { n - 1 }$ , respectively.

Example 8.5 For each undirected ring, there exists a cover, consisting of three acyclic orientations, of the collection of minimum-hop paths. For instance, in the case of a ring of size 6:

![](images/13bfff0cdefe52fcf13a8347f3fc8e938d6be8ebd8b72a792e909c27257c2028.jpg)

Consider an undirected network $G$ that has been equipped with routing tables; $\mathcal { P }$ denotes the collection of paths in $G$ according to the routing tables. Let $G _ { 0 } , \ldots , G _ { n - 1 }$ be an acyclic orientation cover of $\mathcal { P }$ . In the acyclic orientation cover controller, each process in $G$ . . . ,has $n$ buffer slots, numbered from 0 to $n - 1$ .

• A packet generated at a process $q$ is placed in the 0th buffer slot of $q$ . Let qr be an edge in some $G _ { i }$ . A packet in the ith buffer slot of $q$ can be forwarded to the ith buffer slot of $r _ { \cdot }$ . Moreover, if $i < n - 1$ , then a packet in the ith buffer slot of $r$ can be forwarded to the $( i + 1 )$ th buffer slot of $q$ .

We argue that the acyclic orientation cover controller is deadlock-free. Consider a reachable configuration $\gamma$ . Packets are forwarded and consumed until a configuration $\delta$ is reached in which forwarding and consumpγtion are no longer possible. We argue by induction on $j$ δthat in $\delta$ each $( n - j )$ th buffer slot of any process is empty for $j = 1 , \dotsc , n$ . In the base case $j = 1$ δ, consider a packet that is being routed via a concatenation of paths $P _ { 0 } , . . . , P _ { n - 1 }$ . . ,in $G _ { 0 } , \ldots , G _ { n - 1 }$ . It is not hard to see, by the definition of the acyclic orientation cover , . . . , , . . . ,controller, that when this packet is in a kth buffer slot, it is being routed via a $P _ { \ell }$ with $\ell \geq k$ . This implies that any packet in an $( n - 1 ) \operatorname { t h }$ buffer slot is being routed via $G _ { n - 1 }$ . Since $G _ { n - 1 }$ ℓ ℓis acyclic, a packet in an $( n - 1 ) \operatorname { t h }$ buffer slot can always travel to its destination. Now consider the inductive case: a packet in an $( n - ( j + 1 ) ) \mathfrak { t h }$ buffer slot. By induction, in $\delta$ all $( n - j )$ th buffer slots are empty. Hence, packets in $( n - ( j + 1 ) ) \mathbf { t h }$ buffer δslots can be consumed, forwarded via $G _ { n - ( j + 1 ) }$ since it is acyclic, or forwarded to an $( n - j )$ th buffer slot since these are empty. To conclude, in $\delta$ , all buffer slots are empty.

Example 8.6 For each undirected ring, there exists a deadlock-free controller that uses three buffer slots per process and allows packets to travel via minimum-hop paths. This follows from the fact that, according to example 8.5, undirected rings have a cover of the collection of minimum-hop paths that consists of three acyclic orientations. So the resulting acyclic orientation cover controller requires three buffer slots per process. The buffer slots between two neighboring processes are connected as follows, where the edge between these processes in the ring is directed from left to right in $G _ { 0 }$ and $G _ { 2 }$ and in the opposite direction in $G _ { 1 }$ .

![](images/1ef791fbe506e7be35bfd2400ff1d8fde8bf731c2c77cfcfde69aafc71eeaedd.jpg)

# 8.6 Routing on the Internet

The routing approaches discussed so far were not designed to cope with large-sized and dynamic networks. Here we briefly discuss some important methods for routing on the Internet, because they employ classical uniprocessor routing algorithms and use some ideas discussed earlier in this chapter. The AODV routing protocol for dynamic networks will be discussed in detail in chapter 18.

Distance-vector routing and link-state routing are pragmatic routing algorithms that can cope with dynamic directed networks in which processes may join the network or crash temporarily or permanently. In distance-vector routing, each process after a change in its local topology or in its routing table, sends (updates in) its routing table to its neighbors in the network. This way processes can locally keep their routing tables up-to-date and compute shortest paths (typically with the Bellman-Ford algorithm).

In link-state routing, each process periodically and after a change in its local topology sends a link-state packet to its neighbors, reporting the channels between the process and its direct neighbors, as well as their weights (typically based on latency or bandwidth). Moreover, it attaches a sequence number to these linkstate packets, which is increased every time it broadcasts link-state packets to its neighbors. The link-state packets are flooded through the network; all processes store their content, so they obtain a local view of the entire network. Processes also store the sequence numbers of link-state packets on which their local view is based in order to prevent new information from being overwritten by old information. With its local view, a process can locally compute shortest paths using a uniprocessor algorithm (mostly Dijkstra’s algorithm).

The crash failure and subsequent recovery of a process are eventually detected by, and taken into account in the link-state packets broadcast by, its neighbors. When a process recovers from a crash, its sequence number restarts at zero, so the link-state packets it broadcasts after the crash might be ignored by the other processes for a long time. Therefore, link-state packets carry a time-to-live field, defining the moment in time after which the packet becomes stale and its information may be discarded in favor of a link-state packet with a lower sequence number. To reduce the overhead of flooding, each time a link-state packet is forwarded, its time-to-live field is decreased; when it becomes zero, the packet is discarded.

Distance-vector routing and link-state routing deal well with dynamicity but do not scale up to the size of the Internet, because they send routing tables or use flooding, and letting processes compute all their shortest paths does not scale. Therefore, the Internet is divided into what are called autonomous systems, which are basically different subnetworks that use distance-vector routing (by means of the RIP protocol) or linkstate routing (by means of the OSPF Protocol) within their own domain. Routing between (over 100,000) autonomous systems is performed with the Border Gateway Protocol, in which border routers exchange reachability information, meaning that a border router informs its neighboring border routers about updates in its routing table either because it noticed a topology change or as a result of an update in the routing table of one of its neighbors. Thus, each border router maintains an up-to-date routing table based on autonomous system connectivity. When a border router connects to the network for the first time, other border routers provide it with their entire routing tables. An autonomous system typically has multiple border routers, to avoid performance bottlenecks and strengthen fault tolerance.

The Transmission Control Protocol (TCP) aims to guarantee reliable data delivery over the Internet. In this protocol, to control congestion in the network, every process maintains a congestion window for each of its (bidirectional) channels. Packets are acknowledged by the receiver (where the so-called Selective Acknowledgement scheme allows a receiver to inform the sender of segments of data packets that arrived successfully). The congestion window of a channel provides an upper bound on the number of unacknowledged packets a process is allowed to have sent into this channel. The congestion window grows linearly with each received acknowledgment, up to some threshold. The congestion window may effectively double in size during every round-trip time (that is, the time between sending a packet and receiving the corresponding acknowledgment) if all packets are being acknowledged (see exercise 8.28). The congestion window is reset to the initial size (in TCP Tahoe) or halved (in TCP Reno) with each lost data packet.

# Bibliographical notes

The Chandy-Misra algorithm originates from [24], the Merlin-Segall algorithm from [86], Toueg’s algorithm from [120], and Frederickson’s algorithm from [47] (where the algorithm is only sketched). The destination and hops-so-far controllers were proposed in [85], and the acyclic orientation cover controller was proposed in [117]. The mechanisms underlying link-state routing were put forward in [80], and an earlier version of link-state routing was used in ARPANET [81]. Congestion windows can be traced back to [60].

# 8.7 Exercises

Exercise 8.1 Explain in detail how the Dijkstra-Scholten algorithm detects termination of the Chandy-Misra algorithm.

Exercise 8.2 Adapt the Dijkstra-Scholten algorithm so that termination is detected of the Chandy-Misra algorithm without building two distinct sink trees (that is, no separate sink tree is needed for detecting termination).

Exercise 8.3 Why is Rana’s algorithm not an effective method for detecting termination of the Chandy-Misra algorithm?

Exercise 8.4 Let $n$ range over the natural numbers. Generalize example 8.1 to a network with $2 n + 1$ processes and $3 n$ weighted channels, for which the number of messages sent by the Chandy-Misra algorithm in the worst case grows exponentially (in $n$ ). Explain why this is the case.

Exercise 8.5 Consider the network depicted in example 8.2.

(a) Give a computation of the Merlin-Segall algorithm on this network in which all processes already compute the correct distance values in the first round.   
(b) Adapt the initial sink tree be changing the parent of $r$ from $p _ { 0 }$ to $s$ . Explain why no computation of the Merlin-Segall algorithm on this adapted network computes the correct distance values in one round.

Exercise 8.6 Run the Merlin-Segall algorithm on the following undirected weighted network, with sink tree $s \to p \to r \to q \to t$ , to compute all shortest paths toward process $t$ . Give a computation that takes four rounds before the correct sink tree has been computed.

![](images/78333c7d76e4a610d6061c6e14d9fdc053f2c818421987b4667586ec0494d00b.jpg)

Exercise 8.7 Suppose that in the Merlin-Segall algorithm a process $q$ updates parentq each time it updates $d i s t _ { q }$ . Explain what could go wrong.

Exercise 8.8 Adapt the Merlin-Segall algorithm (without adding extra messages) so that if the correct shortest paths have been computed in fewer than $N - 1$ rounds, this will be detected by the initiator, who can then terminate immediately.

Exercise 8.9 Consider the Merlin-Segall algorithm with topology changes. Suppose shortest paths toward the initiator have already been determined. Let a new channel $p q$ become operational. How can processes $p$ and $q$ together determine whether this channel is part of a shortest path toward the initiator, and how could they act if this is the case?

Exercise 8.10 Run Toueg’s algorithm on the network in exercise 8.6. Take as pivot order p q r s t.

Exercise 8.11 Explain how the message complexity of Toueg’s algorithm changes if negative counterparts of the request messages are included, to inform neighbors that no distance values for the current pivot round have to be forwarded.

Exercise 8.12 Analyze the space complexity of Toueg’s algorithm.

Exercise 8.13 In Toueg’s algorithm, when a process $p \neq r$ in the sink tree of the pivot $r$ receives the distance values of $r$ , let $p$ first perform for each process $q$ the check whether $d i s t _ { p } ( r ) + d i s t _ { r } ( q ) < d i s t _ { p } ( q )$ . Explain why $p$ needs to forward only those values $d i s t _ { r } ( q )$ < for which this check yields a positive result.

Exercise 8.14 Apply Frederickson’s algorithm with $\ell = 1$ (the “simple” algorithm) to the following undiℓrected network in order to find a breadth-first search tree rooted in $p$ . Do the same with $\ell = 2$ .

![](images/0cb918e3787603f2d5d29622874c0133b6cc203fe1b31a2101395d14fd077951.jpg)

Exercise 8.15 In Frederickson’s algorithm, consider a process located $k$ hops from the initiator, with $k \neq \ell \cdot n$ for all $n$ . Argue that this process is guaranteed to receive a message ⟨reverse $k + 1 , \ O _ { - } \rangle$ or $\langle \mathbf { e x p l o r e } , j \rangle$ ℓ with $j \in \left\{ k , k + 1 , k + 2 \right\}$ from all its neighbors.

Exercise 8.16 Give a computation of Frederickson’s algorithm on an undirected ring of size 3 and with $\ell = 2$ to show that a forward can be sent to a process that is not a child of the sender.

Exercise 8.17 Analyze the message and time complexity of Frederickson’s breadth-first search algorithm, taking into account the network diameter $D$ . Which value for $\ell$ achieves an optimal worst-case message complexity?

Exercise 8.18 Develop a distributed version of Dijkstra’s celebrated single-source shortest-path algorithm for undirected weighted networks. Discuss the worst-case message and time complexity of your algorithm.

Exercise 8.19 [117] Explain why there does not exist a deadlock-free controller that uses only one buffe slot per process.

Exercise 8.20 [117] Show that the destination controller is not deadlock-free if packet routing is as follows.

![](images/a500920c8ca2281fb0dc0ab8bc90857d75ad77ee4f8230f5fb9373866716f679.jpg)

In this picture, packets from $p _ { 1 }$ to $q$ are routed via the path $p _ { 1 } r _ { 1 } p _ { 2 } \cdots q$ , and packets from $p _ { 2 }$ to $q$ are routed via the path $p _ { 2 } r _ { 2 } p _ { 1 } \cdots q$ .

Exercise 8.21 Argue that the acyclic orientation cover of a ring of size 6 in example 8.5 covers all shortest paths in this ring.

Exercise 8.22 Give an acyclic orientation cover $G _ { 0 } , G _ { 1 }$ of a set of paths in the following undirected network that contains for each pair of processes $p , q$ ,a minimum-hop path from $p$ to $q$ .

![](images/90f3523af63c398cdff4e3895346b4e8ebe6aa02d2a76a5e4ad6a86764cbfd11.jpg)

Describe in detail how the buffer slots are linked in the corresponding acyclic orientation cover controller.

Exercise 8.23 Given the undirected cube, prove that there is an acyclic orientation cover $G _ { 0 } , G _ { 1 }$ such that ,between every two processes in the cube there is a minimum-hop path that is the concatenation of paths in $G _ { 0 }$ and $G _ { 1 }$ .

Exercise 8.24 Show that for any acyclic undirected network there exists a deadlock-free controller that uses only two buffer slots at each process.

Exercise 8.25 Give an example to show that a cyclic orientation cover controller (in which the orientations $G _ { i }$ are allowed to contain cycles) is not always deadlock-free.

Exercise 8.26 Consider the link-state algorithm on a directed weighted network of five processes $p , q , r$ , $s$ , and $t$ . The outgoing channels of $p$ to $q$ and $t$ have weights 1 and 6, respectively. The most recent linkstate packets $p$ received report the following weights: weigh $( q p ) = 1$ , weight $( q r ) = 7$ , weigh $( q s ) = 5$ , $w e i g h t ( q t ) = 3$ , $w e i g h t ( r q ) = 1$ , $w e i g h t ( r s ) = 5$ , $w e i g h t ( s r ) = 2$ , $w e i g h t ( t q ) = 1$ , $w e i g h t ( t r ) = 2$ , and $w e i g h t ( t s ) = 1$ . Explain how $p$ computes its routes to the other four processes using Dijkstra’s shortest path algorithm.

Exercise 8.27 Why does the link-state algorithm become less efficient if processes broadcast their entire routing table instead of only their outgoing channels and weights?

Exercise 8.28 Argue why a congestion window may effectively double in size during every round-trip time.

# Election

In an election algorithm, the processes in the network elect one process among them as their leader. The aim is usually to let the leader act as the organizer of some distributed task, for example in the role of the root of a spanning tree of the network, the initiator of a centralized algorithm, the central decision point, or the assembly point of information. Each computation starts in a configuration in which the processes are unaware which process will serve as the leader and must terminate in a configuration where exactly one process is the leader. The key challenge of an election algorithm is to break the symmetry in a network.

Election algorithms are decentralized: the initiators can be any nonempty set of processes. We require that all processes have the same local algorithm. This disallows the trivial solution where exactly one process has the algorithm “I am the leader.” Process IDs are supposed to be unique and from a totally ordered set. In chapter 10, we will see that unique IDs are essential for constructing election algorithms that always terminate.

# 9.1 Election in Rings

Ring topologies are particularly challenging for election algorithms due to their high degree of symmetry. We start with considering three election algorithms for rings. In each of these algorithms, the initiators determine among themselves which one has the highest ID. This initiator becomes the leader. Initially, the initiators are active, while all noninitiators are passive. In all three algorithms, passive processes are out of the race to become the leader and simply pass on messages.

# Chang-Roberts Algorithm

The Chang-Roberts algorithm targets a directed ring. Since networks are assumed to be strongly connected, a directed ring is oriented either in a clockwise or in a counterclockwise fashion.

Initially, the initiators send a message to the next process in the ring, tagged with their ID. When an active process $p$ receives a message tagged with $q$ , there are three cases:

• If $q < p$ , then $p$ dismisses the message.

• If $q > p$ , then $p$ becomes passive and passes on the message.   
• If $q = p$ , then $p$ becomes the leader.

The idea behind the Chang-Roberts algorithm is that only the message with the highest ID will complete the round trip, because every other message is stopped, at the latest, when it arrives at the initiator with the highest ID (by the first case). Moreover, initiators that do not have the highest ID are made passive, at the latest, when they receive the message with the highest ID (by the second case). When an initiator receives back its own message, it knows it is the leader (by the third case).

Example 9.1 In the ring that follows, all processes are initiators. If the ring is directed counterclockwise, then it takes $\frac { 1 } { 2 } \cdot N \cdot \left( N + 1 \right)$ messages to elect process $N - 1$ as the leader. Each message is stopped at process $N - 1$ , so the message from process $i$ travels $i + 1$ hops for $i = 0 , . . . , N - 1$ ; and $1 + 2 + \cdots + N = { \frac { 1 } { 2 } } \cdot N \cdot ( N + 1 )$ .

![](images/f3fc16a7448880d760d4856df0b53dfb1a4c2f9716ebbedbab3c61380ae44a85.jpg)

If the ring is directed clockwise, then it takes only $2 N - 1$ messages to elect process $N - 1$ as the leader. Each message is stopped after one hop, except for the message from process $N - 1$ , which travels $N$ hops.

The preceding example shows that the worst-case message complexity of the Chang-Roberts algorithm is $O ( N ^ { 2 } )$ . It can be shown, however, that the average-case message complexity is $O ( N { \cdot } \log N )$ .

# Franklin’s Algorithm

Franklin’s algorithm, which requires an undirected ring, improves on the worst-case message complexity of the Chang-Roberts algorithm. In an election round, each active process $p$ compares its own ID with the IDs of its nearest active neighbors on both sides. If $p$ ’s ID is the largest of the three IDs, then $p$ proceeds to the next election round. If one of the other IDs is greater than $p$ ’s ID, then $p$ becomes passive. And if $p$ receives its own ID from either side, then it becomes the leader, because there are no other active processes left in the ring.

To be more precise, at the start of an election round, each active process sends its $\mathrm { I D }$ to its neighbors on either side. When an active process $p$ has received messages tagged with $q$ and $r$ from either side, there are three cases:

• If max $\{ q , r \} < p$ , then $p$ enters another election round by sending its $\mathrm { I D }$ in both directions again.

• If ma $\mathbf { x } \{ q , r \} > p$ , then $p$ becomes passive.   
• If max $\{ q , r \} = p$ , then $p$ becomes the leader.

If a message for the next election round is received by an active process, this message is buffered until it is clear whether the process remains active in that round.

Example 9.2 On the undirected version of the ring in example 9.1, Franklin’s algorithm terminates in two rounds. In the first round, only process $N - 1$ remains active. In the second round, process $N - 1$ finds that it is the leader.

Example 9.3 We run Franklin’s algorithm on the following undirected ring, in which all processes are initiators.

![](images/9fafb18a5e1cde282dabba2975639c695f37c7c719ba2af99840258d33c7ccac.jpg)

Processes 3, 4, and 5 progress to the second election round, because their IDs are larger than those of their (active) neighbors. Processes 0, 1, and 2 become passive in the first round.   
Only process 5 progresses to the third round, because in the second round it finds that its ID is larger than those of its nearest active neighbors, 3 and 4. Conversely, the latter two processes become passive in the second round, because they find that their nearest active neighbor, 5, has a larger ID.   
Finally, in the third round, process 5 finds that it is the leader, because the two messages it sends in either direction complete the round trip.

The worst-case message complexity of Franklin’s algorithm is $O ( N { \cdot } \log N )$ . In each round with two or more active processes, at least half of the active processes become passive because for each pair of nearest active neighbors at least one becomes passive. In the final round, the remaining active process becomes the leader. So there are at most $\lfloor \log _ { 2 } N \rfloor + 1$ rounds. And each round takes $2 { \cdot } N$ messages (two messages per channel).

# Dolev-Klawe-Rodeh Algorithm

The Dolev-Klawe-Rodeh algorithm transposes the idea behind Franklin’s algorithm to a directed ring. In that setting, messages cannot travel in both directions, so an active process cannot easily compare its own ID $p$ with the IDs $q$ and $r$ of its nearest active neighbors. This is resolved by performing this comparison not at $p$ but at its next (in the direction of the ring) active neighbor, $r$ . That is, the IDs $p$ and $q$ are collected at $r _ { \cdot }$ . If $p$ is larger than $q$ and $r$ , then $r$ remains active and progresses to the next election round, in which it assumes the

ID $p$ . If $p$ is smaller than $q$ or $r$ , then $r$ becomes passive. And if $p$ equals $q$ and $r$ , then $r$ becomes the leader. If we really want the initiator with the largest $\mathrm { I D }$ to become the leader, then in the last case $r$ could send a special leader message tagged with its last ID around the ring in order to inform the initiator that started the election with this ID that it is the leader.

To be more precise, at the start of an election round, each active process sends its ID to its next neighbor, with a 0 attached. When an active process $r$ receives this message $\langle \mathbf { i d } , p , 0 \rangle$ , it stores the $\mathrm { I D } ~ p$ and passes on the message with a 1 attached. And when $r$ receives a message $\left. \mathbf { i d } , q , 1 \right.$ , it stores the $\operatorname { I D } q$ . The bits 0 and 1 allow $r$ to determine that $p$ is located between $q$ and $r$ , ,. Now there are three cases:

• If max $\{ q , r \} < p$ , then $r$ enters another round with the new ID $p$ by sending $\langle \mathbf { i d } , p , 0 \rangle$ .   
• If max $\{ q , r \} > p$ , then $r$ becomes passive.   
• If max $\{ q , r \} = p$ , then $r$ becomes the leader (or sends out a special leader message tagged with $r _ { . }$ ).

If a message for a future election round is received by an active process, this message is buffered until it is clear whether the process remains active in that round.

Example 9.4 Just like Franklin’s algorithm, the Dolev-Klawe-Rodeh algorithm takes just two rounds to terminate on the undirected version of the ring in example 9.1.

Example 9.1 shows that an active process $r$ that collects IDs $p$ and $q$ in an election round must really act as if it is the middle process, $p$ . If $r$ would proceed to the next round if its own ID was the largest, then it is easy to see that the message complexity of the Dolev-Klawe-Rodeh algorithm on the ring in example 9.1 would become $O ( N ^ { 2 } )$ . Because then in each successive round, only the active process with the smallest ID among all active processes would become passive.

Example 9.5 We run the Dolev-Klawe-Rodeh algorithm on the ring in example 9.3, oriented in the clockwise direction.

Processes 0, 1, and 2 progress to the second election round because they act like processes 5, 3, and 4, respectively. For instance, process 0 collects the IDs 5 (with a 0 attached) and 1 (with a 1 attached), concludes that 5 is the largest ID among 0, 5, and 1, and progresses to the second round with the ID 5, and likewise for processes 1 and 2. Processes 3, 4, and 5 become passive in the first round because they act like processes 2, 0, and 1, respectively.   
Only process 2 (which assumed the ID 4 for the second round) progresses to the third round, because in the second round it collects the IDs 5 (with a 0 attached) and 3 (with a 1 attached) and concludes that 5 is the largest ID among 4, 5, and 3. Processes 0 (which assumed the ID 5) and 1 (which assumed the ID 3) become passive in the second round.   
Finally, in the third round, process 2 (which assumed the ID 5 for the third round) finds that it is the leader, because it receives back its own ID, first with a 0 attached and next with a 1 attached. Alternatively, process 2 can announce to the other processes that 5 is the largest ID in the ring, after which the process that carried the ID 5 at the start of the election becomes the leader.

The worst-case message complexity of the Dolev-Klawe-Rodeh algorithm is the same as that of Franklin’s algorithm: $O ( N { \cdot } \log N )$ . For there are at most $\lfloor \log _ { 2 } N \rfloor + 1$ rounds, each taking $2 N$ messages. It can be shown that $\mathcal { Q } ( N { \cdot } \log N )$ is a lower bound on the average-case message complexity of any election algorithm for rings.

# 9.2 Tree Election Algorithm

The tree algorithm from section 4.2 serves as the basis for an election algorithm in acyclic undirected networks. The idea is that each process $p$ sends to its parent the largest process ID in the subtree rooted in $p$ . That is, $p$ collects IDs from its children, computes the maximum of these IDs and its own ID, and sends this maximum to its parent. The two decision events determine the overall maximum among the IDs in the network. All processes are informed of this maximum.

In election algorithms, the initiators can be any nonempty set of processes, while the tree algorithm crucially starts from all leaves in the network. To bridge this gap, the tree election algorithm is booted by a wake-up phase, driven by the initiators, which send a wake-up message to all their neighbors. These wake-up messages are then flooded through the network: when a noninitiator receives its first wake-up message, it wakes up and sends a wake-up message to all its neighbors. When a process has received a wake-up message from all its neighbors, it starts the election phase, based on the tree algorithm.

The local election algorithm at a process $p$ is as follows:

$p$ waits until it has received IDs from all its neighbors except one, which becomes its parent.   
$p$ computes the largest ID $\operatorname* { m a x } _ { p }$ among the received IDs and its own ID.   
$p$ sends a parent message to its parent, tagged with $\operatorname* { m a x } _ { p }$ .   
If $p$ receives a parent message from its parent, tagged with an $\textrm { I D } r$ , then it computes $\operatorname* { m a x } _ { p } ^ { \prime }$ , being the maximum of $r$ and $\operatorname* { m a x } _ { p }$ . Next, $p$ sends an information message to all neighbors except its parent, tagged with $\operatorname* { m a x } _ { p } ^ { \prime }$ .   
If $p$ receives an information message from its parent, tagged with the largest ID in the network, then it forwards this message to its children.

Thus, the information message is forwarded through the entire network, and eventually the process with the largest ID becomes the leader.

The only tricky part of the algorithm is at the two neighbors $p$ and $q$ where the decide events happen. When $p$ receives a parent message from $q$ , tagged with an $\operatorname { I D } r$ , it must compute the maximum of $r$ and the value of $\operatorname* { m a x } _ { p }$ it computed earlier. Likewise, $q$ must compute the maximum of the ID it receives from $p$ and the value of $\operatorname* { m a x } _ { \boldsymbol { q } }$ it computed earlier. The reason is that $p$ and $q$ computed the maximum among all IDs in disjoint parts of the network, which together cover the entire network.

Example 9.6 In the pictures here, we consider one possible computation of the tree election algorithm on the network. The wake-up phase is omitted. Messages that are depicted with a solid arrowhead are toward a parent.

![](images/a53ee7f656f7d9b0b03858fbc77c5706b859e64325f029890f52186d60c3cd87.jpg)

In the first picture, the leaves 2, 4, 5, and 6 have selected their only neighbor as their parent and have sent their ID to their parent. In the second picture, process 1 has received the messages from 2 and 4, calculated the maximum, 4, made its remaining neighbor, 3, its parent, and sent the maximum to its parent.

![](images/1942671cd8358c33d5509efac102296051044cf1d7711549c4d5e914c370b649.jpg)

In the third picture, process 3 has received the messages from 1 and 6, calculated the maximum, 6, made its remaining neighbor, 5, its parent, and sent the maximum to its parent. In the fourth picture, processes 3 and 5 have received each other’s messages, and calculated the maximum, 6, concluding that 6 must become the leader; process 3 has, moreover, sent 6 to its two children.

![](images/1901fb309ac2dde525e542e9c7f9f347288bfe0808d14f75ad1b226b134e301d.jpg)

In the fifth picture, processes 1 and 6 have received the message from 3, process 6 has become the leader, and process 1 has sent the $\mathrm { I D } 6$ to its two children. When these two messages have arrived, the algorithm has terminated.

Just like the tree algorithm, the tree election algorithm takes $2 N - 2$ messages: two messages per channel. The wake-up phase also takes $2 N - 2$ messages.

# 9.3 Echo Algorithm with Extinction

We now discuss an election algorithm for undirected networks that works for any topology. The idea is to let each initiator start a run of the echo algorithm from section 4.3, tagged with its ID. Only the wave started by the initiator with the largest ID completes, after which that initiator becomes the leader. Noninitiators join the first wave that hits them. If a process in a wave is hit by another wave with a larger ID, then it switches to that wave; if it is hit by another wave with a smaller ID, it dismisses that wave message.

At any time, each process takes part in at most one wave. Suppose a process $p$ that is participating in a wave tagged with $q$ is hit by a wave tagged with $r$ .

• If $q < r$ , then $p$ makes the sender its parent, switches to the wave tagged with $r$ (it abandons all the wave messages it received earlier), and treats the incoming message accordingly.

• If $q > r$ , then $p$ continues with the wave tagged with $q$ (it dismisses the incoming message).   
• If $q = r$ , then $p$ treats the incoming message according to the echo algorithm of the wave tagged with $q$ .

If the wave tagged with $p$ completes by executing a decide event at $p$ , then $p$ becomes the leader.

Waves of initiators that do not have the largest ID among all initiators will not complete (that is, they are extinguished), because the initiator with the largest ID will refuse to take part in those waves. Conversely, the wave of the initiator with the largest ID is guaranteed to complete, because each process will eventually switch to that wave.

Example 9.7 We consider a computation of the echo algorithm with extinction on an undirected ring of three processes, 0, 1, and 2, all of which are initiators.

The three processes all start a wave and send a wave message to their two neighbors, tagged with their ID. The wave messages from 0, tagged with 0, are dismissed by 1 and 2. 0 receives the wave message from 1, tagged with 1. As a result, 0 switches to 1’s wave, makes 1 its parent, and sends a wave message to 2, tagged with 1. The wave messages from 0 and 1, tagged with 1, are dismissed by 2. 0 and 1 receive the wave message from 2, tagged with 2. As a result, they switch to 2’s wave, make 2 their parent, and send wave messages to each other, tagged with 2. $\mathrm { ~ - ~ } 0$ and 1 receive each other’s wave messages, tagged with 2. Next, they send wave messages tagged with 2 to their parent 2. 2 receives the wave messages from 0 and 1, tagged with 2. As a result, 2’s wave decides and 2 becomes the leader.

The worst-case message complexity of this echo algorithm with extinction is $O ( N \cdot E )$ : there are at most $N$ waves, and each wave uses at most $2 E$ messages.

# 9.4 Minimum Spanning Trees

We now turn our attention to a topic that at first sight has little to do with election: minimum spanning trees. However, the distributed algorithm for constructing a minimum spanning tree that is discussed in this section will turn out to yield an efficient election algorithm.

An undirected weighted network is given, in which the channels carry positive weights. A minimum spanning tree is a spanning tree of the network for which the sum of the weights of its channels is minimal. Such spanning trees can be employed, for example, to minimize the cost of broadcasting messages through the network or of distributing electricity over an electrical grid.

For convenience, we assume that different channels in the network always have different weights; this guarantees that the minimum spanning tree is unique. Alternatively, we could allow different channels to have the same weight and could impose a total order on channels with the same weight by using the IDs of the end points of a channel.

The Gallager-Humblet-Spira algorithm is a distributed version of Kruskal’s famous algorithm for computing minimum spanning trees in a uniprocessor setting. We first briefly discuss Kruskal’s algorithm, which uses the notion of a fragment, being any connected subgraph of the minimum spanning tree. A channel in the network is said to be an outgoing edge for a fragment if exactly one of the processes connected by the channel is in the fragment. Kruskal’s algorithm is based on the observation that the lowest-weight outgoing edge $c$ of a fragment $F$ is always in the minimum spanning tree. Suppose, toward a contradiction, that this is not the case. Then the minimum spanning tree extended with $c$ would contain a cycle, which would include $c$ and another outgoing edge $d$ of $F$ . Replacing $d$ by $c$ in the minimum spanning tree would give another spanning tree of the network, and the sum of the weights of its channels would be smaller than for the minimum spanning tree. This is a contradiction.

In Kruskal’s algorithm, initially each process forms a separate fragment. In each step, two different (disjoint) fragments are joined into one fragment via a channel between these fragments that is the lowest-weight outgoing edge for at least one of the two fragments. The algorithm terminates when only one fragment remains.

In a distributed setting, it is complicated for a process to decide whether or not its channels are outgoing edges with regard to the fragment in which the process resides. For each of its channels, it must communicate with the process at the other side to find out whether it is in the same fragment. If some of its channels turn out to be outgoing edges, the process needs to work together with the other processes in its fragment to determine whether one of them is the lowest-weight outgoing edge of the entire fragment. And when finally the lowest-weight outgoing edge for the fragment has been detected, the fragment at the other side of the channel has to be asked to join together so that the two fragments become one.

In the Gallager-Humblet-Spira algorithm, each fragment carries a name, which is a nonnegative real number, and a level, which is a natural number. Processes keep track of the name and level of their fragment. Each fragment has a unique name, except initially, when each process starts as a fragment with name and level 0. The level of a fragment is the maximum number of joins any process in the fragment has experienced. When two fragments join, there are two scenarios. If the two joining fragments have different levels, the one with the lowest level copies the name and level of the other fragment (in which case the processes in the other fragment do not experience the join). If they have the same level, the new name of the joint fragment is the weight of the core edge via which they are joined, and their level is increased by 1.

The core edge of a fragment, which is the last channel via which two of its subfragments were joined at the same level, plays a key role in the algorithm. It is the central computing unit of the fragment, to which the processes in the fragment report the lowest-weight outgoing edge they are aware of, and from which the join via the lowest-weight outgoing edge of the fragment is initiated. Each process has a parent, toward the core edge of its fragment (except initially, when fragments consist of a single process). The end points of a core edge are called the core nodes; they have each other as parent.

Processes are in one of the following three states:

sleep: This is a special state for noninitiators, so that this algorithm for computing minimum spanning trees can be easily turned into an election algorithm, where we must allow for any nonempty set of initiators. A process that is asleep wakes up as soon as it receives any message. find: The process is looking for its lowest-weight outgoing edge and/or waiting for its children to report the lowest-weight outgoing edge they are aware of.

• found: The process has reported the lowest-weight outgoing edge it is aware of to its parent and is waiting either for an instruction from the core edge that a join should be performed via that channel or for a message informing it that a join has been completed elsewhere in the fragment.

Moreover, processes maintain a status for each of their channels:

• basic edge: It is undecided whether the channel is part of the minimum spanning tree.   
branch edge: The channel is part of the minimum spanning tree. rejected: The channel is not part of the minimum spanning tree.

Each initiator, and each noninitiator after it has woken up, sets its lowest-weight channel to branch, its other channels to basic, and its state to found. It sends the message ⟨connect $0 \rangle$ into the branch edge to inform ,the fragment at the other side that it wants to join via this channel and that its fragment has level 0.

Let two fragments, one with name $f n$ and level $\ell$ and the other with name $f h ^ { \prime }$ and level $\ell ^ { \prime }$ , be joined via channel $p q$ , where $p$ is in the first fragment and $q$ ℓis in the second fragment. Let $\ell \leq \ell ^ { \prime }$ ℓ. As explained earlier, there are two possible scenarios:

• If $\ell < \ell ^ { \prime }$ , then in the past find $p$ sent $\langle \mathbf { c o n n e c t } , \ell \rangle$ to $q$ , and now $q$ sends the message ⟨initiate, $\begin{array} { r } { f n ^ { \prime } , \ell ^ { \prime } , \frac { f n d } { f o u n d } \rangle } \end{array}$ to ℓ < ℓ. We write $\frac { f n d } { f o u n d }$ , ℓ , ℓ ,to express that this parameter can be either find or found, depending on the state $q$ is in. If $\ell = \ell ^ { \prime }$ , then in the past $p$ and $q$ sent $\langle \mathbf { c o n n e c t } , \ell \rangle$ to each other, and now they send the message ℓ ℓ⟨initiate $w e i g h t ( p q ) , \ell + 1 , f u n d \rangle$ to each other.

Upon receipt of a message ⟨initiate, assumes the state find or found dep $\it f n , \itell , \frac { \it f n d } { \it f o u n d } \rangle$ , a process stores fn and he last parameter in the $\ell$ as the name and level of its fragment,message, and adopts the sender as its parent. It passes on the message through its other branch edges.

In the first scenario, $q$ is in the fragment with the higher level, so its initiate message imposes the name and level of its fragment onto $p$ . Moreover, $p$ makes $q$ its parent, toward the core edge of $q$ ’s fragment. By forwarding the initiate message through its other branch edges, $p$ ensures that all other processes in its fragment update the name and level of their fragment and select a new parent toward the core edge of $q$ ’s fragment.

In the second scenario, both fragments have the same level, so the joint fragment gets a new name, level, and core edge. The new name is the weight of the channel $p q$ , the new level is the old level plus 1, and the new core edge is pq. Since all processes in both fragments must be informed, $p$ and $q$ send an initiate message with the new name and level to each other. As this message is being forwarded through the branch edges, the processes in the joint fragment select a new parent toward the core edge $p q$ . The parameter find in the initiate message makes sure that these processes, moreover, start looking for the lowest-weight outgoing edge of the joint fragment.

When a process $p$ receives a message ⟨initiate $f n , \ell , f n d \rangle$ , it checks in increasing order of weight whether one of its basic edges $p q$ is outgoing by sending $\langle \mathbf { t e s t } , f n , \ell \rangle$ to $q$ and waiting for an answer from $q$ . A basic edge $p q$ that was found to be outgoing earlier must be tested again because in the meantime the fragments of $p$ and $q$ may have joined via some other channel. Upon receipt of the test message, $q$ acts as follows:

• If $\ell$ is greater than the level of $q$ ’s fragment, then $q$ postpones processing the incoming test message until ℓthe level of $q$ ’s fragment has reached or surpassed $\ell$ . The reason for this postponement is that $p$ and $q$ ℓmight actually be in the same fragment, in which case the message ⟨initiate $f n , \ell , f n d \rangle$ is on its way to $q$ .

If $\ell$ is not greater than the level of $q$ ’s fragment, then $q$ checks whether the name of $q$ ’s fragment is $f n$ . ℓIf so, then $q$ replies with a reject message to $p$ (except if $q$ is awaiting a reply to a test message to $p$ , because then $p$ and $q$ can interpret each other’s messages $\langle \mathbf { t e s t } , f n , \ell \rangle$ as a reject), and as a result, $p$ and $q$ both set the status of the channel $p q$ to rejected. If not, then $q$ , , ℓreplies with an accept message to $p$ .

When a basic edge $p q$ is accepted or there are no basic edges at $p$ left, $p$ stops the search for its lowest-weight outgoing basic edge.

Moreover, $p$ waits for report messages through its branch edges, except the one to its parent. Then $p$ sets its state to found and computes the minimum $\lambda _ { p }$ of these reports and the weight of its lowest-weight outgoing basic edge (or $\infty$ λ, if no such edge was found). If $\lambda _ { p } < \infty$ , then $p$ stores the branch edge through which it received $\lambda _ { p }$ , or its outgoing basic edge of weight $\lambda _ { p }$ λ <. Finally, $p$ sends $\langle \mathbf { r e p o r t } , \lambda _ { p } \rangle$ to its parent.

λ λ , λOnly the core nodes receive a report message from their parent. Thus, the core nodes can determine the weight $\mu$ of the lowest-weight outgoing edge of their fragment. If $\mu$ is $\infty$ , then the core nodes terminate, µbecause the entire minimum spanning tree has been computed. If $\mu$ µis not $\infty$ , then the core node that received $\mu$ µfirst sends a changeroot message via branch edges toward the process $p$ that originally reported a lowestµweight outgoing basic edge $p q$ with weight $\mu$ . Here it is utilized that processes stored their branch edge that reported $\mu$ µ. From then on, the core edge becomes a regular tree edge. When $p$ receives the changeroot message, it sets the channel $p q$ to branch and sends $\langle \mathbf { c o n n e c t } , \ell \rangle$ into it, where $\ell$ is the level of $p$ ’s fragment.

Let a process $q$ receive a message $\langle \mathbf { c o n n e c t } , \ell \rangle$ , ℓfrom a neighbor $p$ ℓ. We note that the level of $q ^ { \dagger }$ ’s fragment is at least $\ell$ : either $\ell = 0$ , or $q$ , ℓearlier sent accept to $p$ , which it could only do if its fragment had a level of at least $\ell$ ℓ ℓ, and fragment levels never decrease over time. Now $q$ acts as follows:

As long as $q$ ’s fragment also has level $\ell$ and $q p$ is not a branch edge, $q$ postpones processing the connect message from $p$ ℓ. The reason for this postponement is that $q$ ’s fragment might be in the process of joining a fragment with a level $\geq \ell$ , in which case $p$ ’s fragment should subsume the name and level of that joint fragment (instead of $w e i g h t ( p q )$ and $\ell + 1$ ).   
If the level $\ell ^ { \prime }$ of $q$ ℓ’s fragment is or becomes greater than $\ell$ , then $q$ sets the channel $q p$ to branch and sends ⟨initiate $\quad f n ^ { \prime } , \ell ^ { \prime } , \frac { \bar { \hbar } n d } { f o u n d } \rangle$ to $p$ , where $f h ^ { \prime }$ is the name of $q$ ℓ’s fragment and find or found depends on the state of $q$ .   
If $q$ ’s fragment has level $\ell$ and $q p$ is or becomes a branch edge (in which case $q$ sent $\langle \mathbf { c o n n e c t } , \ell \rangle$ to $p$ ), then $q$ sends ⟨initiate $w e i g h t ( q p ) , \ell + 1 , f u n d \rangle$ to $p$ (and vice versa).

In the last case, $p q$ becomes the core edge of the joint fragment.

This completes the description of the Gallager-Humblet-Spira algorithm; we are back at the situation where two fragments are joined at a different level or the same level by means of one or two initiate messages, respectively, which was explained earlier.

Example 9.8 We consider one possible computation of the Gallager-Humblet-Spira algorithm on the following network, in which all processes are initiators.

![](images/717104ff54668f7332a206b2c71faed2b863461ebb0946b18c527d53b0e09518.jpg)

$p$ and $q$ send $\langle \mathbf { c o n n e c t } , 0 \rangle$ to each other, and both make $p q$ a branch edge. Since these fragments join at the same level, 0, $p$ ,and $q$ send ⟨initiate 5 1 find⟩ to each other. Next, $p$ and $q$ send ⟨test 5 1⟩ to $s$ and $r$ , respectively. Since $s$ and $r$ , , ,are at level 0, they postpone processing these messages.   
$t$ sends $\langle \mathbf { c o n n e c t } , 0 \rangle$ to $q$ and makes tq a branch edge. Since the fragment of $q$ is at level 1, $q$ replies with ,⟨initiate 5 1 find⟩. Then $t$ sends $\langle \mathbf { r e p o r t } , \infty \rangle$ to its new parent $q$ , since $t$ has no other channels except tq. $r$ and $s$ , , ,send $\langle \mathbf { c o n n e c t } , 0 \rangle$ , to each other, and both make $r s$ a branch edge. Since these fragments join at the same level, 0, $r$ ,and $s$ send ⟨initiate 3 1 find⟩ to each other. Next, $r$ and $s$ send $\left. \mathbf { t e s t } , 3 , 1 \right.$ to $q$ and $p$ , respectively.   
Since the fragments of $r$ and $s$ are at the same level as the fragments of $q$ and $p$ but have different names, $r$ and $s$ reply to the test messages from $q$ and $p$ , respectively, with an accept message. As a result, $p$ sends $\langle \mathbf { r e p o r t } , 9 \rangle$ to its parent $q$ , while $q$ sends $\langle \mathbf { r e p o r t } , 7 \rangle$ to its parent $p$ . Since 7 is smaller than 9, $q$ sends $\left. \mathbf { c o n n e c t } , 1 \right.$ to $r$ . Since $r$ ,is at level 1 and does not yet consider the channel $r q$ a branch edge, it postpones processing this message.   
Since the fragments of $p$ and $q$ are at the same level as the fragments of $s$ and $r$ but have different names, $p$ and $q$ can reply to the test messages from $s$ and $r$ , respectively, with an accept message. As a result, $r$ sends $\langle \mathbf { r e p o r t } , 7 \rangle$ to its parent $s$ , while $s$ sends $\langle \mathbf { r e p o r t } , 9 \rangle$ to its parent $r$ . Since 7 is smaller than 9, $r$ sends ,⟨connect 1⟩ to $q$ .   
,By the crossing $\left. \mathbf { c o n n e c t } , 1 \right.$ messages between $q$ and $r$ , the channel between these processes becomes a ,branch edge as well as the core edge of the new fragment, which has level 2. Messages ⟨initiate 7 2 find⟩ are forwarded through the branch edges. The channels $p s$ and $p r$ , , ,are tested (in this order) from either side, both times leading to a reject. Finally, all processes report $\infty$ to the core edge $q r$ , and the algorithm terminates.

The computed minimum spanning tree consists of the channels pq, qr, qt, and rs.

We argue that the Gallager-Humblet-Spira algorithm is deadlock-free. There are two potential causes for deadlock, because a process $q$ may postpone an incoming message. The first case is if $q$ receives a message ⟨test $f _ { n , \ell } )$ while $\ell$ is greater than the level of $q$ ’s fragment. This postponement does not lead to a deadlock, , , ℓ ℓbecause there is always a fragment of minimal level, and test messages originating from this fragment will be answered promptly. The second case is if $q$ receives a message $\langle \mathbf { c o n n e c t } , \ell \rangle$ while the level of $q$ ’s fragment equals $\ell$ and $q p$ , ℓis not a branch edge. This postponement also does not lead to a deadlock, because different edges have different weights, so there cannot be a cycle of fragments waiting for a reply to a postponed connect message (see exercise 9.14).

The worst-case message complexity of the Gallager-Humblet-Spira algorithm is $O ( E + N { \cdot } \log N )$ . The summand $E$ is the accumulation of all messages for rejecting channels: each channel outside the minimum spanning tree is rejected by a test-reject or test-test pair. This adds up to $2 { \cdot } ( E - \left( N - 1 \right) )$ messages in total. Furthermore, each process experiences at most $\lfloor \log _ { 2 } N \rfloor$ joins, because each time this happens, the level at the process increases, and a fragment at a level $\ell$ contains at least $2 ^ { \ell }$ processes (see exercise 9.12). Every time ℓa process experiences a join, it receives an initiate message and may send the following messages: one test that triggers an accept, a report, and a changeroot or connect. Including the accept, there are five messages every time a process experiences a join, adding up to at most $5 N { \cdot } \lfloor \log _ { 2 } N \rfloor$ messages in total. This analysis covers all messages in the algorithm.

Finally, as promised at the start of this section, we return to election. By two extra messages at the very end of the Gallager-Humblet-Spira algorithm, the core node with the largest ID can become the leader. This yields an election algorithm for undirected networks. Weights on channels are not needed, a total order on channels suffices, which can for instance be imposed by means of a lexicographical order based on the IDs of the processes connected by a channel.

The lower bound of $\mathcal { Q } ( N { \cdot } \log N )$ for rings, mentioned earlier, implies a lower bound of $\mathcal { Q } ( E + N { \cdot } \log N )$ Ω Ωon the average-case message complexity of any election algorithm for general networks. So the message complexity of the Gallager-Humblet-Spira algorithm is optimal.

# Bibliographical notes

The Chang-Roberts algorithm originates from [26], and Franklin’s algorithm was proposed independently in [56] and in [46]. The Dolev-Klawe-Rodeh algorithm was proposed independently in [37] and in [95], under the assumption that channels are FIFO. The lower bound of $\mathcal { Q } ( N { \cdot } \log N )$ on the average-case message Ωcomplexity of election algorithms for rings was proved in [91]. The Gallager-Humblet-Spira algorithm stems from [49].3

# 9.5 Exercises

Exercise 9.1 [117] Consider the Chang-Roberts algorithm on a directed ring of size $N$ , under the assumption that every process is an initiator. For which distribution of IDs over the ring is the message complexity minimal, respectively maximal, and exactly how many messages are exchanged in these cases? Argue why no distribution of IDs gives rise to fewer or more messages, respectively.

Exercise 9.2 Consider Franklin’s algorithm.

(a) Give an example in which an active process, which will eventually progress to round 1, receives a message for round 1 before receiving the message for round 0 from this same direction, where these two messages carry different IDs.

(b) Explain why this does not jeopardize correctness, even if round numbers were omitted from messages. (c) Argue that an active process in round $n$ , which will eventually progress to round $n + 1$ , cannot receive a message for round $n + 2$ .

Exercise 9.3 [117] Give an initial configuration of a directed ring of size $N$ , with every process an initiator, for which the Dolev-Klawe-Rodeh algorithm requires only two rounds. Also give an initial configuration for which the algorithm requires $\lfloor \log _ { 2 } N \rfloor + 1$ rounds.

Exercise 9.4 Consider the Dolev-Klawe-Rodeh algorithm.

(a) Give an example run on a directed ring of seven processes to show that an active process can receive a message for two rounds ahead.   
(b) Argue that for all $k \geq 1$ , in a directed ring with $2 ^ { k + 1 } - 1$ processes, an active process can receive a message for $k$ rounds ahead.

Exercise 9.5 Give a computation of the tree election algorithm on the network from example 9.6 in which eventually processes 1 and 4 have each other as parent.

Exercise 9.6 Adapt the tree election algorithm so that among the initiators of election, the one with the largest ID becomes the leader.

Exercise 9.7 Consider the tree election algorithm, including the wake-up phase at the start as well as the announcement phase at the end.

(a) [117] Argue that for undirected networks with a diameter $D > 1$ , the time complexity of this algorithm is at most $2 D$ . (b) For $D = 2$ , give an example where this algorithm takes four time units to terminate. (c) Give an example to show that if $D = 1$ , this algorithm may take three time units to terminate.

Exercise 9.8 Develop an election algorithm for general undirected networks based on Cidon’s depth-first search algorithm and the extinction principle. What is the worst-case message complexity of your algorithm?

Exercise 9.9 Would the election algorithms in sections 9.1-9.3 still be correct if the initiator with the smallest (instead of the largest) ID were made the leader? If so, explain how the algorithms can be adapted. If not, explain what could go wrong.

Exercise 9.10 Give one possible computation of the Gallager-Humblet-Spira algorithm on the following undirected weighted network in order to determine the minimum spanning tree.

![](images/d120ce9ee03279d9c7305a78c81de78573ff02a16fb544fd6acd1780210e5d76.jpg)

Exercise 9.11 Give one possible computation of the Gallager-Humblet-Spira algorithm on the following undirected weighted network to determine a minimum spanning tree.

![](images/4f050f4dc658ae138b7eaa53b8c8e981ab2ecf09421a7c141a1bcbfe01600e3d.jpg)

Note that three channels have the same weight. To avoid deadlock, we define an ordering on these channels: $p q < p r < q r$ . During the computation, the handling of test messages from $r$ and $t$ and of a connect message <from $r$ <should be delayed at $p$ .

Exercise 9.12 Argue that in the Gallager-Humblet-Spira algorithm, any fragment at a level $\ell$ always contains at least $2 ^ { \ell }$ processes.

Exercise 9.13 Argue that the Gallager-Humblet-Spira algorithm is deadlock-free.

Exercise 9.14 Suppose that the Gallager-Humblet-Spira algorithm is applied to an undirected weighted network in which different channels may have the same weight. (If a fragment has multiple lowest-weight outgoing edges, one of them can be chosen arbitrarily to connect to a neighboring fragment, and the unique name of a fragment consists of the process IDs of its core nodes.) Give an example to show that a deadlock can occur. Also argue that the deadlock in your example is avoided if a total order is imposed on channels with the same weight.

Exercise 9.15 Suppose that, at some point in the Gallager-Humblet-Spira algorithm, a process reported one of its channels as the (locally) lowest-weight outgoing basic edge, and next it receives a message ⟨initiate fn find⟩. Explain by means of a scenario why it must test again whether this basic edge is outgoing.

Exercise 9.16 Suppose that, at some point in the Gallager-Humblet-Spira algorithm, a process $p$ receives a message $\langle \mathbf { t e s t } , f n , \ell \rangle$ through channel $p q$ , where $p$ ’s fragment has a different name than $f n$ and at least level $\ell$ . Explain why $p$ , ℓcan send an accept message to $q$ without fear that $p$ and $q$ are in the same fragment.

Exercise 9.17 Consider the following scenario for the Gallager-Humblet-Spira algorithm. In a fragment $F$ with level $\ell$ , the core nodes have just determined the lowest-weight outgoing edge of $F$ . Concurrently, another ℓfragment with a level $\ell ^ { \prime } < \ell$ connects to $F$ via a channel $q p$ . Why can we be sure that $F$ has an outgoing edge ℓ < ℓwith a lower weight than pq?

# Anonymous Networks

Sometimes the processes in a network are anonymous, meaning that they lack a unique ID. Typically, this is the case if there are no unique hardware IDs (for example, LEGO Mindstorms). Furthermore, when each process does have a unique ID but cannot reveal it to the other processes, from the perspective of the network this is similar to having no unique process IDs at all. For instance, processes may not want to reveal their IDs because of security concerns, or transmitting or storing IDs may be deemed too expensive, as is the case for the IEEE 1394 serial bus discussed in section 10.7.

In this chapter, it is assumed that processes (and channels) do not have unique IDs.

# 10.1 Impossibility of Election in Anonymous Rings

We show that no election algorithm for anonymous networks always terminates. The idea is that if the initial configuration is symmetric (typically, a ring in which all processes are in the same state and all channels are empty), then there is always an infinite execution that cannot escape this symmetry. Apparently, unique process IDs are a crucial ingredient for the election algorithms in chapter 9 in order to break symmetry.

Note that, vice versa, if one leader has been elected, all processes can be given a unique ID using a traversal algorithm (see section 4.1) initiated by the leader.

We recall from chapter 9 that election algorithms are decentralized. The initiators can be any nonempty set of processes, and all processes must have the same local algorithm.

Theorem 10.1 No election algorithm for anonymous rings always terminates.

Proof. Suppose we have an election algorithm for (directed or undirected) anonymous rings. We run it on an anonymous ring of size $N > 1$ .

>A configuration of the algorithm on the ring is symmetric if all processes are in the same state and all channels carry the same messages. We make three observations:

There is a symmetric initial configuration: all processes can be provided with the same initial state, and initially all channels are empty.

If $\gamma _ { 0 }$ is a symmetric configuration and $\gamma _ { 0 }  \gamma _ { 1 }$ , then there is a sequence of transitions $\gamma _ { 1 } \to \gamma _ { 2 } \to \cdots \to \gamma _ { N }$ where $\gamma _ { N }$ is symmetric. That is, the transition $\gamma _ { 0 }  \gamma _ { 1 }$ is caused by an internal, send, or receive event at γsome process. Since in $\gamma _ { 0 }$ γ γall processes are in the same state and all channels carry the same messages, all γother processes in the ring can also perform this event, and the resulting configuration $\gamma _ { N }$ is symmetric. γIn a symmetric configuration, there is not one leader, because all processes are in the same state.

These observations together imply that the election algorithm exhibits an infinite execution, which infinitely often visits symmetric configurations. ⊓⊔

We can even construct an infinite execution that is fair; that is, if an event can happen in infinitely many configurations in the execution, then this event is performed infinitely often during the execution. Given the symmetric configuration $\gamma _ { 0 }$ in the third case just given, it does not matter which event available in $\gamma _ { 0 }$ is used for the transition $\gamma _ { 0 }  \gamma _ { 1 }$ γ; we can always build the transition sequence to the symmetric configuration $\gamma _ { N }$ . γ γThis implies that we can make sure no event is ignored infinitely often in the infinite execution.

For the impossibility result in theorem 10.1 it is essential that asynchronous message passing communication is used. Election algorithms that always terminate with a single leader do exist for anonymous rings with synchronous communication.

# 10.2 Probabilistic Algorithms

In view of the impossibility result in theorem 10.1, we now turn to probabilistic algorithms, in which a process may, for example, flip a coin and perform an event based on the outcome of this coin flip. That is, events can happen with a certain probability.

For probabilistic algorithms, one can calculate the probability that an execution from some given set of possible executions will occur. Although in the previous section we proved that election algorithms for anonymous rings inevitably contain infinite executions, in the next section we will see that there exists such an algorithm in which the probability that an infinite execution occurs is zero.

Probabilistic algorithms for which all executions terminate in a correct configuration are in general not so interesting, because any deterministic version of such an algorithm (for example, let the coin flip always yield heads) produces a correct nonprobabilistic algorithm. We therefore consider two classes of probabilistic algorithms: ones that always terminate but that may terminate incorrectly and ones that may not terminate but if they do the outcome is always correct.

A probabilistic algorithm is Las Vegas if • the probability that it terminates is greater than zero and . all terminal configurations are correct.

It is Monte Carlo if

• it always terminates and • the probability that a terminal configuration is correct is greater than zero.

Note that if the probability that a Las Vegas algorithm terminates is one, there may still be infinite executions. But in this case the probability mass of all infinite executions together is zero. For example, consider an algorithm that flips a fair coin as long as the result is heads and that terminates as soon as the result of a coin flip is tails. The algorithm has one infinite execution, in which every time the outcome of the coin flip is heads. But the probability that this execution occurs is zero.

# 10.3 Itai-Rodeh Election Algorithm for Rings

The Itai-Rodeh election algorithm targets anonymous directed rings. Although in section 10.1 it was shown that there is no terminating election algorithm for this setting, the Itai-Rodeh election algorithm will achieve the next best thing: a Las Vegas algorithm that terminates with probability one.

We adapt the Chang-Roberts election algorithm from section 9.1 to anonymous directed rings. Since processes do not have a unique ID, initiators randomly select an ID and send out this ID; only messages with the largest ID complete their round trip. The complication is that different initiators may select the same ID, in which case the election can be inconclusive. The Itai-Rodeh election algorithm therefore progresses in election rounds. If one active process in some round selects a larger ID than any other active process, then it becomes the leader at the end of this round. If, on the other hand, multiple active processes select the largest ID in some round, then there will be a next round, in which only active processes that selected the largest ID participate; all other processes become passive. At the start of every round, the active processes randomly select a new ID. Active processes keep track of their round number, so they can recognize and ignore messages from earlier rounds. We will see that this is essential because otherwise the algorithm could terminate in a configuration where all processes have become passive.

Since different processes may select the same ID, a process cannot readily recognize its own message when it completes the round trip. Therefore, messages carry a hop count, keeping track of how many processes have been visited. A message arrives at its source if and only if its hop count is $N$ . Hence, it is required that processes know the ring size; in section 10.5, we will see that this requirement is crucial.

Now the Itai-Rodeh election algorithm is presented in more detail. Initially, at election round 0, initiators are active and noninitiators are passive. At the start of an election round $n \geq 0$ , each active process $p$ randomly selects an ID $i d _ { p }$ from $\{ 1 , . . . , N \}$ and sends the message $\left( n , i d _ { p } , 1 , f a l s e \right)$ into its outgoing channel. The first , . . . , , , ,value is the number of the election round in which this message evolved, the second value is the ID of its source, the third value is the hop count, and the fourth value is a Boolean that is set to true when an active process different from $p$ with the ID $i d _ { p }$ in round $n$ is encountered during the round trip. This allows $p$ to recognize, at the return of its message, whether another process selected the same random ID in the current election round.

Next, $p$ waits for a message $( n ^ { \prime } , i , h , b )$ to arrive. When this happens, $p$ acts as follows, depending on the parameter values in this message:

• $n ^ { \prime } > n$ , or $n ^ { \prime } = n$ and $i > i d _ { p }$ : $p$ > >has received a message from a future round, or from the current round with a larger ID. It becomes passive and sends $( n ^ { \prime } , i , h + 1 , b )$ . $n ^ { \prime } < n$ , or $n ^ { \prime } = n$ and $i < i d _ { p }$ : $p$ < <has received a message from an earlier round, or from the current round with a smaller ID. It dismisses the message.   
• $n ^ { \prime } = n$ , $i = i d _ { p }$ , and $h < N$ : $p$ has received a message from the current round with its own $\mathrm { I D }$ but with a hop count smaller than $N$ . Therefore, $p$ is not the source of this message. It sends $( n , i d _ { p } , h + 1 , t r u e )$ into its outgoing channel. $n ^ { \prime } = n$ , $i = i d _ { p }$ , $h = N$ , and $b = t r u e$ :   
$p$ has received back its own message. Since the Boolean was set to true during the round trip, another active process selected the same $\mathrm { I D }$ as $p$ in this round. Therefore, $p$ proceeds to round $n + 1$ .   
$n ^ { \prime } = n$ , $i = i d _ { p }$ , $h = N$ , and $b = f a l s e$ :   
$p$ has received back its own message. Since the Boolean is still false, all other active processes selected a smaller $\mathrm { I D }$ in this round or were still in an earlier round and have therefore become passive. Hence, $p$ becomes the leader.

Passive processes simply pass on messages that carry a hop count $< N$ , increasing their hop count by 1.

<The Itai-Rodeh election algorithm is a Las Vegas algorithm that terminates with probability one. There are infinite executions, in which the active processes keep on selecting the same ID in every election round. However, in each election round with multiple active processes, with a positive probability not all active processes select the same ID. And, in that case, not all active processes will make it to the next round. Therefore, with probability one, eventually one process will become the leader.

The following example shows that without round numbers, the algorithm would be flawed.

Example 10.1 We consider one possible computation of the Itai-Rodeh election algorithm on an anonymous directed ring of size 3. The processes $p , q$ , and $r$ are all initiators and know that the ring size is 3.

In round 0, $p$ and $q$ both select $\textrm { I D } i$ , while $r$ selects ID $j$ , with $i > j$ . The message sent by $q$ makes $r$ passive, its Boolean is set at $p$ , and it returns to $q$ . Likewise, the Boolean in the message sent by $p$ is set at $q$ , and it returns to $p$ . Next, $p$ and $q$ move to the next round.   
In round 1, $p$ and $q$ select IDs $k$ and $\ell$ , respectively, with $j > k > \ell$ . The message sent by $r$ in round 0   
is slow, only now it reaches $p$ ℓ > > ℓ. If round numbers were omitted, then $p$ and subsequently $q$ would not   
recognize that $r$ ’s message is from the previous round, and they would become passive. Owing to round numbers, however, $r ^ { \mathrm { : } }$ ’s message is dismissed by $p$ , and $p$ and $q$ continue to compete for the leadership. Since $k > \ell$ , the message from $q$ is dismissed at $p$ , while the message from $p$ makes $q$ passive and returns to $p$ > ℓwith the Boolean still false. So $p$ becomes the leader.

The computation in example 10.1 uses in an essential way that channels are non-FIFO. In case of FIFO hannels, round numbers can be omitted (see exercise 10.5).

It can be shown that if all processes are initiators, the average-case message complexity of the Itai-Rodeh election algorithm is $O ( N { \cdot } \log N )$ : on average, the $N$ messages travel a logarithmic number of hops before they are dismissed, and the average number of election rounds is finite. In view of the lower bound of $\mathcal { Q } ( N { \cdot } \log N )$ Ωon the average-case message complexity of election algorithms for rings mentioned in the previous chapter, one cannot hope to do better in a fully asynchronous setting.

Similar to the way the Chang-Roberts algorithm for election in directed rings was turned into a probabilistic version for anonymous directed rings, Franklin’s algorithm for undirected rings can be turned into a probabilistic version for anonymous undirected rings (see exercise 10.7). An advantage of the latter probabilistic algorithm, compared to the Itai-Rodeh algorithm, is that round numbers modulo 2, meaning only 0 and 1, suffice.

# 10.4 Echo Algorithm with Extinction for Anonymous Networks

The echo algorithm with extinction from section 9.3 can be adapted to anonymous undirected networks in a manner similar to the adaptation of the Chang-Roberts algorithm in the previous section. The resulting election algorithm progresses in rounds: at the start of every round, the active processes randomly select an ID and run the echo algorithm with extinction. Again, round numbers are used to recognize messages from earlier rounds. When a process is hit by a wave with a higher round number than its current wave or with the same round number but a higher ID, the process becomes passive (if it was not already) and moves to that other wave.

Each process again needs to know the network size to be able to determine at completion of its wave whether it has covered the entire network. The reason is that different waves with the same ID in the same round can collide with each other, after which these waves may both complete. These waves cover disjoint parts of the network. Therefore, when a process sends a wave message to its parent, it reports the size of its subgraph in this wave so that at the end the initiator of this wave can determine how many processes participated in the wave. If a wave completes but did not cover the entire network, then the initiator moves to the next election round. If a completed wave covered the entire network, then its initiator becomes the leader.

We now present the echo algorithm with extinction for election in anonymous undirected networks i more detail. Initially, at the start of round 0, initiators are active and noninitiators are passive.

Let process $p$ be active. At the start of an election round $n \geq 0$ , $p$ randomly selects an ID $i d _ { p } \in \{ 1 , . . . , N \}$ and starts a wave, tagged with $n$ and $i d _ { p }$ , . . . ,. As third parameter, it adds a 0, meaning that this is not a message to its parent. This third parameter is used to report the subtree size in messages to a parent.

A process $p$ , which is in a wave from round $n$ with $\operatorname { I D } i$ , waits for a wave message to arrive, tagged with a round number $n ^ { \prime }$ and an ID $j$ . When this happens, $p$ acts as follows, depending on the parameter values in this message:

• If $n ^ { \prime } > n$ , or $n ^ { \prime } = n$ and $j > i$ , then $p$ becomes passive, makes the sender its parent, changes to the wave in >round $n ^ { \prime }$ with $\operatorname { I D } j$ >, and treats the message accordingly.   
If $n ^ { \prime } < n$ , or $n ^ { \prime } = n$ and $j < i$ , then $p$ dismisses the message.   
• If $n ^ { \prime } = n$ and $j = i$ , then $p$ <treats the message according to the echo algorithm.

As noted, the echo algorithm is adapted by letting each message sent upward in the constructed tree report the size of its subtree; all other wave messages report 0. When a process decides, meaning that its wave completes, it computes the size of the constructed tree. If this equals the network size $N$ , then the process becomes the leader. Otherwise it moves to the next election round, in which it randomly selects a new ID from $\{ 1 , . . . , N \}$ and initiates a new wave.

, . . . ,This election algorithm is a Las Vegas algorithm that terminates with probability one. There are infinite executions, in which the active processes keep on selecting the same ID in every election round. However, with a positive probability, in election rounds with multiple active processes, not all active processes select the same ID. And, in that case, not all active processes will make it to the next round. Therefore, with probability one, eventually one process will become the leader.

Example 10.2 We consider one possible computation of the echo algorithm with extinction on the anonymous undirected network pictured here. All processes know that the network size is 6.

In round 0, processes $p , r$ , and $t$ select $\operatorname { I D } i$ , while processes $q , s ,$ , and $u$ select ID $j .$ , with $i > j$ . In the picture, only the messages carrying ID $i$ are shown; the messages carrying $j$ >are all dismissed at reception. Messages that are depicted with a solid arrowhead are toward a parent.

$$
\textcircled { p } \frac { \frac { ( 0 , i , 0 ) } { \ddots } } { \frac { ( 0 , i , 1 ) } { ( 0 , i , 1 ) } } \textcircled { q } \frac { \frac { ( 0 , i , 0 ) } { \ddots } } { \frac { ( 0 , i , 0 ) } { ( 0 , i , 0 ) } } \underset { ( u ) } { \overset { ( 1 , i , 0 ) } { \sim } } \bigodot \frac { \frac { ( 0 , i , 0 ) } { \sim } } { \frac { ( 0 , i , 0 ) } { \sim } } \bigodot \frac { \frac { ( 0 , i , 0 ) } { \sim } } { \frac { ( 0 , i , 1 ) } { ( 0 , i , 1 ) } } \textcircled { 1 }
$$

Processes $p , r$ , and $t$ each start their wave by sending $( 0 , i , 0 )$ to their neighbors. Next, $q$ and $s$ receive the messages from $p$ and $t$ , respectively, and send $( 0 , i , 0 )$ , ,to $r$ . When $q$ and $s$ receive $( 0 , i , 0 )$ from $r$ , they interpret this as an answer to their message to $r$ , ,, reporting a subtree of size 0. So $q$ and $s$ ,report a subtree of size 1 to $p$ and $t$ , respectively. Moreover, $u$ receives $( 0 , i , 0 )$ from $r$ and reports a subtree of size 1 to $r$ . Finally, $p , r$ , and $t$ , ,each compute that their wave covered two processes and move to round 1.

– In round 1, $p$ selects $\mathrm { I D } k$ , while $r$ and $t$ select ID $\ell$ , with $k > \ell$ . In the next picture, only the messages carrying the $\operatorname { I D } k$ are shown.

$$
\begin{array}{c} \textcircled { \it { ‰} \textcircled { { ‰} \textcircled { { ‰} } \frac { ( 1 , k , 0 ) } { \mathfrak { A } _ { \left( 1 , k , 5 \right) } } \bigoplus _ { \begin{array} { c } { ( 1 , k , 0 ) } \\ { ( 1 , k , 4 ) } \end{array} } } \end{array} } \frac { \left( 1 , k , 0 \right) } { \mathfrak { A } _ { \left( 1 , k , 4 \right) } } \underset { \left[ 1 \right] } { \overset { \left( 1 , k , 0 \right) } { \overbrace { \mathfrak { A } _ { \left( 1 , k , 2 \right) } } } } \bigodot \frac { \left( 1 , k , 0 \right) } { \mathfrak { A } _ { \left( 1 , k , 1 \right) } } \bigodot
$$

The wave of $p$ completes and reports that it covered six processes. So $p$ becomes the leader.

Note that in round 1 another scenario would be possible, in which the wave of $t$ completes and $t$ computes that its wave covered two processes, so that it moves to round 2. However, in the computation we consider, the wave of $p$ in round 1 travels faster than the waves of $r$ and $t$ , so the wave of $p$ completes.

# 10.5 Computing the Size of an Anonymous Ring Is Impossible

In the previous sections, we discussed Las Vegas algorithms for election in anonymous networks, which require that all processes in the network know the network size. We now prove that this assumption is essential. There is no Las Vegas algorithm to compute the size of anonymous rings; every probabilistic algorithm for computing the size of anonymous rings must allow for incorrect outcomes. This implies there is no Las Vegas algorithm for election in anonymous rings if processes do not know the ring size. Because when there is one leader, network size can be computed using a wave algorithm initiated by the leader, even if the network is anonymous.

Theorem 10.2 There is no Las Vegas algorithm to compute the size of an anonymous ring.

Proof. Suppose we have an algorithm for computing the size of a (directed or undirected) anonymous ring of size $N > 2$ with processes $p _ { 0 } , . . . , p _ { N - 1 }$ . Let $C$ be a computation of the algorithm on this ring that terminates >with the correct outcome $N$ , . . . ,. We cut open this ring between $p _ { 0 }$ and $p _ { N - 1 }$ and glue a copy $p _ { 0 } ^ { \prime } , . . . , p _ { N - 1 } ^ { \prime }$ of the ring in between. That is, we now consider the following anonymous ring, of size $2 N$ .

![](images/764417db3229b1fa386fe38fc66ba174d9520ac624c63d1fa274779d961ac141.jpg)

We construct a computation $C ^ { \prime }$ of the ring size algorithm on the latter ring that produces the incorrect outcome $N$ . The computation $C ^ { \prime }$ consists of replaying $C$ twice: once on the half $p _ { 0 } , . . . , p _ { N - 1 }$ and once on the half $p _ { 0 } ^ { \prime } , . . . , p _ { N - 1 } ^ { \prime }$ . In $C ^ { \prime }$ , compared to $C$ , $p _ { 0 }$ communicates with $p _ { N - 1 } ^ { \prime }$ instead of $p _ { N - 1 }$ , and $p _ { N - 1 }$ communicates , . .with $p _ { 0 } ^ { \prime }$ instead of $p _ { 0 }$ . But since $p _ { 0 }$ and $p _ { 0 } ^ { \prime }$ send the same messages in $C ^ { \prime }$ , and likewise for $p _ { N - 1 }$ and $p _ { N - 1 } ^ { \prime }$ , and they do not have unique IDs to tell each other apart, none of these four processes can determine this difference. In $C ^ { \prime }$ , the processes in the ring of size $2 N$ terminate with the incorrect outcome $N$ . ⊓⊔

# 10.6 Itai-Rodeh Ring Size Algorithm

The Itai-Rodeh ring size algorithm targets anonymous directed rings. In section 10.5, it was shown that it must be a Monte Carlo algorithm, meaning that it must allow for incorrect outcomes. However, in the ItaiRodeh ring size algorithm, the probability of an erroneous outcome can be arbitrarily close to zero by letting the processes randomly select IDs from a sufficiently large domain.

Each process $p$ maintains an estimate $e s t _ { p }$ of the ring size; initially $e s t _ { p } = 2$ . During executions of the algorithm, the values of the $e s t _ { p }$ variables will grow, but never beyond the correct estimate $N$ . The algorithm proceeds in estimate rounds. Every time a process finds that its estimate is too conservative, it moves to another round. That is, each process $p$ initiates an estimate round at the start of the algorithm as well as at every update of $e s t _ { p }$ .

In each round, $p$ randomly selects an ID $i d _ { p }$ from $\{ 1 , \ldots , R \}$ for some positive number $R$ and sends the message $( e s t _ { p } , i d _ { p } , 1 )$ , . . . ,to its next neighbor. The third value is a hop count, which is increased by 1 every time , ,the message is forwarded.

Now $p$ waits for a message $( e s t , i d , h )$ to arrive. An invariant of such messages is that always $h \leq e s t$ When a message arrives, $p$ , ,acts as follows, depending on the parameter values in this message:

$e s t < e s t _ { p }$ :   
<The estimate of the message is more conservative than $p$ ’s estimate, so $p$ dismisses the message.   
$e s t > e s t _ { p }$ :   
>The estimate of the message improves on $p$ ’s estimate, so $p$ increases its estimate. We distinguish between   
two cases:   
– $h < e s t { : }$ <The estimate est may be correct. So $p$ sends $( e s t , i d , h + 1 )$ to give the message the chance to complete its round trip. Moreover, $p$ performs $e s t _ { p } \gets e s t$ ,. $h = e s t$ : The estimate est is too conservative because the message traveled est hops but did not complete its round trip. So $p$ performs $e s t _ { p } \gets e s t + 1$ .   
$e s t = e s t _ { p }$ :   
The estimate of the message and that of $p$ agree. We distinguish between two cases:   
– $h < e s t$ : $p$ <sends $( e s t , i d , h + 1 )$ to give the message the chance to complete its round trip. $h = e s t$ : Once again, we distinguish between two cases:   
$^ *$ $i d \neq i d _ { p }$ : The estimate est is too conservative because the message traveled est hops but did not complete its round trip. So $p$ performs $e s t _ { p } \gets e s t + 1$ .   
$^ *$ $i d = i d _ { p }$ : Possibly $p$ ’s own message returned (or a message originating from another process est hops before $p$ that unfortunately happened to select the same ID as $p$ in this estimate round). In this case, $p$ dismisses the message.

When the algorithm terminates, $e s t _ { p } \leq N$ for all processes $p$ , because a process increases its estimate only when it is certain that its current estimate is too conservative. Furthermore, $e s t _ { p }$ converges to the same value at all processes $p$ . If this were not the case, clearly there would be processes $p$ and $q$ where $p$ is $q$ ’s direct predecessor in the ring and $p$ ’s final estimate is greater than that of $q$ . But then $p$ ’s message in its final estimate round would have increased $q$ ’s estimate to $p$ ’s estimate.

The Itai-Rodeh ring size algorithm is a Monte Carlo algorithm: it may terminate with an estimate smaller than $N$ . This can happen if in a round with an estimate $e s t < N$ all processes at distance est from each other happen to select the same ID.

Example 10.3 We consider one possible computation of the Itai-Rodeh ring size algorithm on the following anonymous ring, which is directed in a clockwise fashion.

![](images/9969d47a47eb25d484f702ad6d959743f8e8b91f478710489074c1395fce4d1a.jpg)

In the initial estimate round with estimate 2, let $p$ and $r$ select ID $i$ , while $q$ and $s$ select ID $j$ . Then $p$ and $r$ send the message (2 i 1), which is forwarded by $q$ and $s$ , respectively, as (2 i 2). Likewise, $q$ and $s$ send $( 2 , j , 1 )$ , ,, which is forwarded by $r$ and $p$ , respectively, as $( 2 , j , 2 )$ , ,. So each of the four processes receives , ,a message $( 2 , k , 2 )$ with $k$ , ,equal to its own ID. Hence, the algorithm terminates with the wrong estimate 2.

Example 10.4 We give another computation of the Itai-Rodeh ring size algorithm on the anonymous directed ring from example 10.3, which does converge to the correct estimate. In the initial estimate round, let $p$ select $\operatorname { I D } i$ , while $q$ and $s$ select ID $j$ and $r$ selects ID $k \neq i$ . Then $p$ and $r$ send messages (2 i 1) and $( 2 , k , 1 )$ , which are forwarded by $q$ and $s$ , as (2 i 2) and $( 2 , k , 2 )$ , respectively. Since $i \neq k$ , , , ,, these messages make $r$ and $p$ , , , ,progress to the next estimate round, in which they both select ID $j$ and send $( 3 , j , 1 )$ . These messages make $q$ and $s$ , ,progress to the next estimate round because their estimates are greater than the estimates of $q$ and $s$ . Let $q$ select ID $j$ and $s$ select ID $\ell \neq j$ . In this estimate round, the message (3 3) originating from $s$ makes $r$ ℓprogress to the next estimate round. The message from $r$ , ℓ,in this last round makes $s , p$ , and $q$ progress to the next estimate round also. Finally, all processes terminate with the correct estimate, 4.

The probability that the algorithm terminates with an incorrect outcome becomes smaller when the domain $\{ 1 , \ldots , R \}$ from which random IDs are drawn is made larger. This probability tends to zero when $R$ tends , . . . ,to infinity for a fixed $N$ (see exercise 10.15).

The worst-case message complexity is $O ( N ^ { 3 } )$ : each process starts at most $N - 1$ estimate rounds, and during each round it sends out one message, which takes at most $N$ steps.

# 10.7 Election in IEEE 1394

The IEEE 1394 serial bus interface standard contains protocols for connecting devices in order to carry different forms of digital video and audio. It was developed in the late 1980s and is comparable to the more widely used USB standard. Its architecture is scalable, and (up to 63) peripheral devices can be added or removed dynamically.

We concentrate on the election algorithm in IEEE 1394, which is employed when devices have been added to or removed from the network. Since it is deemed too expensive to store IDs of other processes, no IDs are attached to messages. This means that election is basically performed within an anonymous network. In view of the dynamic nature of the network, processes are not aware of the network size. We saw in the previous section that no Las Vegas algorithm exists for these types of networks, if cycles can be present. The topology of the undirected network is here assumed to be acyclic, and a variant of the tree algorithm from section 4.2 is employed. While in the tree election algorithm from section 9.2 the process with the largest

ID becomes the leader, in IEEE 1394 the leader is selected from among the two processes that send a parent request to each other.

All processes in the network are initiators (so no wake-up phase is needed). When a process has one possible parent, it sends a parent request to this neighbor. If the request is accepted, an acknowledgment is sent back. The last two parentless processes may send parent requests to each other simultaneously; this is called root contention. A process $p$ finds itself in root contention if it receives a parent request instead of an acknowledgment from a neighbor $q$ in reply to its parent request. Then $p$ randomly decides either to immediately send a parent request again or to wait some time for another parent request from $q$ . In the latter case, if $p$ does not receive another parent request from $q$ within the waiting period, then $p$ once again randomly decides either to immediately send a parent request or to wait some more time. Root contention is resolved when one of the processes waits while the other sends immediately. Then the process that is waiting becomes the leader.

Example 10.5 We run the IEEE 1394 election protocol on an acyclic undirected network of three processes $p , q$ , and $r$ , with channels $p q$ and qr.

$p$ and $r$ have only one possible parent, so they send a parent request to $q$ .   
$q$ receives the parent request of $r$ and sends an acknowledgment back to $r$ .   
$q$ has only one possible parent left, so it sends a parent request to $p$ . Now $p$ and $q$ are in root contention.   
$p$ and $q$ receive each other’s parent requests. Now $p$ (randomly) decides to wait some time, while $q$ decides to send a parent request again immediately.   
$p$ receives the parent request of $q$ and sends back an acknowledgment. Thus, $p$ has become the leader.

In practice, the election algorithm in IEEE 1394 is sometimes employed on networks that contain a cycle, which leads to a deadlock. For example, if the network is an undirected ring, no process ever sends a parent request, because every process has two possible parents. Therefore, the election algorithm contains a timeout mechanism, so networks containing a cycle lead to a timeout.

# Bibliographical notes

The impossibility results regarding election in and computing the size of an anonymous ring date back to [4]. The Itai-Rodeh election and ring size algorithms originate from [59]. The echo algorithm with extinction for anonymous networks stems from [116]. The IEEE 1394 standard was published in [58].

# 10.8 Exercises

Exercise 10.1 [117] Give a centralized algorithm for assigning unique IDs to processes that terminates after at most $D + 1$ time units.

Exercise 10.2 Assume a Monte Carlo algorithm, and assume a (deterministic) algorithm to check whether the Monte Carlo algorithm terminated correctly.

(a) Give a Las Vegas algorithm that terminates with probability one. (b) Suppose the Monte Carlo algorithm gives a correct outcome with some probability $\pi$ . How many applications of your algorithm does it take on average to come to a correct outcome?

Exercise 10.3 Apply the Itai-Rodeh election algorithm to an anonymous directed ring of size 3, in which all processes know the network size. Initially, let two processes select ID $i$ , and let one process select ID $j .$ , with $i > j$ .

(a) Give a computation in which two processes proceed to election round 1.   
(b) Give a computation in which only one process proceeds to election round 1.

Exercise 10.4 Propose an adaptation of the Itai-Rodeh election algorithm in which the Boolean fourth parameter in messages, to recognize whether another process selected the same random ID in the current election round, is omitted.

Exercise 10.5 [44] Develop a variant of the Itai-Rodeh election algorithm without round numbers in case of FIFO channels.

Exercise 10.6 [59] Suppose that in an anonymous directed ring, each process $p$ has an estimate $G _ { p }$ of the ring size with $N \leq G _ { p } < 2 N .$ . Adapt the Itai-Rodeh election algorithm such that it remains a Las Vegas algorithm that terminates with probability one. Argue that your algorithm is correct. Also investigate the correctness of your algorithm if $G _ { p }$ can be $N - 1$ or $2 N$ .

Exercise 10.7 [11] Develop a probabilistic version of Franklin’s algorithm for election in anonymous undirected rings of known size, by augmenting this algorithm with random identity selection, hop counters to detect identity clashes, and round numbers modulo 2. Argue that your algorithm is a Las Vegas algorithm that terminates with probability one.

Exercise 10.8 Apply the echo algorithm with extinction to elect a leader in the anonymous undirected network pictured here. All processes are initiators and know the network size. In election round 0, let $p$ and $r$ select ID $i$ , while $q$ and $s$ select ID $j .$ , with $i > j$ . Give a computation in which $s$ becomes the leader in round 1. Explain why, in such a computation, $p$ and $r$ will not both progress to round 1.

![](images/6bd024a76071ec0d00b81028b63cc1a1c25975af7e4aef9101c4064f38bf06f1.jpg)

Exercise 10.9 Argue that there is no Las Vegas algorithm for election in anonymous rings of unknown size.

Exercise 10.10 Give a Monte Carlo algorithm for election in anonymous networks of unknown size. What is the success probability of your algorithm?

Exercise 10.11 Consider anonymous acyclic undirected networks of unknown size. Could the tree algorithm (with a wake-up phase) serve as the basis for:

(a) An always correctly terminating election algorithm? (b) A Las Vegas election algorithm that terminates with probability one?

In both cases, either describe how this algorithm could work, or explain where you run into problems.

Exercise 10.12 Give an (always correctly terminating) algorithm for computing the size of anonymous acyclic undirected networks.

Exercise 10.13 Apply the Itai-Rodeh ring size algorithm to an anonymous directed ring of size 3 in the following two cases:

(a) All three processes initially choose the same ID. Show that the algorithm computes ring size 2.   
(b) Only two processes initially choose the same ID. Show that the algorithm computes ring size 3.

Exercise 10.14 Let $h < N$ be relatively prime to $N$ . Explain why a run of the Itai-Rodeh ring size algorithm <can only terminate with the (wrong) estimate $h$ if all processes at estimate $h$ select the same ID.

Exercise 10.15 Consider an anonymous ring for which the size $N$ is a prime number.

(a) Determine the probability that the Itai-Rodeh ring size algorithm computes the correct ring size $N$ , under the simplifying assumption that processes never skip a round.   
(b) Repeat the calculation from part (a), but now under the assumption that each process sticks to the random ID it chooses in the first estimate round (instead of choosing a new ID at each round), and with $N > 2$ .   
(c) Argue that in general, letting each process stick to its initial random ID, instead of choosing a new random ID at each estimate round, increases the chance that the Itai-Rodeh ring size algorithm terminates with the correct estimate.

Exercise 10.16 [45] Develop a variant of the Itai-Rodeh ring size algorithm with worst-case message complexity $O ( N ^ { 2 } )$ , in which each process $p$ sends out only one message, carrying $p$ ’s randomly chosen ID and a hop count. This message may be stopped by accident at a process $q \neq p$ that happened to choose the same random ID as $p$ and wrongly thinks $p$ ’s message originates from $q$ . When $q$ realizes its current estimate is too conservative, it passes on $p$ ’s message after all.

Exercise 10.17 In the case of root contention in the IEEE 1394 election algorithm, is it optimal for the average-case time complexity to give an equal chance of 50 percent to both sending immediately and waiting for some time?

Exercise 10.18 (a) [21] Argue that each decentralized termination detection algorithm for anonymous rings of unknown size is Monte Carlo.   
(b) Explain why the Shavit-Francez termination detection algorithm cannot be carried over to (undirected) anonymous networks. That is, where do you run into problems?   
(c) Explain why the phrases “decentralized” and “of unknown size” in (a) are essential.

# Synchronous Networks

A synchronous system is a network in which the processes proceed in what is called lockstep. That is, a synchronous system proceeds in pulses and, in each pulse, each process

1. sends messages to its neighbors,   
2. receives messages from its neighbors, and   
3. performs internal events.

A message that is sent in a pulse must reach its destination before the receiver moves to the next pulse. A key advantage of synchronous systems is that the assumptions of global time and bounded message delay can make it easier to implement certain applications. For example, in case of online shopping, at a query to purchase a product, it can be checked and the customer can be informed whether the item is available before starting the checkout process, preventing a mismatch between inventory and sales (see also chapter 16 on distributed transactions). Synchronous systems will play a crucial role in coping with what are called Byzantine failures, in chapter 13.

A synchronizer turns a network with asynchronous communication into a synchronous system. It must make sure that a process only moves to the next pulse when it has received all messages for its current pulse. This allows one to develop a distributed algorithm for synchronous systems, which in some cases is easier than developing it for a setting with fully asynchronous communication. Then a synchronizer can be used to make this algorithm applicable to general networks.

# 11.1 Awerbuch’s Synchronizer

Awerbuch’s synchronizer for undirected networks comprises three classes of synchronizers: $\alpha , \beta$ , and $\gamma$ . The $\alpha$ synchronizer has a better time complexity, while the $\beta$ α β γsynchronizer has a better message complexity. The $\gamma$ synchronizer is a mix of the $\alpha$ and $\beta$ βsynchronizers, combining the best of both worlds.

α βLet a basic algorithm run on the network. A process can become safe in a pulse when all basic messages it sent in this pulse have reached their destinations. Basic messages are therefore acknowledged, and a process becomes safe in a pulse as soon as all basic messages it sent in this pulse have been acknowledged. A process can move to the next pulse when all its neighbors have become safe in its current pulse, because then the process can be certain it received all basic messages in its current pulse.

For simplicity, we take the liberty of ignoring acknowledgments of basic messages in the analysis of the message overhead of Awerbuch’s synchronizer. This is not entirely unreasonable, since often acknowledgments of messages come for free if they are part of the underlying transport layer, as is the case in the Transmission Control Protocol (see section 8.6).

# $\alpha$ Synchronizer

In the $\alpha$ synchronizer, when a process has received acknowledgments for all basic messages it sent in a pulse, αit sends a safe message to its neighbors. When a process $p$ has received safe messages from all its neighbors in a pulse, it can move to the next pulse. Because then all basic messages sent by $p$ ’s neighbors in this pulse have reached their destinations, so in particular, $p$ must have received all basic messages for this pulse.

In every pulse, the $\alpha$ synchronizer requires $2 E$ safe messages. If the last process to start a pulse does so at time $t$ α, then this process is guaranteed to receive acknowledgments for its basic messages in this pulse no later than at time $t + 2$ , so each neighbor will receive a safe message no later than at time $t + 3$ . Hence, the time overhead is at most three time units per pulse.

# $\beta$ Synchronizer

The $\beta$ synchronizer reduces the number of required safe messages. The key idea is to include an initialization βphase, in which a centralized wave algorithm from chapter 4 is employed to build a spanning tree of the network. The safe messages travel up the tree from the leaves to the root. When the root has received safe messages from all its children, all processes have become safe and can move to the next pulse. Then next messages travel down the tree from the root to the leaves to start this next pulse.

To be more precise, when a nonroot has in a pulse received acknowledgments for all basic messages it sent in this pulse as well as safe messages from all its children in the tree, it sends a safe message to its parent in the tree. When the root has in a pulse received acknowledgments for all basic messages it sent as well as safe messages from all its children, or when a nonroot receives a next message from its parent, it sends a next message to its children and moves to the next pulse.

In comparison to the $\alpha$ synchronizer, where $2 E$ safe messages per pulse are sent, the $\beta$ synchronizer uses $N - 1$ safe and $N - 1$ α β next messages, since they are sent only through tree edges. The time overhead of the $\beta$ synchronizer, however, is more severe than that of the $\alpha$ βsynchronizer. If the last process to start a pulse does so at time $t$ α, then this process is guaranteed to receive acknowledgments for its basic messages in this pulse no later than at time $t + 2$ . So if the spanning tree has depth $k$ , the root will receive a safe message from its children no later than at time $t + k + 2$ , and each nonroot will receive a next message from its parent no later than at time $t + 2 k + 2$ . Hence, the time overhead is at most $2 k + 2$ time units per pulse.

# Synchronizer

The $\gamma$ synchronizer divides the network into clusters, and within each cluster a spanning tree is built. Between each pair of neighboring clusters, meaning distinct clusters that are connected by a channel, one of these connecting channels is selected as a designated channel. Each pulse consists of three phases. First, the $\beta$ synchronizer is applied in each cluster to determine whether all processes in the cluster have become safe. Next, clusters signal to each other via the designated channels that they contain only safe processes, by means of the $\alpha$ synchronizer. Finally, within each cluster, the $\beta$ synchronizer is used once more to conclude that all neighboring clusters are safe, so all processes in the cluster can move to the next pulse. Messages in the second instance of the $\beta$ synchronizer are called cluster-safe and cluster-next, to distinguish them from the safe and next messages in the first instance of the $\beta$ synchronizer.

As noted, in each pulse, first the $\beta$ synchronizer is applied within each cluster. Recall that a process must βreceive acknowledgments for all basic messages it sent, including those to neighbors outside its cluster, before it can become safe. When the next messages of the $\beta$ synchronizer travel down the tree within a cluster from the root to the leaves, the processes do not immediately move to the next pulse. Instead, they send cluster-safe messages into their designated channels. When a nonroot has received cluster-safe messages through all its designated channels as well as from all its children within its own cluster, it sends a cluster-safe message to its parent. When a root has received cluster-safe messages through all its designated channels as well as from all its children, or when a nonroot receives a cluster-next message from its parent, it sends a cluster-next message to its children and moves to the next pulse.

The message overhead of the $\gamma$ synchronizer is

• a safe, a next, a cluster-safe, and a cluster-next message through each tree edge in any cluster, and • two cluster-safe messages, one in each direction, through every designated channel.

The message overhead tends to increase with the number of designated channels; that is, with the number of neighboring clusters.

Let the spanning trees of the clusters have depth at most . If the last process to start a pulse does so at time $t$ , then this process is guaranteed to receive acknowledgments for its basic messages in this pulse no later than time $t + 2$ . So each root will receive a safe message from its children no later than time $t + \ell + 2$ , and each nonroot will receive a next message from its parent no later than at time $t + 2 \ell + 2$ . Then each cluster-safe message through a designated channel will reach its destination no later than at time $t + 2 \ell + 3$ . So each root will receive a cluster-safe message from its children (and through its designated channels) no later than at time $t + 3 \ell + 3$ , and each nonroot will receive a cluster-next message from its parent no later than at time $t + 4 \ell + 3$ ℓ. Hence, the time overhead is at most $4 \ell + 3$ time units per pulse.

ℓ ℓIn conclusion, on the one hand, we want few clusters to minimize the number of designated channels and thus reduce the message overhead. On the other hand, we want the trees in the clusters to have a small depth to minimize the time overhead.

Example 11.1 The network pictured here has been divided into three clusters.

![](images/e353547b3c5ab013f9c333e138122b08ce08e6c5edaf3d78efb6a7b1f33e9764.jpg)

The dark processes depict the roots, while the dark lines depict the tree edges and designated channels. Since there are 15 tree edges in total and 2 designated channels, the message overhead of the $\gamma$ synchronizer γin a pulse consists of 60 messages through the tree edges plus 4 messages through the designated channels. Since the trees all have depth 1, we can take $\ell = 1$ , so the time overhead of the $\gamma$ synchronizer is at most seven time units per pulse.

Note that because the network has 36 channels, the $\alpha$ synchronizer gives a message overhead of 72 safe αmessages per pulse. Furthermore, since each spanning tree of the entire network has depth at least 3, meaning $k \geq 3$ , the $\beta$ synchronizer may give a time overhead of eight time units per pulse.

# 11.2 Bounded Delay Networks with Local Clocks

This section discusses a synchronizer for bounded delay networks, in which an upper bound $d _ { \mathrm { m a x } }$ on network latency is known; when a message is sent, it is guaranteed to reach its destination within $d _ { \mathrm { m a x } }$ time units.

Each process $p$ is supposed to have a local clock $C _ { p }$ . A process can read as well as adjust the value of its local clock. The time domain is $\mathbb { R } _ { \geq 0 }$ ; that is, the nonnegative real numbers. We distinguish real time, meaning time progression in the real world, from local clock time, which tries to estimate real time. At real time $\tau$ , the clock at $p$ returns the value $C _ { p } ( \tau )$ . The local clocks are started at real time 0: for all processes $p$ , $C _ { p } ( 0 ) = 0$ . Each local clock $C _ { p }$ τis assumed to have $\rho$ -bounded drift, for some $\rho > 1$ , compared to real time, putting a ρlower as well as an upper bound on its speed. That is, if $\tau _ { 2 } \geq \tau _ { 1 }$ ρ >(and $C _ { p }$ is not adjusted by $p$ in the time interval $[ \tau _ { 1 } , \tau _ { 2 } ] )$ ), then

$$
\frac { 1 } { \rho } \cdot ( \tau _ { 2 } - \tau _ { 1 } ) \le C _ { p } ( \tau _ { 2 } ) - C _ { p } ( \tau _ { 1 } ) \le \rho \cdot ( \tau _ { 2 } - \tau _ { 1 } ) .
$$

To build a synchronous system, the local clocks should, moreover, have precision $\delta$ for some $\delta > 0$ . That is, at any time $\tau$ and for any pair of processes $p , q$ ,

$$
| C _ { p } ( \tau ) - C _ { q } ( \tau ) | \leq \delta .
$$

Such precision can be realized by a regular synchronization of all local clocks. It will be shown in section 13.2 how this can be achieved (even in the presence of what are called Byzantine processes, who can lie about their local clock values).

Consider a bounded delay network, with local clocks that have $\rho$ -bounded drift and precision $\delta$ ; we assume that upper bounds for $\rho$ and $\delta$ ρ δare known. The synchronizer is defined as follows: when a local clock $C _ { p }$ reaches the time

$$
( i - 1 ) { \cdot } ( \rho ^ { 2 } { \cdot } \delta + \rho { \cdot } d _ { \mathrm { m a x } } )
$$

for some $i \geq 1$ , process $p$ can start pulse $i$ .

Theorem 11.1 The synchronizer for bounded delay networks, with local clocks that have $\rho$ -bounded drift and precision $\delta$ , is correct.

Proof. We must show that each process is guaranteed to receive all its messages for a pulse $i \geq 1$ before starting pulse $i + 1$ . It suffices to prove that for all processes $p , q$ and all $\tau$ ,

$$
C _ { q } ^ { - 1 } ( \tau ) + d _ { \operatorname* { m a x } } \ \le \ C _ { p } ^ { - 1 } ( \tau + \rho ^ { 2 } { \cdot } \delta + \rho { \cdot } d _ { \operatorname* { m a x } } )
$$

(where $C _ { r } ^ { - 1 } ( \tau )$ is the first moment in real time at which the clock of process $r$ returns the value $\tau$ ). Because taking $\tau = ( i - 1 ) { \cdot } ( \rho ^ { 2 } { \cdot } \delta + \rho { \cdot } d _ { \operatorname* { m a x } } )$ , this implies that $q$ starts pulse $i$ at least $d _ { \mathrm { m a x } }$ time units before $p$ τstarts pulse $i + 1$ τ ρ δ ρ. Since network latency is assumed to be at most $d _ { \mathrm { m a x } }$ , this ensures that $p$ receives the messages from $q$ for pulse $i$ in time.

The desired inequality follows immediately from the following two inequalities:

$$
\begin{array} { r l r } { C _ { q } ^ { - 1 } ( \tau ) } & { \leq } & { C _ { p } ^ { - 1 } ( \tau + \rho ^ { 2 } \cdot \delta ) , } \\ { C _ { p } ^ { - 1 } ( \tau ) + \upsilon } & { \leq } & { C _ { p } ^ { - 1 } ( \tau + \rho \cdot \upsilon ) . } \end{array}
$$

In the first inequality, add a summand $d _ { \mathrm { m a x } }$ at both sides; in the second inequality, replace $\tau$ by $\tau + \rho ^ { 2 } \cdot \delta$ and $\upsilon$ by $d _ { \mathrm { m a x } }$ . This yields $C _ { q } ^ { - 1 } ( \tau ) + d _ { \operatorname* { m a x } } \leq C _ { p } ^ { - 1 } ( \tau + \rho ^ { 2 } \cdot \delta ) + d _ { \operatorname* { m a x } } \leq C _ { p } ^ { - 1 } ( \tau + \rho ^ { 2 } \cdot \delta + \rho \cdot d _ { \operatorname* { m a x } } )$

τ τ ρ δ τ ρ δ ρWe now set out to prove (11.1) and (11.2). Consider the moment in time when $q$ ’s clock returns some value $\tau - \delta$ , and let real time progress for $\rho { \cdot } \delta$ time units. Since $q$ ’s clock is $\rho$ -bounded from below, in that period $q$ δ’s clock will progress with at least $\delta$ δ ρtime units, so it will return a clock value of at least $\tau$ . This can be depicted as follows.

![](images/13df1e380c28af2c2b067662005e067a1d39651f95465f1add46448ce19a1dec.jpg)

In other words,

$$
C _ { q } ^ { - 1 } ( \tau ) \leq C _ { q } ^ { - 1 } ( \tau - \delta ) + \rho { \cdot } \delta .
$$

Furthermore, since local clocks have precision $\delta$ , when $p$ ’s clock returns some time $\tau , q$ ’s clock must return at least time $\tau - \delta$ . In other words,

$$
C _ { q } ^ { - 1 } ( \tau - \delta ) \leq C _ { p } ^ { - 1 } ( \tau ) .
$$

Combining these two inequalities, we conclude that for all $\tau$ ,

$$
C _ { q } ^ { - 1 } ( \tau ) \leq C _ { p } ^ { - 1 } ( \tau ) + \rho { \cdot } \delta .
$$

Now consider the moment in time when $p$ ’s clock returns some value $\tau$ , and let real time progress for $\upsilon$ time units. Since $p$ ’s clock is $\rho$ -bounded from above, in that period $p$ τ’s clock will progress with at most $\rho \cdot \upsilon$ time ρunits, so it will return a clock value of at most $\tau + \rho \cdot \upsilon$ . This can be depicted as follows.

![](images/1b7d41efdea7dd9912a2f26f8194dede71e4ddff71b8797e8ef05ed3b2210101.jpg)

In other words, we have argued that inequality (11.2) holds. Furthermore, inequalities (11.3) and (11.2), with $\upsilon = \rho \cdot \delta$ , together yield inequality (11.1). ⊓⊔

# 11.3 Election in Anonymous Rings with Bounded Expected Delay

Bounded expected delay networks relax the restriction of bounded network latency to a known upper bound on the expected network latency. This means that arbitrarily long message delays are possible, but very long delays are less probable than short delays. In this setting, for anonymous directed rings in which all processes know the ring size $N$ , a Las Vegas election algorithm exists of which the average-case message and time complexities are both $O ( N )$ . This shows that even mild synchrony restrictions can be helpful for the development of efficient distributed algorithms. We recall that without restrictions on the expected network latency, there is a lower bound $\mathcal { Q } ( N { \cdot } \log N )$ for the average-case message complexity of election algorithms on rings (see section 9.1).

The election algorithm for anonymous directed rings with bounded expected delay, which we refer to as the resuscitation algorithm, requires that processes have clocks with $\rho$ -bounded drift for some $\rho > 1$ . The ρ ρ >algorithm starts, just as in the tree election algorithm, with a wake-up phase, in which each initiator, and each noninitiator when it is woken up, sends a wake-up message to its successor in the ring. After sending this message, the process becomes idle. Each (awake) process can be in four states: idle, active, passive, or leader. Initially, initiators are idle and noninitiators are passive. A passive process remains passive forever.

Each process $p$ maintains a counter $n p { - } h o p s _ { p }$ , which estimates from below the number of hops between $p$ and its first nonpassive predecessor in the ring. Initially, $n p { - } h o p s _ { p } = 1$ at all processes $p$ . An idle process $p$ at each clock tick (i.e., at every moment that its clock progresses by one time unit) remains idle with some probability $\pi _ { p } \in \langle 0 , 1 \rangle$ and becomes active with probability $1 - \pi _ { p }$ . When $p$ becomes active, it sends a message $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , 1 \right.$ , π, where the argument provides the receiver with a safe value for its np-hops variable.

,Let a message $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , h \right.$ arrive at a process $q$ . Then $q$ performs $\imath p \mathrm { - } h o p s _ { q } \gets \operatorname* { m a x } \left\{ n p \mathrm { - } h o p s _ { q } , h \right\}$ and ,acts as follows, depending on its state:

• If $q$ is idle or passive, it sends $\left. \mathbf { n p - h o p s } , n p \mathbf { - } h o p s _ { q } + 1 \right.$ . And if $q$ is idle, then it becomes passive.   
• If $q$ is active, either it becomes idle, if $h < N$ , or it becomes the leader, if $h = N$ .

Note that if a process sends a message $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , h \right.$ with $h > 1$ , then it is or becomes passive.

When a process $q$ receives a message $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , h \right.$ from its predecessor $p$ , at least the first $h - 1$ predecessors of $q$ ,in the ring are passive. This can be seen by induction on $h$ , where the base case $h = 1$ is trivial. In the inductive case $h > 1$ , $p$ is passive and received a message $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , h - 1 \right.$ in the past, so by induction, the first $h - 2$ predecessors of $p$ in the ring are also passive. This proves the claim. Since np-hop $s _ { q }$ stores the maximum $h \cdot$ -value among all np-hops messages $q$ has received, at least the first np-hop $s _ { q } - 1$ predecessors of $q$ in the ring are passive.

We discuss the correctness of the resuscitation algorithm. The number of messages in transit always equals the number of active processes in the ring. This invariant can be argued as follows: initially both numbers are zero; idle processes that become active send a message; idle and passive processes forward messages and remain nonactive; and active processes remain active until a message arrives, at which point they become nonactive and do not forward the message. Since active processes never become passive upon the arrival of a message, there is always a nonpassive process. Furthermore, when an idle process becomes active, there is a positive probability that the message it sends will complete the round trip, after which the process becomes the leader. And we have argued earlier that when a process receives $\left. \mathbf { n } \mathbf { p } { \cdot } \mathbf { h o p s } , N \right.$ , all other $N - 1$ processes must be passive. To conclude, the resuscitation algorithm is a Las Vegas algorithm that terminates with probability one.

Example 11.2 We consider one possible computation of the resuscitation algorithm on an anonymous directed ring with processes $p , q$ , and $r$ . At the first tick of their clocks all three processes happen to become active and send $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , 1 \right.$ . Next, $p$ and $q$ receive these messages from $r$ and $p$ , respectively, and both be,come idle. At the next tick of its clock, $p$ becomes active again and sends $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , 1 \right.$ . This message arrives at $q$ , which becomes passive and sends $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , 2 \right.$ . This message arrives at $r$ ,, which sets np-hopsr to 2 and becomes idle. Finally, the message $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , 1 \right.$ , that $q$ sent at the start of the computation arrives at $r$ . As a result, $r$ becomes passive and sends $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , 3 \right.$ (because $n p { - } h o p s _ { r } = 2 $ ). When this message arrives at $p$ , it becomes the leader.

The computation in example 11.2 shows that it is beneficial for the message complexity that an idle or passive process $r$ , upon the arrival of a message $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , h \right.$ , forwards $\left. \mathbf { n p - h o p s } , n p \mathbf { - } h o p s _ { r } + 1 \right.$ instead of $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , h + 1 \right.$ ,. Otherwise, at the end of the computation in the example, $r$ ,would send not $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , 3 \right.$ but $\left. \mathbf { n } \mathbf { p } \mathbf { - } \mathbf { h o p s } , 2 \right.$ to $p$ . Then $p$ would have become idle, instead of the leader.

,Key to the favorable average-case message complexity of the resuscitation algorithm mentioned at the start of this section is a smart choice of the probability $\pi _ { p }$ with which an idle process $p$ remains idle at a clock πtick. This choice depends on the number of idle processes in the ring; the more idle processes, the larger $\pi _ { p }$ πshould be to maximize the chance that exactly one idle process becomes active and its message completes the round trip without any other idle process becoming active in the meantime. Therefore, the initial value of $\pi _ { p }$ depends on $N$ , and $\pi _ { p }$ decreases at every increase of np-hop $s _ { p }$ ,

$$
\pi _ { p } = \left( \frac { N - 1 } { N + 1 } \right) ^ { \displaystyle \frac { n p - h o p s _ { p } } { N } } .
$$

We argue that this dynamic value of $\pi _ { p }$ yields an average-case message and time complexity of $O ( N )$ . For πsimplicity, we assume that local clocks are perfectly synchronized with real time, that a message on average takes one time unit to reach its destination, and that the values np-hopsp at nonpassive processes $p$ always equal the number of hops between $p$ and its first nonpassive predecessor. The forthcoming argumentation is somewhat more involved when clocks have $\rho$ -bounded drift, or $n p { - } h o p s _ { p }$ may temporarily be smaller than the number of hops between $p$ ρand its first nonpassive predecessor.

Consider a clock tick at which all nonpassive processes are idle. By assumption, the values of the parameters np-hop $s _ { p }$ of the nonpassive processes $p$ always add up to $N$ . Therefore, the probability that the idle processes all remain idle at this clock tick, meaning the product of the $\pi _ { p }$ for all idle processes $p$ , is $\frac { N - 1 } { N + 1 }$ . So πthe probability that at least one idle process becomes active and sends a message at this clock tick is $\frac { 2 } { N { + } 1 }$ . By assumption, a round trip of this message on average takes $N$ time units. Therefore, the probability that another idle process becomes active during this round trip is at most $\begin{array} { r } { 1 - \big ( \frac { N - 1 } { N + 1 } \big ) ^ { N } } \end{array}$ . This is $\leq \frac { 8 } { 9 }$ because $N \geq 2$ so this probability has an upper bound that is independent of the ring size. In conclusion, on average once every $O ( N )$ <time units an idle process becomes active, and with an average probability of $O ( 1 )$ the message of this active process completes its round trip. These two observations together imply that the average-case message and time complexities of the resuscitation algorithm are $O ( N )$ .

# Bibliographical notes

Awerbuch’s synchronizer originates from [8]. Bounded delay networks were introduced in [29], and a synchronizer for bounded delay networks with local clocks that have bounded drift was presented in [117]. Expected bounded delay networks and the resuscitation algorithm stem from [10].

# 11.4 Exercises

Exercise 11.1 Consider the $\alpha$ synchronizer on a network of processes $p _ { 0 } , . . . , p _ { N - 1 }$ on a line (so the network has diameter $N - 1$ α). Give an example in which at some point $p _ { 0 }$ , . . . ,is in pulse 0 while $p _ { N - 2 }$ is in pulse $N - 2$ .

Exercise 11.2 Argue that with the $\beta$ synchronizer a process can never be two pulses ahead of another proces in the network.

Exercise 11.3 Let the $\gamma$ synchronizer be applied to an undirected network consisting of a complete subnetwork of size $k$ γand a ring subnetwork of size $\ell \geq 4$ , connected by a single designated channel. Choose ℓspanning trees in the two subnetworks that give rise to a minimal time overhead, and determine the message and time overhead of the $\gamma$ synchronizer.

Exercise 11.4 Suppose that performing internal events at the end of a pulse takes time and that an upper bound $\epsilon$ is known for this processing time. Explain how the synchronizer for bounded delay networks, with ϵlocal clocks that have $\rho$ -bounded drift and precision $\delta$ , needs to be adapted. Argue that your adapted synchronizer is correct.

Exercise 11.5 Explain how the resuscitation algorithm needs to be adapted if we want an initiator to become the leader. Also discuss how the wake-up phase of the resuscitation algorithm could then be used to obtain more accurate values for the np-hops variables at the processes.

# Consensus with Crash Failures

In practice, processes in a distributed system may crash, meaning that they permanently and unexpectedly stop executing. The problem of failures can be alleviated by including redundancy and replication in the system and letting processes negotiate before a certain action is taken. A typical example is a database management system in which the processes collectively decide whether to commit or abort a distributed transaction (see section 16.2). In sections 3.3 and 6.5, crashed processes were already considered for the specific challenges of rollback recovery and termination detection. A basic assumption we made in those two sections and also in the current chapter is that the network topology is complete. This guarantees that the network topology always stays strongly connected, even when processes have crashed. (Thus it is reasonable to assume that processes know the network size, as they have $N - 1$ local channels.)

In this chapter, we consider how in general the rest of the system can cope with a crash of one or more processes, if at all possible. The next chapter will consider the more severe type of what is called a Byzantine failure, where a process may show behavior that is not in line with the specification of the distributed algorithm being executed. The challenge we pose to the system is to let its processes agree on a single value, even though some processes may have crashed. The consensus problem is that the correct processes, meaning the processes that have not crashed (or, in the next chapter, that are not Byzantine), must eventually uniformly decide for the same value. In a crash consensus algorithm to solve this problem, each process randomly chooses an initial value from some finite data domain. In all executions of a crash consensus algorithm, the following three properties must be satisfied:

• Termination: Every correct process eventually decides for a value.   
• Agreement: All correct processes decide for the same value.   
• Validity: If all processes choose the same initial value, then all correct processes decide for this value.

The validity requirement rules out trivial solutions where the processes always decide for the same predeter mined value, for example, 0, irrespective of their initial values.

At first sight solving consensus may seem like an esoteric problem. However, it is important to realise that basically each distributed algorithm is solving some form of consensus, in which the individual processes need to come to an agreement. For instance, in termination detection they need to come to the conclusion that an execution of a basic algorithm has terminated. Therefore the negative results presented in this chapter and the next, on the impossibility of solving consensus in the presence of crashing or Byzantine processes, have significant practical implications. And the presented consensus algorithms are at the basis of important practical consensus algorithms such as Paxos and Raft.

This chapter, with the exception of section 12.6, focuses on the binary consensus problem, in which the input values of the processes are restricted to 0 and 1. So with $N$ processes there are $2 ^ { N }$ different initial configurations. By abuse of terminology, we will refer to this problem as consensus.

A reachable configuration of a crash consensus algorithm is called bivalent if from this configuration one can reach a terminal configuration where consensus has been reached on the value 0, as well as a terminal configuration where consensus has been reached on the value 1. The validity requirement implies that each crash consensus algorithm has a bivalent initial configuration; see exercise 12.1.

A $k$ -crash consensus algorithm, for a $k > 0$ , is a crash consensus algorithm that can cope with up to $k$ crashing processes.

# 12.1 Impossibility of 1-Crash Consensus

In this section and the next, we assume that processes cannot observe whether some process has crashed. If no messages are received from some process for a very long time, this may simply be because the process or its outgoing channels are very slow. It turns out that in this setting one cannot hope to develop a terminating 1- crash consensus algorithm. No matter how large the network is, the prospect of one crashing process suffices to yield infinite executions in which no decision is ever made. The basic idea behind this impossibility result is that a decision for either 0 or 1, in an asynchronous setting, must be enforced by an event at a single process $p$ . But what if $p$ crashes immediately after this event, and in the case of a send event, the message travels through the channel for a very long, indefinite amount of time? Then, at some moment in time, the remaining processes should organize themselves to mimic the decision of $p$ but without any input from this crashed process. This is shown to be impossible, if crashes cannot be observed.

Theorem 12.1 There is no (always correctly terminating) algorithm for 1-crash consensus.

Proof. Consider any 1-crash consensus algorithm. Let $\gamma$ be a bivalent configuration. Then $\gamma \to \gamma _ { 0 }$ and $\gamma \to \gamma _ { 1 }$ , where $\gamma _ { 0 }$ can lead to decision 0 and $\gamma _ { 1 }$ γto decision 1. We argue that $\gamma _ { 0 }$ or $\gamma _ { 1 }$ γ γ γ γmust be bivalent. We distinguish γbetween two cases:

The transitions $\gamma \to \gamma _ { 0 }$ and $\gamma \to \gamma _ { 1 }$ correspond to events $a _ { 0 }$ and $a _ { 1 }$ at different processes $p _ { 0 }$ and $p _ { 1 }$ , γrespectively. Then in $\gamma _ { 0 }$ γthe event $a _ { 1 }$ at $p _ { 1 }$ can still be performed, and likewise in $\gamma _ { 1 }$ the event $a _ { 0 }$ at $p _ { 0 }$ can γstill be performed. Performing $a _ { 1 }$ at $p _ { 1 }$ in $\gamma _ { 0 }$ and performing $a _ { 0 }$ at $p _ { 0 }$ in $\gamma _ { 1 }$ γlead to the same configuration $\delta$ , because in both cases the resulting configuration is reached from $\gamma$ by performing the concurrent events $a _ { 0 }$ and $a _ { 1 }$ at $p _ { 0 }$ and $p _ { 1 }$ . So there are transitions $\gamma _ { 0 }  \delta$ and $\gamma _ { 1 }  \delta$ . Hence, $\gamma _ { 0 }$ or $\gamma _ { 1 }$ is bivalent, if $\delta$ can lead to a decision 1 or 0, respectively. The transitions $\gamma \to \gamma _ { 0 }$ and $\gamma \to \gamma _ { 1 }$ correspond to events at the same process $p$ . In $\gamma$ , $p$ can crash. Moreover, γa message sent by $p$ γ γ γ γcan take indefinitely long to reach its destination. Therefore, in $\gamma$ the processes other than $p$ must be 0-potent or 1-potent. In a configuration, a set $s$ of processes is said to be $^ b$ -potent, for some $b \in \{ 0 , 1 \}$ , if by executing only events at processes in $s$ , some process in $s$ can decide for $^ b$ . Since $\gamma \to \gamma _ { 0 }$ and $\gamma \to \gamma _ { 1 }$ concern $p$ , in $\gamma _ { 0 }$ and $\gamma _ { 1 }$ the processes other than $p$ are still $^ b$ -potent. So $\gamma _ { 1 - b }$ is bivalent.

In conclusion, a bivalent configuration can always make a transition to some bivalent configuration. Since the crash consensus algorithm has a bivalent initial configuration (see exercise 12.1), it follows that there is an infinite execution, visiting only bivalent configurations. ⊓⊔

We can even construct an infinite execution that is fair; see exercise 12.3.

# 12.2 Bracha-Toueg Crash Consensus Algorithm

In chapter 10, to circumvent the impossibility of a terminating election algorithm for anonymous networks, we moved to probabilistic algorithms. Here we follow the same approach. First, we discuss another impossibility result: there is no Las Vegas algorithm for crash consensus if half of the processes can crash. Then the network can be divided into two disjoint halves, where in each half the processes do not receive messages from the processes in the other half for a very long time, so that eventually they must act under the assumption that the processes in the other half have crashed. As a result, the two halves may act as independent entities that can come to different decisions.

Theorem 12.2 Let $\begin{array} { r } { k \geq \frac { N } { 2 } } \end{array}$ . There is no Las Vegas algorithm for $k$ -crash consensus.

Proof. Suppose, toward a contradiction, that such an algorithm does exist. Divide the processes into two disjoint sets $s$ and $T$ , which both contain at most $\lceil \frac { N } { 2 } \rceil$ processes. Since $k \geq \lceil \frac { N } { 2 } \rceil$ , it is possible that all processes in $s$ crash, and likewise it is possible that all processes in $T$ crash. Initially, the processes in $s$ all happen to get the value 0, while the processes in $T$ all happen to get the value 1.

Let communication from processes in $s$ to processes in $T$ and vice versa both be extremely slow, so that for a very long time the processes in $s$ do not receive messages from the processes in $T$ and vice versa. At some point, the processes in $s$ must assume that all processes in $T$ have crashed and reach a decision by themselves, which will be 0. Vice versa, at some point, the processes in $T$ must assume that all processes in $s$ have crashed and reach a decision by themselves, which will be 1. ⊓⊔

If $k < \frac { N } { 2 }$ , then a Las Vegas algorithm for $k$ -crash consensus does exist. The Bracha-Toueg $k$ -crash con<sensus algorithm, for $k < \frac { N } { 2 }$ , progresses in rounds. Initially, at the start of round 0, each process $p$ randomly <chooses a value 0 or 1 and assigns it to local variable $\nu a l u e _ { p }$ . The weight of a process $p$ , stored in local variable $w e i g h t _ { p }$ , approximates from below the number of processes that voted $^ b$ in the previous round. In round 0, each process has weight 1, because it only knows its own vote.

In each round $n \geq 0$ , each correct, undecided process $p$ sends its value and weight to all processes and determines a new value and weight, based on $N - k$ messages it receives in this round.

$p$ sends $\langle n , \nu a l u e _ { p } , w e i g h t _ { p } \rangle$ to all processes (including itself).   
$p$ ,waits for $N - k$ messages $\langle n , b , w \rangle$ to arrive. (It dismisses or stores messages from earlier or future , ,rounds, respectively.) With regard to $\nu a l u e _ { p }$ , we distinguish between two cases.   
$^ *$ If $\begin{array} { r } { w > \frac { N } { 2 } } \end{array}$ for an incoming message $\langle n , b , w \rangle$ , then $\nu a l u e _ { p } \gets b$ .   
$^ *$ >Otherwise, value $_ p  0$ , , if most messages voted 0, or else valu ${ \bf \Phi } _ { p } \gets 1$ .   
weightp is changed into the number of incoming votes for valu $e _ { p }$ in round $n$ .

• If $\begin{array} { r } { w > \frac { N } { 2 } } \end{array}$ for more than $k$ incoming messages $\langle n , b , w \rangle$ , then $p$ decides for $^ b$

If $p$ decides for $^ b$ in round $n$ , it broadcasts $\left. n + 1 , b , N - k \right.$ and $\left. n + 2 , b , N - k \right.$ and terminates. This suffices , , , ,because when a process decides, all other correct processes are guaranteed to decide within two rounds; see the proof of theorem 12.3.

In reality, $p$ of course does not send messages to itself but simply includes the message it broadcasts in the collection of messages it receives from other processes in the same round. Note that if $p$ waited for more than $N - k$ messages $\langle n , b , w \rangle$ in a round $n$ , then a deadlock could occur, if $k$ processes have crashed. Note also that if $p$ , ,receives messages $\langle n , b , w \rangle$ and $\langle n , 1 - b , w ^ { \prime } \rangle$ , then $w + w ^ { \prime } \leq N$ , so $w$ and $w ^ { \prime }$ cannot both be greater than $\frac { N } { 2 }$ ,. Note, finally, that since $p$ ,waits for $N - k$ messages $\langle n , b , w \rangle$ and can decide only if more than $k$ of those messages have a weight greater than $\frac { N } { 2 }$ , ,, it is essential for termination that $N - k > k$ .

Example 12.1 Consider a network of three processes $p , q$ , and $r$ , with $k = 1$ . During each round a process requires two incoming messages to determine a new value and weight, and two $^ b$ -votes with weight 2 to decide for $^ b$ . We study one possible computation of the Bracha-Toueg 1-crash consensus algorithm on this network.

Initially, $p$ and $q$ randomly choose the value 0 and $r$ the value 1, with weight 1.   
In round 0, $p$ takes into account the messages from $p$ and $r$ ; it sets its value to 1 and its weight to 1. Moreover, $q$ and $r$ both take into account the messages from $p$ and $q$ ; each sets its value to 0 and its weight to 2.   
In round 1, $q$ takes into account the messages from $q$ and $r$ ; since both messages carry weight 2, it decides for 0. Moreover, $p$ and $r$ both take into account the messages from $p$ and $r$ ; since the message from $r$ carries weight 2, each sets its value to 0 and its weight to 1.

![](images/bb3f9e06ac1458f5f1155dcbad7ac66b6e0c9b05366d7decf7e2406c1d329239.jpg)

– At the start of round 2, $q$ crashes. So $p$ and $r$ can take into account only the messages from $p$ and $r$ ; as a result, each sets its value to 0 and its weight to 2. In round 3, $p$ and $r$ can again only take into account the messages from $p$ and $r$ ; since both messages carry weight 2, they decide for 0. $p$ and $r$ send messages with value 0 and weight 2 for two more rounds and terminate.

Theorem 12.3 If the scheduling of messages is fair, then the Bracha-Toueg $k$ -crash consensus algorithm, for each $k < \frac { N } { 2 }$ , is a Las Vegas algorithm that terminates with probability one.

Proof. First, we prove that agreement and validity are satisfied. Next, we prove that the algorithm terminates with probability one, owing to the assumption that the scheduling of messages is fair, meaning that each possible order of delivery of the messages in a round occurs with a positive probability.

Suppose a process $p$ decides for a value $^ b$ at the end of a round $n$ . Then, at the start of round $n , \nu a l u e _ { q } = b$ and $\begin{array} { r } { w e i g h t _ { q } > \frac { N } { 2 } } \end{array}$ for more than $k$ processes $q$ . Since in every round each correct, undecided process ignores >messages from only $k$ processes, in round $n$ these processes all take into account a message $\langle n , b , w \rangle$ with $w > \frac { N } { 2 }$ . So in round $n + 1$ , all correct processes vote $^ b$ . So in round $n + 2$ , ,, all correct processes vote $^ b$ with >weight $\begin{array} { r } { N - k > \frac { N } { 2 } } \end{array}$ . Hence, after round $n + 2$ , all correct processes have decided for $^ b$ . To conclude, all correct >processes decide for the same value.

If all processes initially happen to select the same random bit $^ b$ , then clearly after round 0 all correct processes have the value $^ b$ with weight $N - k$ , so after round 1 they all decide for $^ b$ .

Because of fair scheduling, in each round there is a positive probability that all processes receive the first $N - k$ messages from the same $N - k$ processes. After such a round $n$ , all correct processes have the same value $^ b$ . Then, after round $n + 1$ , all correct processes have the value $^ b$ with weight $N - k$ . And after round $n + 2$ , all correct processes have decided for $^ b$ . In conclusion, the algorithm terminates with probability one. ⊓⊔

# 12.3 Failure Detectors

The impossibility result in theorem 12.1, that there is no terminating 1-crash consensus algorithm, assumes that crashes of processes cannot be observed. In the next two sections, we will see that this is a crucial assumption: when crashes can be detected, there does exist a terminating crash consensus algorithm. In the current section, the notion of failure detectors, their properties, and two straightforward implementations with different properties are discussed. We recall that failure detectors already played a crucial role in the rollback recovery and termination detection algorithms in sections 3.3 and 6.5.

As time domain we take $\mathbb { R } _ { \geq 0 }$ . Each execution of a crash consensus algorithm is provided with a failure pattern consisting of sets $F ( \tau )$ that contain the crashed processes at time $\tau$ . Crashed processes cannot restart: $\tau _ { 0 } \leq \tau _ { 1 } \Rightarrow F ( \tau _ { 0 } ) \subseteq F ( \tau _ { 1 } )$ τ. It is assumed that processes cannot observe $F ( \tau )$ .

Processes carry a failure detector to try to detect crashed processes. By $H ( p , \tau )$ we denote the set of processes that are suspected to have crashed by (the failure detector of) process $p$ , τat time $\tau$ . Each execution of a crash consensus algorithm is provided with a failure detector history $H$ τ. In general, such suspicions may turn out to be false, typically because at a time $\tau$ a process $p$ receives a message from a suspected process in $H ( p , \tau )$ τ. However, we require that failure detectors be always complete: from some time onward, every crashed process is suspected by every correct process.

A failure detector is called strongly accurate if only crashed processes are ever suspected. In bounded delay networks (see section 11.2), a strongly accurate (and complete) failure detector can be implemented as follows. Suppose $d _ { \mathrm { m a x } }$ is a known upper bound on network latency. Let each process broadcast a message alive every $\nu$ time units. A process from which no message has been received for more than $\nu + d _ { \mathrm { m a x } }$ time units ν νhas crashed. Since crashed processes stop sending alive messages, the failure detector is clearly complete. And the bound on network latency ensures that there can never be more than $\nu + d _ { \mathrm { m a x } }$ time units between the arrival at $p$ of subsequent alive messages from $q$ , so the failure detector is strongly accurate.

A failure detector is called eventually strongly accurate if in each execution, from some point in time onward only crashed processes are suspected. In other words, there can be false suspicions, but only up to a certain moment in time. Suppose there is an unknown upper bound on network delay. Again, let each process broadcast a message alive every $\nu$ time units. An eventually strongly accurate (and complete) failure detector νcan be implemented as follows. Each correct process $p$ initially guesses as network latency $d _ { p } = 1$ . If $p$ does not receive a message from a process $q$ for more than $\nu + d _ { p }$ time units, then $p$ suspects that $q$ has crashed. This suspicion may be false if the value of $d _ { p }$ is too conservative. When $p$ receives a message from a suspected process $q$ , then $q$ is no longer suspected by $p$ and $d _ { p } \gets d _ { p } + 1$ . Since crashed processes stop sending alive messages, the failure detector is clearly complete. And since network latency is bounded, each process $p$ can receive a message from a suspected process and as a result increase $d _ { p }$ only finitely many times. This guarantees that the failure detector is eventually strongly accurate.

# 12.4 Consensus with a Weakly Accurate Failure Detector

A failure detector is called weakly accurate if some correct process is never suspected by the other processes. In the presence of a (complete and) weakly accurate failure detector, there is a simple $k$ -crash consensus algorithm that works for each $k$ .

Let the processes be numbered: $p _ { 0 } , . . . , p _ { N - 1 }$ . Initially, each process $q$ randomly chooses a value 0 or 1. , . . . ,The crash consensus algorithm proceeds in rounds $n = 0 , \ldots , N - 1$ . In a round $n$ , the process $p _ { n }$ acts as the coordinator.

• $p _ { n }$ (if not crashed) broadcasts its value. Each process waits $^ *$ either for a message from $p _ { n }$ , in which case it adopts the value of $p _ { n }$ , $^ *$ or until it suspects that $p _ { n }$ has crashed. Next, if $n < N - 1$ , the process moves to the next round.

After round $N - 1$ , each correct process decides for its value at that time.

This rotating coordinator algorithm is a $k$ -crash consensus algorithm for each $k < N$ . Termination is guaranteed because, owing to completeness of the failure detector, each alive process will complete each round. And since the failure detector is weakly accurate, some correct process $p _ { i }$ is never suspected by the other processes. This implies that after round $i$ , all correct processes have the same value $^ b$ . Then clearly in rounds $i + 1 , . . . , N - 1$ , all processes keep this value $^ b$ . Hence, after round $N - 1$ , all correct processes decide for $^ b$ .

# 12.5 Chandra-Toueg Algorithm

With an eventually strongly accurate failure detector, the proof of theorem 12.2, that there is no Las Vegas algorithm for $k$ -crash consensus if $\begin{array} { r } { k \geq \frac { N } { 2 } } \end{array}$ , still applies. Because it may take a very long, indefinite period of time before the failure detector becomes strongly accurate, and up to that point there can still be false suspicions.

Theorem 12.4 Let $\begin{array} { r } { k \geq \frac { N } { 2 } } \end{array}$ . There is no Las Vegas algorithm for $k$ -crash consensus based on an eventually strongly accurate failure detector.

Proof. Suppose, toward a contradiction, that such an algorithm does exist. Divide the processes into two disjoint sets $s$ and $T$ , which both contain at most $\lceil \frac { N } { 2 } \rceil$ processes. Since $k \geq \lceil \frac { N } { 2 } \rceil$ , it is possible that all processes in $s$ crash, and likewise it is possible that all processes in $T$ crash. Initially, the processes in $s$ all happen to get the value 0, while the processes in $T$ all happen to get the value 1.

Let communication from processes in $s$ to processes in $T$ and vice versa both be extremely slow, so that for a very long time the processes in $s$ do not receive messages from the processes in $T$ and vice versa. Since the failure detector is only eventually strongly accurate, the processes in $s$ may falsely suspect for a very long period of time that all processes in $T$ have crashed. At some point, the processes in $s$ must assume that all processes in $T$ have crashed and reach a decision by themselves, which will be 0. Vice versa, the processes in $T$ may falsely suspect for a very long period of time that all processes in $s$ have crashed and reach a decision by themselves, which will be 1. ⊓⊔

A failure detector is called eventually weakly accurate if in each execution, from some point in time on some correct process is never suspected by the other processes. The Chandra-Toueg crash consensus algorithm, which uses an eventually weakly accurate failure detector, is an always correctly terminating $k$ - crash consensus algorithm if $k < \frac { N } { 2 }$ .

<Let the processes be numbered: $p _ { 0 } , . . . , p _ { N - 1 }$ . Initially, each process randomly chooses a value 0 or 1 and , . . . ,assigns it to local variable valueq. The algorithm proceeds in rounds. Each process $q$ records the number of the last round last-updateq in which it updated its value; initially last-update $\dot { \boldsymbol { q } } = - 1$ .

Each round $n \geq 0$ is coordinated by the process $p _ { c }$ with $c = n$ mod $N$ . Round $n$ progresses as follows.

• Every correct, undecided process $q$ (including $p _ { c }$ ) sends to $p _ { c }$ the message $\left. \mathbf { v o t e } , n , \nu a l u e _ { q } \right.$ last-updateq⟩. $p _ { c }$ (unless crashed or decided) waits until $N - k$ , , , such messages have arrived, selects one, say $\langle \mathbf { v o t e } , n , b , \bar { \ell } \rangle$ , with $\ell$ as large as possible, and broadcasts $\langle \mathbf { v a l u e } , n , b \rangle$ . Every correct, undecided process $q$ (including $p _ { c }$ ) waits until either $\begin{array} { r l } { * } & { { } \ \langle \mathbf { v a l u e } , n , b \rangle } \end{array}$ arrives; then it performs $\nu a l u e _ { q } \gets b$ and last-update ${ \bf \dot { \boldsymbol { q } } } \gets { \boldsymbol { n } }$ , and sends $\langle \mathbf { a c k } , n \rangle$ to $p _ { c }$ , $^ *$ , ,or it suspects that $p _ { c }$ has crashed, at which time it sends $\langle \mathbf { n a c k } , n \rangle$ to $p _ { c }$ . $p _ { c }$ waits for $N - k$ acknowledgments. If more than $k$ ,of them are positive, then $p _ { c }$ decides for $^ b$ , broadcasts $\langle \mathbf { d e c i d e } , b \rangle$ , and terminates.

A correct, undecided process that receives $\langle \mathbf { d e c i d e } , b \rangle$ decides for $^ b$ and terminates.

,The idea behind the decision criterion for the coordinator in a round $n$ , the receipt of more than $k$ positive acknowledgments, is that then more than $k$ processes have adopted the value $^ b$ of the coordinator and set their last-update parameter to $n$ . Since in each round the coordinator ignores messages of only $k$ processes and adopts the value from a message with a maximal last-update, this guarantees that in future rounds (correct) coordinators will always adopt the value $^ b$ ; see the proof of theorem 12.5.

Example 12.2 Consider a complete network of three processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ , with $k = 1$ . During each round the coordinator waits for two incoming votes and needs two positive acknowledgments to decide. We study one possible computation of the Chandra-Toueg 1-crash consensus algorithm on this network.

– Initially, $p _ { 0 }$ and $p _ { 2 }$ randomly choose the value 1 and $p _ { 1 }$ chooses the value 0; last-update $= - 1$ at all three processes.

In round 0, the coordinator $p _ { 0 }$ takes into account the messages from $p _ { 0 }$ and $p _ { 1 }$ , selects the message from $p _ { 1 }$ to determine its new value, and broadcasts the value 0. When $p _ { 0 }$ and $p _ { 1 }$ receive this message, each sets its value to 0 and last-update to 0 and sends ack to $p _ { 0 }$ ; moreover, $p _ { 1 }$ moves to round 1. However, $p _ { 2 }$ moves to round 1 without waiting for a message from $p _ { 0 }$ , because its failure detector falsely suspects that $p _ { 0 }$ has crashed; $p _ { 2 }$ sends nack to $p _ { 0 }$ . The coordinator $p _ { 0 }$ receives the acks of $p _ { 0 }$ and $p _ { 1 }$ , decides for 0, and crashes before it can broadcast a decide message.

$$
\displaystyle \int _ { \scriptstyle p _ { 0 } } ^ { \scriptstyle \mathrm { { v a l u e } = 0 } } \displaystyle \sum _ { \scriptstyle { \left( p _ { 0 } \right) } } ^ { \scriptstyle \mathrm { { v a l u e } = 0 } } \displaystyle \sum _ { \scriptstyle l a s t - u p d a t e = - 1 } ^ { \scriptstyle \mathrm { { v a l u e } = 0 } }
$$

decided for 0 and crashed

In round 1, the coordinator $p _ { 1 }$ can take into account only the messages from $p _ { 1 }$ and $p _ { 2 }$ . It must select the message from $p _ { 1 }$ to determine its new value, because it has the highest last-update. So $p _ { 1 }$ broadcasts the value 0. When $p _ { 1 }$ receives this message, it sets its value to 0 and last-update to 1 and sends ack to itself. The process $p _ { 2 }$ moves to round 2 without waiting for a message from $p _ { 1 }$ , because its failure detector falsely suspects that $p _ { 1 }$ has crashed; $p _ { 2 }$ sends nack to $p _ { 1 }$ . After $p _ { 1 }$ has received the ack and nack from $p _ { 1 }$ and $p _ { 2 }$ , respectively, it also moves to round 2.

![](images/5b006e9f898587da77d7ce0375670f8d3722c57ee9fde50ac332e1df5d2e9acd.jpg)

In round 2, the coordinator $p _ { 2 }$ can take into account only the messages from $p _ { 1 }$ and $p _ { 2 }$ . It must select the message from $p _ { 1 }$ to determine its new value, because it has the highest last-update. So $p _ { 2 }$ broadcasts the value 0. When $p _ { 1 }$ and $p _ { 2 }$ receive this message, each sets its value to 0 and last-update to 2 and sends ack to $p _ { 2 }$ ; moreover, $p _ { 1 }$ moves to round 3. The coordinator $p _ { 2 }$ receives the acks of $p _ { 1 }$ and $p _ { 2 }$ , decides for 0, and broadcasts $\langle \mathbf { d e c i d e } , 0 \rangle$ . When $p _ { 1 }$ receives this message, it also decides for 0.

Theorem 12.5 In the presence of an eventually weakly accurate failure detector, the Chandra-Toueg algorithm is an (always correctly terminating) $k$ -crash consensus algorithm for each $k < \frac { N } { 2 }$ .

Proof. First, we prove that agreement and validity are satisfied, and next that the algorithm always terminates. Let the coordinator in a round $n$ decide for a value, say $^ b$ . Then the coordinator received more than $k$ acks in this round, so at the end of this round

(1) there are more than $k$ processes $q$ with last-update $_ q \geq n$ , and (2) last-update $\mathbf { \dot { q } } \geq n$ implies value ${ \bf \dot { \boldsymbol { q } } } = { \boldsymbol { b } }$ .

We argue, by induction on $m - n$ , that properties (1) and (2) are preserved in all rounds $m \geq n$ . The base case $m = n$ was already argued. For the inductive case, consider a round $m > n$ . By induction, (1) and (2) hold at the start of this round. Since the coordinator ignores the votes of only $k$ >processes, by (1) it takes into account at least one vote with last-update $\geq n$ to determine its new value. Hence, by (2), the coordinator sets its value to $^ b$ and broadcasts $\langle \mathbf { v a l u e } , m , b \rangle$ . This means that (1) and (2) still hold at the end of round $m$ , which concludes the proof of the claim. It implies that from round $n$ onward, processes can decide only for $^ b$ .

If all processes initially happen to select the same random bit $^ b$ , then clearly in each round all correct processes stick with the value $^ b$ , so they can only decide for $^ b$ .

Now we argue that eventually some correct process will decide. Since the failure detector is eventually weakly accurate, from some round onward, some correct process $p$ will never be suspected. So in the next round where $p$ is the coordinator, all correct processes will wait for a value message from $p$ . Therefore, $p$ will receive at least $N - k$ acks, and since $N - k > k$ , it will decide. All correct processes will eventually receive the decide message of $p$ and will also decide. ⊓⊔

# 12.6 Consensus for Shared Memory

In this last section on consensus in the presence of crashes, we make a shift to the shared memory paradigm, in which processes communicate with each other via shared variables in main memory, called registers (see section 2.3). Since shared memory will take a more prominent role from chapter 14 onward, first it is discussed how the message passing and shared memory paradigms can be related to each other. Then we will turn our attention to the consensus problem in the shared memory setting.

# Emulating shared memory with message passing

A multi-reader single-writer register can be emulated in a wait-free manner with message passing, under the assumption that less than half the network crashes. Recall that in a wait-free algorithm, even if some processes crash, the correct processes are still guaranteed to make progress. Basically this emulation works as follows. Each process holds a copy of the register, containing both its value and a sequence number. At each write operation, the writer increases the sequence number by 1 and broadcasts the new value and the sequence number. Every process that receives this pair stores it and sends back an acknowledgment. The write operation is completed when more than $\frac { N } { 2 }$ acknowledgments have been received. A read operation starts by asking all processes (including the reader itself) for their value and sequence number pairs. When more than $\frac { N } { 2 }$ such pairs have been received by the reader, it picks the value with the greatest sequence number. It broadcasts this pair and completes the read operation after receiving more than $\frac { N } { 2 }$ acknowledgments from readers that they have taken in this pair.

A read operation starting after a write operation with sequence number $k$ is guaranteed to receive at least one value with a sequence number $\geq k$ , so will return a value associated to a sequence number $\geq k$ . Now consider a read operation $R _ { 1 }$ starting after the completion of a read operation $R _ { 0 }$ that returned a value associated to a sequence number $k$ . Since $R _ { 0 }$ broadcast this pair, $R _ { 1 }$ is guaranteed to receive at least one value with a sequence number $\geq k$ , so will return a value associated to a sequence number $\geq k$ .

A multi-writer register with $k$ writers can be emulated by means of $k$ multi-reader single-writer registers (see exercise 12.18). Hence multi-writer registers can also be emulated with message passing.

# Impossibility of consensus with read and write operations

We start the discussion of consensus in shared memory with another impossibility result. With only atomic read and write operations it is impossible to develop a wait-free binary consensus algorithm, even if there are only two processes. To formally argue this impossibility result, we use the notion of a critical configuration, meaning the configuration is bivalent and each of its transitions results in a configuration that is not bivalent. In other words, the configuration is still undecided, but each possible event enforces a decision. Every consensus algorithm contains such a critical configuration because by validity we can start in a bivalent initial configuration and by termination we must after a finite number of transitions reach a configuration that is not bivalent (cf. the proof of theorem 12.1).

Suppose toward a contradiction that a wait-free consensus algorithm for two processes $p$ and $q$ using only atomic read and write operations does exist. Consider a critical configuration: let an event from $p$ lead to decision 0, and an event from $q$ to decision 1. We distinguish four different cases.

• If $p$ does a read, then $q$ can still run solo to a decision 1.   
• Likewise, if $q$ does a read, $p$ can still run solo to a decision 0.   
Let $p$ and $q$ do writes to different registers. Both orders of these two events lead to the same configuration. Let $p$ and $q$ do writes to the same register. If $p$ does its write first, $q$ can still run solo to a decision 1. Likewise, if $q$ does its write first, $p$ can still run solo to a decision 0.

All cases contradict the assumption that a first event from $p$ or from $q$ is guaranteed to lead to the decision 0 or 1, respectively.

# Consensus with compare-and-set

We can achieve wait-free consensus using the read-modify-write operation compare-and-set, which carries two arguments. Recall that when this operation is applied on a register, first it checks whether the current value of the register equals the value in the first argument. If so, the current value of the register is overwritten with the value in the second argument. A Boolean value is returned to signal whether the new value was actually written.

Instead of binary consensus, we now consider the consensus problem that all processes should uniformly decide for the same value from some data domain $D$ , because this more general problem can be solved conveniently with compare-and-set. The consensus algorithm works as follows. Initially, each process $p$ is provided with a random value valuep from $D$ . Let $\perp$ denote a special value that is not in $D$ . Some multiwriter register initially carries the value $\perp$ . Each process $p$ performs compare-and-se $t ( \perp , \nu a l u e _ { p } )$ on this ,register. The idea is that all processes decide for the value of the first process to perform this operation. If $p$ gets true returned, then it can decide for its own value, since it is the first to perform this operation on the register. If it gets false returned, some other process was the first to perform this operation. Then $p$ reads the value in the register and decides for that value. This is a correct consensus algorithm because the first compare-and-se $( \perp , \nu )$ operation that is performed on the register reads the value $\perp$ and overwrites it with $\nu$ ,in one atomic step. All subsequent compare-and-set operations on the register will therefore return false.

Remarkably, other standard read-modify-write operations, such as test-and-set and get-and-increment, do not allow for a wait-free consensus algorithm, if there are three or more processes. The problem is that these operations are either overwriting, meaning that they write a predetermined new value without taking into account the current value of the register, or commuting, meaning that the two orders in which two processes can apply this operation are guaranteed to produce the same value in the register. We now argue this impossibility result in more detail, for binary consensus, distinguishing between the two types of readmodify-write operations: overwriting and commuting.

Suppose, toward a contradiction, that a binary consensus algorithm exists that is based on test-and-set or get-and-increment. Consider a critical configuration of the algorithm. Let $p , q$ , and $r$ be different processes, where a read-modify-write operation by $p$ or $q$ enforces the decision 0 or 1, respectively. If these critical operations are performed on different registers, and $p$ and $q$ crash immediately after having performed their operations, then $r$ cannot figure out whether $p$ or $q$ performed its operation first, so $r$ does not know whether to decide for 0 or 1. Hence, these operations must be performed on the same register. We distinguish between the two types of read-modify-write operations.

First, consider test-and-set, which is overwriting in nature. As a result, even if these operations by $p$ and $q$ are performed on the same register, $r$ still may not be able to figure out who performed this operation first if $p$ and $q$ crash. Because $r$ cannot discriminate between the situation where first $p$ and then $q$ perform the operation and the situation where only $q$ performs the operation.   
Now consider get-and-increment, which is commuting in nature. As a result, again $r$ still may not be able to figure out who performed this operation on a register first if $p$ and $q$ crash. Because $r$ cannot discriminate between the situation where first $p$ and then $q$ perform the operation and the situation where first $q$ and then $p$ perform the operation.

# Bibliographical notes

The impossibility of a terminating 1-crash consensus algorithm was proved in [42].4 The Bracha-Toueg crash consensus algorithm originates from [16], The Chandra-Toueg crash consensus algorithm was proposed in [22].5 The emulation of a multi-reader single-writer register in a message passing framework stems from [7].6

The strong consensus property of compare-and-set, in contrast to atomic read and write operations as well as overwriting and commuting read-modify-write operations, was observed in [53].7

# 12.7 Exercises

Exercise 12.1 Prove that, if $N > 1$ , every 1-crash consensus algorithm has a bivalent initial configuration.

Exercise 12.2 [117] Give terminating 1-crash consensus algorithms for each of the following restrictions on the chosen values in initial configurations.

(a) An even number of processes choose the value 1.   
(b) At least $\lceil \frac { N } { 2 } + 1 \rceil$ processes choose the same value.

Exercise 12.3 Argue that each algorithm for 1-crash consensus exhibits a fair infinite execution.

Exercise 12.4 Give a Monte Carlo algorithm for $k$ -crash consensus that works for each $k < N$ .

Exercise 12.5 Consider a complete network of five processes. Apply the Bracha-Toueg 2-crash consensus algorithm, where initially three processes choose the value 0 and two processes choose the value 1. Give two computations, one where all correct processes decide for 0 and one where all correct processes decide for 1.

Exercise 12.6 Consider the Bracha-Toueg $k$ -crash consensus algorithm for $k < \frac { N } { 2 }$

(a) [117] Let more than N+k2 processes choose the value $^ b$ in the initial configuration. Prove that then the correct processes always decide for $^ b$ within three rounds.   
(b) Let more than $\frac { N - k } { 2 }$ processes choose the value $^ b$ in the initial configuration. Give a computation in which all correct processes decide for $^ b$ within three rounds.   
(c) Let $N - k$ be even. Is a decision for $^ b$ possible if exactly $\frac { N - k } { 2 }$ processes choose the value $^ b$ in the initial configuration?

Exercise 12.7 Give examples to show that if the scheduling of messages is not fair, then the Bracha-Toueg crash consensus algorithm may not terminate with probability one.

(a) One example with $N = 4$ and $k = 1$ .   
(b) A second example with $N = 3$ and $k = 1$ .

Exercise 12.8 Suppose that in the Bracha-Toueg $k$ -crash consensus algorithm, processes can randomly select values from a finite data domain with more than two elements (instead of the bit 0 or 1). Is the resulting algorithm, with $k < \frac { N } { 2 }$ and the assumption that scheduling of messages is fair, still a Las Vegas algorithm that <terminates with probability one? If so, argue why this is the case. If not, give a counterexample.

Exercise 12.9 Suppose the Bracha-Toueg $k$ -crash consensus algorithm is adapted as follows. Only $k$ (instead of $k + 1$ ) incoming messages with a weight greater than $\frac { N } { 2 }$ are sufficient to perform a decide event. Give an example, with $N = 3$ and $k = 1$ , to show that this could lead to inconsistent decisions.

Exercise 12.10 Suppose that the implementation of the eventually strongly accurate failure detector is adapted as follows. If $p$ receives a message from a suspected process $q$ , then it no longer suspects $q$ . If this message arrives $\nu + d _ { p } + \rho$ time units after the previous message from $q$ , for some positive real number $\rho$ , then $d _ { p } \gets d _ { p } + \rho$ ν ρ ρ. Give an example to show that this failure detector need not be eventually strongly accurate.

Exercise 12.11 Consider a complete network of five processes. Apply the Chandra-Toueg 2-crash consensus algorithm, where initially four processes choose the value 0 and one process chooses the value 1. Give a computation in which all correct processes decide for 1.

Exercise 12.12 What is the purpose of the negative acknowledgment nack in the Chandra-Toueg crash con sensus algorithm?

Exercise 12.13 Suppose we adapt the Chandra-Toueg $k$ -crash consensus algorithm for $k < \frac { N } { 2 }$ as follows. If the coordinator $p _ { c }$ receives at least (instead of more than) $k$ acknowledgments ack, then $p _ { c }$ decides for its value. Give an example, with $N = 3$ and $k = 1$ , to show that this could lead to inconsistent decisions.

Exercise 12.14 Explain where the proof of theorem 12.1 breaks down in the presence of a (complete and) eventually weakly accurate failure detector.

Exercise 12.15 Explain why the rotating coordinator crash consensus algorithm may not terminate if it employs an incomplete, strongly accurate failure detector.

Exercise 12.16 Consider the requirement that processes that never crash are never suspected. Argue that this requirement is weaker than strong accuracy and stronger than eventual strong accuracy.

Exercise 12.17 Suppose that in the emulation of a multi-reader single-writer register, a read operation would complete after broadcasting its value and sequence number pair, without waiting for acknowledgments. Explain what could go wrong.

Exercise 12.18 Explain how a multi-writer register with $k$ writers can be emulated by $k$ multi-reader singlewriter registers, by letting each writer write a value paired with a sequence number in its register and letting readers consult all $k$ registers before deciding upon a value. Be careful that concurrent writers may write values with the same sequence number.

Exercise 12.19 Give examples to show that compare-and-set is neither overwriting nor commuting. In other words, this operation does not blindly overwrite the value in a register, and performing two of these operations on a register in a different order may produce different results.

Exercise 12.20 Argue that the consensus algorithm using compare-and-set satisfies the termination, agreement, and validity properties.

Exercise 12.21 Give a wait-free consensus algorithm using test-and-set that works for two processes.

# Consensus with Byzantine Failures

In this chapter, we consider Byzantine failures, meaning that a process may start to show behavior that is not in line with the specification of the distributed algorithm that is being executed. This can happen when a hardware error occurs or if one of the processes is a malicious intruder (see also chapter 19). The class of Byzantine failures encompasses crash failures. We assume that processes are either correct or Byzantine from the start. Processes do not know which of the other processes are Byzantine. The network topology is still assumed to be complete.

Again, the challenge we pose to the distributed system is to let its correct processes agree on a value. In a (binary) Byzantine consensus algorithm, each correct process randomly chooses an initial value 0 or 1. In all executions of a Byzantine consensus algorithm, each correct process should perform exactly one decide event. The termination and agreement properties mentioned at the start of chapter 12 must be satisfied, together with a slightly adapted version of validity.

• Validity: If all correct processes choose the same initial value, then all correct processes decide for this value.

A $k$ -Byzantine consensus algorithm, for a $k > 0$ , is a Byzantine consensus algorithm that can cope with up to $k$ >Byzantine processes. Similar to the case of crash consensus, the validity requirement implies that each Byzantine consensus algorithm has a bivalent initial configuration (cf. exercise 12.1).

# 13.1 Bracha-Toueg Byzantine Consensus Algorithm

With Byzantine failures, fewer incorrect processes can be allowed than in the case of crashing processes, if one wants to achieve a Las Vegas consensus algorithm. A $k$ -Byzantine consensus algorithm is possible only if $k < \frac { N } { 3 }$ . Intuitively, this is for the following reason. Correct processes must be able to cope with $k$ Byzantine <processes, which may not cast a vote. So they can collect votes from at most $N - k$ processes, since otherwise a deadlock could occur. Among these $N - k$ processes, $k$ could be Byzantine. Only if $k < \frac { N } { 3 }$ is it guaranteed that (in the worst case) the $N - 2 k$ <collected votes from correct processes outnumber the $k$ collected votes from Byzantine processes.

Theorem 13.1 Let $\begin{array} { r } { k \geq \frac { N } { 3 } } \end{array}$ . There is no Las Vegas algorithm for $k$ -Byzantine consensus.

Proof. Suppose, toward a contradiction, that such an algorithm does exist. Since $k \geq \lceil \frac { N } { 3 } \rceil$ , the processes can be divided into two sets $s$ and $T$ that both contain $N - k$ processes, while $S \cap T$ contains at most $k$ processes.

Since $s$ contains $N - k$ elements, the processes in $s$ must be able to come to a decision by themselves if all processes outside $s$ are Byzantine. In other words, $s$ is always 0-potent or 1-potent. Likewise, $T$ is always 0-potent or 1-potent. In each reachable configuration, $s$ and $T$ should be either both 0-potent or both 1-potent, for otherwise they could independently decide for different values. Because the processes in $S \cap T$ could all be Byzantine, and could therefore be free to participate in an execution leading to a decision for $^ b$ with the processes in $s$ , while participating in an execution leading to a decision for $1 - b$ with the processes in $T$ .

Consider a bivalent initial configuration $\gamma$ . Then there must be a configuration $\delta$ reachable from $\gamma$ , and a transition $\delta  \delta ^ { \prime }$ , with $s$ and $T$ both only $^ b$ -potent in $\delta$ and only $( 1 - b )$ -potent in $\delta ^ { \prime }$ , for some $b \in \{ 0 , 1 \}$ . δ δ δSince this transition would correspond to a single event, at a process in either $s$ or $T$ δ ,, clearly such a transition cannot exist. ⊓⊔

If $k < \frac { N } { 3 }$ , then a Las Vegas algorithm for $k$ -Byzantine consensus does exist. The Bracha-Toueg $k$ -Byzantine consensus algorithm works roughly as follows. Just as in the Bracha-Toueg $k$ -crash consensus algorithm, there are successive rounds in which every correct, undecided process sends its value to all processes and determines a new value, based on the first $N - k$ messages it receives in this round: the new value is 0 if most messages voted 0 and 1 otherwise. A process $p$ decides for $^ b$ if in a round it receives more than $\textstyle { \frac { N + k } { 2 } } $ $^ b$ -votes; note that by assumption $\begin{array} { r } { \frac { N + k } { 2 } < N - k } \end{array}$ . In that case, $p$ broadcasts $\langle \mathbf { d e c i d e } , b \rangle$ and terminates. The other processes interpret $\langle \mathbf { d e c i d e } , b \rangle$ as a $^ b$ -vote by $p$ for all rounds to come. Note that they cannot simply decide for $^ b$ ,at the reception of this message, since $p$ might be Byzantine. This completes the informal description of the algorithm, except for a crucial verification phase of votes.

The following example shows that this algorithm is flawed if in a round two correct processes can accept different votes from a Byzantine process.

Example 13.1 Consider a network of four processes $p , q , r$ , and $s$ , with $k = 1$ . Suppose $q$ is Byzantine. We study one possible computation of the Bracha-Toueg 1-Byzantine consensus algorithm. During each round, a correct process waits for three votes and needs three $^ b$ -votes to decide for $^ b$ . Initially, $p$ and $s$ randomly choose the value 1, and $r$ chooses the value 0.

In round 0, $p , r$ , and $s$ broadcast their values, while $q$ sends a 0-vote to $p$ and $r$ and a 1-vote to $s$ . Next, $p$ and $r$ take into account the 1-vote by $p$ and 0-votes by $q$ and $r$ , and each sets its value to 0. Furthermore, $s$ takes into account 1-votes by $p , q$ , and $s$ , as a result decides for 1, and broadcasts $\langle \mathbf { d e c i d e } , 1 \rangle$ . In round 1, $p$ , and $r$ broadcast their values, while $q$ broadcasts a 0-vote. Next, $p$ and $r$ ,take into account 0-votes by $p , q$ , and $r$ and as a result decide for 0. So we have inconsistent decisions.

The cause of the inconsistent decisions in example 13.1 is that in round 0, $p$ and $r$ use a 0-vote from $q$ , while $s$ uses a 1-vote from $q$ , which can happen because $q$ is Byzantine. To avoid this mishap, the BrachaToueg Byzantine $k$ -consensus algorithm includes a verification phase of votes. When a process $p$ receives a $^ b$ -vote from a process $q , p$ does not accept this vote straightaway. Instead, $p$ echoes this vote to all processes, and it accepts a $^ b$ -vote by $q$ only if it receives an echo of a $^ b$ -vote by $q$ in this round from more than $\textstyle { \frac { N + k } { 2 } } $ processes. This guarantees that the correct processes in a round never accept different votes from the same process, even if that process is Byzantine (see the proof of theorem 13.2).

oted, a correct process decides for , each correct process then will find $^ b$ if it acceptsat more than e than of the $\frac { N + k } { 2 }$ $^ b$ -votes in a round. Since votes it accepts in this ro ${ \frac { N + k } { 2 } } =$ ${ \frac { N - k } { 2 } } + k$ $\frac { N - k } { 2 }$ $N - k$ $^ b$ -votes. So, at the end of this round, all correct processes will take on the value $^ b$ and hence will continue to do so for all future rounds. This guarantees that the correct processes all decide for the same value (again, see the proof of theorem 13.2).

We now give a more precise description of the Bracha-Toueg $k$ -Byzantine consensus algorithm. Initially, each correct process $p$ randomly chooses a value 0 or 1 and assigns it to local variable value $_ p$ . In each round $n \geq 0$ , each correct, undecided process $p$ acts as follows:

$p$ sends $\left. \mathbf { v o t e } , n , \nu a l u e _ { p } \right.$ to all processes (including itself).   
When $p$ , ,receives $\langle \mathrm { v o t e } , m , b \rangle$ from a process $q$ , it sends $\langle \mathbf { e c h o } , q , m , b \rangle$ to all processes (including itself).   
• $p$ stores incoming messages $\langle \mathrm { v o t e } , m , b \rangle$ and $\langle \mathbf { e c h o } , q , m , b \rangle$ with $m > n$ for future rounds. $p$ counts incoming messages $\langle \mathbf { e c h o } , q , n , b \rangle$ , , , for each pair $q , b$ >. When more than $\displaystyle \frac { N + k } { 2 }$ such messages have arrived, $p$ accepts a $^ b$ -vote by $q$ . The round is completed when $p$ has accepted votes from $N - k$ processes. If most votes are for 0, then value $_ p  0$ . Otherwise value ${ \bf \Phi } _ { p } \gets 1$ . If more than $\textstyle { \frac { N + k } { 2 } }$ of the accepted votes are for $^ b$ , then $p$ decides for $^ b$ , broadcasts $\langle \mathbf { d e c i d e } , b \rangle$ , and terminates.

The other processes interpret $\langle \mathbf { d e c i d e } , b \rangle$ as a $^ b$ -vote by $p$ , and a $^ b$ -echo by $p$ for each $q$ , for all rounds to come.

Processes keep track of whether multiple messages $\left. \mathbf { v o t e } , m , \right.$ or $\langle \mathbf { e c h o } , q , m , \rangle$ arrive via the same chan, , , , ,nel; the sender must be Byzantine. To avoid miscounts, only the first of these messages is taken into account.

Theorem 13.2 If the scheduling of messages is fair, then the Bracha-Toueg $k$ -Byzantine consensus algorithm, for each $k < \frac { N } { 3 }$ , is a Las Vegas algorithm that terminates with probability one.

Proof. First, we prove that agreement is satisfied: correct processes cannot decide for different values. Next, we prove that the algorithm terminates with probability one, under the assumption that the scheduling of messages is fair. The proof of validity is left as an exercise (see exercise 13.4).

During each round, the correct processes eventually accept $N - k$ votes, since there are at least $N - k$ correct processes that faithfully confirm each other’s votes, and by assumption $\begin{array} { r } { N - k > { \frac { N + k } { 2 } } } \end{array}$ .

In a round $n$ , let correct processes $p$ and $q$ accept votes for $^ b$ and $b ^ { \prime }$ , respectively, from a (possibly Byzantine) process $r$ . Then $p$ and $q$ received more than $\textstyle { \frac { N + k } { 2 } } $ messages $\langle \mathbf { e c h o } , r , n , b \rangle$ and $\langle \mathbf { e c h o } , r , n , b ^ { \prime } \rangle$ , respectively. Since this adds up to more than $N + k$ messages in total, more than $k$ , , , , ,processes, and therefore at least one correct process, sent such messages to both $p$ and $q$ . This implies that $b = b ^ { \prime }$ .

Suppose a correct process $p$ decides for $^ b$ at the end of a round $n$ , meaning that $p$ accepted more than $\frac { N + k } { 2 }$ $^ b$ -votes. In every round, each correct process ignores votes from only $k$ processes, and we argued that two orrect processes never accept different values from-votes, all correct processes will accept more than So, since -votes in r $p$ acnd pted more than . Hence, after r $\textstyle { \frac { N + k } { 2 } } $ $^ b$ $\begin{array} { r } { \frac { N + k } { 2 } - k = \frac { N - k } { 2 } } \end{array}$ $b _ { \mathbf { \ell } }$ $n$

$n$ , all correct processes have the value $^ b$ . If after a round $m$ all correct processes have the value $^ b$ , then after round $m + 1$ they still do, because they accept at least $\begin{array} { r } { N - 2 k > { \frac { N - k } { 2 } } b } \end{array}$ -votes in round $m + 1$ . This implies that the correct processes stick to the value $^ b$ from round $n$ >onward and hence cannot decide for different values.

Let $s$ be a set of $N - k$ correct processes. Because of fair scheduling, in each round there is a probability $\rho > 0$ that each process in $s$ accepts $N - k$ votes from the processes in $s$ . With probability $\rho ^ { 2 }$ this happens ρ >in consecutive rounds $n , n + 1$ . After round $n$ , all processes in $s$ have the same value $^ b$ ρ. After round $n + 1$ , all processes in $s$ have decided for $^ b$ , and broadcast $\langle \mathbf { d e c i d e } , b \rangle$ . To conclude, the algorithm terminates with probability one. ⊓⊔

Example 13.2 We revisit example 13.1 but now taking into account the verification phase of votes. It concerns a network of four processes $p , q , r .$ , and $s$ , with $k = 1$ , where $q$ is Byzantine. We study one possible computation of the Bracha-Toueg 1-Byzantine consensus algorithm on this network. During each round, a correct process needs three confirming echoes to accept a vote, three accepted votes to complete the round, and three accepted $^ b$ -votes to decide for $^ b$ . Initially, $p$ and $s$ randomly choose the value 1, and $r$ chooses the value 0. In the pictures of the consecutive rounds, for every process, two accepted votes from other processes and its own value in that round are depicted, which are used to determine the value of that process in the next round.

In round 0, $p$ and $r$ accept the 1-vote by $p$ and 0-votes by $q$ and $r$ , because they get confirmations for these votes from $p , q$ , and $r$ . As a result, each sets its value to 0. Furthermore, $s$ accepts 1-votes by $p$ and $s$ , because it gets confirmations for these votes from $p , r ,$ and $s$ . However, $s$ does not accept the 1-vote by $q$ , because it receives only two confirmations, from $q$ and $s$ . In the end, $s$ accepts the 0-vote by $r$ , for which it gets confirmations from $p , r _ { \ast }$ , and $s$ , and sets its value to 1.

![](images/f2e0f45c1e0b5bf0ec2f072158035c37380cec98c1a3051d2792a8913a32cd15.jpg)

In round 1, $p$ and $r$ accept 0-votes by $p$ and $q$ , because they get confirmations for these votes from $p , q$ , and $r$ . Moreover, $r$ accepts the 0-vote by $r _ { \cdot }$ , decides for 0, and broadcasts $\langle \mathbf { d e c i d e } , 0 \rangle$ . On the other hand, $p$ accepts the 1-vote by $s$ , because it gets confirmations for these votes from $p , r ,$ , and $s$ , and sets its value to 0. Once again, $s$ does not accept the 1-vote by $q$ , because it receives only two confirmations, from $q$ and $s .$ . Instead, $s$ accepts 0-votes by $p$ and $r$ and the 1-vote by $s$ , because it gets confirmations for these votes from $p , r$ , and $s$ . As a result, $s$ sets its value to 0.

![](images/b5860aa6160c737de1f4c86065362400a1b1faaf12033cfac179665e5c147188.jpg)

Now that all correct processes have the value 0, in all future rounds this will remain the case. A decision for 0 by $p$ and $s$ could be postponed indefinitely if $q$ gets a 1-vote accepted by $p$ and $s$ in successive rounds. However, in order to complete this computation swiftly, we let $\langle \mathbf { d e c i d e } , 0 \rangle$ arrive at $p$ and $s$ , and in round 2 we let $p$ and $s$ accept each other’s 0-votes, so they decide for 0.

![](images/06f431b736caefb2f00fa2a5396af564dc000d72fabb2142e2e85b2b711c9d5d.jpg)

# 13.2 Mahaney-Schneider Synchronizer

In this section, we revisit bounded delay networks, in which there is an upper bound $d _ { \mathrm { m a x } }$ on network latency; processes carry a local clock with $\rho$ -bounded drift for some $\rho > 1$ (see section 11.2). It is shown that even in ρthe presence of Byzantine processes, a precision $\delta > 0$ ρ > of the local clocks can be achieved: at any time $\tau$ and for each pair of correct processes $p$ and $q$ , $| C _ { p } ( \tau ) - C _ { q } ( \tau ) | \leq \delta$ τ. Since local clocks may drift from real time, they need to be synchronized regularly to obtain such precision.

First, it is shown that a synchronization algorithm to keep local clocks in sync is possible only if fewer than one-third of the processes are Byzantine.

Theorem 13.3 Let $\begin{array} { r } { k \geq \frac { N } { 3 } } \end{array}$ . There is no $k$ -Byzantine clock synchronization algorithm.

Proof. Suppose we want to achieve clock synchronization so that the local clocks have precision $\delta > 0$ . Consider a network of three processes $p , q$ , and $r$ , where $r$ is Byzantine, and let $k = 1$ δ >. (The following computation can be easily extended to general $N$ and $\begin{array} { r } { k \geq \frac { N } { 3 } } \end{array}$ ; see exercise 13.6.)

Let the clock of $p$ run faster than the clock of $q$ . Suppose a synchronization round takes place at real time $\tau$ , when $r$ sends $C _ { p } ( \tau ) + \delta$ to $p$ , and $C _ { q } ( \tau ) - \delta$ to $q$ . Since $r$ reports a clock value to $p$ that is within $\delta$ of $p$ ’s τ τ δlocal clock value, and since $p$ τ δ δcan compare it only with the clock value from one other process (i.e., $q$ ), $p$ cannot recognize that $r$ is Byzantine. Likewise, $q$ cannot recognize that $r$ is Byzantine. So $p$ and $q$ must stay within range $\delta$ of the value reported by $r$ , meaning that $p$ cannot decrease and $q$ cannot increase its clock value.

By repeating this scenario at each synchronization round, the clock values of $p$ and $q$ get farther and farther apart. So eventually $p$ will need to choose whether its clock stays within range $\delta$ of $q$ ’s or $r$ ’s clock δwithout being able to determine which of the two processes is Byzantine, and likewise for $q$ . ⊓⊔

If at most $k < \frac { N } { 3 }$ processes are Byzantine, then clock synchronization can be achieved. To simplify the <forthcoming presentation of Byzantine clock synchronization, we take the bound $d _ { \mathrm { m a x } }$ on network latency to be zero. (In a sense, we assume that $d _ { \mathrm { m a x } }$ is negligible compared to $\delta$ .) Taking into account $d _ { \mathrm { m a x } }$ is left as an exercise (see exercise 13.8).

In the Mahaney-Schneider $k$ -Byzantine clock synchronization algorithm, processes regularly communicate their clock values to each other, and each process takes the average of all these clock values, whereby clock values that are provably from Byzantine processes are disregarded. It is assumed that at the start of a clock synchronization round, the local clocks have precision $\delta > 0$ . This algorithm achieves that after each clock synchronization round, the local clocks have precision $\frac { 2 } { 3 } \cdot \delta$ >.

δThe Mahaney-Schneider synchronizer proceeds in synchronization rounds, in which each correct process

collects the clock values of all processes,   
• discards those reported values $\tau$ for which fewer than $N - k$ processes report a value in the interval $\left[ { \tau - \delta , \tau + \delta } \right]$ τ (they are from Byzantine processes), τ δ, τ δreplaces all discarded and nonreceived values by an accepted value, and takes the average of these $N$ values as its new clock value.

Theorem 13.4 The Mahaney-Schneider synchronizer is a $k$ -Byzantine clock synchronization algorithm for each k  N3 .

Proof. Consider two correct processes $p$ and $q$ in some synchronization round. First, we argue that if in this round $p$ and $q$ accept clock values $a _ { p }$ and $a _ { q }$ , respectively, then

$$
| a _ { p } - a _ { q } | \leq 2 \delta .
$$

Since $p$ accepted $a _ { p }$ , in this round at least $N - k$ processes reported a value in $[ a _ { p } - \delta , a _ { p } + \delta ]$ to $p$ . Likewise, at least $N - k$ processes reported a value in $\left[ a _ { q } - \delta , a _ { q } + \delta \right]$ to $q$ . So at least $N - 2 k$ δ, δprocesses reported a value in $\left[ a _ { p } - \delta , a _ { p } + \delta \right]$ to $p$ as well as a value in $\left[ a _ { q } - \delta , a _ { q } + \delta \right]$ δ to $q$ . Since $N - 2 k > k$ , there is a correct process among δ, δ δ, δthese processes. This correct process reports the same value to $p$ and $q$ >, so $\left[ a _ { p } - \delta , a _ { p } + \delta \right]$ and $\left[ a _ { q } - \delta , a _ { q } + \delta \right]$ have a nonempty intersection. This implies $| a _ { p } - a _ { q } | \leq 2 \delta$ .

For each process $r$ , let $a _ { p r }$ and $a _ { q r }$ δdenote the value that $p$ and $q$ , respectively, accept from (or assign to) $r$ . Then $p$ and $q$ compute as new clock values $\begin{array} { r } { \frac { 1 } { N } { \cdot } \left( \sum _ { \mathrm { p r o c e s s e s } r } a _ { p r } \right) } \end{array}$ and $\begin{array} { r } { \frac { 1 } { N } { \cdot } \left( \sum _ { \mathrm { p r o c e s s e s } r } a _ { q r } \right) } \end{array}$ , respectively. By the preceding argument, $| a _ { p r } - a _ { q r } | \leq 2 \delta$ for all processes $r$ . And ${ a _ { p r } = a _ { q r } }$ for all correct processes $r$ . Hence,

$$
\left| { \frac { 1 } { N } } \cdot \left( \sum _ { \mathrm { p r o c e s s e s } ~ r } a _ { p r } \right) - { \frac { 1 } { N } } \cdot \left( \sum _ { \mathrm { p r o c e s s e s } ~ r } a _ { q r } \right) \right| \leq { \frac { 1 } { N } } \cdot k \cdot 2 \delta < { \frac { 2 } { 3 } } \cdot \delta .
$$

In the proof of theorem 13.4, it was shown that, after a synchronization round, the clocks at correct processes have a precision smaller than $\frac { 2 } { 3 } \cdot \delta$ . If the local clocks have been synchronized at time $\tau$ , then because of $\rho$ δ-bounded drift of local clocks, if no synchronization takes place in the time interval $[ \tau , \tau + R ]$ ,

$$
| C _ { p } ( \tau + R ) - C _ { q } ( \tau + R ) | < \frac { 2 } { 3 } \cdot \delta + \Bigl ( \rho - \frac { 1 } { \rho } \Bigr ) \cdot R < \frac { 2 } { 3 } \cdot \delta + \rho \cdot R .
$$

So, to achieve precision $\delta$ , a synchronization of local clocks should be performed every $\frac { \delta } { 3 \rho }$ time units.

# 13.3 Lamport-Shostak-Pease Broadcast Algorithm

To cope with crash failures, failure detectors were introduced in section 12.3 to try to detect crashed processes. Both implementations of failure detectors that were discussed are based on the absence of messages from a crashed process over a certain period of time. Detecting Byzantine processes is much more complicated, since they can keep on sending messages, and in general it is far from easy to determine that a process is performing events that are not in line with the specification of the distributed algorithm that is being executed. Therefore, to obtain an always correctly terminating consensus algorithm in the presence of Byzantine processes, another strategy is followed: the network is transformed into a synchronous system. As discussed in section 11.2, this can be realized in a bounded delay network if all processes have a $\rho$ -bounded clock, using also the ρMahaney-Schneider synchronizer from the previous section to achieve some precision $\delta$ for these clocks. In a synchronous network, it can be guaranteed that the votes from all correct processes are taken into account in each voting round. This will make it possible to accomplish consensus within a finite number of voting rounds.

In this section and the next, we consider a variation on the Byzantine consensus problem, called Byzantine broadcast, in the setting of synchronous networks. One process, called the general, randomly chooses an initial value 0 or 1. The other processes, called lieutenants, know who the general is. In each execution of a (binary) Byzantine broadcast algorithm, the requirements termination and agreement must be satisfied, together with a variation on validity.

• Dependence: If the general is correct, then it decides for its own initial value.

A $k$ -Byzantine broadcast algorithm can cope with at most $k$ Byzantine processes. It will come as no surprise that for $\begin{array} { r } { k \geq \frac { N } { 3 } } \end{array}$ such an algorithm does not exist, even if we have a synchronous network.

Theorem 13.5 Let $\begin{array} { r } { k \geq \frac { N } { 3 } } \end{array}$ . There is no (always correctly terminating) $k$ -Byzantine broadcast algorithm for synchronous networks.

Proof. Suppose, toward a contradiction, that a $k$ -Byzantine broadcast algorithm for synchronous networks does exist. Divide the processes into three disjoint sets $S , T$ , and $U$ , each with at most $k$ elements. Let the general be in $s$ . We consider three different scenarios, which are depicted as follows.

![](images/12abae20ad0cee2dd329c529b3d5b543c0ef7a88ff1678e6808f67536840dfb0.jpg)

In the first scenario, at the left, the processes in $U$ are Byzantine and the general starts with the value 0. The processes in $s$ and $T$ propagate 0. Moreover, by dependence and agreement, all processes in $S \cup T$ should decide for 0. The Byzantine processes in $U$ , however, propagate 1 to the processes in $T$ .

In the second scenario, in the middle, the processes in $T$ are Byzantine and the general starts with the value 1. The processes in $s$ and $U$ propagate 1. Moreover, by dependence and agreement, all processes in $S \cup U$ should decide for 1. The Byzantine processes in $T$ , however, propagate 0 to the processes in $U$ .

In the third scenario, at the right, the processes in $s$ , including the general, are Byzantine. The processes in $s$ propagate 0 to $T$ , and as a result the processes in $T$ do so also. Likewise, the processes in $s$ propagate 1 to $U$ , and as a result the processes in $U$ do so also. Note that the inputs of the processes in $T$ agree with the first scenario, so they all decide for 0. By contrast, the inputs of the processes in $U$ agree with the second scenario, so they all decide for 1. This violates agreement. ⊓⊔

The Lamport-Shostak-Pease broadcast algorithm for synchronous networks is a $k$ -Byzantine broadcast algorithm for each $\begin{array} { r } { k < \frac { N } { 3 } } \end{array}$ . Since the algorithm contains recursive calls to itself, we denote it with Broadcas $\dot { \mathbf { \rho } } _ { g } ( N , k )$ , where $g$ denotes the general. Let majority be a (deterministic) function that maps each ,multiset of elements from $\{ 0 , 1 \}$ either to 0 or to 1; in a multiset, the same element can occur multiple times. ,If more than half of the elements in a multiset $M$ are equal to $^ b$ , then it is required that majority $( M ) = b$ .

The algorithm Broadcas ${ \bf \chi } _ { g } ( N , k )$ proceeds in $k + 1$ pulses.

Pulse 1: The general $g$ , if correct, broadcasts its value and decides for its value.   
Each correct lieutenant $q$ acts as follows. If $q$ receives a value $^ b$ from $g$ , then it sets its value to $^ b$ ; otherwise it sets its value to 0.   
$^ *$ If $k = 0$ , then $q$ decides for its value.   
$^ *$ If $k > 0$ , then for every lieutenant $p , q$ takes part in Broadcast $_ p ( N - 1 , k - 1 )$ , starting in pulse 2. Pulse $k + 1$ (if $k > 0$ ): Each correct lieutenant $q$ ,has, for every lieutenant $p$ , computed a value in Broadcast $_ p ( N - 1 , k - 1 )$ ; it stores these $N - 1$ values in a multiset Decisionsq. Finally, $q$ sets its value to majority $( D e c i s i o n s _ { q } )$ and decides for this value.

Note that if the general is correct, then it can decide immediately, because by the dependence requirement all correct lieutenants are supposed to decide for the general’s value. If $k = 0$ , then the general is certainly correct, so the lieutenants can also decide immediately for the received value. However, if $k > 0$ , then the lieutenants must take into account that the general may be Byzantine. Therefore, each correct lieutenant $p$ starts a recursive call Broadcast $\cdot _ { p } ( N - 1 , k - 1 )$ , reminiscent of the echo principle in the Bracha-Toueg ,Byzantine consensus algorithm; the general is excluded from these calls. This gives rise to a cascade of recursive calls because if $k > 1$ , then each of these calls starts another $N - 2$ recursive calls, and so on.

>We now argue the correctness of the Lamport-Shostak-Pease broadcast algorithm in an informal fashion; a more formal proof will be given at the end of this section. If the general is correct, each recursive call

Broadcast $_ p ( N - 1 , k - 1 )$ with $p$ correct is guaranteed to produce the general’s value. Since a majority of the ,lieutenants are correct, by the definition of the majority function, all correct lieutenants will decide for the general’s value. On the other hand, if the general is Byzantine, by induction on $k$ , all correct lieutenants are guaranteed to compute the same values in the $N - 1$ recursive calls Broadcast $_ p ( N - 1 , k - 1 )$ , because there are at most $k - 1$ Byzantine lieutenants and $\begin{array} { r } { k - 1 < { \frac { N - 1 } { 3 } } } \end{array}$ ,. So owing to the deterministic nature of the majority function, in pulse $k + 1$ < all correct lieutenants will compute and decide for the same value in Broadcast ${ \bf \chi } _ { g } ( N , k )$ .

,We consider two examples of the Lamport-Shostak-Pease broadcast algorithm, one where the general is correct and one where the general is Byzantine.

Example 13.3 Consider a complete network of four processes $g , p , q$ , and $r$ , with $k = 1$ . Suppose the general $g$ and lieutenants $p$ and $q$ are correct, while lieutenant $r$ is Byzantine. We study one possible computation of the Lamport-Shostak-Pease broadcast algorithm Broadcas $_ g ( 4 , 1 )$ on this network.

In pulse 1, $g$ ,broadcasts and decides for 1. So after pulse 1, $p$ and $q$ carry the value 1. These two correct lieutenants build, by the three recursive calls Broadcas $_ s ( 3 , 0 )$ with $s \in \{ p , q , r \}$ , multisets $\{ 1 , 1 , b _ { p } \}$ and $\{ 1 , 1 , b _ { q } \}$ . The values $b _ { p }$ and $b _ { q }$ ,may be distinct if in Broadcastr $\left( 3 , 0 \right)$ , , the Byzantine process $r$ , ,sends different , ,values to $p$ and $q$ ,. Since the majority of values in these two multisets are 1, both $p$ and $q$ decide for 1, irrespective of the values $b _ { p }$ and $b _ { q }$ .

Example 13.4 Consider a complete network with $N = 7$ and $k = 2$ . Suppose the general $g$ and one lieutenant $r$ are Byzantine. We study one possible computation of the Lamport-Shostak-Pease broadcast algorithm Broadcas $_ { g } ( 7 , 2 )$ on this network.

,In pulse 1, the general sends 0 to three correct lieutenants and 1 to the two other correct lieutenants. The five correct lieutenants all build, using the six recursive calls Broadcast ${ \mathit { \Pi } } _ { s } ( 6 , 1 )$ , the same multiset $M =$ $\{ 0 , 0 , 0 , 1 , 1 , b \}$ for some $b \in \{ 0 , 1 \}$ . That is, even in Broadcast ${ \dot { r } } _ { r } ( 6 , 1 )$ , all correct lieutenants are guaranteed to compute the same value $^ b$ , so they all decide for majority $( M )$ .

For instance, in Broadcastr $( 6 , 1 )$ , the Byzantine lieutenant $r$ could send 0 to two correct lieutenants and 1 to the three other correct lieutenants. Then the five correct lieutenants all build, using five recursive calls Broadcas $\dot { \mathbf { \zeta } } _ { s } ( 5 , 0 )$ , the same multiset $M = \{ 0 , 0 , 1 , 1 , 1 \}$ . So in this case, b = majority $( \{ 0 , 0 , 1 , 1 , 1 \} ) = 1$ .

Theorem 13.6 The Lamport-Shostak-Pease broadcast algorithm is a $k$ -Byzantine broadcast algorithm for each k  N3 .

Proof. First, we prove that if the general is correct and fewer than $\frac { N - k } { 2 }$ lieutenants are Byzantine, then in Broadcas ${ \bf \chi } _ { g } ( N , k )$ all correct processes decide for $g$ 2’s value. (This holds even if ${ \frac { N - k } { 2 } } > k .$ .)

,We prove this claim by induction on . The base case is trivial because $g$ >is assumed to be correct, so all correct processes decide for $g$ ’s value in pulse 1. We now consider the inductive case $k > 0$ . Since $g$ is assumed to be correct, in pulse 1 each correct lieutenant sets its value to $g$ ’s value. Since $\begin{array} { r } { \frac { ( N - 1 ) - ( k - 1 ) } { 2 } = \frac { \bar { N - k } } { 2 } } \end{array}$ , by induction, for all correct lieutenants $q$ , in Broadcas $\cdot _ { q } ( N - 1 , k - 1 )$ the value of $q$ , meaning $g$ ’s value is ,computed. By assumption, a majority of the lieutenants are correct (because $k > 0$ ), so in pulse $k + 1$ a majority >of the values that a correct lieutenant computes in the recursive calls Broadcast $_ q ( N - 1 , k - 1 )$ equal $g$ ’s value. Hence, by the definition of the majority function, in pulse $k + 1$ , each correct lieutenant computes and decides for $g$ ’s value.

Now we prove that the Lamport-Shostak-Pease broadcast algorithm is a $k$ -Byzantine broadcast algorithm for each $\begin{array} { r } { k < \bar { \frac { N } { 3 } } } \end{array}$ , again by induction on $k$ . The case where $g$ is correct follows immediately from the statement < proved earlier, together with the fact that $\begin{array} { r } { \frac { N } { 3 } < \frac { N - k } { 2 } } \end{array}$ . Therefore, we can assume that $g$ is Byzantine (so $k > 0$ ). Then at most $k - 1$ < lieutenants are Byzantine. Since $\begin{array} { r } { k < \frac { N } { 3 } } \end{array}$ implies $\begin{array} { r } { k - 1 < \frac { N - 1 } { 3 } } \end{array}$ >, by induction all correct lieutenants compute the same value in Broadcast $_ p ( N - 1 , k - 1 )$ for every lieutenant $p$ . Hence, all correct lieutenants compute the same multiset $M$ in pulse $k + 1$ . So all correct lieutenants decide for the same value majority $( M )$ . ⊓⊔

# 13.4 Lamport-Shostak-Pease Authentication Algorithm

A signature scheme assumes finite (but very large) domains $\mathcal { M }$ of messages, also called plaintexts, and $\mathcal { E }$ of encryptions, also called cyphertexts. Each process $p$ has a private key $S _ { p } : \mathcal { M }  \mathcal { E }$ and a public key $P _ { p } : \mathcal { E }  \mathcal { M }$ , where the public key is the inverse of the private key, i.e., $P _ { p } ( S _ { p } ( m ) ) = m$ for all $m \in \mathcal { M }$ . (In particular, this means $S _ { p }$ is injective and $P _ { p }$ is surjective.) The private key is kept secret by $p$ while the public key is made public. The underlying assumption is that computing $S _ { p }$ from $P _ { p }$ is very expensive.

A private key can be used to provide a message with a digital signature, which serves as an authentication of the sender and makes it impossible for the sender to deny that it has sent the message. (Another digital signature scheme will be discussed in section 19.5.) If $p$ wants to send a signed message $m$ to $q$ such that other processes cannot fraudulently sign their messages with $p$ ’s signature, then $p$ can send $\langle m , S _ { p } ( m ) \rangle$ to $q$ . Because only $p$ can compute $S _ { p } ( m )$ , and $q$ can obtain $p$ ’s public key $P _ { p }$ ,, apply it to the signature $S _ { p } ( m )$ , and check whether the result equals the message $m$ .

The Lamport-Shostak-Pease authentication algorithm for synchronous systems uses a signature scheme to ensure that Byzantine processes cannot lie about the values they have received. It is a correct and terminating $k$ -Byzantine broadcast algorithm for each $k$ . Every process $p$ has a private key $S _ { p }$ and a public key $P _ { p }$ . We step away from binary consensus: the correct processes must uniformly pick a value from a large set of possible values, which constitutes the domain of private keys. The reason is that for a small domain (in the case of binary consensus consisting of only two values), computing $S _ { p }$ from $P _ { p }$ would be easy. It is assumed that processes $q \neq p$ cannot guess $S _ { p } ( \nu )$ for values $\nu$ without acquiring extra knowledge about $S _ { p }$ .

The Lamport-Shostak-Pease authentication algorithm proceeds in $k + 1$ pulses. Initially, the set $V a l u e s _ { q } =$ $\varnothing$ at all lieutenants $q$ .

• In pulse 1, the general, if correct, broadcasts $\left. \nu a l u e _ { g } , ( S _ { g } ( \nu a l u e _ { g } ) , g ) \right.$ and decides for valueg.   
• If in a pulse $i \leq k + 1$ a correct lieutenant $q$ , ,receives a message $\left. \nu , \left( \sigma _ { 1 } , p _ { 1 } \right) : \cdots : \left( \sigma _ { i } , p _ { i } \right) \right.$ that is valid, meaning that $^ *$ $p _ { 1 } = g$ , $^ *$ $p _ { 1 } , . . . , p _ { i } , q$ are all distinct, and $\begin{array} { r l } { \ast } & { { } P _ { p _ { k } } ( \sigma _ { k } ) = \nu } \end{array}$ for all $k = 1 , \dots , i ,$ , then $q$ σincludes $\nu$ in the set $V a l u e s _ { q }$ . If $i \leq k$ , then in pulse $i + 1$ , $q$ sends to all other lieutenants the message

$$
\langle \nu , ( \sigma _ { 1 } , p _ { 1 } ) : \cdot \cdot \cdot : ( \sigma _ { i } , p _ { i } ) : ( S _ { q } ( \nu ) , q ) \rangle .
$$

After pulse $k + 1$ , each correct lieutenant $q$ decides for $\nu$ if $V a l u e s _ { q }$ is a singleton $\{ \nu \}$ , or 0 otherwise. (In the latter case, the general is Byzantine.)

The second part of a message is a list of signatures. Suppose a correct lieutenant $q$ receives a valid message, meaning that the signatories are distinct, include the general and not the receiver, and each signatory $p$ has added the correct signature $S _ { p } ( \nu )$ , where $\nu$ is the value contained in the first part of the message. Then $q$ takes $\nu$ on board as a possible value, adds its own signature to the list of signatures, and broadcasts the message. A key observation is that each such message in pulse $k + 1$ contains a list of $k + 1$ signatures and thus at least one signature from a correct process. This means that no later than pulse $k + 1$ , every lieutenant will have received a valid message with this value. As a result, after pulse $k + 1$ , all correct lieutenants have computed the same set Values, so they all decide for the same value. And if the general is correct, then these sets are guaranteed to contain only $\nu a l u e _ { g }$ because then Byzantine processes cannot forge signatures by the general for other values. This will be argued more formally in the proof of theorem 13.7.

Example 13.5 Consider a complete network of four processes $g , p , q$ , and $r$ , with $k = 2$ . Suppose the general $g$ and lieutenant $r$ are Byzantine. We study one possible computation of the Lamport-Shostak-Pease authentication algorithm:

In pulse 1, $g$ sends $\langle 0 , ( S _ { g } ( 0 ) , g ) \rangle$ to $p$ and $q$ and $\langle 1 , ( S _ { g } ( 1 ) , g ) \rangle$ to $r$ . Then Value $s _ { p }$ and Value $s _ { q }$ become $\{ 0 \}$ . In pulse 2, $p$ and $q$ broadcast $\langle 0 , ( S _ { g } ( 0 ) , g ) : ( S _ { p } ( 0 ) , p ) \rangle$ and $\langle 0 , ( S _ { g } ( 0 ) , g ) : ( S _ { q } ( 0 ) , q ) \rangle$ , respectively. And $r$ sends $\langle 1 , ( S _ { g } ( 1 ) , g ) : ( S _ { r } ( 1 ) , r ) \rangle$ ,to only $q$ ,. Then Value $s _ { p }$ , remains $\{ 0 \}$ , ,, while Value $s _ { q }$ becomes $\{ 0 , 1 \}$ . ,In pulse 3, $q$ ,broadcasts $\langle 1 , ( S _ { g } ( 1 ) , g ) : ( S _ { r } ( 1 ) , r ) : ( S _ { q } ( 1 ) , q ) \rangle$ . Then $V a l u e s _ { p }$ becomes $\{ 0 , 1 \}$ . After pulse 3, $p$ and $q$ , , , , both decide for 0 because Valuesp and Value $s _ { q }$ ,contain two elements.

Theorem 13.7 The authentication algorithm from Lamport-Shostak-Pease is a $k$ -Byzantine broadcast algorithm for each $k < N$ .

Proof. If the general is correct, then Byzantine processes will not get an opportunity to forge a signature for a value different from valueg on behalf of the general. So owing to authentication, correct lieutenants will only add valu $e _ { g }$ to their set Values. Hence, all processes will decide for valueg.

Suppose a correct lieutenant $q$ receives a valid message $\langle \nu , \ell \rangle$ in a pulse $i = 1 , \ldots , k + 1$ . We distinguish between two cases:

• $i \leq k$ : Then, in the next pulse, $q$ broadcasts a message that will make all correct lieutenants add $\nu$ to their set Values. $i = k + 1$ : Since the list $\ell$ of signatures has length $k + 1$ , it contains a correct process $p$ . Then $p$ received a valid message $\langle \nu , \ell ^ { \prime } \rangle$ in a pulse $j \leq k$ . In pulse $j + 1$ , $p$ has broadcast a message that makes all correct lieutenants add $\nu$ , ℓto their set Values.

So after pulse $k + 1$ , Valuesq is the same for all correct lieutenants $q$ . Hence, after pulse $k + 1$ , they all decid for the same value. ⊓⊔

The Dolev-Strong optimization minimizes the number of required messages. This optimization lets each correct lieutenant broadcast at most two messages, with different values. When it has broadcast two different values, all correct lieutenants are certain to compute a set Values with at least two values, so all correct lieutenants will decide for 0.

# Bibliographical notes

The tight bound of $\frac { N } { 3 }$ on the number of Byzantine processes in achieving consensus dates back to [92].8 The Bracha-Toueg Byzantine consensus algorithm stems from [16]. The Mahaney-Schneider synchronizer originates from [77]. The Lamport-Shostak-Pease broadcast and authentication algorithms were proposed in [71]. The Dolev-Strong optimization is due to [38].

# 13.5 Exercises

Exercise 13.1 Give an $( N - 1 )$ -crash consensus algorithm for synchronous networks.

Exercise 13.2 Consider a complete network of four processes, in which one process is Byzantine. Apply the Bracha-Toueg 1-Byzantine consensus algorithm, where initially one correct process chooses the value 0 and two correct processes choose the value 1. Give a computation in which all correct processes decide for 0.

Exercise 13.3 [117] In the Bracha-Toueg $k$ -Byzantine consensus algorithm, suppose that more than $\textstyle { \frac { N + k } { 2 } } $ correct processes initially choose the value $^ b$ . Explain why the correct processes will eventually decide for $^ b$ .

Exercise 13.4 Argue that the Bracha-Toueg $k$ -Byzantine consensus algorithm, for each $k < \frac { N } { 3 }$ , satisfies validity.

Exercise 13.5 Consider three correct processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ and a Byzantine process $q$ . Let the local clocks of $p _ { 0 }$ and $p _ { 1 }$ run half as fast as real time, and let the local clock of $p _ { 2 }$ run twice as fast as real time. Consider the Mahaney-Schneider synchronizer for some precision $\delta > 0$ , whereby it is assumed that $d _ { \operatorname* { m a x } } = 0$ (that is, messages are communicated instantaneously).

(a) What is the smallest $\rho > 1$ for which the clocks of $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ are all $\rho$ -bounded?   
ρ >(b) Suppose that, at real time $\tau$ , the clocks of $p _ { 0 }$ and $p _ { 1 }$ are at $\begin{array} { r } { \tau - \frac { \delta } { 3 } } \end{array}$ ρ, while the clock at $p _ { 2 }$ is at $\begin{array} { r } { \tau + \frac { \delta } { 3 } } \end{array}$ . Let $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ τsynchronize their clocks at real time $\begin{array} { r } { \tau + \frac { \delta } { 3 \rho } } \end{array}$ τ (with the $\rho$ τ from part (a)). Show that whatever input $q$ gives at this synchronization point, the clocks of $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ are less than $\frac { 2 \delta } { 3 }$ apart.   
(c) Reptime exercise in par, the clocks of ) buand w leaving out can be more t $p _ { 0 }$ .n ow that in this case, after synchronization at realapart. $\begin{array} { r } { \tau + \frac { \delta } { 3 \rho } } \end{array}$ $p _ { 1 }$ $p _ { 2 }$ $\frac { 2 \delta } { 3 }$

Exercise 13.6 Argue the impossibility of $k$ -Byzantine clock synchronization for general $N$ and $\begin{array} { r } { k \geq \frac { N } { 3 } } \end{array}$ .

Exercise 13.7 The $k$ -Byzantine synchronizer of Lamport and Melliar-Smith differs from the MahaneySchneider synchronizer in one aspect: a correct process $p$ accepts a local clock value of another process $q$ if at the moment of synchronization it differs by no more than $\delta$ from its own clock value. Explain why that synchronizer has precision $\frac { 3 k } { N } \cdot \delta$ (versus precision $\frac { 2 k } { N } \cdot \delta$ δof the Mahaney-Schneider synchronizer).

Exercise 13.8 Explain how the Mahaney-Schneider synchronizer must be adapted if $d _ { \operatorname* { m a x } } > 0$ .

Exercise 13.9 Apply the Lamport-Shostak-Pease broadcast algorithm to a complete network of five processes, with $k = 1$ . Let the general $g$ be Byzantine. Suppose that, in pulse 1, $g$ sends the value 1 to two lieutenants, and the value 0 to the two other lieutenants. Give a computation of Broadcas $_ g ( 5 , 1 )$ (including a definition of the majority function) such that all lieutenants decide for 0.

Exercise 13.10 Apply the Lamport-Shostak-Pease broadcast algorithm to a complete network of seven processes, with $k = 2$ . Let the general $g$ and one lieutenant be Byzantine. Give a computation of Broadcas $t _ { g } ( 7 , 2 )$ (and its subcalls) in which all correct lieutenants decide for majority $( \{ 0 , 0 , 0 , 1 , 1 , 1 \} )$ .

Exercise 13.11 Apply the Lamport-Shostak-Pease broadcast algorithm to a complete network of eight processes, with $k = 2$ . Let three of the lieutenants be Byzantine. (The general $g$ and the four other lieutenants are correct.) Give a computation of Broadcas $t _ { g } ( 8 , 2 )$ (and its subcalls) in which a correct lieutenant decides for a value diffreplaced by from .) $g$ ,. (This shows that the bound $\scriptstyle { \frac { N - k } { 2 } }$ at the start of the proof of theorem 13.6 cannot be $\frac { N - 1 } { 2 }$

Exercise 13.12 Determine the worst-case message complexity of the correct processes in Broadcas $\mathbf { \chi } _ { \boldsymbol { g } } ( N , k )$

Exercise 13.13 Apply the Lamport-Shostak-Pease authentication algorithm to a complete network of five processes. Let three of the processes be Byzantine. Give a computation in which the two correct processes would decide for different values at the end of pulse 3 but decide for the same value in pulse 4.

Exercise 13.14 Let $k \geq N - 1$ . Explain why the Lamport-Shostak-Pease authentication algorithm can then be adapted by letting it already terminate at the end of pulse $N - 1$ .

Exercise 13.15 Determine the worst-case message complexity of the correct processes in the LamportShostak-Pease authentication algorithm, taking into account the Dolev-Strong optimization.

# Mutual Exclusion

Mutual exclusion in distributed systems addresses the problem that different processes may concurrently want to perform a related task but should perform these tasks sequentially. Mutual exclusion is of vital importance especially in a shared-memory setting in order to serialize access to a shared resource. Notably, a thread may want to lock a block of shared memory, to ensure exclusive access to it. For example, purchasing a plane ticket or a specific seat on an airplane over the Internet requires mutual exclusion to avoid having different persons acquire the same seat on a flight. Mutual exclusion is also important in a message-passing framework, for instance to avoid race conditions, such as serializing control signals to an I/O device.

Although multiple processes may want to access the resource concurrently, at any moment in time at most one process should be privileged, meaning that it is allowed access or can perform a certain task. A process that becomes privileged is said to enter its critical section, which is a block of source code where the process needs access to the resource or performs the task. When a process gives up the privilege, it is said to exit its critical section. Mutual exclusion algorithms are supposed to satisfy the following two properties in each of their executions:

• Mutual exclusion: In every configuration, at most one process is privileged.   
• Starvation-freeness: If a process tries to enter its critical section and no process remains privileged forever, then this process will eventually become privileged.

In a message-passing setting, mutual exclusion algorithms are generally based on one of the following three paradigms:

• A logical clock: Requests for entering a critical section are prioritized by means of logical time stamps.   
• Token passing: The process holding the token is privileged.   
Quorums: To become privileged, a process needs the permission from a quorum of processes. Each pair of quorums has a nonempty intersection.

We will first discuss one mutual exclusion algorithm for each of these categories. Next, we will consider several mutual exclusion algorithms for shared memory, all of which use spinning, meaning that values of certain registers are read repeatedly until some condition is met.

# 14.1 Ricart-Agrawala Algorithm

The Ricart-Agrawala mutual exclusion algorithm uses Lamport’s logical clock (see section 2.2). For simplicity, we assume that the network topology is complete. Processes are indexed: $p _ { 0 } , . . . , p _ { N - 1 }$ . When a process $p _ { i }$ , . . . ,wants to enter its critical section, it asks permission from all other processes by broadcasting the message $\langle \mathbf { r e q u e s t } , t s _ { i } , i \rangle$ with $t s _ { i }$ its logical time stamp, i.e., the logical time of its last event (initially it is zero). The , ,smaller the time stamp of the request, the higher its priority. The second argument of this message, the index $i$ , is meant to break ties between competing processes that happen to send concurrent requests with the same time stamp. Then the request from the process with the lowest index has the higher priority. When another process $p _ { j }$ receives $p _ { i }$ ’s request, it sends permission to $p _ { i }$ as soon as

• $p _ { j }$ is not privileged, and $p _ { j }$ does not have a pending request with a logical time stamp $t s _ { j }$ , where $( t s _ { j } , j ) < ( t s _ { i } , i )$ (with respect to the lexicographical order).

Process $p _ { i }$ enters its critical section when it has received permission from all other processes. When $p _ { i }$ exits its critical section, it sends permission in reply to all pending requests.

Actually, the Ricart-Agrawala algorithm does not require a full-blown logical clock. It suffices that only requests be taken into account. That is, if a process receives a request with time stamp $t$ , then it increases its clock value to $t + 1$ .

We consider two examples, both with $N = 2$ . Let clocks start at time 0.

Example 14.1 $p _ { 1 }$ sends $\langle \mathbf { r e q u e s t } , 0 , 1 \rangle$ to $p _ { 0 }$ . Upon receipt of this request, $p _ { 0 }$ sends permission to $p _ { 1 }$ , setting its clock value to 2. Next, $p _ { 0 }$ , ,sends $\langle \mathbf { r e q u e s t } , 2 , 0 \rangle$ to $p _ { 1 }$ . When $p _ { 1 }$ receives this message, it does not send permission to $p _ { 0 }$ , because $( 0 , 1 ) < ( 2 , 0 )$ , ,. Eventually, $p _ { 1 }$ receives permission from $p _ { 0 }$ and enters its critical section. When $p _ { 1 }$ , < ,leaves its critical section, it sends permission to $p _ { 0 }$ .

Example $1 4 . 2 ~ p _ { 0 }$ and $p _ { 1 }$ concurrently exchange requests: $p _ { 0 }$ sends $\langle \mathbf { r e q u e s t } , 0 , 0 \rangle$ to $p _ { 1 }$ and $p _ { 1 }$ sends $\langle \mathbf { r e q u e s t } , 0 , 1 \rangle$ to $p _ { 0 }$ . When $p _ { 0 }$ receives the request from $p _ { 1 }$ , ,, it does not send permission to $p _ { 1 }$ , because $( 0 , 0 ) < ( 0 , 1 )$ . When $p _ { 1 }$ receives the request from $p _ { 0 }$ , it does send permission to $p _ { 0 }$ , because $( 0 , 0 ) < ( 0 , 1 )$ . , < ,Eventually, $p _ { 0 }$ receives permission from $p _ { 1 }$ and enters its critical section. When $p _ { 0 }$ , < ,leaves its critical section, it sends permission to $p _ { 1 }$ .

We argue that the Ricart-Agrawala algorithm guarantees mutual exclusion. Suppose a process $p$ wants to enter its critical section and sends requests to all other processes. When another process $q$ sends permission to $p , q$ is not privileged. Moreover, either $q$ ’s pending request is smaller than $p$ ’s request or the fact that $p$ ’s request is taken into account in $q$ ’s logical clock ensures that $q$ ’s future request will be greater than $p$ ’s request. Hence, $q$ will not get permission from $p$ to enter its critical section until after $p$ has entered and left its critical section. The Ricart-Agrawala algorithm is also starvation-free, because each request will eventually become the smallest request in the network.

A drawback of the Ricart-Agrawala algorithm is the high message overhead because requests must be sent to all other processes. The Carvalho-Roucairol optimization reduces this message overhead. Suppose a process $p _ { i }$ entered its critical section earlier and wants to enter it again. Then $p _ { i }$ only needs to send requests to the processes, recorded in a set Requestsi, to which $p _ { i }$ has sent permission since the last exit from its critical section. This set initially contains all processes except $p _ { i }$ and is emptied every time $p _ { i }$ exits its critical section.

When $p _ { i }$ sends permission to a process $q$ , it adds $q$ to Requestsi. If a process $q \notin R e q u e s t s _ { i }$ sends a request to $p _ { i }$ while $p _ { i }$ is waiting for permissions, and $q$ ’s request is smaller than $p _ { i }$ /’s outstanding request, then $p _ { i }$ sends both permission and a request to $q$ .

We argue that in all reachable configurations, $p _ { i } \in R e q u e s t s _ { j }$ or $p _ { j } \in R e q u e s t s _ { i }$ for each pair of different processes $p _ { i } , p _ { j }$ . In initial configurations, this trivially holds. It suffices to show that when $p _ { i }$ is removed from Requestsj, $p _ { j } \in R e q u e s t s _ { i }$ holds. To remove $p _ { i }$ from Requestsj, $p _ { j }$ must (enter and) exit its critical section. When $p _ { j }$ becomes privileged, it must have received permission from $p _ { i }$ , because $p _ { i } \in R e q u e s t s _ { j }$ . As a result, $p _ { j } \in R e q u e s t s _ { i }$ , which will clearly remain the case until after $p _ { j }$ has exited its critical section. This completes the argument. Since in each reachable configuration, for every pair of different processes, at least one of them must ask permission from the other, mutual exclusion is guaranteed.

# 14.2 Raymond’s Algorithm

Raymond’s mutual exclusion algorithm is based on token passing; only the process holding the token may be privileged. It assumes an undirected network and starts with building a spanning tree in this network. At any moment, the root of this sink tree is supposed to hold the token. The root of the spanning tree therefore changes over time, meaning that parent-child relations in the tree may be inverted.

Each process maintains a FIFO queue, which can contain IDs of its children in the sink tree, and its own ID. An enqueue operation adds an ID at the tail of the queue, while a dequeue operation removes the ID at the other side of the queue, called the head, if the queue is nonempty. Initially, the queues at the processes are empty. Each process maintains its queue as follows:

When a nonroot wants to enter its critical section, it enqueues its ID at the tail of its own queue. When a process receives a request for the token from a child, it enqueues the ID of this child at the tail of its own queue. Each time a nonroot gets a new head at its (nonempty) queue, it sends a request for the token to its parent. When the root has left its critical section and its queue is or becomes nonempty, it sends the token to the process $q$ at the head of its queue, makes $q$ its parent, and dequeues $q$ ’s ID from the head of its queue.

In the special case where the root wants to enter its critical section again and its queue is empty, it can becom privileged straightaway.

Let a nonroot $p$ get the token from its parent, and let the ID of the process $q$ be at the head of $p$ ’s queue.

• If $p \neq q$ , then $p$ sends the token to $q$ and makes $q$ its parent.   
• If $p = q$ , then $p$ becomes the root; that is, it has no parent and is privileged.

In both cases, $p$ removes $q$ ’s ID from the head of its queue.

Example 14.3 We consider one possible computation of Raymond’s algorithm, on an undirected network of five processes. In every picture, the gray process is the root.

Initially, in the following picture at the left, $p _ { 3 }$ is the root and is in its critical section. Next, in the picture at the right, the following has happened. Since $p _ { 8 }$ wants to enter its critical section, it enqueued its own ID in its queue. Since this was a new head of its queue, $p _ { 8 }$ sent a request for the token to its parent $p _ { 1 }$ . As a result, $p _ { 1 }$ also placed the $\textrm { I D } 8$ in its queue. Since this was a new head of its queue, $p _ { 1 }$ sent a request for the token to its parent $p _ { 3 }$ . As a result, $p _ { 3 }$ enqueued the ID 1 in its queue.

![](images/54c68a1869b047d2e9a7af9e4efe95c6d878698ee6708f56eea7ec4d17d3b4fd.jpg)

In the following picture at the left, $p _ { 5 }$ wants to enter its critical section, so it enqueued its own ID in its queue. Since this was a new head of its queue, $p { 5 }$ sent a request for the token to its parent $p _ { 3 }$ . As a result, $p _ { 3 }$ also enqueued the $\mathrm { I D } 5$ in its queue. In the picture at the right, $p _ { 2 }$ wants to enter its critical section, so it enqueued its own ID in its queue. Since this was a new head of its queue, $p _ { 2 }$ sent a request for the token to its parent $p _ { 1 }$ . As a result, $p _ { 1 }$ also enqueued the $\mathrm { I D } 2$ in its queue.

![](images/b1977c1f0cf6919b0355a0c33925cddc342b2dc46530647592aee1326b891e61.jpg)

In the following picture at the left, $p _ { 3 }$ has exited its critical section. Since the $\textrm { I D } 1$ was the head of its queue, it sent the token to $p _ { 1 }$ , made $p _ { 1 }$ its parent, and dequeued 1 from its queue. Then 5 became the new head of its queue, so $p _ { 3 }$ sent a request for the token to its parent $p _ { 1 }$ . When $p _ { 1 }$ received the token, it became the root. Moreover, the request from $p _ { 3 }$ made $p _ { 1 }$ enqueue the ID 3 in its queue. In the picture at the right, since the $\textrm { I D } 8$ was the head of its queue, $p _ { 1 }$ forwarded the token to $p _ { 8 }$ , made $p _ { 8 }$ its parent, and dequeued 8 from its queue. Then 2 became the new head of its queue, so $p _ { 1 }$ sent a request for the token to its parent $p _ { 8 }$ . When $p _ { 8 }$ received the token, it became the root, dequeued 8 from its queue, and entered its critical section. Moreover, the request from $p _ { 1 }$ made $p _ { 8 }$ enqueue the ID 1 in its queue.

![](images/baaf329d8ac7de435bf275fc57850ba4d3dbe0b192a1f1ea6aaf78d9d5eb8ac2.jpg)

In the following picture at the left, $p _ { 8 }$ has exited its critical section. Since the $\textrm { I D } 1$ was the head of its queue, it sent the token to $p _ { 1 }$ , made $p _ { 1 }$ its parent, and dequeued 1 from its queue. When $p _ { 1 }$ received the token, it became the root. In the picture at the right, since the $\mathrm { I D } 2$ was the head of its queue, $p _ { 1 }$ forwarded the token to $p _ { 2 }$ , made $p _ { 2 }$ its parent, and dequeued 2 from its queue. Then 3 became the new head of its queue, so $p _ { 1 }$ sent a request for the token to its parent $p _ { 2 }$ . When $p _ { 2 }$ received the token, it became the root, dequeued 2 from its queue, and entered its critical section. Moreover, the request from $p _ { 1 }$ made $p _ { 2 }$ enqueue the $\textrm { I D } 1$ in its queue.

![](images/4ef5d6c58c8449fe971af0a7a2e396c90a0cc701e7defc0bc7d8792110cb5c93.jpg)

In the following picture at the left, $p _ { 2 }$ has exited its critical section. Since the $\textrm { I D } 1$ was the head of its queue, it sent the token to $p _ { 1 }$ , made $p _ { 1 }$ its parent, and dequeued 1 from its queue. When $p _ { 1 }$ received the token, it became the root. In the picture at the right, since the ID 3 was the head of its queue, $p _ { 1 }$ forwarded the token to $p _ { 3 }$ , made $p _ { 3 }$ its parent, and dequeued 3 from its queue. When $p _ { 3 }$ received the token, it became the root.

![](images/9f0cec5a11a028719d72659ab7e5f124db8fc186f7ef21440d20596d1c3ab282.jpg)

In the final picture, since the ID 5 was the head of its queue, $p _ { 3 }$ sent the token to $p _ { 5 }$ , made $p _ { 5 }$ its parent, and dequeued 5 from its queue. When $p { 5 }$ received the token, it became the root, dequeued 5 from its queue, and entered its critical section.

![](images/ba501c328214e859ec7a2de93c6fbf109cc35c96762473b91e20197a8045c768.jpg)

If the root wants the token back immediately after it sent the token, because its queue is nonempty, then it is of course efficient to combine the token and the ensuing token request into one message.

Whenever a process is privileged, it holds the token. So Raymond’s algorithm provides mutual exclusion, since at all times at most one process holds the token. Raymond’s algorithm also provides starvation-freeness, because eventually each ID in a queue moves to the head of this queue, and if a process wants the token, then the resulting chain of IDs in queues never contains a cycle.

The Chang-Singhal-Liu algorithm is a fault-tolerant version of Raymond’s algorithm. Instead of a sink tree, a sink graph within the network is maintained. Each nonroot may have multiple outgoing edges in this graph, such that all paths in the subnetwork of directed edges lead to the process holding the token. Increasing the number of outgoing edges of a process increases the degree of fault-tolerance but also the performance overhead. One of the outgoing edges of a process is its preferred edge. Nonroots send a token request into their preferred edge. The root makes the edge into which it sends the token outgoing and preferred. To avoid cycles, the receiver of the token reverses each of its outgoing edges. It moreover informs its neighbor at the other side to make this edge outgoing and preferred. If a nonroot finds that the neighbor at the other side of its preferred edge has crashed and it still has remaining outgoing edges, it nominates one of those edges as preferred. The algorithm is greedy in the sense that a process that receives the token and wants to enter its critical section, becomes privileged immediately, even if its ID is not at the head of its queue (cf. exercise 14.8).

# 14.3 Agrawal–El Abbadi Algorithm

In the Agrawal–El Abbadi mutual exclusion algorithm, a process must obtain permission from a quorum of processes to enter its critical section. Crucially, each pair of quorums has a nonempty intersection. This guarantees mutual exclusion because different quorums cannot concurrently make different processes privileged. The crux of the Agrawal–El Abbadi algorithm is how quorums are defined. A strong point of this algorithm is that it can cope with processes that are not responsive or have crashed.

For simplicity, we assume that the network topology is complete and that $N = 2 ^ { k + 1 } - 1$ for some $k > 0$ . The processes are structured in a complete binary tree of depth $k$ , meaning that nodes at a depth $< k$ >have exactly two children and the $2 ^ { k }$ leaves are all at depth $k$ <. A quorum consists of all processes on a path in this binary tree from the root to a leaf. If a nonleaf $r$ is unresponsive, then instead of asking permission from $r$ , permission can be asked from all processes on two paths: from each child of $r$ to some leaf. We note that a process may have to ask permission from itself.

To be more precise, a process $p$ that wants to enter its critical section places the root of the tree in a queue. Then it repeatedly tries to get permission from the process $r$ at the head of its queue. If successful, $r$ is removed from $p$ ’s queue; if $r$ is a nonleaf, one of the two children of $r$ is appended at the end of $p$ ’s queue. If a nonleaf $r$ is found to be unresponsive, then $r$ is removed from $p$ ’s queue, and both of its children are appended at the end of the queue, in a fixed order, to avoid deadlocks; for instance, the left child is always placed before the right node. Otherwise two processes $p$ and $q$ could find that a nonleaf $r$ is unresponsive, after which $p$ and $q$ might obtain permission from the left and right child of $r$ , respectively, leading to a deadlock. If a leaf $r$ is found to be unresponsive, $p$ must abort this attempt to become privileged and retry. When $p$ ’s queue becomes empty, it has received permission from a quorum of processes, so it can enter its critical section. After exiting its critical section, $p$ informs each process in the quorum that its permission to $p$ can be withdrawn.

If processes may crash, a complete and strongly accurate failure detector is required, and a process withdraws its permission if it detects that the process to which it has given permission has crashed.

Example 14.4 Let $N = 7$ , and suppose the processes are structured in a binary tree as follows.

![](images/7e63987dadf45450759af2db4b923e96d5b794acb85b340b351ee5cb30b3a8e4.jpg)

Some possible quorums are

• $\left\{ p 9 , p _ { 3 } , p _ { 8 } \right\}$ , $\left\{ p 9 , p _ { 3 } , p _ { 1 } \right\}$ , $\{ p _ { 9 } , p _ { 4 } , p _ { 0 } \}$ , and $\{ p _ { 9 } , p _ { 4 } , p _ { 5 } \}$ ; if $p 9$ , , ,is not responding: $\{ p _ { 3 } , p _ { 8 } , p _ { 4 } , p _ { 0 } \}$ , $\{ p _ { 3 } , p _ { 1 } , p _ { 4 } , p _ { 0 } \}$ , $\{ p _ { 3 } , p _ { 8 } , p _ { 4 } , p _ { 5 } \}$ , and $\{ p _ { 3 } , p _ { 1 } , p _ { 4 } , p _ { 5 } \}$ ;   
• if $p _ { 3 }$ is not responding: $\left\{ p 9 , p _ { 8 } , p _ { 1 } \right\}$ ;   
• if $p _ { 4 }$ is not responding: $\{ p { 9 } , p { 0 } , p { 5 } \}$ .

For more possible quorums in this network, see exercise 14.11.

Suppose two processes $p$ and $q$ concurrently want to enter their critical section; we consider one possible computation, with regard to the preceding binary tree. First, $p$ obtains permission from $p 9$ , and now it wants to obtain permission from $p _ { 4 }$ . Next, $p 9$ crashes, which is observed by $q$ , which now wants to obtain permission from $p _ { 3 }$ and $p _ { 4 }$ . Let $q$ obtain permission from $p _ { 3 }$ , after which it appends $p _ { 8 }$ at the end of its queue. Next, $q$ obtains permission from $p _ { 4 }$ , after which it appends $p { 5 }$ at the end of its queue. Next, $p _ { 4 }$ crashes, which is observed by $p$ , which now wants to obtain permission from $p _ { 0 }$ and $p { 5 }$ . Next, $q$ obtains permission from $p _ { 8 }$ , and now it wants to obtain permission from $p { 5 }$ . Finally, $p$ obtains permission from both $p _ { 0 }$ and $p { 5 }$ and enters its critical section. It has obtained permission from the quorum $\{ p { 9 } , p { 0 } , p { 5 } \}$ .

We argue, by induction on the depth of the binary tree, that each pair of quorums $Q$ and $\boldsymbol { Q ^ { \prime } }$ has a nonempty intersection. This implies that the Agrawal–El Abbadi algorithm guarantees mutual exclusion. A quorum that includes the root contains a quorum in one of the subtrees below the root, while a quorum without the root contains a quorum in both subtrees below the root. If $Q$ and $Q ^ { \prime }$ both contain the root, then we are done, because the root is in their intersection. (Note that this covers the base case of the induction, where the depth is 0.) If they both do not contain the root, then by the induction hypothesis they have elements in common in the two subtrees below the root. Finally, if $Q$ contains the root while $Q ^ { \prime }$ does not, then $Q$ contains a quorum in one of the subtrees below the root, and $Q ^ { \prime }$ also contains a quorum in this subtree. So, by induction, $Q$ and $Q ^ { \prime }$ have an element in common in this subtree.

Starvation may happen if a process that wants to become privileged e.g. runs into a crashed leaf an infinite number of times. The Agrawal–El Abbadi algorithm however is starvation-free if a quorum of processes remains alive and no crashes happen anymore. This property depends crucially on strict queue management. Suppose that in the case of an unresponsive process its left child is placed before its right child in the queue of a process that wants to become privileged. Consider the following total order $<$ on processes, based on their positions in the binary tree: $p < q$ either if $p$ occurs at smaller depth than $q$ <in the binary tree or if $p$ and $q$ occur at the same depth and $p$ < is placed more to the left than $q$ in the binary tree. Then a process that has obtained permission from a process $q$ never needs permission from a process $p < q$ to enter its critical section.

Starvation could still happen if a process $r$ <fails to get permission from a (live) process $s$ for an infinite amount of time because $s$ keeps on giving permissions to other processes than $r$ . This can be resolved by letting each process grant permissions in a first-come-first-served fashion. Moreover, inevitably the algorithm deadlocks if a process crashes while being in its critical section.

# 14.4 Peterson’s Algorithm

It was explained at the start of this chapter that mutual exclusion is of vital importance in a shared-memory setting in order to serialize access to a shared resource. In the remainder of this chapter, we focus on mutual exclusion for shared memory with processes $p _ { 0 } , . . . , p _ { N - 1 }$ . The algorithms we discuss are based on spinning, , . . . ,meaning that values of registers are read repeatedly until some condition is met.

# Mutual Exclusion for Two Processes

Peterson’s algorithm provides mutual exclusion for two processes, $p _ { 0 }$ and $p _ { 1 }$ . The basic idea is that when a process $p _ { b }$ with $b \in \{ 0 , 1 \}$ wants to enter its critical section, it signals its intention to the other process $p _ { 1 - b }$ by setting a Boolean flag from false to true. Next, $p _ { b }$ repeatedly checks whether $p _ { 1 - b }$ ’s flag is false. As soon as this is the case, $p _ { b }$ enters its critical section. When $p _ { b }$ exits its critical section, it resets its flag to false.

This simple mutual exclusion algorithm suffers from livelock, meaning that the processes perform a continuous stream of events without making progress. This can happen if $p _ { 0 }$ and $p _ { 1 }$ concurrently set their own flag to true and spin on the other’s flag forever. Note that livelock induces starvation. To avoid this, Peterson’s algorithm exploits a multi-writer wait register. When $p _ { b }$ wants to enter its critical section, it not only sets its flag to true but also sets wait to $^ b$ . If $p _ { b }$ now finds that $\nu a i t = 1 - b$ , it can enter its critical section, even when the flag of $p _ { 1 - b }$ is set to true. In that case, $p _ { 0 }$ and $p _ { 1 }$ concurrently set their flag to true and $p _ { 1 - b }$ wrote to wait last, so it must wait.

To be more precise, Peterson’s algorithm uses a multi-writer register wait with range $\{ 0 , 1 \}$ and multireader single-writer registers $\hbar a g [ b ]$ of type Boolean for $b = 0 , 1$ ; only $p _ { b }$ can write to $\hbar a g [ b ]$ . Initially, $\displaystyle { \mathcal { H } a g [ b ] = f a l s e }$ . When $p _ { b }$ ,wants to enter its critical section, it first sets $\hbar a g [ b ]$ to true and then sets wait to $^ b$ . Next, it spins on $f l a g [ 1 - b ]$ and wait until $\begin{array} { r } { \hbar a g [ 1 - b ] = } { \ } .  \end{array}$ false or $w a i t = 1 - b$ , and then enters its critical section. When $p _ { b }$ exits its critical section, it resets flag $[ b ]$ to false.

Example 14.5 We consider one possible execution of Peterson’s algorithm. Initially, fla $g [ b ] =$ false for $b =$ $0 , 1$ .

$p _ { 1 }$ wants to enter its critical section and sets flag[1] to true and wait to 1.   
$p _ { 0 }$ wants to enter its critical section and sets flag[0] to true.   
Since $\begin{array} { r } { f d a g [ 0 ] = t r u e } \end{array}$ and $w a i t = 1$ , $p _ { 1 }$ does not yet enter its critical section.   
$p _ { 0 }$ sets wait to 0. Since $\ f l a g [ 1 ] = t r u$ e and wait $= 0$ , $p _ { 0 }$ does not yet enter its critical section.   
Since $w a i t = 0$ , $p _ { 1 }$ enters its critical section.   
$p _ { 1 }$ exits its critical section and resets flag[1] to false.   
$p _ { 1 }$ wants to enter its critical section and sets flag[1] to true and wait to 1. Since flag $[ 0 ] = i$ true and wait $p _ { 1 }$ does not yet enter its critical section.   
Since wait $= 1$ , $p _ { 0 }$ enters its critical section.

We argue that Peterson’s algorithm provides mutual exclusion. Suppose $p _ { b }$ is in its critical section (so it set flag $[ b ]$ to true and wait to $^ b$ ) and $p _ { 1 - b }$ tries to enter its critical section. There are two possibilities:

1. Before entering its critical section, $p _ { b }$ read fla $\left[ 1 - b \right] =$ false. Then $p _ { 1 - b }$ must set flag $[ 1 - b ]$ to true and wait to $1 - b$ before it can enter its critical section.   
2. Before entering its critical section, $p _ { b }$ read wait $\dot { \mathbf { \theta } } = 1 - b$ .

In both cases, wait has the value $1 - b$ by the time $p _ { 1 - b }$ starts spinning on $\hbar a g [ b ]$ and wait. Since, moreover, $\displaystyle \mathit { f l a g } [ b ] = t r u e .$ , $p _ { 1 - b }$ can enter its critical section only after $p _ { b }$ has reset $\hbar a g [ b ]$ to false or set wait to $^ b$ . Hence, $p _ { 1 - b }$ must wait until $p _ { b }$ is no longer in its critical section.

Peterson’s algorithm is starvation-free. Let $p _ { 1 - b }$ try to enter its critical section. Then it sets $f l a g [ 1 - b ]$ to true and wait to $1 - b$ . Now $p _ { b }$ could only starve $p _ { 1 - b }$ by repeatedly trying to enter its critical section, because $p _ { 1 - b }$ should continuously read $f l a g [ b ] = t r u e$ . However, before (re)entering, $p _ { b }$ sets wait to $^ b$ , after which $p _ { 1 - b }$ can enter its critical section.

# Mutual Exclusion for More Than Two Processes

To obtain a mutual exclusion algorithm for $N > 2$ processes, we build a tournament tree, a binary tree of depth $k > 0$ in which each node represents an application of Peterson’s algorithm for two processes. For >simplicity, we assume that $N = 2 ^ { k + 1 }$ . Each process is assigned to a leaf of the tournament tree, where exactly two processes are assigned to each of the $2 ^ { k }$ leaves. A process that wants to enter its critical section performs Peterson’s algorithm at its leaf. When a process becomes privileged at a nonroot of the tournament tree, it proceeds to the parent of this node. There it runs Peterson’s algorithm again, where it may need to compete with the winner of the competition of the subtree below the other side of this node. A process that becomes privileged at the root in the tournament tree enters its critical section.

To be more precise, nodes in the tournament tree are numbered as follows: the root carries number 0, and given a node with the number $n$ , its left and right children carry the numbers $2 n + 1$ and $2 n + 2$ , respectively. To each node $n$ we associate three multi-writer registers: waitn with range $\{ 0 , 1 \}$ and $\hbar a g _ { n } [ b ]$ of type Boolean for $b = 0 , 1$ . Initially, $\begin{array} { r } { f a g _ { n } [ b ] = f a l s } \end{array}$ ,e. Each node has two sides, 0 and 1, and a process $p _ { i }$ that wants to enter ,its critical section is assigned to the leaf $( 2 ^ { k } - 1 ) + \lfloor i / 2 \rfloor$ at the side $i$ mod 2. A process at side $^ b$ of a node $n$ performs the following procedure Peterson $( n , b )$ :

$f a g _ { n } [ b ] \gets t r u e ; \quad w a i t _ { n } \gets b ;$ while $\displaystyle f a g _ { n } [ 1 - b ] = t r u$ e and $w a i t _ { n } = b$ do

$\{ \}$ ; end while if $n = 0$ then enter critical section; exit critical section; else perform procedure Peterson $\left( \lceil n / 2 \rceil - 1 , ( n + 1 ) \right)$ mod 2); end if $f a g _ { n } [ b ] \gets f a l s e ;$ ;

The first four lines are simply Peterson’s algorithm at node $n$ . The next six lines express that at the root becoming privileged means entering the critical section, while at a nonroot it means moving to the parent node, where Peterson’s algorithm is run once again. The last line makes sure that when a process exits its critical section, its flags at all the nodes it visited are reset to false, thus releasing processes that may be waiting at these nodes.

Example 14.6 We consider one possible execution of Peterson’s algorithm in a tournament tree. Let $N = 8$ , so $k = 2$ . Suppose $p _ { 1 }$ and $p _ { 6 }$ both want to enter their critical section; $p _ { 1 }$ starts at node 3, side 1, and $p _ { 6 }$ at node 6, side 0.

![](images/4662424ed5a6c1144d89ced9d0c0da4ff767220835b8e467ffbe479591deb87a.jpg)

Initially, $\scriptstyle { \mathcal { f l a g } } _ { n } [ b ] = f$ alse for all $n$ and $^ b$ .

$p _ { 6 }$ executes Peterson $( 6 , 0 )$ . It sets $\hbar a g _ { 6 } [ 0 ]$ to true and wait6 to 0, and (since $f l a g _ { 6 } [ 1 ] = f a l s e )$ continues executing Peterson $( 2 , 1 )$ . It sets $f l a g _ { 2 } [ 1 ]$ to true and wait2 to 1, and (since $\mathcal { H } a g _ { 2 } [ 0 ] = \mathcal { f } a l s e )$ continues executing Peterson $( 0 , 1 )$ . It sets $\scriptstyle { \mathit { f l a g } } _ { 0 }$ [1] to true.   
$p _ { 1 }$ executes Peterson $( 3 , 1 )$ . It sets $\displaystyle \mathit { \mathcal { H } a g _ { 3 } [ 1 ] }$ to true and wait3 to 1, and (since $\mathcal { H } a g _ { 3 } [ 0 ] = f a l s e )$ continues executing Peterson $( 1 , 0 )$ . It sets $\hbar a g _ { 1 } [ 0 ]$ to true and wait $_ 1$ to 0, and (since $\mathcal { H } a g _ { 1 } [ 1 ] = \mathcal { f } a l s e )$ continues executing Peterson $( 0 , 0 )$ . It sets $\hbar a g _ { 0 } [ 0 ]$ to true and wai $^ { \dag } 0$ to 0. Since $f l a g _ { 0 } [ 1 ] = t r u e$ and $w a i t _ { 0 } = 0$ , $p _ { 1 }$ must wait.   
$p _ { 6 }$ finally sets wait0 to 1. Since $f l a g _ { 0 } [ 0 ] = t r u e$ and wait $\mathrm { \dot { \rho } } _ { 0 } = 1$ , $p _ { 6 }$ must wait.   
Since $w a i t _ { 0 } = 1$ , $p _ { 1 }$ can enter its critical section.   
When $p _ { 1 }$ exits its critical section, it resets $f l a g _ { 0 } [ 0 ] , f a g _ { 1 } [ 0$ ], and flag [1] to false.   
Since $\begin{array} { r } { \displaystyle \# a g _ { 0 } [ 0 ] = . } \end{array}$ false, $p _ { 6 }$ can enter its critical section.

The tournament tree provides mutual exclusion. If a process $p$ is in its critical section, then it is privileged with regard to Peterson’s mutual exclusion algorithm for each node on the path from $p$ ’s leaf to the root in the tournament tree, stopping all other processes that want to enter their critical section in their tracks. The tournament tree, moreover, is starvation-free. Suppose a process $p$ has arrived at a node $n$ in the tournament tree. We argue by induction on the depth of $n$ in the tournament tree that $p$ will eventually enter its critical section. Suppose $p$ is at the moment stuck at $n$ . Then some other process $q$ is privileged (in the base case $n = 0$ ) or moved to the parent of $n$ (in the inductive case $n > 0$ ), thereby blocking $p$ ; in the case $n > 0$ , by induction, $q$ will eventually enter its critical section. When $q$ > >exits its critical section, it will reset the flag at its side of $n$ to false, after which $p$ can enter its critical section (if $n = 0$ ) or move to the parent of $n$ (if $n > 0$ ); in the latter case, by induction, $p$ will eventually enter its critical section.

The tournament tree does not let processes enter their critical section in a first-come, first-served manner. That is, let the doorway of a process that wants to become privileged consists of one or more initial write operations; in particular, a doorway cannot include spinning on a variable. In the tournament tree, the doorway of a process consists of its initial write operations to flag and wait, the first two assignments in the pseudocode of Peterson $( n , b )$ , at its starting leaf. If a process $p$ exits its doorway before another process $q$ enters its ,doorway at another leaf, it remains possible that $q$ will become privileged before $p$ .

# 14.5 Bakery Algorithm

The bakery algorithm enforces mutual exclusion similar to the way customers in a shop are served in a firstcome, first-served fashion. When entering, say, a bakery, each customer gets a ticket with a number, which is increased by 1 with each ticket that follows. The waiting customer with the smallest number is the next to be served.

Tickets could in principle be modeled by means of a multi-writer register of type integer. However, avoiding that multiple processes concurrently read the value of this register and increase it by 1 requires the use of a read-modify-write operation, which can perform a read and a write step as one atomic operation (see section 14.7). In the bakery algorithm, a process instead reads the numbers of all other processes and selects the number that is the maximum of all those numbers plus 1. To break ties between different processes that concurrently select the same number, the ticket of a process $p _ { i }$ that selects a number $k$ consists of the pair $( k , i )$ , and tickets are ordered lexicographically: $( k , i ) < ( \ell , j )$ if either $k < \ell$ or $k = \ell$ and $i < j$ . A process can , , < ℓ, < ℓ ℓ <enter its critical section if its ticket is the smallest among all processes that have a number greater than zero. When a process exits its critical section, it resets its number to zero.

To be more precise, the bakery algorithm uses multi-reader single-writer registers choosingi of type Boolean and numberi of type integer, for $i = 0 , . . . , N - 1$ ; only $p _ { i }$ can write to choosin $\boldsymbol { g } _ { i }$ and numberi. Initially, choosingi $=$ false and $n u m b e r _ { i } = 0$ ,. A process $p _ { i }$ ,that wants to enter its critical section sets choosin $g _ { i }$ to true, reads the values of the registers numberj for all $j \neq i$ , writes $\operatorname* { m a x } \{ n u m b e r _ { j } | 0 \leq j < N \} + 1$ into numberi, and resets choosingi to false. Next, for each $j \neq i$ , $p _ { i }$ first spins on choosin $g _ { j }$ until it is false and then on numbe $r _ { j }$ until either numbe $r _ { j } = 0$ or $( n u m b e r _ { i } , i ) < ( n u m b e r _ { j } , j )$ . After that, $p _ { i }$ can enter its critical section. When $p _ { i }$ , <exits its critical section, it resets numberi to 0.

Example 14.7 We consider one possible execution of the bakery algorithm. Consider three processes $p _ { 0 } , p _ { 1 }$ and $p _ { 2 }$ ; initially, choosing $: =$ false and number $i = 0$ for $i = 0 , 1 , 2$ .

$p _ { 1 }$ wants to enter its critical section, sets choosin $g _ { 1 }$ to true, and reads numbe $r _ { 0 }$ and number2.   
$p _ { 0 }$ wants to enter its critical section, sets choosin $g _ { 0 }$ to true, and reads number1 and number2.   
$p _ { 0 }$ sets number0 to 1 and resets choosin $g _ { 0 }$ to false. It does not yet enter its critical section, because choosin $g _ { 1 } = t r u e$ .   
$p _ { 1 }$ sets number1 to 1 and resets choosin $g _ { 1 }$ to false. It does not yet enter its critical section, because $( n u m b e r _ { 0 } , 0 ) < ( n u m b e r _ { 1 } , 1 )$ and numbe $r _ { 0 } > 0$ .   
,Since choosin $g _ { 1 } = c h o o s i n g _ { 2 } = .$ false, $( n u m b e r _ { 0 } , 0 ) < ( n u m b e r _ { 1 } , 1 )$ , and numbe $\cdot _ { 2 } = 0$ , $p _ { 0 }$ enters its critical section.   
$p _ { 0 }$ exits its critical section and resets numbe $r _ { 0 }$ to 0.   
$p _ { 0 }$ wants to enter its critical section, sets choosin $g _ { 0 }$ to true, and reads number1 and number2.   
$p _ { 0 }$ sets number0 to 2 and resets choosin $g _ { 0 }$ to false. It does not yet enter its critical section, because $( n u m b e r _ { 1 } , 1 ) < ( n u m b e r _ { 0 } , 0 )$ and number $\cdot _ { 1 } > 0$ .   
,Since choosin $g _ { 0 } = c h o o s i n g _ { 2 } = .$ >false, number1  number0, and numbe $r _ { 2 } = 0$ , $p _ { 1 }$ enters its critical section.

The bakery algorithm provides mutual exclusion. Suppose a process $p _ { i }$ is in its critical section. Then clearly numbe $r _ { i } > 0$ . Moreover, let number $_ { i } > 0$ for some $j \neq i$ . We argue that then $( n u m b e r _ { i } , i ) < ( n u m b e r _ { j } , j )$ . Before $p _ { i }$ > >entered its critical section, it must have read choosin $g _ { j } = f a l s e$ ,, and either $n u m b e r _ { j } = 0$ , or $( n u m b e r _ { i } , i ) < ( n u m b e r _ { j } , j )$ . In the first case, if $p _ { j }$ chooses a new ticket while $p _ { i }$ is in its critical section, then $p _ { j }$ is guaranteed to take numberi into account and therefore will choose a larger number. This concludes the argument. Since a privileged process always carries a positive number, and has the smallest ticket among all processes with a positive number, only one process can be in its critical section at any time.

The bakery algorithm is starvation-free. If a process $p _ { i }$ wants to enter its critical section and other processes keep on entering and exiting their critical section, then eventually $p _ { i }$ will have the smallest ticket. That is, other processes that want to become privileged will take the current value of numbe $r _ { i }$ into account and will choose numbers greater than numberi for their own tickets.

The doorway of a process $p _ { i }$ that wants to enter its critical section consists of the sequence of events from setting choosin $g _ { i }$ to true up to and including resetting choosin $g _ { i }$ to false. The bakery algorithm treats processes in a first-come, first-served fashion, in the sense that if a process $p$ exits its doorway before another process $q$ enters its doorway, then $p$ will enter its critical section before $q$ .

The values of the number fields could grow without bound. The bakery algorithm can however be adapted such that these values are limited to a finite range; see exercise 14.21.

The mutual exclusion algorithms we consider for shared memory are spin locks, meaning that a process wanting to enter its critical section performs some writes to announce its intention (including the doorway) and spins on certain variables until some condition is met before it becomes privileged. In the bakery algorithm, a process that wants to enter its critical section spins on two registers at every other process. This renders the algorithm impractical in case of a large number of processes. The following theorem states that every spin lock for $N$ processes, using only atomic read and write operations, requires at least $N$ registers.

Recall that a livelock occurs if processes perform a continuous stream of events without making progress. Livelock clearly implies starvation. Therefore the following theorem induces that a spin lock offering starvation-free mutual exclusion for $N$ processes requires at least $N$ atomic registers.

Theorem 14.1 Each spin lock for N processes that uses fewer than $N$ atomic registers suffers from livelock.

Proof. We sketch a proof for the case $N = 2$ ; the general case is similar. Suppose, toward a contradiction, that a livelock-free spin lock for two processes $p$ and $q$ uses only one multi-writer register $R$ .

Before $p$ can enter its critical section, it must write to $R$ , for otherwise $q$ would not be able to recognize whether $p$ is in its critical section. Likewise, before $q$ can enter its critical section, it must write to $R$ . Because of livelock-freeness, we can bring $p$ and $q$ into a position where they are both about to write to $R$ , after which each will enter its critical section.

Suppose without loss of generality that $p$ writes to $R$ first and enters its critical section. The subsequent write by $q$ obliterates the value $p$ wrote to $R$ , so $q$ cannot tell that $p$ is in its critical section. Consequently $q$ will also enter its critical section. This contradicts the mutual exclusion property. ⊓⊔

# 14.6 Fischer’s Algorithm

Fischer’s algorithm circumvents the impossibility result at the end of the previous section by means of time delays.

The multi-writer register turn ranges over $\{ - 1 , 0 , . . . , N - 1 \}$ . Initially, it has the value $^ { - 1 }$ . A process $p _ { i }$ , , . . . ,that wants to enter its critical section spins on turn until its value is $^ { - 1 }$ . Within one time unit of this read, $p _ { i }$ completes a write operation that sets the value of turn to $i$ . Afterwards, $p _ { i }$ waits for more than one time unit and then reads turn again. If it still has the value $i$ , then $p _ { i }$ enters its critical section. Otherwise $p _ { i }$ returns to spinning on turn until its value is $^ { - 1 }$ . When a process exits its critical section, it resets the value of turn to $^ { - 1 }$ .

Example 14.8 We consider a possible execution of Fischer’s algorithm. Consider three processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ , with $p _ { 0 }$ in its critical section, so $t u r n = 0$ . Processes $p _ { 1 }$ and $p _ { 2 }$ both want to enter their critical section and are spinning on turn.

When $p _ { 0 }$ exits its critical section, it resets turn to $^ { - 1 }$ . Now $p _ { 1 }$ and $p _ { 2 }$ concurrently read that $t u r n = - 1$ . First, $p _ { 1 }$ sets the value of turn to 1, and less than one time unit later, $p _ { 2 }$ sets its value to 2. More than one time unit after it performed its write, $p _ { 1 }$ reads turn, finds that its value was changed to 2, and returns to spinning on turn. On the other hand, more than one time unit after it performed its write, $p _ { 2 }$ reads turn, finds that its value is still 2, and enters its critical section.

We argue that Fischer’s algorithm guarantees mutual exclusion. When $t u r n = - 1$ , clearly no process is in its critical section. And after a process $p _ { i }$ has set the value of turn to $i$ , other processes $p _ { j }$ can only set the value of turn to $j \neq i$ within one time unit. So if the value of turn remains $i$ for more than one time unit, $p _ { i }$ can be certain that the value of turn will remain unchanged and hence no other process can become privileged.

Fischer’s algorithm is livelock-free: when the value of turn becomes $^ { - 1 }$ , a process $p _ { i }$ that wants to enter its critical section can freely write the value $i$ in turn. The last process to set the value of turn within one time unit of the first write will enter its critical section. However, there can be starvation, if a process $p _ { i }$ wants to enter its critical section, infinitely often turn is reset to $^ { - 1 }$ and $p _ { i }$ writes $i$ in turn, but every time this value is overwritten by a $j \neq i$ within one time unit.

A strong requirement of this algorithm is the presence of a global clock. Another drawback is that processes all spin on the same register turn. Why this can be problematic will be explained in the next section.

# 14.7 Test-and-Test-and-Set Lock

# Test-and-Set Lock

The test-and-set lock circumvents the impossibility result from section 14.5 by using a read-modify-write operation: test-and-set. This lock uses one Boolean multi-writer register locked, which initially holds the value false. A process that wants to acquire the lock repeatedly applies test-and-set to locked. This operation sets the value of locked to true and returns the previous value of locked in one atomic step. The process obtains the lock (in other words, it becomes privileged) as soon as false is returned by a test-and-set operation. To unlock, the process resets locked to false.

The test-and-set lock provides mutual exclusion. When locked contains false, clearly no process holds the lock. And when a process $p$ acquires the lock, meaning that it applies a test-and-set that turns the value of locked from false to true, then no other process can acquire the lock until $p$ unlocks by resetting locked to false. The test-and-set lock, moreover, is livelock-free but not starvation-free.

The test-and-set lock, although conceptually simple, tends to have a very poor performance. The reason is that each test-and-set operation on locked comes with a memory barrier: it invalidates all cached values of locked. As a result, all processes that want to acquire the lock take a cache miss and fetch the (mostly unchanged) value from main memory. Thus, the processes performing test-and-set operations on locked cause a continuous storm of unnecessary messages over the bus that connects the processes and main memory.

# Test-and-Test-and-Set Lock

The test-and-test-and-set lock improves on the test-and-set lock by letting processes that want to acquire the lock spin on a cached copy of the Boolean register locked. When false is returned, the process applies test-and-set to locked itself. The process obtains the lock if false is returned; otherwise it goes back to spinning on its cached copy of locked. To unlock, the process resets locked to false.

The test-and-test-and-set lock provides mutual exclusion and livelock-freeness. It avoids a considerable part of the bus traffic of the test-and-set lock, because it does not continuously hammer the locked variable with test-and-set operations, and therefore tends to have a much better performance. Still, the test-and-testand-set lock generates unnecessary bus traffic, but only when the lock is released. Then an instance of what is referred to as the thundering herd problem arises, where all waiting processes simultaneously try to acquire the lock. Since false is written in locked, they all invalidate the corresponding cache line and then go to the bus to fetch the value of locked. Then they concurrently perform test-and-set to try to acquire the lock, invalidating the cached copies at other processes and thus leading to another round of cache misses. Finally, the storm subsides and processes return to local spinning on their cached copy of locked.

The performance of the test-and-test-and-set lock can be significantly improved by applying exponential back-off to reduce contention. The idea is that when a process applies test-and-set to locked but fails to get the lock, it backs off for a certain amount of time to avoid collisions. Each subsequent failure to get the lock by means of a test-and-set is interpreted as a sign that there is a high contention for the lock. Therefore, the waiting time is doubled at each failed attempt, up to some maximum. Two important parameters for the performance of the lock are the initial minimum delay and the maximum delay; optimal values for these parameters are platform dependent. Waiting durations are randomized to avoid having competing processes fall into lockstep.

Example 14.9 Consider three processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ that all want to acquire the test-and-test-and-set lock.   
Initially, the Boolean register locked is false.

Processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ concurrently read that (their cached copy of) locked is false. Let $p _ { 1 }$ apply test-and-set to locked first, setting it to true. Since this operation returns false, $p _ { 1 }$ takes the lock. Next, $p _ { 0 }$ and $p _ { 2 }$ apply test-and-set to locked. In both cases, this operation returns true, so $p _ { 0 }$ and $p _ { 2 }$ back off for (a randomization of) the minimum delay. After this delay, $p _ { 0 }$ and $p _ { 2 }$ start spinning on their cached copy of locked.

When $p _ { 1 }$ releases the lock, it resets locked to false. Now $p _ { 0 }$ and $p _ { 2 }$ concurrently read that the value has changed and apply test-and-set to locked. Let $p _ { 2 }$ be the first to do so, setting its value to true. Since this operation returns false, $p _ { 2 }$ takes the lock. The test-and-set by $p _ { 0 }$ returns true, after which $p _ { 0 }$ backs off for twice the minimum delay. After this delay, $p _ { 0 }$ returns to spinning on its cached copy of locked.

The test-and-test-and-set lock with exponential back-off is easy to implement and can give excellent performance in case of low contention. However, it may suffer from starvation, processes may be delayed longer than necessary because of back-off, and last but not least, all processes still spin on the same register locked, which creates a bottleneck and generates bus traffic, especially in case of high contention.

# 14.8 Queue Locks

Queue locks overcome the drawbacks of the test-and-test-and-set lock by placing processes that want to acquire the lock in a queue. A process $p$ in the queue spins on a register to check whether its predecessor in the queue has released the lock. When this is the case, $p$ takes the lock. Key to the success of queue locks is that each process in the queue spins on a different register. Queue locks provide mutual exclusion because only the head of the queue holds the lock. Moreover, processes are treated in a first-come, first-served manner: the sooner a process is added to the queue, the earlier it is served.

# Anderson’s Lock

Anderson’s lock places processes that want to acquire the lock in a queue by means of a Boolean array of size $n$ . Here $n$ is the maximum number of processes that may concurrently compete for the lock (so $n \leq N ,$ . A counter is used to assign a slot in the array to every process that wants to acquire the lock; this counter is interpreted modulo $n$ . At any moment, at most one process is assigned to each slot in the array, and at most one slot in the array holds true; the process that is assigned to this slot holds the lock. The slots in the array and the counter are multi-writer registers. Initially, slot 0 of the array holds true, slots $1 , \ldots , n - 1$ hold false, and the counter is zero.

A process $p$ that wants to acquire the lock applies the read-modify-write operation get-and-increment to the counter, which increases the counter by 1 and returns the previous value of the counter in one atomic step. The returned value modulo $n$ is the slot in the array that is assigned to the process. Next, $p$ spins on (a cached copy of) this slot in the array until it holds true, at which moment $p$ acquires the lock. To unlock, $p$ first sets its slot in the array to false and then the next slot modulo $n$ to true, signaling to its successor (if any) that it can take the lock.

Example 14.10 Let $N = n = 3$ , and suppose processes $p , q$ , and $r$ all want to acquire Anderson’s lock.   
Initially, only slot 0 in the array holds true and the counter is 0. $q$ applies get-and-increment to the counter, increasing it to 1. Since this operation returns 0 and slot 0 holds true, $q$ takes the lock.   
$p$ applies get-and-increment to the counter, increasing it to 2. Since this operation returns 1 and slot 1 holds false, $p$ starts spinning on this slot.   
$r$ applies get-and-increment to the counter, increasing it to 3. Since this operation returns 2 and slot 2 holds false, $r$ starts spinning on this slot.   
When $q$ releases the lock, it sets slot 0 to false and slot 1 to true.   
$p$ reads that the value of slot 1 has changed to true and takes the lock.   
$q$ wants to acquire the lock again. It applies get-and-increment to the counter, increasing it to 4. Since this operation returns 3 and slot 3 mod $3 = 0$ holds false, $q$ starts spinning on slot 0.

Anderson’s lock resolves the weaknesses of the test-and-test-and-set lock. In particular, different processes spin on different registers. However, a risk is the occurrence of what is called false sharing: different slots in the array may be kept on a single cache line, being the smallest unit of memory to be transferred between main memory and a cache. When a data item in the cache becomes invalid, the entire cache line where the data item is kept is invalidated. So if different slots of the array happen to be kept on the same cache line, releasing the lock still gives rise to unnecessary bus traffic. This can be mitigated by padding; the array size is, say, quadrupled, and slots are separated by three unused places in the array.

Another drawback of Anderson’s lock is that it requires an array of size $n$ (or more, in case of padding), even when no process wants the lock. In a setting with a large number of processes and multiple locks, this memory overhead can become costly.

# CLH Lock

The CLH lock does not use a fixed array. Instead, the queue of processes that are waiting for the lock is maintained by means of a dynamic list structure. Each element $\varepsilon$ in the list contains a Boolean multi-reader single-writer register $a c t i v e _ { \varepsilon }$ ε, which becomes false after the process that added $\varepsilon$ to the list has released the ε εlock. A multi-writer register last points to the most recently added element in the list. Initially, last points to a dummy element in which the active field is false, indicating that the lock is free.

A process $p$ wanting to acquire the lock creates an element $\varepsilon$ with $a c t i \nu e _ { \varepsilon } = t r u e .$ . It applies get-and-set $( \varepsilon )$ to last to make $\varepsilon$ ε ε εthe last element in the queue and get a pointer to the element of its predecessor in the queue. Next, $p$ εspins on (a cached copy of) the active field in its predecessor’s element in the list until it becomes false. When this happens, $p$ takes the lock. To unlock, $p$ sets $a c t i v e _ { \varepsilon }$ to false, signaling to its successor (if any) that it can take the lock; $p$ εcan reuse the element of its predecessor for a future lock access (but not its own element $\varepsilon$ ; see exercise 14.29).

εWe note that the queue is virtual: a process $p$ that is waiting for the lock knows the element of its predecessor $q$ in the queue, but there is no explicit pointer between the elements of $p$ and $q$ .

Example 14.11 Processes $p _ { 0 }$ and $p _ { 1 }$ want to acquire the CLH lock; they create elements $\varepsilon _ { 0 }$ and $\varepsilon _ { 1 }$ , respectively, with act $i \nu e _ { \varepsilon _ { 0 } } = a c t i \nu e _ { \varepsilon _ { 1 } } = t r u e .$ ε ε. Initially, last points to a dummy element in which the active field is false.

$p _ { 1 }$ applies get-and-set $\left( \varepsilon _ { 1 } \right)$ to last to let it point to $\varepsilon _ { 1 }$ . Since this operation returns the dummy element that contains false, $p _ { 1 }$ εtakes the lock.   
$p _ { 0 }$ applies get-and-set $\left( \varepsilon _ { 0 } \right)$ to last to let it point to $\varepsilon _ { 0 }$ . Since this operation returns $\varepsilon _ { 1 }$ , which contains true, $p _ { 0 }$ εstarts spinning on a cached copy of $a c t i \nu e _ { \varepsilon _ { 1 } }$ .   
When $p _ { 1 }$ releases the lock, it sets $a c t i \nu e _ { \varepsilon _ { 1 } }$ εto false.   
$p _ { 0 }$ finds that the value of $a c t i \nu e _ { \varepsilon _ { 1 } }$ εhas changed to false and takes the lock.

The CLH lock exhibits the same good performance as Anderson’s lock and uses space more sparingly. The Achilles’ heel of the CLH lock is that because of remote spinning, on the active field in the predecessor’s element in the list, its performance is heavily dependent on the presence of caches.

# MCS Lock

The MCS lock avoids remote spinning; instead, a process $q$ waiting for the lock spins on a Boolean wait field in its own element. To achieve this, $q$ must inform its predecessor $p$ in the queue that $q$ is its successor, so that after $p$ releases the lock, it will invert the wait field in $q$ ’s element. The price to pay is a more involved and expensive unlock procedure to deal with the case where $q$ joins the queue before $p$ releases the lock but informs $p$ that $q$ is its successor after $p$ has released the lock.

Again, processes that want the lock add an element $\varepsilon$ to the list, containing two multi-writer registers: the Boolean $w a i t _ { \varepsilon }$ εis true while the process is waiting in the queue, and $s u c c _ { \varepsilon }$ points to the successor element εin the (this time physical) queue or is a null pointer while $\varepsilon$ εis the last element in the queue. Moreover, the εmulti-writer register last points to the last element in the queue. Initially, $l a s t = \mathtt { n u l 1 }$ .

A process $p$ that wants to acquire the lock creates an element $\varepsilon$ with $w a i t _ { \varepsilon } = f a l s e$ and $s u c c _ { \varepsilon } = \mathtt { n u l 1 }$ . It applies get-and- $\cdot s e t ( \varepsilon )$ to last to make $\varepsilon$ ε ε εthe last element in the queue and get a pointer to the element of its predecessor in the queue. If last contained null, then $p$ takes the lock immediately. Otherwise, $p$ first sets $w a i t _ { \varepsilon }$ to true and then lets the succ field in the element of its predecessor point to $\varepsilon$ . Next, $p$ spins on wait εuntil it becomes false. When this is the case, $p$ can take the lock.

When $p$ releases the lock, it checks whether $s u c c _ { \varepsilon }$ points to another element. If so, $p$ sets the wait field in εthe latter element to false, signaling to its successor that it can take the lock. If, on the other hand, $s u c c _ { \varepsilon } =$ null, then $p$ applies compare-and-set $( \varepsilon , \tt n u l l )$ to last, signaling that the queue has become empty. If this ε,operation fails, meaning it returns false, then in the meantime another process $q$ that joined the queue has written to last. In that case, $p$ starts spinning on $s u c c _ { \varepsilon }$ until an element is returned, which is the element added by $q$ . Finally, $p$ sets the wait field in $q$ ε’s element to false. After releasing the lock, $p$ can reuse its own element $\varepsilon$ for future lock accesses.

Example 14.12 Processes $p _ { 0 }$ and $p _ { 1 }$ want to acquire the MCS lock; they create elements $\varepsilon _ { 0 }$ and $\varepsilon _ { 1 }$ , respectively, containing false and null. Initially, $l a s t = \mathtt { n u l 1 }$ .

$p _ { 1 }$ applies get-and-set $\left( \varepsilon _ { 1 } \right)$ to last to let it point to $\varepsilon _ { 1 }$ . Since this operation returns null, $p _ { 1 }$ takes the lock.   
$p _ { 0 }$ applies get-and-set $\left( \varepsilon _ { 0 } \right)$ ε to last to let it point to $\varepsilon _ { 0 }$ . Since this operation returns $\varepsilon _ { 1 } , p _ { 0 }$ sets $w a i t _ { \varepsilon _ { 0 } }$ to true, lets $s u c c _ { \varepsilon _ { 1 } }$ point to $\varepsilon _ { 0 }$ , and starts spinning on $w a i t _ { \varepsilon _ { 0 } }$ .   
When $p _ { 1 }$ ε εreleases the lock, it finds that ${ s u c c } _ { \varepsilon _ { 1 } }$ points to $\varepsilon _ { 0 }$ . Therefore, $p _ { 1 }$ sets $w a i t _ { \varepsilon _ { 0 } }$ to false.   
$p _ { 0 }$ reads that the value of $w a i t _ { \varepsilon _ { 0 } }$ ε εhas changed to false and takes the lock.

Example 14.13 Processes $p _ { 0 }$ and $p _ { 1 }$ want to acquire the MCS lock; they create elements $\varepsilon _ { 0 }$ and $\varepsilon _ { 1 }$ , respectively, containing false and null. Initially, $l a s t = \mathtt { n u l 1 }$ .

$p _ { 1 }$ applies get-and-set $\left( \varepsilon _ { 1 } \right)$ to last to let it point to $\varepsilon _ { 1 }$ . Since this operation returns null, $p _ { 1 }$ takes the lock.   
$p _ { 0 }$ applies get-and-set $\left( \varepsilon _ { 0 } \right)$ to last to let it point to $\varepsilon _ { 0 }$ . This operation returns $\varepsilon _ { 1 }$ .   
When $p _ { 1 }$ ε releases the lock, it finds that $s u c c _ { \varepsilon _ { 1 } } = \mathtt { n u l 1 }$ ε. Therefore, it applies compare-and-se $\left( \varepsilon _ { 1 } , \tt n u l 1 \right)$ to last. Since last points to $\varepsilon _ { 0 }$ ε, this operation returns false. Therefore, $p _ { 1 }$ starts spinning on $s u c c _ { \varepsilon _ { 1 } }$ , .   
$p _ { 0 }$ sets $w a i t _ { \varepsilon _ { 0 } }$ to true, lets $s u c c _ { \varepsilon _ { 1 } }$ point to $\varepsilon _ { 0 }$ , and starts spinning on $w a i t _ { \varepsilon _ { 0 } }$ .   
$p _ { 1 }$ finds that $s u c c _ { \varepsilon _ { 1 } }$ points to $\varepsilon _ { 0 }$ , and it sets $w a i t _ { \varepsilon _ { 0 } }$ to false.   
$p _ { 0 }$ εreads that the value of $w a i t _ { \varepsilon _ { 0 } }$ εhas changed to false and takes the lock.

The MCS lock tends to outperform the CLH lock on what are called cacheless NUMA (Non-Uniform Memory Access) architectures, in which each processor is provided with its own memory unit instead of having one shared-memory unit.

# Timeouts

With queue locks, a process $p$ in the queue cannot easily give up its attempt to acquire the lock, because $p$ ’s successor in the queue depends on $p$ to be informed when it can take the lock. We now explain how the CLH lock can be adapted to include such timeouts. The key is that when $p$ wants to leave the queue, it first needs to tell its successor to start spinning on the element of $p$ ’s predecessor in the queue.

Again, a process $p$ that wants to acquire the lock places an element $\varepsilon$ in the list, containing a multi-reader single-writer register pred that can have the following values:

• null if $p$ is waiting in the queue or is in its critical section; a pointer to the element of $p$ ’s predecessor in the queue if $p$ has given up waiting for the lock; or • a pointer to a special element called released if $p$ has left its critical section.

The multi-writer register last points to the last element in the queue. Initially, $l a s t = \mathtt { n u l 1 }$

When $p$ wants to acquire the lock, it creates an element $\varepsilon$ with $p r e d _ { \varepsilon } = \mathtt { n u l 1 }$ . It applies get-and-set $( \varepsilon )$ to last to make $\varepsilon$ ε ε εthe last element in the queue and get a pointer to the element of its predecessor. If last εcontained null, then $p$ takes the lock immediately. Otherwise it spins on (a cached copy of) the pred field in its predecessor’s element until it is not null. If that pred field then points to the element released, $p$ takes the lock. Otherwise it points to the element $\varepsilon ^ { \prime }$ of the new predecessor of $p$ (meaning that $p$ ’s original predecessor has timed out). In that case, $p$ εcontinues to spin on $p r e d _ { \varepsilon ^ { \prime } }$ until it is not null.

If $p$ εquits its attempt to acquire the lock, it applies compare-and-se $\scriptstyle { \left( { \varepsilon , p r e d _ { \varepsilon } } \right) }$ to last. If this operation fails, then $p$ has a successor in the queue; in that case, $p$ ε, εsets pred to the element of its predecessor, signaling to the successor of $p$ that it has a new predecessor.

When $p$ releases the lock, it applies compare-and-se $\mathtt { \backslash } ( \varepsilon , \mathtt { n u l l } )$ to last. If this operation succeeds, then the queue has become empty. If it fails, then $p$ ε,has a successor in the queue. In the latter case, $p$ sets $p r e d _ { \varepsilon }$ to the element released, signaling to its successor that it can take the lock.

Example 14.14 Processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ want to acquire the CLH lock with timeouts; they create elements $\varepsilon _ { 0 } , \varepsilon _ { 1 }$ , and $\varepsilon _ { 2 }$ , respectively, with their pred fields having the value null. Initially, $l a s t = \mathtt { n u l 1 }$ .

$p _ { 1 }$ applies get-and-set $\left( \varepsilon _ { 1 } \right)$ to last to let it point to $\varepsilon _ { 1 }$ . Since this operation returns null, $p _ { 1 }$ takes the lock. $p _ { 0 }$ applies get-and-set $\left( \varepsilon _ { 0 } \right)$ ε to last to let it point to $\varepsilon _ { 0 }$ . Since this operation returns $\varepsilon _ { 1 } , p _ { 0 }$ starts spinning on $p r e d _ { \varepsilon _ { 1 } }$ .   
$p _ { 2 }$ ε applies get-and-set $\left( \varepsilon _ { 2 } \right)$ to last to let it point to $\varepsilon _ { 2 }$ . Since this operation returns $\varepsilon _ { 0 } , p _ { 2 }$ starts spinning on $p r e d _ { \varepsilon _ { 0 } }$ .   
$p _ { 0 }$ ε decides to abort its attempt to acquire the lock. It lets $p r e d _ { \varepsilon _ { 0 } }$ point to $\varepsilon _ { 1 }$ .   
$p _ { 2 }$ finds that $p r e d _ { \varepsilon _ { 0 } }$ has changed from null to $\varepsilon _ { 1 }$ εand starts spinning on $p r e d _ { \varepsilon _ { 1 } }$ .   
When $p _ { 1 }$ ε  εreleases the lock, it applies compare-and- $\mathsf { s e t } ( \varepsilon _ { 1 } , \tt n u l 1 )$ ε  to last. This operation fails because last points to $\varepsilon _ { 2 }$ instead of $\varepsilon _ { 1 }$ . Therefore, $p _ { 1 }$ lets $p r e d _ { \varepsilon _ { 1 } }$ ε ,point to released.   
$p _ { 2 }$ εfinds that $p r e d _ { \varepsilon _ { 1 } }$ ε εhas changed from null to released and takes the lock.

# Bibliographical notes

The Ricart-Agrawala algorithm was presented in [102], and the Carvalho-Roucairol optimization was proposed in [20]. Raymond’s algorithm comes from [101] and its fault-tolerant version from [27]. The Agrawal– El Abbadi algorithm originates from [2]. Peterson’s mutual exclusion algorithm for two processes stems from [94], and the approach to extend such an algorithm to general $N$ via a tournament tree was proposed in [96]. The bakery algorithm originates from [67]; it was proved in [18] that such an algorithm requires $N$ atomic registers. Fischer’s algorithm was proposed in an email by Michael J. Fischer in 1985 and was presented in [70]. The test-and-test-and-set lock is due to [63]. Anderson’s lock stems from [3], the CLH lock comes from [31, 76], and the CLH lock with timeouts from [104]. The MCS lock originates from [82].9

# 14.9 Exercises

Exercise 14.1 Say for both mutual exclusion and starvation-freeness whether it is a safety or liveness prop erty.

Exercise 14.2 Consider the Ricart-Agrawala algorithm with the Carvalho-Roucairol optimization. Let processes $p _ { 0 } , p _ { 1 }$ , and $p _ { 2 }$ become privileged for the first time, in this order. Next $p _ { 0 }$ and $p _ { 1 }$ concurrently want to become privileged again, and send requests with the same logical time stamp. Explain how first $p _ { 0 }$ and then $p _ { 1 }$ can become privileged, as well as how first $p _ { 1 }$ and then $p _ { 0 }$ can become privileged.

Exercise 14.3 In the Carvalho-Roucairol optimization, each set Requestsi initially contains all processes except $p _ { i }$ . Would it be sufficient if for each pair of distinct processes $p _ { i }$ and $p _ { j }$ , initially Requestsi contains $p _ { j }$ or Requestsj contains $p _ { i }$ ?

Exercise 14.4 Would it make sense to replace Lamport’s logical clock by the vector clock in the RicartAgrawala algorithm?

Exercise 14.5 The logical clock values in the Ricart-Agrawala algorithm are unbounded. Adapt the algorithm (without the Carvalho-Roucairol optimization) so that the range of these values becomes finite, using modulo arithmetic.

Exercise 14.6 Explain how the Ricart-Agrawal algorithm could be adapted to make it fault-tolerant. Does the Carvalho-Roucairol optimization still work properly in this setting?

Exercise 14.7 Run Raymond’s algorithm on the network from example 14.3. Initially, process $p _ { 3 }$ holds the token and all buffers are empty. Give a computation (including all messages) in which first $p _ { 8 }$ , then $p _ { 2 }$ , and finally $p _ { 5 }$ requests the token, but they receive the token in the opposite order.

Exercise 14.8 Adapt Raymond’s algorithm so that a process that receives the token and wants to enter its critical section becomes privileged immediately, even if its ID is not at the head of its queue.

Exercise 14.9 Argue that in Raymond’s algorithm each request to enter a critical section gives rise to at most $2 D$ messages.

Exercise 14.10 Explain in detail why Raymond’s algorithm is starvation-free.

Exercise 14.11 Consider the Agrawal–El Abbadi algorithm with seven processes structured in a binary tree as in example 14.4. What are the quorums if $p _ { 9 }$ and $p _ { 4 }$ crashed? If $p _ { 9 } , p _ { 3 }$ , and $p _ { 4 }$ crashed? If $p _ { 9 } , p _ { 3 }$ , and $p _ { 8 }$ crashed?

Exercise 14.12 In the Agrawal–El Abbadi algorithm, what are the minimum and maximum sizes of a quorum (in terms of $N = 2 ^ { k + 1 } - 1 \mathrm { ~ , ~ }$ )?

Exercise 14.13 Consider the Agrawal–El Abbadi algorithm with $N = 2 ^ { k } - 1$ . Let fewer than $k$ processes have crashed. Argue that the remaining network still contains a quorum.

Exercise 14.14 Prove that for each pair of quorums $Q$ and $Q ^ { \prime }$ in the Agrawal–El Abbadi algorithm, $Q \subseteq Q ^ { \prime }$ implies $Q = Q ^ { \prime }$ .

Exercise 14.15 Explain why the following mutual exclusion algorithm is flawed. Let flag be a multi-writer Boolean register. A process $p$ wanting to enter its critical section waits until flag $= .$ false. Then $p$ sets flag to true and becomes privileged. When $p$ exits its critical section, it resets flag to false.

Exercise 14.16 Suppose that in Peterson’s lock, a process $p _ { b }$ would set wait to $^ b$ before setting flag[b] to true. Give an execution to show that then mutual exclusion could be violated.

Exercise 14.17 2-mutual exclusion is satisfied if at any time at most two processes are in their critical section. Modify the tournament tree (in which the nodes run Peterson’s algorithm) to yield a solution for the 2-mutual exclusion problem.

Exercise 14.18 Present a starvation-free 2-mutual exclusion algorithm using one register and a read-modifywrite operation.

Exercise 14.19 For each of the following two adaptations of the bakery algorithm, give an execution to show that mutual exclusion could be violated.

(a) A process $p _ { i }$ that wants to enter its critical section first computes numberi, and only then sets choosingi to true. (b) A process can enter its critical section without waiting for all choosing registers to become false.

Exercise 14.20 Describe an execution of the bakery algorithm in which the values of number registers grow without bound.

Exercise 14.21 Adapt the bakery algorithm such that the range of the number registers becomes finite.

Exercise 14.22 Argue the correctness of theorem 14.1 for the case $N = 3$ .

Exercise 14.23 Consider the following mutual exclusion algorithm for $N$ processes $p _ { 0 } , . . . , p _ { N - 1 }$ , using one multi-writer register turn of which the values range over $\{ 0 , . . . , N - 1 \}$ .

When turn has the value $i$ , process $p _ { i }$ can enter its critical section. If $p _ { i }$ does not want to become privileged or when it leaves its critical section, it writes the value $( i + 1 )$ mod $N$ in turn.

Why does this starvation-free mutual exclusion algorithm not contradict theorem 14.1? What are drawbacks of this algorithm?

Exercise 14.24 Give an example to show that in Fischer’s algorithm, mutual exclusion could be violated if one process, after writing to turn, would read turn less than one time unit later.

Exercise 14.25 Give an example of starvation with Fischer’s algorithm.

Exercise 14.26 Explain why the proof of theorem 14.1 does not apply to Fischer’s algorithm.

Exercise 14.27 Argue that Anderson’s lock provides mutual exclusion and first-come, first-served fairness.

Exercise 14.28 Give an example (with $n = 3$ ) to show what could go wrong if in Anderson’s lock a process that releases the lock would first set the next slot modulo $n$ in the array to true and only then reset its own slot to false.

Exercise 14.29 [55] Suppose that in the CLH lock, a process would reuse its own element (instead of the element of its predecessor). Give an execution to show that then the algorithm would be flawed.

Exercise 14.30 Suppose that in the CLH lock the last pointer is null when there is no thread at the lock, instead of pointing to a node with the active value false, so that if nobody wants the lock, this node can be reclaimed by a garbage collector.

(a) Explain which adaptations then need to be made to the CLH lock. (b) Why is this design more fitting for the MCS than for the CLH lock?

Exercise 14.31 For each of the two read-modify-write operations in the MCS lock, replace this operation by read and write operations and give an execution to show that the resulting lock is flawed. In both cases, explain which property is violated.

Exercise 14.32 Argue in detail that the unlock procedure of the MCS lock does not suffer from deadlock.

Exercise 14.33 Consider for the MCS lock the situation where a process $p$ wants to acquire the lock and finds that last points to an element. Suppose $p$ would first set the succ field of that element to its own element and only then set the wait field in its own element to true. What could go wrong?

Exercise 14.34 [104] Develop a variant of the MCS lock that includes timeouts, allowing a process to abandon its attempt to obtain the lock.

Exercise 14.35 Give an execution of the CLH lock with timeouts in which initially the lock is free, four processes concurrently want to take the lock, two of the processes that are waiting for the lock concurrently leave the queue, the last process in the queue is pointed forward twice, and ultimately this process takes the lock.

Exercise 14.36 In the CLH queue lock with timeouts, when a process releases the lock, it first applies compare-and-s $\boldsymbol { \mathscr { o } } t ( \varepsilon , \mathrm { \tt n u l 1 } )$ to last, with $\varepsilon$ its own node. Why does it not simply set pred to released, ε, εsignaling to its successor in the queue (if any) that the lock is free?

# Barriers

Sometimes during a computation processes must collectively wait at some point, called a barrier, until all processes have arrived there, after which they can leave the barrier and resume execution. For example, in parallel programs, a barrier is often used to make sure that all threads have completed some parallel loop before the computation proceeds any further. Or a barrier may be employed in a soft real-time application, in which a number of subtasks must be completed by different processes before the overall application can proceed. A barrier generally keeps track of how many processes have reached it and signals to all waiting processes when the last process has reached the barrier. We discuss several barrier algorithms in a sharedmemory setting. Waiting at a barrier resembles waiting to enter a critical section. Waiting processes can either spin on local or (locally cached copies of) remote variables or fall asleep when the barrier is reached and be woken up when all processes have reached the barrier.

# 15.1 Sense-Reversing Barrier

A straightforward way of implementing a barrier is to maintain a counter, a multi-writer register, with initial value 0. Each process that reaches the barrier performs get-and-increment on the counter; a read-modifywrite operation is needed because otherwise multiple processes could concurrently increase the counter to the same value, leading to an incorrect count. When the counter equals the number $N$ of processes that must reach the barrier, all processes can leave the barrier.

If a process reaches the barrier and applies a get-and-increment that returns a value smaller than $N - 1$ , then it can fall asleep. The last process to reach the barrier, for which get-and-increment returns $N - 1$ , resets the value of the counter to 0, so that it can be reused. Then this process could be given the task to wake up all other processes at the barrier. A drawback of such a waking-up phase is that it can be time consuming. A better idea is to use a global Boolean sense field, a multi-writer register, initially false, on which the last process to reach the barrier can signal to all other process that they can resume execution. Moreover, each process carries a local Boolean sense field, a single-reader single-writer register, which initially is true. As explained before, a process $p$ that reaches the barrier applies get-and-increment to the counter. If $p$ is not the last to reach the barrier, meaning that get-and-increment returns a value smaller than $N - 1$ , it starts spinning on the barrier’s global sense field until it equals $p$ ’s local sense, after which $p$ can leave the barrier. On the other hand, suppose $p$ is the last to reach the barrier, meaning that get-and-increment returns $N - 1$ . Then $p$ first resets the counter to 0, so that it can be reused, and then reverses the value of the global sense field, signaling to the other processes that they can leave the barrier. Processes resume execution with reversed local sense, so that not only the counter but also the (global and local) sense fields can be reused for the next barrier.

Example 15.1 We study a possible execution of the sense-reversing barrier. Consider three processes $p , q$ , and $r$ , initially with local sense true. The barrier’s counter initially is 0 and its global sense is false.

Process $q$ reaches the barrier and applies get-and-increment to the counter, which returns 0. Therefore, $q$ starts spinning on the global sense field until it is true.   
Process $p$ reaches the barrier and applies get-and-increment to the counter, which returns 1. Therefore, $p$ starts spinning on the global sense field until it is true.   
Process $r$ reaches the barrier and applies get-and-increment to the counter, which returns 2. Therefore, $r$ resets the value of the counter to 0, reverses the global sense field to true, and leaves the barrier with reversed local sense false.   
Processes $p$ and $q$ notice that the global sense of the barrier has become true and also leave the barrier with reversed local sense false.

The main drawback of the sense-reversing barrier is that, similar to the situation with the test-and-testand-set lock (see section 14.7), processes that have arrived at the barrier are all spinning on (a cached copy of) the same global sense field. The following two barriers alleviate this performance bottleneck.

# 15.2 Combining Tree Barrier

The combining tree barrier uses a tree structure to reduce contention on the global sense field. Each node in the tree represents a sense-reversing barrier; processes that are waiting at the barrier are spinning on the global sense field of a node.

Let the tree have depth $k$ , and let each node at a depth smaller than $k$ have $r$ children. The corresponding combining tree barrier can cope with $r ^ { k + 1 }$ processes: to each leaf, at most $r$ processes are assigned. For simplicity, we assume that $N = r ^ { k + 1 }$ . Each node maintains a counter and a global sense field. At a leaf, the counter keeps track of how many of the processes assigned to this leaf have reached the barrier, while at a nonleaf it keeps track of the number of children of this node for which the counter has become $r _ { \cdot }$ . As soon as the counter of a nonroot becomes $r$ , the counter of the parent of this node is increased by 1. When finally the counter at the root of the tree becomes $r$ , we can be certain that all processes have reached the barrier. Then the counters are reset and the global sense fields are reversed at all the nodes, from top (the root) to bottom (the leaves), after which all processes resume execution.

To be more precise, the nodes in the tree are numbered as follows: the root carries number 0, and given a nonleaf with the number $n$ , its children carry the numbers $r n + 1$ up to $r n + r$ . Each node $n$ carries two multi-writer registers: $c o u n t _ { n }$ of type integer and $g s e n s e _ { n }$ of type Boolean. We assume there are processes $p _ { 0 } , . . . , p _ { r ^ { k + 1 } - 1 }$ . Each process $p _ { i }$ maintains a single-reader single-writer local sense field lsensei. Initially, $c o u n t _ { n } = 0$ , $g s e n s e _ { n } = f a l s$ e, and $l s e n s e _ { i } = t r u e$ . Process $p _ { i }$ is assigned to leaf $( r ^ { k } - 1 ) + \lfloor i / r \rfloor$ in the tree. That is, when $p _ { i }$ reaches the barrier, it performs the following procedure CombiningTree $( n )$ /with $n = ( r ^ { k } - 1 ) +$ $\lfloor i / r \rfloor$ :

if counte $r _ { n }$ get-and-increment $< r - 1$ then .while gsense $_ n \neq$ lsensei do $\{ \}$ ; end while   
else if $n > 0$ then >perform procedure CombiningTree $\left( \left\lceil { \frac { n } { r } } \right\rceil - 1 \right)$ ; end if $c o u n t _ { n } \gets 0 ; \quad g s e n s e _ { n } \gets l s e n s e _ { i } ;$   
end if

A process $p _ { i }$ performing CombiningTree $( n )$ first applies get-and-increment to the counter at node $n$ . If the counter is increased to a value smaller than $r$ , then $p _ { i }$ starts spinning on the global sense field of $n$ until it equals $p _ { i }$ ’s local sense. On the other hand, if $p _ { i }$ increases the counter at $n$ to $r$ , then we distinguish the case where $n$ is a nonroot from the case where $n$ is the root of the tree. If $n$ is a nonroot, then $p _ { i }$ moves to the parent of $n$ in the tree, where it performs CombiningTree again. If $n$ is the root of the tree, then all processes have reached the barrier. In this case, $p _ { i }$ resets the counter at the root to 0, so that it can be reused, and next reverses the value of the global sense field at the root, signaling to the $r - 1$ processes spinning on this field that they can leave the barrier.

Processes that find the global sense field they are spinning on reversed, and the process that reverses the global sense at the root, reset the counter and reverse the global sense field at all the nodes they visited earlier, signaling to the $r - 1$ processes spinning on such a field that they can leave the barrier. Processes resume execution with reversed local sense so that the counters and sense fields can be reused for the next barrier.

Example 15.2 We consider a possible execution of the combining tree barrier. Let $k = 2$ , $r = 2$ , and $N = 8$ . Processes $p _ { 0 }$ to $p _ { 7 }$ are assigned to leaves of the tree as shown in the following picture. Initially, the counters at the nodes are 0, the global sense fields at the nodes are false, and all processes have local sense true.

![](images/cbdff8dbfe54f5fb3cf3570a0018454d642dcde4469a6815b8db01b0f2c20c4a.jpg)

Let $p _ { 0 } , p _ { 2 } , p _ { 4 }$ , and $p _ { 7 }$ arrive at the barrier. Each applies get-and-increment to the counter of its leaf, increasing it to 1. Next, each starts spinning on the global sense field of its leaf until it becomes true. Let $p _ { 1 }$ and $p _ { 6 }$ arrive at the barrier. They apply get-and-increment to the counters of leaf 3 and leaf 6, respectively, increasing them to 2. Next, they move to nodes 1 and 2, respectively, where they apply get-and-increment to the counters, increasing them to 1. They start spinning on the global sense fields of nodes 1 and 2, respectively, until they become true. Let $p _ { 3 }$ arrive at the barrier. It applies get-and-increment to the counter of leaf 4, increasing it to 2. Next, it moves to node 1, where it applies get-and-increment to the counter, increasing it to 2. Next, it moves to the root, where it applies get-and-increment to the counter, increasing it to 1. It starts spinning on the global sense field of the root until it becomes true. The resulting situation is as follows.

![](images/7dee0aca083981eae9dfd58499de7f6b7a43f417c4d274d52f104953a02ca00e.jpg)

Finally, $p { 5 }$ arrives at the barrier. It applies get-and-increment to the counter of leaf 5, increasing it to 2. Next, it proceeds to node 2, where it applies get-and-increment to the counter, increasing it to 2. Then it moves to the root, where it applies get-and-increment to the counter, increasing it to 2. It reverses the global sense field of the root to true. $p { 5 }$ moves to node 2, where it reverses the global sense field to true. And $p _ { 3 }$ , which finds that the global sense field of the root has become true, moves to node 1, where it reverses the global sense field to true. $p { 5 }$ and $p _ { 3 }$ move to leaves 5 and 4, respectively, where they reverse the global sense fields to true. And $p _ { 1 }$ and $p _ { 6 }$ , which find that the global sense fields of nodes 1 and 2, respectively, have become true, move to leaves 3 and 6, respectively, where they reverse the global sense fields to true. $p _ { 0 } , p _ { 2 } , p _ { 4 }$ , and $p _ { 7 }$ find that the global sense fields they are spinning on have become true. Each of the eight processes leaves the barrier and continues its execution with reversed local sense false.

We briefly argue that the combining tree barrier is correct. It is easy to see, by induction on depth, that the counter at a node $n$ becomes $r$ if and only if all processes assigned to the leaves below $n$ have reached the barrier: in the base case of the induction, $n$ is a leaf, and in the inductive case, the claim has already been proved for the children of $n$ . So, in particular, the counter at the root becomes $r$ if and only if all processes have reached the barrier. Furthermore, when this happens, it is guaranteed that the global sense fields at all nodes are reversed, so all processes leave the barrier.

# 15.3 Tournament Barrier

The tournament barrier is an improvement over the combining tree barrier in the sense that it allows processes to spin on local variables and does not use any read-modify-write operations.

A tournament tree is a binary tree, of a depth $k > 0$ , in which each node represents a barrier of size 2. >The corresponding tournament barrier can cope with $2 ^ { k + 1 }$ processes: to each leaf at most two processes are assigned. For simplicity, we assume that $N = 2 ^ { k + 1 }$ . Each node is divided into an active and a passive side; both sides of the node carry a global sense field. One child is assigned to the active as well as to the passive side of every nonleaf in the tree, and likewise one process is assigned to the active as well as to the passive side of every leaf in the tree.

The idea behind the tournament barrier is that a process $p$ at the passive side of a node signals to (the global sense field of) its active partner at this node that $p$ has arrived at the barrier. Next, $p$ starts spinning on the global sense field of its passive side until it has been reversed by its active partner. Conversely, a process at the active side of a node waits until it receives a signal that its passive partner at this node has arrived at the barrier and then either moves on to the parent of this node, at a nonroot, or concludes that the barrier has been completed, at the root. In the latter case, the passive global sense fields are reversed at all the nodes, from top (the root) to bottom (the leaves), after which all processes resume execution, with reversed local sense.

To be more precise, nodes in the tree are numbered in the same fashion as the combining tree barrier with $r = 2$ (and the tournament tree for Peterson’s mutual exclusion algorithm in section 14.4). Each node $n$ carries two Boolean multi-writer registers: $a s e n s e _ { n }$ and psensen. We assume there are processes $p _ { 0 } , . . . , p _ { 2 ^ { k + 1 } - 1 }$ . Each process $p _ { i }$ maintains a single-reader single-writer local sense field lsensei. Initially, $a s e n s e _ { n } = p s e n s e _ { n } = f a l s e$ and $l s e n s e _ { i } = t r u e$ . Process $p _ { i }$ is assigned to leaf $( 2 ^ { k } - 1 ) + \lfloor i / 2 \rfloor$ in the tree, at the active side if $i$ is even and at the passive side if $i$ is odd. That is, when $p _ { i }$ /reaches the barrier, it performs the following procedure Tournament $\cdot ( n , b )$ with $n = \left( 2 ^ { k } - 1 \right) + \lfloor i / 2 \rfloor$ and $b = i$ mod 2; here, $b = 0$ represents the active side and $b = 1$ ,the passive side of node $n$ .

if $b = 1$ then asensen ← lsensei; while psensen ̸= lsensei do $\{ \}$ ; end while   
else while asensen ̸= lsensei do $\{ \}$ ; end while if $n > 0$ then >perform procedure Tournament $\textstyle { \left( { \left\lceil { \frac { n } { 2 } } \right\rceil } - 1 , ( n + 1 ) \right) }$ mod 2); end if $p s e n s e _ { n } \gets l s e n s e _ { i } ;$   
end if

A process $p _ { i }$ that performs Tournament $( n , b )$ acts as follows:

• If $b = 1$ , then $p _ { i }$ sets the active sense field of $n$ to $p _ { i }$ ’s local sense and starts spinning on the passive sense field of $n$ until it equals $p _ { i }$ ’s local sense. When this happens, $p _ { i }$ reverses the passive sense fields of the nodes it visited earlier and leaves the barrier. If $b = 0$ , then $p _ { i }$ starts spinning on the active sense field of $n$ until it equals $p _ { i }$ ’s local sense. When this happens, if $n$ is not the root of the tree, $p _ { i }$ moves to the parent of $n$ , where it performs Tournament again. On the other hand, if $n$ is the root of the tree, $p _ { i }$ reverses the passive sense fields of the nodes it visited earlier and leaves the barrier.

As noted, processes resume execution with reversed local sense.

It is determined beforehand which global sense fields a process will spin on while waiting for the barrier to complete. And for each global sense field of each active or passive part of a node there is exactly one process that will spin on this field. Therefore, each of these fields can be kept in the local memory of the process that spins on it.

Example 15.3 We consider a possible execution of the tournament barrier. Let $k = 2$ and $N = 8$ . The processes $p _ { 0 }$ to $p _ { 7 }$ are assigned to the leaves of the tree in the accompanying picture, where $p _ { 0 } , p _ { 2 } , p _ { 4 }$ , and $p _ { 6 }$ are assigned to the active sides and $p _ { 1 } , p _ { 3 } , p _ { 5 }$ , and $p _ { 7 }$ to the passive sides of their leaves. For each nonleaf, its even and odd children are assigned to its active and passive sides, respectively. Initially, the sense fields at both sides of the nodes are false and all processes have local sense true.

![](images/5fce62d522bc26dd73e033d93567daf7333e608a6ee00fab0267f7ebfeb57bda.jpg)

Let $p _ { 0 } , p _ { 2 } , p _ { 4 }$ , and $p _ { 7 }$ arrive at the barrier. Then $p _ { 0 } , p _ { 2 }$ , and $p _ { 4 }$ move to their leaves and start spinning on the active sense fields until they equal true. And $p _ { 7 }$ moves to its leaf 6, sets the active sense field to true, and starts spinning on the passive sense field until it equals true.   
Let $p _ { 1 }$ arrive at the barrier. It moves to its leaf 3, sets the active sense field to true, and starts spinning on the passive sense field.   
When $p _ { 0 }$ finds that the active sense field of leaf 3 has become true, it moves to node 1, where it starts spinning on the active sense field.   
Let $p _ { 6 }$ arrive at the barrier. It moves to its leaf 6, where it finds that the active sense field is true. Therefore, it moves to node 2, sets the active sense field to true, and starts spinning on the passive sense field. Let $p _ { 3 }$ arrive at the barrier. It moves to its leaf 4, sets the active sense field to true, and starts spinning on the passive sense field.   
When $p _ { 2 }$ finds that the active sense field of leaf 4 has become true, it moves to node 1, where it sets the active sense field to true and starts spinning on the passive sense field.

When $p _ { 0 }$ finds that the active sense field of node 1 has become true, it moves to the root and starts spinning on the active sense field. The resulting situation is depicted in the following diagram, where $p _ { 0 }$ is spinning on the active sense field of the root, while six other processes are spinning on a passive sense field.

![](images/f59ba06f3354cd0d4bdb513317e9d24258d546cf4c9f4dcc33f907d0ff140b40.jpg)

Finally, $p _ { 5 }$ arrives at the barrier. It moves to its leaf 5, sets the active sense field to true, and starts spinning on the passive sense field.   
When $p _ { 4 }$ finds that the active sense field of leaf 5 has become true, it moves to node 2. Since the active sense field of node 2 is true, $p _ { 4 }$ moves on to the root, where it sets the active sense field to true and starts spinning on the passive sense field.   
When $p _ { 0 }$ finds that the active sense field of the root has become true, it sets the passive sense fields at nodes 0, 1, and 3 to true.   
When $p _ { 4 }$ finds that the passive sense field of the root has become true, it sets the passive sense fields at nodes 2 and 5 to true.   
When $p _ { 2 }$ and $p _ { 6 }$ find that the passive sense fields of nodes 1 and 2, respectively, have become true, they set the passive sense fields at leaves 4 and 6, respectively, to true.   
$p _ { 1 } , p _ { 3 } , p _ { 5 }$ , and $p _ { 7 }$ find that the passive sense field they are spinning on has become true. Each of the eight processes leaves the barrier and continues its execution with reversed local sense false.

Correctness of the tournament tree can be argued in a similar fashion as for the combining tree barrier.

# 15.4 Dissemination Barrier

The dissemination barrier progresses in rounds; in each round, every process that has reached the barrier notifies some other process and waits for notification by some other process. Just as in the tournament barrier, no read-modify-write operation is used.

Suppose that $N$ processes $p _ { 0 } , . . . , p _ { N - 1 }$ must reach the barrier. A process that reaches the barrier starts by executing round 0. In a round $n \geq 0$ ,, each process $p _ { i }$ that has reached the barrier

. notifies process p(i+2n) mod N, waits for notification by process $p _ { ( i - 2 ^ { n } ) }$ mod $N$ , and   
• progresses to round $n + 1$ .

When a process completes round $\lceil \log _ { 2 } N \rceil - 1$ , all $N$ processes have reached the barrier. So then the process can leave the barrier.

Example 15.4 We consider one execution of the dissemination barrier, with $N = 5$ . Since $\lceil \log _ { 2 } 5 \rceil = 3$ , the barrier is completed after round 2.

– In round 0, each process $p _ { i }$ notifies process $p _ { ( i + 1 ) }$ mod 5 and waits for notification by process $p _ { ( i - 1 ) }$ mod 5.   
– In round 1, each process $p _ { i }$ notifies process $p _ { ( i + 2 ) }$ mod 5 and waits for notification by process $p _ { ( i - 2 ) }$ mod 5.   
– In round 2, each process $p _ { i }$ notifies process $p _ { ( i + 4 ) } \bmod { 5 }$ and waits for notification by process $p _ { ( i - 4 ) }$ mod 5.

When a process has completed round 2, it can leave the barrier. The notifications in the three successive rounds can be depicted as follows.

![](images/fea7390297f4c14d3d115ec0b87976a35110701f39ac6d23faeb2baaa6f8856a.jpg)

Note that if, for instance, $p _ { 0 }$ has not yet reached the barrier, then $p _ { 1 }$ cannot complete round 0, $p _ { 2 }$ and $p _ { 3 }$ cannot complete round 1, and $p _ { 4 }$ cannot complete round 2. So no process can leave the barrier.

We argue the correctness of the dissemination barrier. When all $N$ processes have reached the barrier, clearly all $\lceil \log _ { 2 } N \rceil$ rounds can be completed by all processes. Now suppose that some process $p _ { i }$ has not yet reached the barrier; we argue that then no process can have completed round $\lceil \log _ { 2 } N \rceil - 1$ . For simplicity, we take $N = 2 ^ { k }$ for some $k > 0$ , so that $\lceil \log _ { 2 } N \rceil = k$ . In the following explanation, subscripts of processes are to be interpreted modulo $2 ^ { k }$ .

Since $p _ { i }$ has not reached the barrier, $p _ { i + 1 }$ has not completed round 0.   
Since $p _ { i } , p _ { i + 1 }$ have not completed round 0, $p _ { i + 2 } , p _ { i + 3 }$ have not completed round 1.   
Since $p _ { i } , p _ { i + 1 } , p _ { i + 2 } , p _ { i + 3 }$ , have not completed round 1, $p _ { i + 4 } , p _ { i + 5 } , p _ { i + 6 } , p _ { i + 7 }$ have not completed round 2. ·   
Since $p _ { i } , . . . , p _ { i + 2 ^ { k - 1 } - 1 }$ have not completed round $k - 2$ , $p _ { i + 2 ^ { k - 1 } } , . . . , p _ { i + 2 ^ { k } - 1 }$ have not completed round $k - 1$ .

Since subscripts are interpreted modulo $2 ^ { k }$ , ${ { p } _ { i + 2 } } { { k } _ { - 1 } }$ is $p _ { i - 1 }$ . So no process has left the barrier.

# Bibliographical notes

The combining tree barrier originates from [127]. The tournament barrier and the dissemination barrier stem from [52].

# 15.5 Exercises

Exercise 15.1 Explain under which circumstances it is more favorable to let processes that have arrived at the barrier fall asleep and under which circumstances it is better to use spinning.

Exercise 15.2 Consider the sense-reversing barrier. Suppose the last process to reach the barrier would first reverse the value of the global sense field and only then reset the counter to 0. What could go wrong?

Exercise 15.3 Continue the application of the sense-reversing barrier in example 15.1 by reusing the counter and the sense fields (with their values reversed) for the next barrier. Give one possible execution.

Exercise 15.4 Argue that the sense-reversing barrier is a correct barrier. Take into account that the counter and sense fields are reused for multiple subsequent barriers.

Exercise 15.5 Suppose that in the combining tree barrier, the process that decreases the counter at the root to 0 would invert the global sense field at the root before resetting the counter. Give a scenario, with $r = 2$ , $k = 1$ , and $N = 4$ , which shows that then the barrier would be flawed.

Exercise 15.6 [55] Argue that the combining tree barrier can employ any barrier algorithm in its nodes (not just the sense-reversing barrier).

Exercise 15.7 Consider the tournament barrier with $k = 2$ and $N = 8$ . Give an execution in which at some point only one process has not yet reached the barrier and all other processes are spinning on a passive sense field.

Exercise 15.8 Suppose the tournament barrier is applied to an odd number of threads. Explain how the barrier needs to be adapted.

Exercise 15.9 Argue the correctness of the dissemination barrier for any $N$ .

# Exercise 15.10

(a) [55] Adapt the dissemination barrier to make it reusable, by keeping track of the sense and parity of the current phase.   
(b) Consider two processes, where one process is very slow in detecting that it can leave the barrier, while the other process leaves the barrier and reaches it again. Argue that your reusable dissemination barrier works correctly (also) in this situation.

# Distributed Transactions

A transaction is a sequence of events that are performed as one indivisible unit. A transaction either commits, in which case all of its events are performed at once, or aborts, meaning that none of its events take effect. A transaction is distributed if there are multiple processes involved.

Distributed transactions are especially important in the context of a distributed database consisting of different storage locations that together are supposed to provide a centralized view of the overall database. The database usually has a client-server architecture in which servers hold all the data and clients can access the data. For example, consider a customer who wants to buy a pair of shoes from an online shop by using an electronic banking service. If the bank agrees that the customer’s credit is sufficient and the shop determines that the selected shoes can be supplied, then the events of placing the order, transferring the money, and shipping the shoes are all performed, in that order. Otherwise all these events are canceled.

Transactions are required to satisfy the following four ACID properties.

Atomicity: Either all events of a transaction take effect or none of them.   
Consistency: If a transaction commits, the result is a valid configuration of the system.   
Isolation: Intermediate effects of a transaction remain invisible to others as long as it has not committed. Durability: Once a transaction has committed, its effects are permanent.

These properties are supposed to hold even if some of the processes crash; this is especially relevant for atomicity and durability. If a participant in an ongoing transaction crashes, then in principle the transaction is aborted, unless it is being committed at the moment of the crash (see section 16.2). When a process crashes, typically a fresh process is started to take over its role. The Peterson-Kearns checkpointing and rollback recovery algorithm from section 3.3 can be used to resume execution after a crash. It is assumed that each process $p$ has stable storage at its disposal, which remains accessible for the other processes in a consistent state even after $p$ has crashed.

Transactions can be nested, meaning that inside a transaction other subtransactions are started, which may be run by different processes. If a subtransaction commits, this is only provisional, in the sense that if the overall transaction aborts, then all its subtransactions are aborted as well. If a subtransaction aborts, the overall transaction is not forced to abort but may, for instance, initiate an alternative subtransaction. Another positive aspect of nested transactions is that they allow for additional concurrency. For simplicity, the techniques for distributed transactions discussed in this chapter focus on so-called flat transactions that do not contain any nesting, but they can all be lifted to nested transactions.

We consider distributed transactions in the context of (distributed) shared memory, in which different processes can read or write to the same variables. We note that these operations in shared memory can be emulated in a message passing framework.

# 16.1 Serialization

Each execution of multiple concurrent transactions should be serializable, meaning that each configuration equals the outcome of a sequential execution of the committed transactions in the order in which they commit. Here sequential means that the committed transactions appear not to overlap in time. In particular, transactions should always read values of variables in line with the order in which transactions commit. A key challenge is to avoid synchronization conflicts between concurrent transactions. Such a conflict may occur if one transaction writes to a variable in shared memory while concurrently another transaction reads or also writes to this variable. Ignoring such synchronization conflicts would give rise to two problems, which occur if a read operation by a transaction returns a wrong (typically, stale) value.

Lost update: A write by a committed transaction may mistakenly be ignored by a transaction that commits later. Suppose, for example, that one transaction wants to add $\notin 1 0$ and a second transaction $\notin 2 0$ to the same bank account. Both transactions read the current balance of the account, $\notin 5 0$ . Next, the first transaction writes $\notin 6 0$ as the new value of the account and commits. Finally, the second transaction writes $\yen 70$ as the new value of the account and commits. The final result is that only $\notin 2 0$ has been added to the account instead of $\notin 3 0$ .   
Inconsistent retrievals: A transaction may read inconsistent values because of writes by a concurrent transaction. For example, suppose one transaction wants to move $\notin 1 0$ from one bank account to another, while a second transaction wants to compute the sum of both accounts. The first transaction reads the balance of one of the accounts and subtracts $\notin 1 0$ from it. Next, the second transaction reads the values of both accounts, computes their sum, and commits. Finally, the first transaction reads the balance of the second account, adds $\notin 1 0$ to it, and commits. The sum of the two accounts computed by the second transaction misses out on $\notin 1 0$ .

Concurrent transactions that perform only reads to the same variable do not constitute a synchronization conflict. Now three different methods are discussed to enforce serializable transactions: locks, time stamps, and an optimistic approach in which a transaction only worries about synchronization conflicts at the end. Instead of detailed algorithmic descriptions, it is explained at a more abstract level what the methods aim to achieve.

# Two-Phase Locking

A straightforward way to achieve serialization, applied often in practice, is through the use of locks with regard to variables in shared memory on which synchronization conflicts may occur. Basically, locking enforces an ordering on concurrent transactions that may give rise to synchronization conflicts; the transaction that obtains a lock on a contested memory object first is the one that goes first in the serialization order. A distinction can be made between read and write locks. Multiple transactions may concurrently obtain the same read lock, because concurrent read operations do not constitute a synchronization conflict. However, while a write lock is granted to a transaction, no other transaction is allowed to hold this write lock or the corresponding read lock. In particular, a read lock may only be promoted to a write lock after all other granted claims on this read lock have been lifted. To guarantee a correct serialization, it is essential that after a transaction has released a lock, it will no longer claim locks. Therefore, the two-phase locking scheme consists of a growing phase, in which locks are accumulated, and a subsequent shrinking phase, in which the acquired locks are released. A transaction can release its read locks early on in the shrinking phase, but its write locks can only be released after the transaction has committed or aborted, because up to that point it remains unclear whether its written values will take effect. When a write lock is released, the corresponding variable carries either the written value if the transaction committed or its original value if the transaction aborted.

The locking approach has several drawbacks. First of all, a deadlock can occur if two concurrent transactions need to obtain the same two locks and request these locks in opposite orders. In that case, both transactions may succeed in obtaining one of the locks but will then never obtain the other lock. Such deadlocks can be avoided either by prudent lock management, which inevitably has a negative impact on performance, or by a deadlock detection scheme using wait-for graphs, as explained in chapter 5, and aborting transactions if a deadlock is detected. A second drawback is that locking tends to impose a considerable performance penalty because of the overhead of lock management and the reduction in concurrency, which is aggravated by the fact that in two-phase locking locks can only be released after the growing phase. Note that if a process crashes while it is involved in a transaction holding a lock, then the lock can only be released after the corresponding transaction has been aborted or another process has resumed the execution of the crashed process.

Example 16.1 We revisit the scenario from the explanation of lost updates. If both transactions concurrently obtain the read lock of the bank account, then a deadlock ensues because both transactions are incapable of getting the write lock of the account. Either this deadlock must be resolved after the fact or prudent lock management disallows the transactions concurrent access to the read lock. In the latter case, one of the transactions obtains the read lock, promotes it to a write lock, adds its amount to the account, commits, and releases the write lock. Next, the other transaction can perform this same sequence of events. At the end, the balance of the account has increased from $\notin 5 0$ to $\notin 8 0$ by adding $\notin 1 0$ and $\notin 2 0$ in some sequential order.

# Premature Writes and Dirty Reads

We now discuss two alternative approaches for serializing transactions that do not use locks. Next to lost updates and inconsistent retrievals, two other possible problems related to aborted transactions need to be avoided.

Premature write: A write to a variable $x$ by a transaction that commits may be obliterated by a concurrent transaction that wrote to $x$ earlier, aborts, and resets the value of $x$ . Suppose, for example, that one transaction wants to add $\notin 1 0$ and a second transaction wants to add $\notin 2 0$ to the same bank account. Both transactions read the current balance of the account, $\notin 5 0$ . Next, the first transaction writes $\notin 6 0$ as the new value of the account. Now the second transaction writes $\yen 70$ as the new value of the account and commits. Finally, the first transaction aborts and resets the balance to $\notin 5 0$ . The final result is that no money has been added to the account instead of $\notin 2 0$ .

Dirty read: A transaction may read a value that was written by a concurrent transaction that eventually aborts. Suppose once again that one transaction wants to add $\notin 1 0$ and a second transaction wants to add $\notin 2 0$ to the same bank account. The first transaction reads the current balance of the account, $\notin 5 0$ , and writes $\notin 6 0$ as the new value of the account. Next, the second transaction reads $\notin 6 0$ as the value of the account. Now the first transaction aborts and resets the balance to $\notin 5 0$ . Finally, the second transaction writes $\notin 8 0$ as the new value of the account and commits. The final result is that $\notin 3 0$ has been added to the account instead of $\notin 2 0$ .

Premature writes and dirty reads are evaded by letting transactions perform tentative writes on local variables instead of in shared memory. We discuss two lockless approaches to avoid that transactions read stale values.

# Time Stamps

One approach to achieve a proper serialization is through time stamps. Each transaction is furnished with a unique time stamp from a totally ordered domain, typically the time of a clock at the moment of its instantiation. Committed transactions are serialized according to their time stamps. A transaction cannot commit as long as there are ongoing transactions with a smaller time stamp. Transactions tentatively perform write operations on local copies of variables, which become definite only when the transaction commits. Each (tentative) read or write operation is immediately visible to all other ongoing transactions. Consider a read operation by a transaction $T$ with time stamp $t$ on variable $x .$ If $T$ wrote to $x$ earlier, then the read operation simply returns the last value $T$ wrote to $x$ . If $T$ did not yet write to $x _ { \ast }$ , then this read operation is delayed while there are ongoing transactions with time stamps smaller than $t$ that wrote to $x$ . When there are no such transactions anymore, the read operation returns the last value written to $x$ by a committed transaction with a time stamp smaller than $t$ (or the original value of $x$ if no such transaction wrote to $x$ ).

Now consider a write operation by transaction $T$ on variable $x$ . This operation is performed only if no extant transaction with a time stamp greater than $t$ read $x$ . The write is therefore first checked against all ongoing transactions with a time stamp greater than $t$ . For this purpose, before a transaction starts, it is first announced at all ongoing transactions. If an extant transaction with a time stamp greater than $t$ read $x$ , then $T$ must abort. Else the write operation can be (tentatively) performed.

Premature writes cannot occur because transactions perform tentative writes on local copies of variables, so aborted transactions do not obliterate values written by other transactions. Dirty reads cannot occur because reads always return a value written by a committed or the same transaction. Lost updates cannot occur because (1) a transaction can only read a variable when all transactions with a smaller time stamp that wrote to this variable have either committed or aborted, and (2) after a transaction read a variable, ongoing transactions with a smaller time stamp cannot write to this variable anymore. And inconsistent retrievals cannot occur because (1) lost updates cannot happen, so a transaction takes into account all writes by committed transactions with a smaller time stamp, and (2) a transaction never takes into account writes by (ongoing) transactions with a greater time stamp.

Example 16.2 We again revisit the scenario from the explanation of lost updates. Let the first and second transactions have time stamps $t _ { 1 }$ and $t _ { 2 }$ , respectively, with $t _ { 1 } < t _ { 2 }$ . The two transactions both read the balance, $\notin 5 0$ , of the bank account $^ b$ <. The first transaction is disallowed to add $\notin 1 0$ to the account and aborts, in view of the read by the second transaction and $t _ { 1 } < t _ { 2 }$ . The second transaction changes the balance of the account to $\yen 70$ and commits.

Another lockless serialization approach is by means of optimistic concurrency control. The underlying assumption is that the chance a synchronization conflict occurs is low. Therefore, a transaction is allowed to perform reads and tentative writes without worrying about such conflicts. Only at the end of the transaction is it validated whether indeed no synchronization conflicts have occurred.

To avoid dirty reads, a transaction $T _ { 1 }$ that has read a value written by another ongoing transaction $T _ { 2 }$ cannot commit until $T _ { 2 }$ has committed. If $T _ { 2 }$ eventually aborts, then $T _ { 1 }$ must also abort. This may in turn lead to aborts of other transactions that read values written by $T _ { 1 }$ . These are called cascading aborts, which can be avoided by requiring that a transaction only be allowed to read values that were written by committed transactions. A transaction that wants to read a value written by an ongoing transaction must then delay this read until the other transaction has committed or aborted.

A more effective approach is to let a transaction copy memory objects to a private workspace at the start. The workspace consists of local memory at the processes involved in the transaction that is only accessible by this transaction. During its working phase, a transaction performs reads and writes on this private workspace. If in the end the transaction commits, then before doing so the updates in its private workspace are copied to shared memory. If the transaction aborts, then these updates remain invisible to the other transactions. Since writes are not rolled back by aborted transactions and all reads are performed with regard to committed values of variables, premature writes and dirty reads are precluded.

To avoid lost updates, after its working phase, a transaction enters a validation phase to determine whether it erroneously used stale values. At the start of this phase, the transaction is assigned a unique sequence number; these numbers are issued in ascending order and represent the order in which transactions are serialized. A transaction can only commit when all transactions with a smaller sequence number have aborted or committed. The advantage of assigning a sequence number to a transaction at the start of its validation instead of before its working phase is that a transaction with a long working phase does not delay transactions that start later but complete much earlier than this transaction.

A transaction $T$ at the start, before copying memory objects to its private workspace, stores the sequence number $k$ of the transaction that was the last to commit. After having been assigned a sequence number $\ell > k$ itself, $T$ can perform its validation phase when all transactions with a smaller sequence number than $\ell$ have ℓeither aborted or committed (and in the latter case, made all written values visible to the other transactions). Then $T$ checks whether each variable it read (in its private workspace) during its working phase was (1) not written to by a committed transaction with a sequence number between $k$ and $\ell$ , or (2) written to by $T$ before this read. If so, then $T$ commits; if not, then $T$ ℓaborts because it used stale values of variables with regard to the serialization order. This technique to determine and avoid synchronization conflicts is called backward validation, as opposed to the alternative forward validation technique, in which a transaction checks whether the variables it wrote to were read by overlapping active transactions. Backward validation requires the write operations by a committed transaction $T$ to be archived until all transactions concurrent to $T$ have completed their validation phases.

Finally, if its validation phase concludes positively with a commit, then in a subsequent update phase a transaction makes all its written values visible to the other transactions by copying them from its private workspace to shared memory.

Example 16.3 We again revisit the scenario from the explanation of lost updates. Let both transactions store the same highest sequence number $k$ of any committed transaction so far. Next, they both copy the value $\notin 5 0$ of the bank account to their private workspaces. The first and second transactions concurrently read this value and write $\notin 6 0$ and $\yen 70$ , respectively, in their private workspaces as the new value of the account. The first and second transactions proceed to their validation phases, where they are assigned sequence numbers $k + 1$ and $k + 2$ , respectively. Validation of the first transaction succeeds, so it commits and copies the value $\notin 6 0$ from its private workspace to shared memory. Now validation of the second transaction fails because the first transaction has a sequence number between $k$ and $k + 2$ and it wrote a value to the bank account, while the second transaction read the value of the bank account (before writing to it).

With optimistic concurrency control, again premature writes cannot occur because transactions perform tentative writes on local copies of variables, so aborted transactions do not obliterate values written by other transactions. Dirty reads cannot occur because transactions make local copies of committed values when they start. Finally, lost updates and inconsistent retrievals cannot occur owing to the validation phase.

Time stamps and the optimistic approach avoid the reduction in concurrency and overhead of lock management and do not suffer from deadlock. But read operations may still be delayed, and a surge of synchronization conflicts may lead to a massive abortion of transactions.

# 16.2 Two- and Three-Phase Commit Protocols

A distributed transaction is initiated by a process called the coordinator of this transaction, while the other processes involved in the transaction are called cohorts. A transaction is started by the coordinator sending a request to all cohorts. In the end, it is up to the coordinator to decide whether the transaction can be committed or should be aborted. First, we discuss the two-phase commit protocol. It employs a unanimous voting scheme: the coordinator commits the transaction if and only if all participants in the transaction vote to do so. In the context of databases, next to a synchronization conflict, another ground for a process to vote for (and thus enforce) abortion of a transaction is if it detects that the transaction causes a resource deadlock (see section 5.1).

Each participant in the transaction locally keeps track of updates it makes to data values during the transaction. The old and new values are both kept, so that the process can stick to the old values or move to the new values if the transaction aborts or commits, respectively. In view of the isolation property, as long as the transaction has not been committed, the new values must remain invisible to others.

In the voting phase, the coordinator asks each participant in the transaction (including itself) whether it agrees to commit the transaction. Each participant replies with either a yes vote, if all its events during the transaction succeeded, or a no vote, if it experienced an obstruction that makes it impossible to commit. Before replying with a yes vote, a process must make sure that its tentative changes for the transaction have been copied to stable storage, to be able to cope with a crash of the process while the coordinator decides to commit the transaction. After casting its vote, each process blocks until it receives either a commit or an abort message from the coordinator. The coordinator waits for votes from all participants to start the completion phase. If all participants vote yes, then the coordinator sends a commit message to all cohorts; if, on the other hand, at least one of the participants votes no, then the coordinator broadcasts an abort message.

If a commit message is received, a cohort makes the effects of its events during the transaction visible to others, annihilating the old values. If an abort message is received, a cohort annihilates the effects of its events during the transaction, which means it rolls back to the old values. In both cases, cohorts release the resources they held during the transaction and send an acknowledgment to the coordinator. The coordinator completes the transaction, and in case of a commit makes the effects of its events during the transaction visible, when acknowledgments have been received from all cohorts.

To cope with crashed processes, we assume there is a complete and strongly accurate failure detector. As explained in section 12.3, such a failure detector can be implemented using a timeout mechanism if there is a known upper bound on network latency and processes regularly send a heartbeat message. In the voting phase, if the coordinator detects that a cohort has crashed before casting its vote, then this counts as a no vote. In the completion phase, if the coordinator broadcasts a commit message and finds that a cohort has crashed, then it needs to be ensured that the effects of the transaction at the crashed process are made visible and permanent before the transaction can be completed. This is possible because the crashed process must have copied its written values during the transaction to stable storage, clearly marked, before replying with a yes.

The Achilles’ heel of the two-phase commit protocol is that the coordinator may crash at the end of the voting or at the start of the completion phase, especially if a cohort crashes concurrently. It might be the case that the coordinator sent a commit or abort message only to the crashed cohort, which before crashing made the effects of the transaction visible or undid these effects irrevocably, respectively. Even after a new coordinator has been put in place, the cohorts must still reach agreement on whether the transaction should be committed. Until this agreement has been reached, the cohorts are blocked.

The three-phase commit protocol eliminates this problem by introducing an intermediate precommit phase, which the coordinator enters after receiving a yes from all participants. Instead of immediately broadcasting a commit, it first sends a precommit message to all participants, informing them of the intention to commit the transaction. Upon receipt of this message, each participant replies with an ack message. After receiving this reply from all participants, the coordinator finally broadcasts a commit and proceeds as in the two-phase commit protocol. If a cohort crashes before sending an ack, the coordinator can still decide to commit the transaction. Then the recovery protocol must make sure that the process replacing the crashed cohort will eventually take care of properly completing its part of the transaction.

Suppose the coordinator crashes during the precommit phase. If at least one live cohort received a precommit message, then the cohorts can choose to commit the transaction because all participants in the transaction voted yes. The processes replacing the crashed coordinator or crashed cohorts will then eventually take care that their parts of the transaction will be made visible and permanent as well. If on the other hand not all live cohorts replied with an ack to a precommit message, then the cohorts can safely abort the transaction, because it is guaranteed that no participant in the transaction yet made visible its written values during the transaction.

# 16.3 Transactional Memory

In chapter 14 it was explained that locks tend to play a key role in coping with concurrency in the presence of shared memory. However, as already discussed in section 16.1, they have some serious disadvantages. They can become a performance bottleneck if multiple processes want to concurrently obtain the same lock. A deadlock may occur if two processes need to claim the same two locks and obtain them in opposite orders. And if a process crashes while holding the lock, this needs to be resolved before the lock can be released. Last but not least, it turns out that in the development of large software systems, locks are vulnerable to design errors, because the intended relation between a lock and the data it protects remains implicit. Readmodify-write operations do not really come to the rescue, because they, too, impose a performance penalty and are delicate to use. Furthermore, they operate on a single variable, while designing a concurrent computer program would become much simpler if one could perform multiple read and write operations on different variables in one atomic step.

Transactional memory is a concurrent programming paradigm inspired by the transactions explained in the first part of this chapter. The idea is that a sequence of events executed by a single process can be declared a transaction, in which case these steps either commit and take effect in one atomic step or are aborted and do not take effect. In the latter case, the transaction is often retried later. A transaction may be aborted by another transaction if a synchronization conflict arises between these two transactions. For example, a process may try to move the head of one queue to the tail of another queue in one atomic step. To do this, it tentatively performs a dequeue to the first queue followed by an enqueue to the second queue, within one transaction. If no conflicting operation by another transaction is performed to these queues in the meantime, these two operations are made visible to the other processes in one atomic step.

Transactions may be nested in the sense that a transaction may start a subtransaction. However, for sim plicity, we again restrict the discussion to flat transactions, disregarding nesting.

As explained in section 2.3, at the hardware level, a cache buffers writes that were performed but still need to be transferred to main memory. A cache coherence protocol, such as the MSI protocol described in section 2.3, takes care of most of the work needed to support transactions: its main purpose is to detect and resolve synchronization conflicts. Hardware transactional memory adds a transactional bit to each cache line. If a value is written in a cache line on behalf of a transaction, the transactional bit of this line is set. If such a so-called transactional line is invalidated before the transaction has committed, then the transaction aborts, meaning that all transactional lines in the corresponding cache are invalidated. If, on the other hand, the transaction in the end commits, then simply all its transactional bits are set, so the corresponding transactional lines become permanent.

Hardware transactional memory exploits a cache coherence protocol in an effective way but does have some serious drawbacks. The size of a transaction is limited by the size of the cache, which tends to be relatively small. Because of the granularity of cache lines, transactions can suffer from false sharing. In particular, care must be taken that a transaction does not abort itself if it happens to write twice to the same cache line. And transactions can starve each other by repeatedly aborting another process, being aborted by another process, and restarting. In spite of these weak points, Intel’s TSX provides widely used hardware transactional memory support.

Software transactional memory implements transactions at the software level. The idea is that the status of a transaction is maintained in a field that initially is ACTIVE and ultimately is changed either to COMMIT or to ABORT. A transaction can try to commit by applying compare-and-set(ACTIVE COMMIT) to its own ,status field, or it can try to abort another transaction by applying compare-and-set(ACTIVE ABORT) to that ,transaction’s status field. The use of the compare-and-set operation is vital in case a transaction tries to commit while concurrently another transaction tries to abort this transaction. Since the check whether the status field is ACTIVE and its change to COMMIT or ABORT is performed in one atomic step, only one of these concurrent operations can succeed.

Each memory object $x$ carries a pointer to the transaction $T$ that performed the last write to it. Two values for $x$ are maintained: the new one written by $T$ and the old one before this write. While $T$ is in ACTIVE, the value of $x$ is undecided. If $T$ is in COMMIT, the new value is the current value of $x$ and the old value is obsolete. If, on the other hand, $T$ is in ABORT, the old value is the current value of $x$ and the new value is obsolete. When another transaction $\hat { T }$ reads $x .$ , it can see from $T$ ’s status which value of $x$ it should consider. If this status is ACTIVE, then $\hat { T }$ observes a synchronization conflict, in which case it either waits for $T$ to complete or performs compare-and-set(ACTIVE ABORT) to $T$ ’s status field. When another transaction $\hat { T }$ writes to $x _ { \ast }$ ,, it prepares a new object pointing to the ACTIVE status field of $\hat { T }$ . If $T$ ’s status is COMMIT, then in $\hat { T }$ ’s object its new value is a copy of the new value of $x$ and its old value points to the new value of $x$ in $T$ ’s object. Next, $\hat { T }$ applies a compare-and-set to try and swing $x ^ { \mathrm { { ' } } }$ ’s pointer from $T$ ’s object to the object $\hat { T }$ has prepared, so that all changes take effect in one atomic step. This can be depicted as follows.

![](images/d4ce3e8f24b34d30fce709ba181e75d2bf26105d51025d7e728def76d3c03d25.jpg)

Similarly, if $T$ ’s status is ABORT, then in $\hat { T }$ ’s object its new value is a copy of the old value of $x$ and its old value points to the old value of $x$ in $T$ ’s object.

![](images/67bb44fea0f4eccd7589dfafbf49178c920d9e3df70b907824e0a432c1466d10.jpg)

If $T$ ’s status is ACTIVE, then again $\hat { T }$ observes a synchronization conflict and acts accordingly.

There are different policies regarding the circumstances under which a transaction is allowed to abort another conflicting transaction. One could, for instance, provide transactions with a time stamp or keep track of the amount of work they have performed so far, and give precedence to transactions with an older time stamp or that have done more work.

An active transaction must take care that it does not encounter an inconsistent state. For example, let a transaction $T _ { 1 }$ read $x$ , then another transaction $T _ { 2 }$ writes to $x$ and $y$ and commits, and finally $T _ { 1 }$ reads $y$ . Then $T _ { 1 }$ may enter a state in which the combination of values of $x$ and $y$ is inconsistent. This is dangerous because it could for instance cause $T _ { 1 }$ to spuriously enter an infinite loop or divide by zero, which could derail the entire computation. To avoid such situations, each transaction keeps a log of its reads and must after every read and before it commits check that the values it has read before have not been changed by another transaction. If one of these values did change, it must immediately abort itself by writing ABORT in its status field. In the aforementioned example, $T _ { 1 }$ would find after reading $y$ that another transaction has written to $x$ , causing $T _ { 1 }$ to abort.

Example 16.4 We revisit the scenario from the explanation of lost updates in section 16.1 for the last time, in the context of software transactional memory. Both transactions concurrently read the value $\notin 5 0$ of the bank account. The first transaction tentatively writes $\notin 6 0$ as the new value of the account and commits, making this new value permanent. The second transaction tentatively tries to write $\yen 70$ as the new value of the account, but this fails because of the earlier write by the first transaction. The second transaction therefore aborts and restarts.

A general drawback of the transactional memory paradigm is that it cannot cope well with output a transaction may want to send to a remote process or the environment, since this cannot be rolled back if the transaction aborts. One approach is to buffer such output until the transaction has completed, which works only if no immediate input is required in reply to the output. Another approach is that at any time at most one privileged transaction is guaranteed to commit and can freely perform output operations. In any case, only a very limited amount of output by transactions is possible in a transactional memory setting.

# Bibliographical notes

The ACID properties were put forward in [51], and serializability is due to [40]. The time stamp ordering for transactions was introduced in [14], and optimistic concurrency control stems from [64]. The two-phase commit protocol appeared in [50], and the three-phase commit protocol is found in [109]. Hardware transactional memory was proposed in [54] and software transactional memory in [108].10

# 16.4 Exercises

Exercise 16.1 Let transactions $T _ { 1 }$ and $T _ { 2 }$ execute the sequences of events $r e a d ( x ) ; w r i t e ( y ) ; w r i t e ( x )$ and $r e a d ( y ) ; w r i t e ( y ) ; w r i t e ( x )$ , respectively, for some variables $x$ and $y$ . Give three different interleavings of the executions of $T _ { 1 }$ and $T _ { 2 }$ for which $T _ { 1 }$ can be serialized before $T _ { 2 }$ . How many interleavings exist for which $T _ { 2 }$ can be serialized before $T _ { 1 }$ ?

Exercise 16.2 Give examples to show how two-phase locking, the time stamp ordering, optimistic concurrency control, and software transactional memory deal with the scenario regarding a bank account in the explanation of inconsistent retrievals.

Exercise 16.3 Give examples to show that the following two relaxations of two-phase locking could lead to a violation of serializability.

(a) A transaction is allowed to claim a read lock after it has released a read lock.   
(b) A transaction is allowed to release a write lock before it commits.

Exercise 16.4 Give examples to show how the time stamp ordering, optimistic concurrency control, and software transactional memory deal with the scenario regarding a bank account in the explanation of dirty reads.

Exercise 16.5 In the two lockless serialization approaches for transactions, based on time stamps and on optimistic concurrency control, why can a write operation by an ongoing transaction disregard write operations to the same variable by concurrent transactions?

Exercise 16.6 In the time stamp ordering approach for transactions, suppose transaction $T _ { 1 }$ wants to perform a write on a variable, but finds that another ongoing transaction $T _ { 2 }$ that comes later in the serialization order read this same variable. Explain why it would be a bad idea, instead of aborting $T _ { 1 }$ immediately, to let $T _ { 1 }$ wait to see whether $T _ { 2 }$ will maybe abort, in which case $T _ { 1 }$ could still perform the write.

Exercise 16.7 In the time stamp ordering approach for transactions, suppose (only) two transactions $T _ { 1 }$ and $T _ { 2 }$ start concurrently, with time stamps $t _ { 1 }$ and $t _ { 2 }$ , respectively. Variable $x$ initially contains the value $\notin 1 0$ . Transaction $T _ { 1 }$ writes the value $\notin 3 0$ to $x$ and then reads $x$ , while $T _ { 2 }$ reads $x$ and then increases its value by $\notin 1 0$ .

(a) Explain for all possible interleavings of the events of $T _ { 1 }$ and $T _ { 2 }$ which read is delayed or which write leads to an abort. Distinguish two possible cases: $t _ { 1 } < t _ { 2 }$ and $t _ { 2 } < t _ { 1 }$ .   
(b) Explain why in the case $t _ { 2 } < t _ { 1 }$ , aborts by $T _ { 2 }$ < <are spurious. Propose an optimization of the time stamp ordering approach that avoids these aborts.

Exercise 16.8 Consider the optimistic concurrency control approach. Let transactions $T _ { 1 }$ and $T _ { 2 }$ from the previous exercise at their start store the same sequence number of the last committed transaction. Explain whether $T _ { 1 }$ and $T _ { 2 }$ commit or abort. Distinguish two possible cases: the sequence number of $T _ { 1 }$ is smaller or greater than the sequence number of $T _ { 2 }$ .

Exercise 16.9 Consider a distributed transaction with one coordinator and three cohorts. Give two computations of the two-phase commit protocol in which crashed processes must resume their execution before agreement can be reached on whether the transaction commits. One computation in which a cohort committed its changes and another computation in this cohort rolled back its changes, right before it crashed. Also show how these two computations could proceed in the case of the three-phase commit protocol.

Exercise 16.10 In the voting phase of the two-phase commit protocol, why must participants in a distributed transaction copy the tentative changes they made during the transaction to stable storage right before and not right after sending yes to the coordinator?

Exercise 16.11 In the two-phase commit protocol, let only the coordinator crash, right between the voting and the completion phases. Why can the cohorts safely abort the transaction? You may assume there is a known upper bound on network latency.

Exercise 16.12 Explain how the two-phase commit protocol can be extended to nested transactions.

Exercise 16.13 In the three-phase commit protocol, why is there no need for a preabort phase in case one or more participants in a distributed transaction vote no?

Exercise 16.14 [50] Two divisions of an army are camped on separate hilltops overlooking a valley where their enemy is located. Their generals can only communicate with each other through messengers that may be captured by the enemy. Argue that no communication protocol can guarantee both divisions will attack at exactly the same moment in time.

Exercise 16.15 In software transactional memory, why is it unnecessary for an active transaction to check whether the values it has written to are unchanged?

Exercise 16.16 In software transactional memory, why can a transaction abort itself by simply writing ABORT in it status field (instead of applying a compare-and-set)?

Exercise 16.17 In software transactional memory, how can a transaction proceed if it performs a read or write that constitutes a synchronization conflict with itself?

# Self-Stabilization

A distributed algorithm is self-stabilizing if it will always end up in a correct configuration, even if it is initialized in an incorrect (unreachable) configuration. A strong advantage of self-stabilization is that it provides fault tolerance even in circumstances where the system is forced into an incorrect configuration by an unanticipated event due to, for example, a fault that was not anticipated in the design of the algorithm or a malicious intruder. Self-stabilization can offer an attractive solution if failures are infrequent and a temporary malfunction is acceptable, as is often the case in operating systems and database systems. An important requirement is that failures be resolved within a relatively short period of time.

Self-stabilizing algorithms are generally presented in a shared-memory framework. The reason is that in a message-passing framework, all processes might be initialized in a state in which they are waiting for a message to arrive, in which case the network would exhibit no behavior at all. In shared memory, processes may take into account the values of multi-reader variables at their neighbors, in which case such deadlocks can be avoided. We assume that local variables at the processes are single-writer registers and that processes can read values of variables at their neighbors.

We will discuss a self-stabilizing algorithms for mutual exclusion, where initially multiple processes may be privileged. We will moreover discuss two self-stabilizing algorithms for computing a spanning tree, where initially there may, for instance, be a cycle in the spanning tree. Such a spanning tree construction serves as a cornerstone for several other self-stabilizing algorithms in the literature, for example, to compute a snapshot or to elect a leader. The algorithms assume that process IDs are never affected by e.g. hardware errors.

# 17.1 Dijkstra’s Token Ring for Mutual Exclusion

Dijkstra’s self-stabilizing token ring for mutual exclusion presupposes a directed ring of processes $p _ { 0 } , . . . , p _ { N - 1 }$ . It is assumed that processes do not crash and the network topology remains stable. Each process $p _ { i }$ . . ,holds a register $x _ { i }$ with values in $\{ 0 , . . . , K - 1 \}$ , where $K \geq N$ ; process $p _ { i }$ can read the value of the register at its predecessor $p _ { ( i - 1 ) }$ mod $N$ , . . . ,in the ring. Recall that at any moment in time, at most one process can consider itself privileged and enter its critical section (see chapter 14). The privileged processes are defined as follows:

• $p _ { i }$ for $i = 1 , \ldots , N - 1$ is privileged if $x _ { i } \neq x _ { i - 1 }$ .

• $p _ { 0 }$ is privileged if $x _ { 0 } = x _ { N - 1 }$ .

Since Dijkstra’s token ring can be initialized in any configuration, there can be multiple privileged processes at the start (if $N \geq 3$ ).

In Dijkstra’s token ring, each privileged process is allowed to change its value, causing the loss of its privilege.

• $p _ { i }$ can perform $x _ { i } \gets x _ { i - 1 }$ if $x _ { i } \neq x _ { i - 1 }$ , for any $i = 1 , \ldots , N - 1$ . $p _ { 0 }$ can perform $x _ { 0 } \gets ( x _ { 0 } + 1 )$ mod $K$ if $x _ { 0 } = x _ { N - 1 }$ ,.

Example 17.1 Consider a ring of size 3 with $K = 3$ . Initially, each process has the value 0, so only process $p _ { 0 }$ is privileged. Then $p _ { 0 }$ can pass on the privilege to $p _ { 1 }$ by setting $x _ { 0 }$ to 1. Next, $p _ { 1 }$ can pass on the privilege to $p _ { 2 }$ by setting $x _ { 1 }$ to 1. Now $p _ { 2 }$ can pass on the privilege to $p _ { 0 }$ by setting $x _ { 2 }$ to 1, and so on.

Always at least one process is privileged. That is, if $p _ { 1 } , . . . , p _ { N - 1 }$ are not privileged, then clearly the registers $x _ { 0 } , \ldots , x _ { N - 1 }$ all contain the same value. But then $p _ { 0 }$ , . . . ,is privileged because $x _ { 0 } = x _ { N - 1 }$ . Furthermore, , . . . ,an event at a process $p _ { i }$ never increases the number of privileged processes, because $p _ { i }$ loses its privilege, and the event can at most cause $p _ { i }$ ’s successor $p _ { ( i + 1 ) }$ mod $N$ in the ring to become privileged. So if the initial configuration is correct, in the sense that only one process is privileged, then mutual exclusion is guaranteed.

Example 17.2 Let $N = K = 4$ , and consider the following initial configuration.

![](images/40466719dd279d2c7c9416c858f017b9d72bbe67073280ed0cc9d65659504656.jpg)

Initially, $p _ { 1 } , p _ { 2 }$ , and $p _ { 3 }$ are privileged. Each computation will eventually lead to a configuration in which only one process is privileged. The value at $p _ { 0 }$ is different from the values at $p _ { 1 } , p _ { 2 }$ , and $p _ { 3 }$ . In the proof of theorem 17.1, it will be argued that in each infinite computation, $p _ { 0 }$ must eventually perform an event. The only way $p _ { 0 }$ can perform an event is if the register at $p _ { 3 }$ attains the value 0. This can happen only if first the register at $p _ { 2 }$ attains this value. And in turn this can happen only if first the register at $p _ { 1 }$ attains the value 0. Then the registers at $p _ { 1 } , p _ { 2 }$ , and $p _ { 3 }$ have attained the value 0, so only $p _ { 0 }$ is privileged.

For instance, first $x _ { 3 } \gets 1$ ; next $x _ { 2 } \gets 3$ and $x _ { 3 } \gets 3$ ; and finally $x _ { 1 } \gets 0$ , $x _ { 2 } \gets 0$ , and $x _ { 3 } \gets 0$ . Now only $p _ { 0 }$ is privileged.

Theorem 17.1 If $K \geq N$ , then Dijkstra’s token ring for mutual exclusion always eventually reaches a correct configuration, in which starvation-free mutual exclusion is guaranteed.

Proof. Since always at least one process is privileged and each privileged process can perform an event, all computations are infinite.

Consider a computation. We need to argue that eventually a configuration is reached in which only one process is privileged. The longest possible sequence of transitions without an event at $p _ { 0 }$ consists of $\frac { 1 } { 2 } \cdot ( N -$ $1 ) \cdot N$ events at $p _ { 1 } , . . . , p _ { N - 1 }$ : one event at $p _ { 1 }$ (copying $p _ { 0 }$ ’s value), two events at $p _ { 2 }$ (copying $p _ { 1 }$ ’s first and , . . . ,second values), and so on, up to $N - 1$ events at $p _ { N - 1 }$ . So the infinite computation involves infinitely many events at $p _ { 0 }$ . At each such event, $p _ { 0 }$ increases its value by 1 modulo $K$ , so during the computation, $x _ { 0 }$ ranges over all values in $\{ 0 , . . . , K - 1 \}$ . Initially, at least one of those values is not present at $p _ { 1 } , . . . , p _ { N - 1 }$ , because $K \geq N$ , . . . , , . . . ,. Since these processes only copy values from their predecessors, it follows that in some configuration of the computation, $x _ { 0 } \neq x _ { i }$ for all $i = 1 , \ldots , N - 1$ . The next time $p _ { 0 }$ becomes privileged, when $x _ { N - 1 } = x _ { 0 }$ , clearly $x _ { i } = x _ { 0 }$ for all $i = 1 , \ldots , N - 1$ , . . . ,. Then only $p _ { 0 }$ is privileged, so mutual exclusion has been achieved.

, . . . ,Starvation-freeness follows from the fact that in each correct configuration, the privileged process will pass on the privilege to its successor (if $N \geq 2$ ). ⊓⊔

For $N \geq 3$ , theorem 17.1 also holds if $K = N - 1$ . (If $N = 2$ and $K = 1$ , starvation-freeness is violated.) Let us revisit the argumentation in the proof of theorem 17.1. When $p _ { N - 1 }$ copies the value from $p _ { N - 2 }$ , the processes $p _ { 1 } , . . . , p _ { N - 1 }$ hold at most $N - 2$ different values (because $N \geq 3$ ). Since $p _ { 1 } , . . . , p _ { N - 1 }$ only copy , . . . ,values, they are then restricted to these $N - 2$ values, as long as the value of $x _ { 0 }$ , . . . ,is also among these $N - 2$ values. Since $K \geq N - 1$ , and in an infinite computation $p _ { 0 }$ performs infinitely many events, it follows that in some configuration of the computation, $x _ { 0 } \neq x _ { i }$ for all $i = 1 , \ldots , N - 1 .$ . The next time $p _ { 0 }$ becomes privileged, $x _ { i } = x _ { 0 }$ for all $i = 1 , \ldots , N - 1 .$ . Then only $p _ { 0 }$ is privileged.

The value $K = N - 1$ is sharp; the next example shows that if $K = N - 2$ , then there are infinite computations in which mutual exclusion is never achieved.

Example 17.3 Let $N \geq 4$ and $K = N - 2$ , and consider the following initial configuration.

![](images/cde0b49e488fb65b028910dab7f297bdb9b0e6addc09419ae2c4c123f4f7bf21.jpg)

In this configuration, only $p _ { 1 }$ is not privileged. We consider one possible computation of Dijkstra’s token ring. First, $p _ { 0 }$ sets $x _ { 0 }$ to $\left( \left( N - 3 \right) + 1 \right)$ mod $( N - 2 ) = 0$ . Next, $p _ { N - 1 }$ sets $x _ { N - 1 }$ to 0. Then, $p _ { N - 2 }$ sets $x _ { N - 2 }$ to 1, and so on. This sequence of events proceeds in a clockwise fashion until finally $p _ { 1 }$ sets $x _ { 1 }$ to 0. Then we have reached the following configuration.

![](images/a42d1f966f068d0bba366d6e65c929aa6260071fa72d9041d4ba7a0ab0f41bda.jpg)

The only difference with the initial configuration is that the values of the registers have increased by 1, modulo $N - 2$ . In particular, in the preceding configuration, again only $p _ { 1 }$ is not privileged. This execution pattern can be repeated over and over again, leading to an infinite computation. In each of its configurations, $N - 1$ processes are privileged.

# 17.2 Arora-Gouda Spanning Tree Algorithm

In the Arora-Gouda self-stabilizing spanning tree algorithm for unstable, undirected networks, the process with the largest ID eventually becomes the root of a spanning tree of the network. The algorithm requires that all processes know an upper bound $K$ on the network size.

Each process keeps track of its parent in the spanning tree, which process is the root, and the distance to this root via the spanning tree. Because of arbitrary initialization, there are three complications: first, multiple processes may consider themselves the root; second, there may be a cycle in the spanning tree; and third, there may be a “false” root, meaning that processes may consider a process $q$ the root while $q$ is not the ID of any process in the network. The idea behind the Arora-Gouda algorithm is that these inconsistencies can be resolved if a process declares itself the root of the spanning tree, and adapts its local variables accordingly, every time it detects an inconsistency in the values of its local variables. Moreover, a process may resolve inconsistencies between the values of its own local variables and those of its neighbors.

Each process $p$ maintains the following variables:

$p a r e n t _ { p } : p$ ’s parent in the spanning tree;   
$r o o t _ { p }$ : the root of the spanning tree;   
$d i s t _ { p } : p$ ’s distance from the root, via the spanning tree.

The value $\perp$ for $p a r e n t _ { p }$ means that $p$ ’s parent is undefined (in particular, when $p$ considers itself the root). A process $p$ declares itself the root by executing

$$
p a r e n t _ { p } \gets \perp \qquad \quad r o o t _ { p } \gets p \qquad d i s t _ { p } \gets 0 ,
$$

when it detects an inconsistency in the values of its local variables:

$r o o t _ { p } < p$ ; or   
$p a r e n t _ { p } = \bot$ , and $r o o t _ { p } \neq p$ or $d i s t _ { p } \neq 0$ ; or   
$p a r e n t _ { p } \neq \bot$ and paren $\dot { p }$ is not a neighbor of $p$ ; or $d i s t _ { p } \geq K$ .

In the first case, $r o o t _ { p }$ is not the largest $\mathrm { I D }$ in the network. In the second case, $p a r e n t _ { p }$ says $p$ is the root, while $r o o t _ { p }$ or $d i s t _ { p }$ says it is not. In the third case, $p a r e n t _ { p }$ has an improper value. And the fourth case is in contradiction with the fact that $K$ is an upper bound on the network size.

Suppose there is no such inconsistency in the local variables of $p$ . Let $q$ be a neighbor of $p$ with $d i s t _ { q } < K$ . If $q = p a r e n t _ { p }$ and $p$ detects an inconsistency between its own variables and $q$ ’s, then $p$ < can bring its root and distance values in line with those of $q$ :

$$
r o o t _ { p } \gets r o o t _ { q } \qquad d i s t _ { p } \gets d i s t _ { q } + 1 .
$$

If on the other hand $q \neq p a r e n t _ { p }$ and $r o o t _ { p } < r o o t _ { q }$ , then $p$ can make $q$ its parent:

$$
\begin{array} { c c c } { { p a r e n t { } _ { p } \gets q ~ } } & { { ~ r o o t _ { p } \gets r o o t _ { q } ~ } } & { { ~ d i s t _ { p } \gets d i s t _ { q } + 1 . } } \end{array}
$$

Example 17.4 We consider one possible computation of the Arora-Gouda algorithm on the following undirected network with $K = 5$ . Arrows point from a child to its parent. Note that all processes consider process 8 the root, but this is a false root.

$$
\begin{array} { c c c c c c } { { r o o t _ { 2 } = 8 } } & { { \quad } } & { { r o o t _ { 3 } = 8 } } & { { \quad } } & { { r o o t _ { 1 } = 8 } } & { { \quad } } & { { r o o t _ { 5 } = 8 } } \\ { { d i s t _ { 2 } = 4 } } & { { \quad } } & { { d i s t _ { 3 } = 2 } } & { { \quad } } & { { d i s t _ { 1 } = 3 } } & { { \quad } } & { { d i s t _ { 5 } = 4 } } \end{array}
$$

![](images/d5cc94181934a5f77eedfa2ab770b85c9dc1ddb296217ae922453a9d28472cea.jpg)

First, process 3 notes that it has distance 2 to the root, while its parent, 2, has distance 4. Therefore, process 3 sets its distance to 5. Then it has a distance equal to $K = 5$ , so it declares itself the root: $p a r e n t _ { 3 } \gets \bot$ ,

$r o o t _ { 3 } \gets 3$ , and $d i s t _ { 3 } \gets 0$ . As a result, processes 7 and 1 set their root to 3 and their distance to 1; next, processes 2 and 5 set their root to 3 and their distance to 2.

$$
\begin{array} { c c c c c c } { { r o o t _ { 2 } = 3 } } & { { \quad } } & { { r o o t _ { 3 } = 3 } } & { { \quad } } & { { r o o t _ { 1 } = 3 } } & { { \quad } } & { { r o o t _ { 5 } = 3 } } \\ { { d i s t _ { 2 } = 2 } } & { { \quad } } & { { d i s t _ { 3 } = 0 } } & { { \quad } } & { { d i s t _ { 1 } = 1 } } & { { \quad } } & { { d i s t _ { 5 } = 2 } } \end{array}
$$

![](images/eb17904e29d850401c378babc6685238875a08e656d616efc92619d564a0f112.jpg)

Now process 5 finds an inconsistency in its local variables: its root value is smaller than its own ID. Therefore, it declares itself the root: $p a r e n t _ { 5 } \gets \perp$ , $r o o t _ { 5 } \gets 5$ , and $d i s t _ { 5 } \gets 0$ . As a result, first process 1 makes process 5 its parent: parent $_ 1  5$ , $r o o t _ { 1 } \gets 5$ , and $d i s t _ { 1 } \gets 1$ ; next, process 3 makes process 1 its parent: paren $_ 3 \gets 1$ , $r o o t _ { 3 } \gets 5$ , and $d i s t _ { 3 } \gets 2$ ; and then, process 2 makes process 3 its parent: $p a r e n t _ { 2 } \gets 3$ , $r o o t _ { 2 } \gets 5$ , and $d i s t _ { 2 } \gets 3$ .

![](images/54a4b54816c43c609bc8437bcb2beeabf2f0725b5b867bbea3ff960de4e7c60d.jpg)

Now process 7 finds an inconsistency in its local variables: its root value is smaller than its own ID. Therefore, it declares itself the root: paren $t _ { 7 }  \bot$ , $r o o t _ { 7 } \gets 7$ , and $d i s t _ { 7 } \gets 0$ . As a result, processes 2 and 3 make process 7 their parent; next, process 1 makes process 3 its parent; and finally process 5 makes process 1 its parent.

$$
\begin{array} { l l l l } { { r o o t _ { 2 } = 7 \quad } } & { { r o o t _ { 3 } = 7 \quad } } & { { r o o t _ { 1 } = 7 \quad } } & { { r o o t _ { 5 } = 7 } } \\ { { d i s t _ { 2 } = 1 \quad } } & { { d i s t _ { 3 } = 1 \quad } } & { { d i s t _ { 1 } = 2 \quad } } & { { d i s t _ { 5 } = 3 } } \end{array}
$$

![](images/df99a48e2b80982ca68e5d83818a8645208b48835755afb3bb627774b333a6f0.jpg)

The resulting configuration, depicted in the preceding diagram, is stable.

We argue that the Arora-Gouda spanning tree algorithm is self-stabilizing if only fair computations are considered (see exercise 17.5). The key is that false root values, which are not an ID of any process in the network, will eventually disappear. Because a false root value can survive only in a cycle of processes that all agree on this root value. Distance values of processes in such a cycle will keep on increasing until one of them gets distance $K$ and declares itself the root. Then the cycle is broken, and by fairness the cycle can be reestablished only a finite number of times. Hence, the false root of the (former) cycle will eventually be eradicated. Since false roots are guaranteed to disappear, the process with the largest ID in the network will eventually declare itself the root. Then the network will converge to a spanning tree with this process as the root, if the network topology is connected and remains stable and no more faults occur.

To obtain a breadth-first search tree, in the Arora-Gouda algorithm, the case where $q \neq p a r e n t _ { p }$ is a neighbor of $p$ with $d i s t _ { q } < K$ has one extra subcase: if $r o o t _ { p } = r o o t _ { q }$ and $d i s t _ { p } > d i s t _ { q } + 1$ , then paren $t _ { p } \gets q$ and $d i s t _ { p } \gets d i s t _ { q } + 1 .$ < >. That is, a process can select a new parent if it offers a shorter path to the root.

# 17.3 Afek-Kutten-Yung Spanning Tree Algorithm

The Afek-Kutten-Yung self-stabilizing spanning tree algorithm for unstable, undirected networks does not require a known upper bound on the network size. Moreover, it does not exhibit any (unfair) infinite computations. Again, the process with the largest ID eventually becomes the root of a spanning tree of the network.

Each process $p$ again maintains the variables parentp, $r o o t _ { p }$ , and $d i s t _ { p }$ . A process $p$ declares itself the root by executing

$$
p a r e n t _ { p } \gets \perp \qquad \quad r o o t _ { p } \gets p \qquad d i s t _ { p } \gets 0 ,
$$

if it does not yet consider itself the root and a local variable indicates it is the root (the first two cases) or it detects an inconsistency between the values of its local variables and those of its parent (the third case):

– $r o o t _ { p } \leq p$ ; or   
– $p a r e n t _ { p } = \bot$ ; or   
– $p a r e n t _ { p } \neq \bot$ , and parentp is not a neighbor of $p$ or $r o o t _ { p } \neq r o o t _ { p a r e n t _ { p } }$ or $d i s t _ { p } \neq d i s t _ { p a r e n t _ { p } } + 1 .$

Note that if there is a cycle in the spanning tree, then a process in this cycle will always declare itself the root. Because there is always some process $p$ in this cycle with $d i s t _ { p } \neq d i s t _ { p a r e n t _ { p } } + 1$ .

A process $p$ that considers itself the root can make a neighbor $q$ its parent if $r o o t _ { q }$ is greater than $p$ . If several neighbors of $p$ have root values greater than $r o o t _ { p }$ , $p$ selects a neighbor $q$ with the largest root value among all $p$ ’s neighbors. Before $p$ can make $q$ its parent, $p$ must wait until $q$ ’s component of the spanning tree has a proper root, for otherwise processes could infinitely often join a component of the spanning tree with a false root, as shown in the next example.

Example 17.5 Consider the following initial configuration.

$$
\begin{array}{c} \mathbf { \Lambda } _ { d i s t _ { 0 } = 0 } ^ { r o o t _ { 0 } } \bigcirc \begin{array} { l } { \boldsymbol { \bigcirc } } \\ { \boldsymbol { \bigcirc } } \end{array} ⨏ \mathop { { \ r { d i s t } _ { 1 } = 1 } } ^ { r o o t _ { 1 } = 2 } \mathop { { d i s t } _ { 1 } = 1 }  \end{array}
$$

Since $d i s t _ { 0 } \neq d i s t _ { 1 } + 1$ , process 0 declares itself the root: $p a r e n t _ { 0 } \gets \bot$ , $r o o t _ { 0 } \gets 0$ , and $d i s t _ { 0 } \gets 0$ . Next, since $r o o t _ { 0 } < r o o t _ { 1 }$ , process 0 makes process 1 its parent: $p a r e n t _ { 0 } \gets 1$ , $r o o t _ { 0 } \gets 2$ , and $d i s t _ { 0 } \gets 2$ . Next, since $d i s t _ { 1 } \neq d i s t _ { 0 } + 1$ , process 1 declares itself the root: $p a r e n t _ { 1 } \gets \bot$ , $r o o t _ { 1 } \gets 1$ , and $d i s t _ { 1 } \gets 0 .$ . Next, since $r o o t _ { 1 } < r o o t _ { 0 }$ , process 1 makes process 0 its parent: paren $t _ { 1 } \gets 0$ , $r o o t _ { 1 } \gets 2$ , and $d i s t _ { 1 } \gets 3$ . And so on.

Therefore, before $p$ makes $q$ its parent, it first sends a join request to $q$ , which is forwarded through the spanning tree to a root, which sends back an acknowledgment to $p$ via the spanning tree. When $p$ receives this acknowledgment, $p$ makes $q$ its parent by executing

$$
\begin{array} { c c c } { { p a r e n t { } _ { p } \gets q ~ } } & { { ~ r o o t _ { p } \gets r o o t _ { q } ~ } } & { { ~ d i s t _ { p } \gets d i s t _ { q } + 1 . } } \end{array}
$$

Since we are in a shared-memory framework, join requests and acknowledgments need to be encoded in shared variables; see the pseudocode in the appendix. The path of a join request is remembered in local variables, so the resulting acknowledgment can follow this path in the reverse order. A process can be forwarding and awaiting an acknowledgment for at most one join request at a time. The encoding of join requests in shared variables is rather convoluted. Therefore the examples present join requests in a message-passing style.

Example 17.6 We revisit the initial configuration from example 17.5 but now with join requests and ac knowledgments. We consider one possible computation of the Afek-Kutten-Yung algorithm.

Since $d i s t _ { 0 } \neq d i s t _ { 1 } + 1$ , process 0 declares itself the root: paren $\tan  \bot$ , $r o o t _ { 0 } \gets 0$ , and $d i s t _ { 0 } \gets 0$ . Next, since $r o o t _ { 0 } < r o o t _ { 1 }$ , process 0 sends a join request to process 1. Note that process 1 cannot forward this join request to its parent 0, because 0 is awaiting an acknowledgment. Next, since $r o o t _ { 1 } \neq r o o t _ { 0 }$ , process 1 declares itself the root: paren $t _ { 1 } \gets \bot , r o o t _ { 1 } \gets 1$ , and $d i s t _ { 1 } \gets 0$ . Since process 1 is now a proper root, it replies to the join request of process 0 with an acknowledgment. As a result, process 0 makes process 1 its parent: $p a r e n t _ { 0 } \gets 1$ , $r o o t _ { 0 } \gets 1$ , and $d i s t _ { 0 } \gets 1$ . The resulting spanning tree, with process 1 as root, is stable.

Join requests are forwarded only between processes for which the local variables have consistent values; otherwise there could be infinite computations, as shown in example 17.7. And processes forward an acknowledgment only if they sent a corresponding join request previously. This check avoids spurious acknowledgments caused by improper initial values of local variables.

Example 17.7 Consider an undirected ring with three processes 0, 1, and 2. Initially, processes 0 and 1 consider themselves the root, while process 2 has process 0 as its parent, considers the (nonexistent) process 3 the root, and has some distance value $k$ .

$$
\displaystyle { \begin{array} { l } { \displaystyle { \bigcap _ { i = { i \atop i } s t _ { 1 } = 0 } ^ { r o o t _ { 1 } = 1 } } } \\ { \displaystyle { \binom { 2 } { i } \sum _ { d i s t _ { 2 } = k } ^ { r o o t _ { 2 } = k } } } \end{array} }
$$

Since $r o o t _ { 2 } > r o o t _ { 1 }$ (and $r o o t _ { 2 } > r o o t _ { 0 }$ ), process 1 sends a join request to process 2. Without the consistency check, process 2 would forward this join request to process 0. Since process 0 considers itself the root, it would send back an acknowledgment to process 1 (via process 2), and process 1 would make process 2 its parent and consider process 3 the root. Next, since $r o o t _ { 2 } \neq r o o t _ { 0 }$ , process 2 could make itself the root.

$$
\displaystyle \sum _  \begin{array} { l } { { r o o t } _ { 0 } = 0 \displaystyle \sum _ { \begin{array} { l } { 0 } \end{array} } } ^ { \prime o o t _ { 1 } = 3 } \end{array}
$$

Now we would have a configuration that is symmetric to the original one. This scenario could be repeated to obtain an infinite computation that never reaches a stable configuration.

We briefly argue that the Afek-Kutten-Yung spanning tree algorithm is self-stabilizing. Each component in the network with a false root contains an inconsistency, so a process in this component will declare itself the root. Join requests guarantee that processes only finitely often join a component with a false root, each time caused by improper initial values of local variables. Here it is important that join requests are forwarded only between consistent processes. Furthermore, in part since processes can be involved in only one join request at a time, it is guaranteed that each join request will eventually be acknowledged. These observations together imply that eventually false roots will disappear. Therefore, the process with the largest ID in the network will declare itself the root, and the network will converge to a spanning tree with this process as the root, if the network topology is connected and remains stable and no more faults occur.

# Bibliographical notes

Dijkstra’s token ring originates from [34].11 A proof that this ring is self-stabilizing for $K = N - 1$ is presented in [43]. The Arora-Gouda algorithm stems from [6], and the Afek-Kutten-Yung algorithm was proposed in [1].

# 17.4 Exercises

Exercise 17.1 Give a computation of Dijkstra’s token ring with $N = K = 4$ that takes 13 events to reach a correct configuration.

Exercise 17.2 [117] Argue that from each configuration of Dijkstra’s token ring (with $K \geq N$ ), a correct configuration will be reached in at most $O ( N ^ { 2 } )$ transitions.

Exercise 17.3 Consider an undirected ring of three processes with $\mathrm { I D s } 0 , 1$ , and 2. In the initial configuration, $p a r e n t _ { 0 } = 1 , p a r e n t _ { 1 } = 2$ , and paren $\mathfrak { z } = 0$ ; $r o o t _ { 0 } = r o o t _ { 1 } = r o o t _ { 2 } = 3$ ; and $d i s t _ { 0 } = 1$ , $d i s t _ { 1 } = 0$ , and $d i s t _ { 2 } = 2$ . Describe one possible computation of the Arora-Gouda algorithm on this network, with $K = 4$ .

Exercise 17.4 One part of the Arora-Gouda algorithm considers a neighbor $q$ of process $p$ with $d i s t _ { q } < K$ .   
Show that if the side condition “with $d i s t _ { q } < K ^ { \prime }$ were omitted, then the algorithm might not stabilize.

Exercise 17.5 Give an unfair infinite computation of the Arora-Gouda algorithm that never stabilizes. Let only one process perform events.

Exercise 17.6 Adapt the Arora-Gouda algorithm so that it no longer exhibits (unfair) infinite computations.

Exercise 17.7 Describe one possible computation of the Afek-Kutten-Yung algorithm on the network from exercise 17.3.

Exercise 17.8 Argue that in the Afek-Kutten-Yung algorithm, each join request eventually results in an acknowledgment.

Exercise 17.9 Argue that the Afek-Kutten-Yung algorithm takes at most $O ( N ^ { 2 } )$ transitions to stabilize.

Exercise 17.10 Suppose that at the start of the Afek-Kutten-Yung algorithm, all processes would declare themselves root.

(a) Explain how this allows to simplify the algorithm.   
(b) Motivate why the resulting algorithm is not really self-stabilizing, in the sense that it should be able to cope with e.g. arbitrary bit flips at the hardware level.

Exercise 17.11 Let the Afek-Kutten-Yung algorithm be optimized in the following way. Suppose a nonroot forwarded a join request to its parent and later answered this join request with an acknowledgment. As long as this nonroot keeps its current parent, it will immediately answer all subsequent incoming join requests with an acknowledgment. Is this still a correct self-stabilizing algorithm for computing a spanning tree?

Exercise 17.12 [5] Develop a self-stabilizing algorithm for computing a minimum spanning tree in an undirected weighted network in which all channels carry different weights. Exploit the fact that in such a network a channel $p q$ is not in the minimum spanning tree if and only if there is a path between $p$ and $q$ of channels that all carry a weight less than weight $( p q )$ . Let each process $r$ compute for every other process $s$ the smallest value $d$ such that there is a path between $r$ and $s$ of channels with weights $\leq d$ . Of course $r$ needs to take into account such values at its neighbors.

# Dynamic Networks

In a peer-to-peer $( P 2 P )$ network, a task can be divided between processes, called peers, who all have equal rights. Such a network is dynamic, in the sense that peers can freely join and leave the network or may crash. A peer can make part of its resources, such as disk storage or processing power, available to other peers without a need for central coordination. Peers can both consume and supply resources, as opposed to the client-server architecture, in which clients only consume and servers only supply resources. The P2P paradigm avoids performance bottlenecks and provides fault-tolerance. It moreover tends to accomplish a balanced work load over peers with regard to e.g. message passing or data storage. Its applications on the Internet range from music streaming and telephony to digital cryptocurrencies, the latter of which will be discussed in chapter 19. The absence of a central authority in P2P networks offers freedom from censorship. Napster, the first hugely popular P2P service, for sharing MP3 music files, was eventually closed down due to law suits regarding copyright infringements.

A mobile ad hoc network (MANET) is a wireless network in which nodes can move freely, so that the network topology changes over time. Network connectivity is typically based on radio waves with a limited range and signal quality fluctuates. Therefore, links between nodes tend to change over time and communication between two nodes may be indirect, taking multiple hops via different nodes. Each node must continuously maintain the information required to properly route messages through the MANET. Nodes may join or leave the network or crash. MANETs may dynamically self-organize and self-configure, which facilitates their employment for e.g. mobile robots and in dire circumstances such as an earthquake disaster area. MANETs are widely used in practice, notably in disaster relief and in maritime applications.

This chapter discusses two efficient and popular routing algorithms, the Chord ring for P2P networks and the AODV protocol for MANETs. Furthermore, it is explained how election, mutual exclusion, and checkpointing can be performed in a MANET.

# 18.1 Chord Ring

P2P networks tend to consist of a small number of peers at the start and become densely populated over time. Scalability of P2P protocols is essential, as eventually such networks may comprise millions of nodes that span the globe and often support applications that impose a significant communication overhead. For example, the widely used P2P protocol BitTorrent for sharing digital video files via the Internet is especially tailored to cope with very large data files. A file is divided into pieces that are placed at different peers. Downloading these pieces requires less bandwidth and reduces the load on individual servers, compared to downloading the entire file from a single source.

A P2P network is built as a virtual overlay network on top of a physical network topology, typically the Internet. Although data is exchanged via the physical network, at the more abstract application layer, peers appear to communicate directly with each other via logical links, which correspond to paths in the physical network. Logical links are assumed to be bidirectional.

Gossip protocols disseminate information through P2P networks in the same way gossip spreads through a social network. They are also often referred to as epidemic algorithms, because they mimic the spread of a contagious disease. Just as a piece of gossip (or a virus) is passed on from one human being to another, in a gossip protocol, each peer relays pieces of information to some randomly chosen neighbors. In turn, these peers forward the information to some of their neighbors, and so on. Gossip protocols inherently contain redundancy, as a peer may receive the same piece of information multiple times from different neighbors, which makes them robust against node crashes and link failures, at the cost of communication overhead.

Early P2P networks were unstructured, meaning that data files, which are replicated among peers, can be kept at any of the nodes in the network. This is convenient because of the dynamic character of the network; if a peer joins or leaves, there is less need to redistribute files. The price to pay is that looking for a particular file is much harder than in a so-called structured P2P network, in which each data file is kept at a predefined peer. A search in an unstructured network can be performed by flooding, meaning that a peer probes its neighbors in the overlay network, which in turn probe their neighbors, et cetera. Similar to link-state routing (see section 8.6), a time-to-live field can be used to ensure that this storm of probes eventually dies down. However, then not the entire the network may be covered, and anyway flooding imposes a severe communication overhead. An alternative is to perform the search by a random walk, but this means the peer that holds the file may be missed, or is visited only after a long time. A smart replication scheme of data files can help to increase the chance of finding a file relatively soon.

In a structured P2P network, it is predefined at which peer a data file is stored and how the overlay network is altered if a peer joins or leaves the network. This structure is usually provided on the basis of a hash function, which maps elements from a large and possibly heterogeneous data domain $D$ to a much smaller data domain $E$ in which all elements have a fixed length. Hash functions were originally developed to fit elements from a vast data domain into a so-called hash table of fixed size and perform fast lookups. There are two standard techniques to cope with a hash collision, meaning that an element $d$ in $D$ is hashed to a slot in the hash table that is already occupied by another element from $D$ that happens to hash to the same value in $E$ . Either each slot in the hash table represents a linked list of elements from $D$ , or the hash table is probed in a predefined manner until an empty slot for $d$ is found.

The Chord protocol provides a structured P2P network based on a distributed hash table, meaning that each peer contains part of the hash table. The domain $E$ of hash values consists of the bit strings of length $m$ , where this value is chosen so large that hash collisions are rare. (In practice, typically $m = 1 2 8 .$ ) For simplicity, it is assumed such collisions do not occur. Conceptually, the overlay network is a ring of $2 ^ { m }$ locations, with IDs ranging from 0 up to $2 ^ { m } - 1$ ; they are interpreted modulo $2 ^ { m }$ . For each pair of distinct IDs $i$ and $j .$ , $\langle i , j \rangle$ denotes the segment of IDs in the ring between $i$ and $j .$ , i.e., $( i + 1 )$ mod $2 ^ { m }$ , $( i + 2 )$ mod $2 ^ { m }$ ,, et cetera, up to but not including $j .$ . The ID of a peer in the ring is the hash value of the peer’s physical network address. Each data file in the network can be found by calculating its hash value $h$ ; the file is located at the peer associated to the ID $h$ in the ring, if such a peer is present, or else at the nearest successor of $h$ in the ring to which a peer has been associated. More formally, the file is located at the ID $s i t e ( h )$ , where either $s i t e ( h ) = h$ if a peer is associated to ID $h$ in the ring, or $s i t e ( h ) = s i t e ( ( h + 1 ) \bmod 2 ^ { m }$ ) otherwise. In summary, obtaining a file consists of computing the hash value of this file, determining through the ring which peer holds the file, and fetching the file from that peer.

To support an efficient search, each peer $p$ maintains a routing table, called a finger table, containing $m$ entries, each one providing the ID (and physical address) of a peer in the ring. For $\ell = 0 , \ldots , m - 1$ , the entry $f i n g e r _ { p } [ \ell ]$ points to the peer associated to the ID s $i t e ( i d _ { p } + 2 ^ { \ell } )$ , where $i d _ { p }$ ℓdenotes the $\mathrm { I D }$ . , of $p$ in the ring. ℓSuppose $p$ wants to find a file with the ID $h$ that is located at another peer. If $h$ happens to equal fi $\operatorname* { i n } g e r _ { p } [ \ell _ { 0 } ]$ for some $\ell _ { 0 } = 0 , \ldots , m - 1$ , then $p$ locates the file at the peer at $f i n g e r _ { p } [ \ell _ { 0 } ]$ . Else, if $h$ is in $\langle i d _ { p } , f i n g e r _ { p } [ \mathrm { i } ] \rangle$ ℓ, then $p$ ℓ , . . . ,locates the file at the peer at fingerp[1]. Else, $p$ ℓ determines the largest $\ell _ { 1 } = 1 , . . . , m - 1$ , such that fi $n g e r _ { p } [ \ell _ { 1 } ]$ is inside $\langle i d _ { p } , h \rangle$ . Then $p$ contacts the peer at $f u n g e r _ { p } [ \ell _ { 1 } ]$ ℓ , . . . , ℓ, who in turn uses its finger table to locate the file. , ℓThis lookup method resembles a binary search, in the sense that each time the lookup request is passed on to another peer, the search space is at least halved. Its strength is that on the one hand finger tables contain only $m$ entries, while on the other hand the search takes at most $m$ hops (if the network is stable).

Example 18.1 Consider a Chord ring with $m = 6$ , so there are $6 4 ~ \mathrm { I D s }$ . Suppose there are peers at IDs 1, 8, 14, 21, 32, 38, 42, 48, 51, and 56. The finger table of the peer $p$ at $\textrm { I D } 8$ is given next to the depicted ring. Solid arrows inside the ring represent the successive values of $8 + 2 ^ { \ell }$ for $\ell = 0 , . . . , 5$ ; dotted arrows outside the ring represent the corresponding values under fingerp.

![](images/417288cd90828b7d3775970d4b22329dd9b6e8475f03f043bf3e994c237bd307.jpg)

<html><body><table><tr><td></td><td></td><td>l|8+2e|fingerp[e]</td><td></td></tr><tr><td>0</td><td>9</td><td>14</td><td rowspan="4"></td></tr><tr><td>1</td><td>10</td><td>14</td></tr><tr><td>2</td><td>12</td><td>14</td></tr><tr><td>3 4</td><td>16</td><td>21</td></tr><tr><td></td><td>24</td><td>32</td></tr><tr><td>5</td><td>40</td><td>42</td></tr></table></body></html>

Suppose the peer $p$ at $\textrm { I D } 8$ wants to obtain a file with hash value 54. Then it contacts the peer $q$ at ID $f i n g e r _ { p } [ 5 ] = 4 2$ , because 42 is inside $\langle 8 , 5 4 \rangle$ . Next, $q$ contacts the peer $r$ at $\mathrm { I D } f i n g e r _ { q } [ 3 ] = 5 1$ , because 51 is inside while fingerq $, [ 4 ] = 1$ is outside $\langle 4 2 , 5 4 \rangle$ . Finally, since fingerr $. [ 0 ] = 5 6$ and 54 is inside $\langle 5 1 , 5 6 \rangle$ , $r$ locates the file at the peer at ID 56 and informs $p$ about this location.

The successor and predecessor of a peer $p$ in the ring are denoted by $s u c c _ { p }$ and $p r e d _ { p }$ , respectively. When a peer $q$ joins the Chord ring, it contacts some peer $r$ already in the network. Such possible initial points of contact may be listed separately. Peer $r$ then employs the lookup method to find the proper value for $s u c c _ { q }$ , by searching for $s i t e ( i d _ { q } + 1 )$ . When $s u c c _ { q }$ has been determined, the peer $s$ with this ID is asked to transfer to $q$ those files that carry an ID in $\langle p r e d _ { s } , i d _ { q } ]$ , i.e., in $\langle p r e d _ { s } , i d _ { q } \rangle \cup \{ i d _ { q } \}$ . Moreover, $s$ sets preds to $i d _ { q }$ . Peer $q$ can copy its predecessor from $s$ and can efficiently initialize its finger table by copying the finger table of $s$ and using it to search for the values of those $s i t e ( i d _ { p } + 2 ^ { \ell } )$ that are unequal to $s$ , for $\ell < m$ , using the lookup method described previously.

Example 18.2 Suppose a peer $q$ wants to join the Chord ring from example 18.1 at $\mathrm { I D } 2 9$ . Let $q$ contact the peer at ID 51, who determines that the successor of $q$ in the ring is the peer $s$ at $\textrm { I D } 3 2$ . Then $s$ is asked to transfer to $q$ the files that carry an ID in the range 22-29. Furthermore, $s$ stores that $q$ is its new predecessor. Finally, $q$ copies the old predecessor of $s$ and uses the finger table of $s$ to build its own finger table.

When a peer $p$ wants to leave the network, it first informs the peers at $s u c c _ { p }$ and $p r e d _ { p }$ , who make each other their successor and predecessor. Furthermore, $p$ transfers its files to the peer at $s u c c _ { p }$ .

To cope with crashing peers, a failure detector is employed (see section 12.3). Since the P2P network is dynamic, each peer $p$ regularly performs a stabilization procedure, to keep an up-to-date view of the values of $s u c c _ { p }$ and pred ${ \bf \Pi } _ { p } ^ { \prime }$ as well as its finger values. At a run of the stabilization procedure, $p$ asks the peer $q$ at $s u c c _ { p }$ for the value of $p r e d _ { q }$ . If it is in $\langle i d _ { p } , s u c c _ { p } \rangle$ , then $p$ sets $s u c c _ { p }$ to that value and contacts its new successor ,to announce itself as the predecessor and possibly obtain files. At the same time, $q$ checks whether $i d _ { p }$ is in $\langle p r e d _ { q } , i d _ { q } \rangle$ . If so, or if $p r e d _ { q }$ crashed, then $q$ sets $p r e d _ { q }$ to $i d _ { p }$ . Furthermore, $p$ at regular time intervals checks whether its finger values are still accurate. This means $p$ searches for the values of $s i t e ( i d _ { p } + 2 ^ { \ell } )$ for $\ell = 0 , \ldots , m - 1$ , using the lookup method described previously.

, . . . ,A problem may arise if there are multiple simultaneous crashes. For example, suppose the peers at $f i n g e r _ { p } [ 0 ] , f i n g e r _ { p } [ 1 ] .$ and fingerp[2] crash simultaneously, and there is a peer $q$ with an ID between fingerp[2] and $f u n g e r _ { p }$ [3]. Then $p$ will be unable to locate files at $q$ . To cope with this situation, each peer maintains a successor list, containing its nearest $K$ successors, for some $K > 2$ . This list can be consulted if a crashed peer is encountered during a call to the lookup method. All $K$ >successors of a peer would have to fail simultaneously to disrupt the Chord protocol. Clearly, the larger the value of $K$ , the smaller the chance of this happening. Each peer $p$ updates its successor list during the stabilization procedure: it obtains the successor list of the peer at $s u c c _ { p }$ , removes its last entry, and prepends $s u c c _ { p }$ to it. The ring is supposed to contain more than $K$ peers from the very beginning.

Due to joining, leaving, or crashing peers, finger values at peers may temporarily be inaccurate. On the one hand, a search may take some more hops than strictly necessary. On the other hand, a search may overshoot its target, in which case it will have to be retried. Since succ values are updated almost immediately when a peer joins and finger values are updated regularly, the chance of this happening is small.

Example 18.3 Consider once again the Chord ring from example 18.1, including the peer that joined with $\mathrm { I D } 2 9$ in example 18.2. Let $K = 4$ . Suppose the peers at IDs 14, 21, and 29 crash simultaneously. When the failure detector of peer $p$ at $\textrm { I D } 8$ has detected these three crashes, $p$ finds through its successor list that its successor $r$ is now at ID 32. During the next stabilization phase, $p$ obtains the successor list of $r$ , removes its last entry 51, and prepends 32 to it. Moreover, in the next stabilization phase, $r$ sets predr to 8.

To avoid that a crash of a peer leads to loss of files, stable storage can be employed, or peers can store only pointers to files instead of the files themselves. The latter approach has the additional advantage that transferring files from one peer to another becomes much cheaper.

Since a hash function tends to attribute IDs to peers and hosts to files in a random fashion, one might expect that files are spread evenly over the peers in the ring. However, a hash function generally does not provide a uniform distribution of occupied IDs over the Chord ring. This means there can be clusters of occupied IDs in the ring, where the first peer in this cluster gets many files while the others get very few. To mitigate this problem, a peer that joins the Chord ring can be made owner of multiple IDs in the ring, increasing the chance of an even load balance.

# 18.2 AODV Routing Protocol

A key challenge in the dynamic setting of a MANET is to let nodes continuously maintain information needed to route data traffic through the network, over multiple hops from the source to the destination of a data packet. This is complicated by the fact that MANETs can grow very large and its devices often need to share limited communication bandwidth. The Ad hoc On-demand Distance Vector (AODV) routing protocol is especially designed for MANETs. When a node $p$ wants to send a packet to another node $q$ , it first looks in its routing table (see chapter 8) whether it knows an active route to $q$ , i.e., a route that has not yet been invalidated. If so, $p$ forwards the packet to the next hop on this route. If not, $p$ starts a route discovery procedure aimed at finding a minimum-hop route to $q$ , by broadcasting a route request (RREQ) message, containing the IDs of $p$ and $q$ . Furthermore, this message holds a hop count, started at 0, and the sequence number $s n _ { p }$ of its originator $p$ , which is increased by 1 each time $p$ starts a route discovery procedure. The RREQ is flooded through the network. Let it arrive at a node $r$ with hop count $h$ . If $r$ knows an active route to $p$ with a more recent sequence number than $s n _ { p }$ , or with the sequence number $s n _ { p }$ and a distance value $d \leq h + 1$ , then $r$ purges this RREQ, because it already acted on this or on a more recent request from $p$ . Else, $r$ updates its routing information to $p$ , decorated with $s n _ { p }$ , and acts as follows. If $r$ does not know an active route to $q$ , then it broadcasts the currently received RREQ, with the hop count increased by 1. If on the other hand $r$ does know an active route to $q$ , then it answers with a route reply (RREP) message, which contains the IDs of $p$ and $q$ , the distance of the route from $r$ to $q$ , and the sequence number of the route, originating from $q$ . In particular, if $r = q$ , the RREP is provided with the sequence number of $q$ , which is increased by 1. The RREP from $r$ impels a chain of RREPs on the route from $r$ to $p$ . Suppose a node $s$ receives such an RREP and either it carries a more recent sequence number than $s$ ’s current route to $q$ , or it carries the same sequence number and yields a shorter route to $q$ . Then $s$ updates its routing information to $q$ and (if it is not $p$ ) forwards this message toward $p$ , based on the entry for $p$ in $s$ ’s routing table, with the distance value increased by 1. Nodes memorize to which precursors they sent RREPs, in case information about an improved route needs to be passed on or a route needs to be canceled.

Example 18.4 Consider the following MANET, where the edges depict which nodes are currently within each other’s ranges. In particular, the nameless nodes at the left- and right-hand sides are outside the ranges of the nodes $p , q , r , s , t , u .$ , and $\nu$ . It is assumed the network topology does not change during the following run of the route discovery procedure. At the start, no node knows an active route to $\nu$ .

![](images/5ccd6a50b6b714b2848030a65e7fb75f680298558d42c548647b698e272fa093.jpg)

![](images/e245536c967d7a9bc60efcc91a22bafd84a5981900621ea4a15798ee9defda48.jpg)

Suppose $p$ wants to find a route to $\nu$ , increases $s n _ { p }$ by 1, and broadcasts an RREQ with hop count 0. This RREQ is received by $q , r .$ , and $s$ . An RREQ in transit is depicted by a solid arrow if this message will cause the recipient to update its routing information to $p$ .

![](images/eccbf4e6fe1d4f111d369c5b93ffd5b33b369f13392620911fe7cdf6355f982b.jpg)

In turn, $q , r$ , and $s$ broadcast an RREQ with hop count 1. A dashed arrow depicts an RREQ message in transit that will be ignored by its recipient.

$$
\cos ^ { \prime } = \frac { \cos \theta } { \cos ^ { \prime } \theta } - \frac { \cos \theta } { \cos \theta }
$$

The RREQ from $s$ is received by $u$ , who in turn broadcasts an RREQ with hop count 2. The RREQ from $u$ reaches $t$ before the RREQ from $s$ .

![](images/6432ac7971fbfc03c6a9317ab708efca08bcb6df6c7505f8660d2143f8b2c959.jpg)

When the RREQ from $u$ is received by $t$ , it broadcasts an RREQ with hop count 3, which will be ignored by all recipients.

$$
\cos < \cdots < 0 \atop \overset { \prime } { \underset { i } {  } } \overset { \prime } { \longrightarrow } \overset { \prime } { \underset { i } {  } }
$$

Finally, the RREQ from $s$ reaches $t$ , which in view of its hop count gives rise to another broadcast of an RREQ with hop count 2. Again this message from $t$ is ignored by all recipients. Furthermore, the RREQ from $u$ reaches $\nu$ (before the RREQs from $t$ ). In reply, $\nu$ increases $s n _ { \nu }$ by 1 and sends a RREP to $u$ with distance value 0. The RREP from $\nu$ gives rise to a chain of RREPs toward $p$ , depicted with open arrow heads, where the distance value is increased by 1 at each step. As a result, at $u , s ,$ , and $p$ , the routing information to $\nu$ is updated.

![](images/c1ec4b9208e771c72914d6c9881db5702a702e9517b1121721fc5db2451f2f79.jpg)

Thus a route from $p$ to $\nu$ has been established, via $s$ and $u$ .

Sequence numbers are 16-bit values that wrap back to 1 when they reach $2 ^ { 1 6 }$ . (The value 0 indicates that the corresponding route has been invalidated or its sequence number is unknown.) Suppose two pieces of information, tagged with positive sequence numbers $s n _ { 1 }$ and $s n _ { 2 }$ , both originate from $p$ . The piece with $s n _ { 2 }$ is considered more recent than the piece with $s n _ { 1 }$ if either $s n _ { 2 } > s n _ { 1 }$ and $s n _ { 2 } - s n _ { 1 } \leq 2 ^ { 1 5 }$ , or $s n _ { 1 } > s n _ { 2 }$ and $s n _ { 1 } - s n _ { 2 } > 2 ^ { 1 5 }$ >. The underlying idea is that in the second case the sequence number at $p$ >was wrapped back >to 1 between the creations of $s n _ { 1 }$ and $s n _ { 2 }$ . By the time $2 ^ { 1 5 }$ sequence numbers beyond $s n _ { 1 }$ have been created at $p$ , messages carrying this installment of $s n _ { 1 }$ will have vanished from the network.

To limit the overhead imposed by flooding, the idea behind the time-to-live field from link-state routing is employed (see section 8.6). Every RREQ includes a ceiling value. If its hop count reaches this ceiling, the RREQ is discarded. If the origin $p$ of the RREQ does not receive an RREP within a predefined amount of time, it broadcasts another RREQ with a higher ceiling value (and an increased sequence number). If after a predefined number of attempts no RREP has returned to $p$ , it must stop trying to find a route to this destination.

Links in a MANET may be broken, when a node moves outside the communication range of a neighbor, leaves the network, or crashes. Nodes are therefore supposed to keep track of connectivity to neighbors, for instance by letting nodes broadcast hello messages at regular time intervals. When a node detects that a neighbor who is the next hop on one or more active routes has become unresponsive, it may attempt a local repair by sending RREQs. If a node finds a route cannot be repaired, it sends a route error (RERR) message to all precursors for these routes. The RERR contains the list of routes that are no longer available for the recipient, who in turn forwards the RERR to those precursors that are affected by the link break. Nodes invalidate a disabled route by setting its distance to infinity. Information about an invalid route is preserved in routing tables until fresh information is received that establishes a valid replacement route, as this invalidated information can still help to classify future incoming route messages as stale or fresh.

Example 18.5 In the network from example 18.4 with the established route from $p$ to $\nu$ , suppose the link between $u$ and $\nu$ breaks and $u$ does not manage to repair its route to $\nu$ . Then this gives rise to an RERR from $u$ to $s$ , which in turn yields an RERR from $s$ to $p$ .

If an entry in a routing table is not used to forward a packet along the corresponding route for a certain predefined amount of time, then this entry is invalidated. Furthermore, if the sequence number of a route remains unchanged for a certain predefined amount of time, the sequence number of the route is set to 0, meaning that the route is considered stale and has been invalidated.

When a node $p$ wants to rediscover a route to a node $q$ , the sequence number of $p$ ’s most recently invalidated route to $q$ is appended to the ensuing RREQ messages. A node can only reply to an RREQ if it knows a route to the destination with a more recent sequence number. This is important to avoid the formation of loops, as shown in the next example.

Example 18.6 Consider a network of five nodes $p , q , r , s .$ , and $t$ . Suppose $p$ knows a route to the destination $t$ via $q$ and $s$ , with a sequence number $k$ that originates from $t$ . Let the link between $s$ and $t$ break. Then $s$ sends an RERR to $q$ , who is slow. Next, $s$ wants to find a route to $t$ and broadcasts an RREQ, containing $k$ .

![](images/80972b09fabe9a647fee9d2e7a3c87e955e318f06115778ee6a15e885f6b0353.jpg)

The RREQ is received and broadcast by $r$ , and is in turn received by $p$ . Since $p$ knows a route to $t$ , if the $k$ were absent from the RREQ, $p$ would reply with an RREP to $r$ . This message would be forwarded to $s$ , leading to a route from $s$ to $t$ that would loop over $r$ , $p$ , and $q$ , back to $s$ . However, owing to the $k$ in the RREQ, $p$ realizes that its route to $t$ is outdated and does not send an RREP to $r$ .

Concluding, each entry in a routing table contains the ID of the destination, the ID of the next hop, the distance of the route, the maximum life time of the entry, a list of precursors, and a sequence number provided by the destination.

Several details have been omitted from the description of the AODV protocol, which was published as an Internet standard under RFC 3561. Notably, nodes may test for bidirectionality of a link and can give routing information an unconfirmed status pending such a test. It is possible to request routes to multiple targets in one RREQ. To avoid congestion, there is an upper bound on the rate of message generation at each node.

# 18.3 Vasudevan-Kurose-Towsley Election Algorithm

The Vasudevan-Kurose-Towsley algorithm elects a leader in a MANET. It is assumed transmission ranges of the nodes in the MANET are uniform, so that edges are bidirectional. The underlying idea of the algorithm is that when a node detects the leader abandoned the network or crashed, it initiates a wave to establish which node has the largest ID. Each wave builds a spanning tree rooted in its initiator, and noninitiators send the largest ID in their subtree to their parent. When a wave completes, the node with the largest ID is made the new leader.

Each node maintains a sequence number associated to the last election round. If a node detects (1) the current leader disappeared from the network and it is not yet participating in a wave, or (2) the initiator of the wave it is participating in crashed, then it increases its sequence number by 1 and starts a wave, tagged by this sequence number and its ID. When a node $p$ receives a wave message $m$ , the following cases can be distinguished, similar to the echo algorithm with extinction (see section 9.3).

If $m$ has a greater sequence number than $p$ , or the same sequence number and a larger ID than $p$ ’s current or last wave, then $p$ starts participating in $m$ ’s wave and adopts its sequence number. If $p$ was participating in another wave, it abandons that wave. If $m$ has the same sequence number as $p$ and the same ID as $p$ ’s current wave, then $p$ treats it according to the wave algorithm. If $m$ has a smaller sequence number than $p$ , or the same sequence number and a smaller ID than $p$ ’s current or last wave, then it is purged.

If a wave completes, its initiator communicates the largest $\mathrm { I D }$ to all nodes, together with the associated sequence number.

To cope with mobility, heartbeat messages as well as an upper bound on network latency are assumed. If a node detects that a child in the spanning tree of an ongoing wave disappeared, because it moved out of range or crashed, then it stops waiting for an acknowledgement from that child. On the other hand, if a node detects that its parent in the spanning tree of an ongoing wave disappeared, then in the end it broadcasts the largest ID in its subtree (and its sequence number) to all its neighbors.

When two or more nodes appear in each other’s transmission ranges, they exchange their current leaders and sequence numbers. If these do not agree, the largest ID and sequence number are chosen, and a node that changes one or both of these values broadcasts them to its neighbors. If one or more of these nodes are involved in a wave, they wait until these waves have completed before exchanging their leader IDs and sequence numbers.

As long as the network remains connected and the leader does not disappear undetected (see exercise 18.10), there is one leader or a leader will be elected. If the network breaks up in disconnected components, each of these components will elect a leader separately.

# 18.4 Walter-Welch-Vaidya Mutual Exclusion Algorithm

The Walter-Welch-Vaidya algorithm carries Raymond’s mutual exclusion algorithm (see section 14.2) over to MANETs. Again, edges are bidirectional. Moreover, it is assumed here they are FIFO. As in Raymond’s algorithm, a token is passed through the network, the one holding the token is privileged, and nodes maintain a queue to manage token passing. All edges are directed such that they form an acyclic graph with the node holding the token, called the root, as sink. (Unlike Raymond’s algorithm, where only the edges in the sink tree are directed.)

Each node keeps track of a height, consisting of a pair of integers $\left( h _ { 1 } , h _ { 2 } \right)$ , such that heights on each path ,toward the root are strictly decreasing, with regard to the lexicographical order. That is, each edge in the network is directed from the node with greater to the node with smaller height. If two neighbors happen to have the same height, their node IDs serve as tiebreaker. Nonroots direct a token request to their neighbor of minimal height. Initially, heights of nodes can for instance be determined using a shortest path algorithm toward the root.

Each message (including the token) contains the height of its sender, and a node that changes its height informs its neighbors of this new height. This way nodes can keep track of the heights of their neighbors. The fact that edges are FIFO guarantees that height updates are received in the proper order. With non-FIFO edges, a height update of a node could reach its neighbor with great delay, at a point where the height of the sender has already changed multiple times, and those later updates already reached the receiver. This could e.g. lead to a cycle in the sink graph, because the receiver has an outdated image of the height of the sender.

When all edges of a nonroot become incoming (because its parent disappeared or increased its height), this node increases its height beyond that of at least one neighbor. If $k _ { 1 }$ is the minimum $h _ { 1 }$ -value of its neighbors, then it changes its $h _ { 1 }$ -value to $k _ { 1 } + 1$ . Moreover, if at least one of its neighbors has $h _ { 1 }$ -value $k _ { 1 } + 1$ , with $k _ { 2 }$ the minimum $h _ { 2 }$ -value among those neighbors, then it changes its $h _ { 2 }$ -value to $k _ { 2 } - 1$ . (Else it leaves its $h _ { 2 }$ -value unchanged.) Note that the first parameter $h _ { 1 }$ is used to make sure at least one edge becomes outgoing, while the second parameter $h _ { 2 }$ is used to minimize the number of outgoing edges.

At each local update of heights of itself and/or its neighbors, a node checks whether its queue contains token requests from neighbors with a smaller height than its own height, and if so, removes these requests from its queue. Likewise, when a node receives a token request, it only adds this request to its queue if its own height is smaller than the height of the sender. Vice versa, if a nonroot updates the height of a neighbor and has an outstanding token request, it checks whether its height has become smaller than the height of the neighbor to which it forwarded this token request. If so, it resends the token request to its neighbor of minimal height.

When the new root receives the token carrying height $\left( h _ { 1 } , h _ { 2 } \right)$ , it adopts height $\left( h _ { 1 } , h _ { 2 } - 1 \right)$ , i.e., a height just smaller than the one of the previous root. After sending this token, the previous root registers that the height of the new root is $\left( h _ { 1 } , h _ { 2 } - 1 \right)$ and ignores height updates from the new root until it receives the height update $\left( h _ { 1 } , h _ { 2 } - 1 \right)$ ,. Else it could wrongly increase its value of the height of the new root.

,If a node $p$ notices a neighbor $q$ disappeared from its range, $p$ checks whether $q$ occurs in its queue, and if so, removes it. If $p$ is a nonroot and has no more outgoing edges in the sink graph, it forges a new outgoing edge, by increasing its height. If (nonroot) $p$ has an outstanding token request at $q$ , then $p$ sends the token request to another neighbor. When a new link is formed in the MANET, the two nodes at either side exchange their heights.

Example 18.7 We consider one possible scenario of the Walter-Welch-Vaidya algorithm on a MANET of four nodes. Arrows represent the sink graph and the nodes carry their height and queue. Note that each edge is directed from the node with greater to the node with smaller height. Initially, as depicted at the left-hand side, for nodes 1 and 2 their IDs serve as tiebreaker. Node 0 is the root and nodes 2 and 3 have issued token requests, which have both reached (the queue of) the root.

![](images/438aef1e39a9991e9dfa46a9daa378e6b751bb90989e0a80ff6249cf66e53b59.jpg)

![](images/076fef0484de08a86cbf3778f600fde0a0ecd2e10f7715a7f964cb494e8d26e7.jpg)

Next, nodes 0 and 3 move outside of each other’s ranges, so that this link disappears. At the right-hand side is depicted how this changes the layout. When the root 0 notices its link to node 3 disappeared, it removes 3 from its queue. Meanwhile, because all edges of node 3 have become incoming, it changes its height to $( 1 , 1 )$ , in view of the heights (0 2) of its neighbors 1 and 2. Next, node 3 reroutes its token request to node 1, , ,because nodes 1 and 2 have the same height and 1 has the smaller ID of the two. Node 1 notices that node 3 has increased its height, so that all edges of node 1 have become incoming, and changes its height to $( 1 , 0 )$ , in view of the heights (0 2) and $( 1 , 1 )$ , of its neighbors 2 and 3. Moreover, by node 3’s token request, node 1 , ,adds 3 to its (empty) queue and as a result sends a token request to node 2, who adds 1 to its queue.

The Walter-Welch-Vaidya algorithm provides mutual exclusion, and if the network stays connected and the token is never lost, then it is starvation-free. If the network moreover remains stable, the sink graph will eventually always be acyclic and rooted in the node that holds the token or toward which the token is traveling.

# 18.5 Cao-Singhal Checkpointing Algorithm

In section 3.3, the uncoordinated Peterson-Kearns checkpointing algorithm was discussed, in which processes save checkpoints independently and log their messages. After a crash, a rollback is performed to a consistent snapshot, i.e., a configuration that may have existed during the ongoing execution. The Cao-Singhal algorithm is a coordinated checkpointing algorithm for MANETs, in which nodes synchronize their checkpointing activities to determine a consistent snapshot without the need for a rollback.

The use of stable storage is particularly cumbersome and expensive in a MANET. A key aim of the CaoSinghal algorithm therefore is to minimize this. A node may take what is called a mutable checkpoint, which is not stored in stable storage immediately, but only if it turns out this checkpoint is needed for the snapshot.

It is assumed there is a wired FIFO network of fixed base stations with which the mobile nodes communicate wirelessly. All nodes in the range of some base station can communicate with each other through the wired network. While a node $p$ is outside the range of all base stations, it cannot communicate with any of the other nodes. During this period of time, $p$ ’s events are not causally before events at other nodes, so from a checkpointing perspective they are irrelevant to other nodes. Just before moving outside the range of all base stations, $p$ takes a checkpoint and sends sufficient information to a base station that enables it to play $p$ ’s role in a checkpointing run. When $p$ reconnects to a base station, it sends its state changes and in return receives buffered messages and information on e.g. checkpoints taken during $p$ ’s absence.

Each node $p$ maintains the sequence number $c s n _ { p } [ p ]$ of the last checkpoint it performed and attaches this number to all messages it sends. Since this field is increased by 1 also when $p$ takes a mutable checkpoint, the sequence number of the last checkpoint $p$ stored in stable storage is kept in old- $. c s n _ { p }$ . Only part of the network nodes may participate in a checkpointing run, so sequence numbers at the nodes are generally not in sync. Therefore, for each other node $q , p$ stores in $c s n _ { p } [ q ]$ the most recent sequence number it received in a message from $q$ .

The initial state counts as the first checkpoint of each node, with sequence number 0. The Cao-Singhal algorithm is nonblocking, in the sense that after taking a checkpoint, nodes can proceed to perform basic events without delay. For simplicity, the following explanation assumes there are no concurrent checkpointing runs by different initiators. These can be treated without serious complications, by letting nodes maintain the bookkeeping and add information to sent messages for all checkpointing runs they are participating in.

Before a node $p _ { 0 }$ initiates a checkpointing run, it increases $c s n _ { p _ { 0 } } [ p _ { 0 } ]$ and $o l d - c s n _ { p _ { 0 } }$ by 1 and takes a checkpoint, which it tentatively saves in stable storage. Then $p _ { 0 }$ sends a checkpoint request to the nodes from which it received a basic message after its last permanent checkpoint in stable storage, to prevent these messages from becoming orphans in the computed snapshot. Those nodes may then in turn take checkpoints and send checkpoint requests and basic messages that induce receivers to take a checkpoint, et cetera. The weight-throwing scheme (see section 6.4) is applied to detect termination of this run, so positive weights are attached to checkpoint requests in this run and nodes that complete their tasks in the run return their remaining weight to $p _ { 0 }$ . These control messages moreover carry what is called the trigger of the checkpointing run, consisting of $p _ { 0 }$ ’s $\mathrm { I D }$ and its sequence number $c s n _ { p _ { 0 } } [ p _ { 0 } ]$ at the start of the run. Nodes participating in a checkpointing run also include the corresponding trigger in the basic messages they send.

A checkpoint request from a node $p$ to a node $q$ includes $c s n _ { p } [ q ]$ . When this request arrives, $q$ checks whether $c s n _ { p } [ q ] < o l d \ – c s n _ { q }$ . If so, $q$ saved a checkpoint in stable storage after sending basic messages to $p$ <that triggered this checkpoint request, which means $q$ does not need to take a checkpoint now. In this case, or if $q$ already (tentatively) saved a checkpoint in stable storage during this run, $q$ simply returns the weight in the checkpoint request to the initiator. Else, it proceeds as follows. If $q$ did not yet take a mutable checkpoint during this run, then it first increments $c s n _ { q } [ q ]$ by 1 and takes a checkpoint. The value of $c s n _ { q } [ q ]$ is copied to $o l d \ – c s n _ { q }$ and $q$ ’s checkpoint is tentatively saved in stable storage. Next, $q$ sends checkpoint requests to nodes from which it received basic messages between its last permanent checkpoint in stable storage and the checkpoint during this run. Any remaining weight is returned to $p _ { 0 }$ . To reduce the number of checkpoint requests, nodes piggyback on checkpoint requests their knowledge on which nodes were sent a checkpoint request in this run and with which sequence number. $q$ does not send checkpoint requests to nodes $r$ of which it knows they were already sent a checkpoint request for this run with a sequence number $c s n _ { s } [ r ] \geq c s n _ { q } [ r ]$ by some other node $s$ .

When a node $q$ receives a basic message from a node $p$ , it records that a basic message was received from $p$ after $q$ ’s last checkpoint. If the value of $c s n _ { p } [ p ]$ in this message is greater than $c s n _ { q } [ p ]$ , then $q$ sets $c s n _ { q } [ p ]$ to the value of $c s n _ { p } [ p ]$ and checks by means of the trigger in the received message whether $p$ is participating in a checkpointing run. If so, $q$ moreover checks whether: (1) it did not send a basic message since its last checkpoint (during this run, or else since its last permanent checkpoint in stable storage), or (2) the sequence number of initiator $p _ { 0 }$ at the start of this run is smaller or equal to $c s n _ { q } [ p _ { 0 } ]$ . In either case, $q$ does not need to take a checkpoint. In the first case because so far in this run no node depends on $q$ ; if $q$ is not yet participating in this run, it starts doing so and increases $c s n _ { q } [ q ]$ by 1. In the second case because $q$ received basic messages from $p _ { 0 }$ after it initiated the run, meaning $q$ is already participating in this run or $p$ sent these messages after the run completed. If both cases do not hold and $q$ is not yet partipating in this run, it increases $c s n _ { q } [ q ]$ by 1 and takes a mutable checkpoint, before processing the received basic message. This prevents the message from becoming an orphan in the computed snapshot. The checkpoint is not yet stored in stable storage and $q$ does not yet send checkpoint requests because $q$ is unsure whether its checkpoint is going to be needed for the snapshot, i.e., whether it will receive a checkpoint request in this run.

When initiator $p _ { 0 }$ has regained all weight, it makes its tentative checkpoint in stable storage permanent. Then it broadcasts a commit message to all nodes in the network, similar to the two-phase commit protocol (see section 16.2). Upon receipt of this message, other partipants in this checkpointing run also make their tentative checkpoints in stable storage permanent, while mutable checkpoints are discarded. This completes the checkpointing run.

If it is detected a node participating in a checkpointing run crashed before it may have stored its checkpoint in stable storage, one option is to abort the entire run. Nodes that tentatively stored a checkpoint in stable storage must then decrease their value of old-csn. Nodes can restart their basic execution from their last permanent checkpoints in stable storage. An alternative approach is to allow a node to make its checkpoint in stable storage permanent as soon as all nodes it depends on in the checkpointing run have saved their checkpoints in stable storage (see exercise 18.18). An advantage is that in case of a crash, nodes that do not depend on the crashed node can still make their checkpoints permanent. Nodes that depend on the crashed node, inevitably including the initiator $p _ { 0 }$ , must discard their checkpoints.

Example 18.8 The picture below shows the time line of events at five nodes $p _ { 0 } , q , r , s .$ , and $t$ with regard to some basic computation, where real time progresses from left to right. Checkpoints are marked with a cross; a circle is drawn around the mutable checkpoint that is never saved in stable storage. Suppose all nodes have sequence number 0 at the left-hand side of the picture. Basic messages are drawn as solid arrows and checkpoint requests as dashed arrows. Control messages in which nodes return weight to the initiator and commit messages are excluded from the picture.

![](images/7c33d25f656fbd31dd1bc72046518b7f6964a407facc16d558300ad9faf7dfe5.jpg)

Initiator $p _ { 0 }$ increases $c s n _ { p _ { 0 } } [ p _ { 0 } ]$ and old- $c s n _ { p _ { 0 } }$ to 1, takes a checkpoint, and tentatively saves it in stable storage. In view of basic message $m _ { 1 }$ , $p _ { 0 }$ sends a checkpoint request to $r _ { \cdot }$ . Next, $p _ { 0 }$ receives basic message $m _ { 3 }$ from $t$ and sends basic messages $m _ { 4 } , m _ { 6 }$ , and $m _ { 7 }$ to $q , t$ , and $q$ , respectively. When $t$ receives $m _ { 6 }$ , it increases $c s n _ { t } [ t ]$ to 1 and takes a mutable checkpoint before processing $m _ { 6 }$ . When $q$ receives $m _ { 4 }$ , it increases $c s n _ { q } [ q ]$ to 1 but does not take a checkpoint, because it did not send a basic message since its last permanent checkpoint in stable storage, or rather, since it started its execution. Next, $q$ sends basic message $m _ { 5 }$ to $r$ . When $q$ receives $m _ { 7 }$ , again it does not take a checkpoint, this time because it is already participating in this run. When $r$ receives $m _ { 5 }$ , it increases $c s n _ { r } [ r ]$ to 1 and takes a mutable checkpoint before processing $m _ { 5 }$ . When $r$ receives the checkpoint request from $p _ { 0 }$ , it increases old- $. c s n _ { r }$ to 1 and tentatively saves its mutual checkpoint in stable storage. Moreover, in view of basic message $m _ { 2 }$ , $r$ sends a checkpoint request to $s$ . When $s$ receives this checkpoint request, it increases $c s n _ { s } [ s ]$ and old- $. c s n _ { s }$ to 1, takes a checkpoint, and tentatively saves it in stable storage. Finally, $p _ { 0 }$ regains all weight and broadcasts commit messages, after which $p _ { 0 } , r _ { : }$ , and $s$ make their tentative checkpoints in stable storage permanent. On the other hand, $t$ discards its mutable checkpoint and decreases $c s n _ { t } [ t ]$ to 0.

# Bibliographical notes

The Chord protocol was proposed in [112]. The AODV protocol was described in [93]. The VasudevanKurose-Towsley algorithm originates from [123]. The Walter-Welch-Vaidya algorithm stems from [125] and the approach in this algorithm to maintain a dynamic sink graph toward the root from [48]. The Cao-Singhal algorithm was presented in [19].

# 18.6 Exercises

Exercise 18.1 Consider the Chord ring in example 18.1.

(a) Suppose the peer at $\textrm { I D } 3 8$ wants to obtain a file with ID 29. Explain how the peer locates this file by means of its finger table.   
(b) Suppose the peer at ID 51 leaves the ring. Explain what happens.   
(c) Let $K = 4$ . Suppose the peers at IDs 1, 8, and 14 crash. Explain what happens at the peer at ID 56.

Exercise 18.2 Give an example to show how in the Chord ring, a search for a file by a peer $p$ may overshoot its target due to an improper succ value at another peer $q$ , resulting from a recently joined peer $s$ . Also explain how the peer $r$ who gets the request that overshoot its target could act to resolve this matter.

Exercise 18.3 In the Chord ring, let peers $r$ and $s$ concurrently join the ring between $p$ and its successor $q$ , where $r$ is the new successor of $p$ and $s$ the new predecessor of $q$ .

(a) Explain how $r$ and $s$ discover each other through the stabilization procedure. (b) Explain how it may occur that $s$ receives files from $q$ that should be located at $r$ instead. How is this resolved?

Exercise 18.4 Suppose a hash collision occurs in the Chord ring, in the sense that a peer joining the ring gets an ID assigned that is already occupied by another peer in the ring. Explain how this can be resolved.

Exercise 18.5 Consider example 18.2, in which a peer $q$ joins the Chord ring at ID 29. Explain in detail how $q$ computes its initial finger table.

Exercise 18.6 Consider the MANET from example 18.4. Suppose that, after $p$ has established a route to $\nu$ , $q$ also wants to find a route to $\nu$ . Explain which steps are taken according to the AODV protocol to establish this route. Consider two scenarios: one in which the route is established via $p$ , and one in which the route is established via $r$ .

Exercise 18.7 Suppose that in the previous exercise the route from $q$ to $\nu$ was established via $r$ . Suppose moreover that the link between $u$ and $\nu$ breaks. Explain how $p$ and $q$ are notified that their routes to $\nu$ have been disabled.

Exercise 18.8 Sketch how the AODV protocol can be adapted to allow a node to look for multiple minimum hop routes to different destinations with the broadcast of a single RREQ message.

Exercise 18.9 Vasudevan, Kurose, and Towsley require for their election algorithm that edges are FIFO Explain why this requirement is redundant.

Exercise 18.10 Suppose that in the Vasudevan-Kurose-Towsley algorithm, only neighbors of the leader are responsible for detecting whether the leader disappeared. Explain how this could lead to a problem and suggest a possible solution.

Exercise 18.11 Suppose that in the MANET depicted at the left-hand side in example 18.7, node 0 leaves its critical section. Explain how the token is forwarded through the network by the Walter-Welch-Vaidya algorithm, where first node 3 and then node 2 becomes privileged, and how this changes the layout, including heights and buffers.

Exercise 18.12 Suppose that the Walter-Welch-Vaidya algorithm is adapted as follows: after the previous root, at height $\left( h _ { 1 } , h _ { 2 } \right)$ , forwards the token, it takes height updates from the next root into account immediately ,(instead of only until it receives $\left( h _ { 1 } , h _ { 2 } - 1 \right)$ from the next root). Give an example to show that then the old ,root could wrongly increase the height of the new root.

Exercise 18.13 Consider heights $\left( h _ { 1 } , h _ { 2 } \right)$ in the Walter-Welch-Vaidya algorithm.

(a) Argue that the minimum $h _ { 1 }$ -value in the network never decreases during computations. (b) Give an example in which the minimum $h _ { 2 }$ -value in the network increases during a computation (while no node crashes).

Exercise 18.14 Consider height changes in the Walter-Welch-Vaidya algorithm.

(a) If the new root has a smaller ID than the previous root, could the new root adopt as new height the same height $\left( h _ { 1 } , h _ { 2 } \right)$ as the previous root (instead of $( h _ { 1 } , h _ { 2 } - 1 ) )$ ?   
,(b) Let a nonroot with ID $i$ ,increase its height. If it finds that among its neighbors of minimal weight there is (at least) one with an ID $j < i$ , could it then adopt the same height as that node?

Exercise 18.15 (a) In the Walter-Welch-Vaidya algorithm, what is the advantage of using a pair of values $\left( h _ { 1 } , h _ { 2 } \right)$ instead of a single value $h ?$

(b) Why does a node, when all its edges have become incoming, not change its height as follows, to push its height above only one of its neighbors? For the first parameter, pick the minimum $k _ { 1 }$ among the $h _ { 1 }$ -values of its neighbors. For the second parameter, if $k _ { 2 }$ is the minimum among the $h _ { 2 }$ -values of its neighbors with $h _ { 1 }$ -value $k _ { 1 }$ , then pick $k _ { 2 } + 1$ .

Exercise 18.16 Explain how sequence numbers can be used to make the Walter-Welch-Vaidya algorithm operate correctly if edges are not FIFO.

Exercise 18.17 The picture below shows the time line of events at five nodes $p _ { 0 } , q , r , s$ , and $t$ with regard to some basic computation, where real time progresses from left to right.

![](images/d7b74c83422139e9a63d5a6770df4ab4ec9ec4774f09c7a4cbc7b5d37b2864d6.jpg)

Explain in detail how the five nodes perform checkpoints using the Cao-Singhal algorithm. Take into account different moments at which checkpoint requests may arrive at their destinations.

Exercise 18.18 (a) Formally define the “depends on” relation for the Cao-Singhal algorithm mentioned in the last paragraph of section 18.5.   
(b) [62] Explain how the Cao-Singhal algorithm can be adapted to allow that a node makes its checkpoint in stable storage permanent as soon as all nodes it depends on in this checkpointing run have saved their checkpoints in stable storage.

Exercise 18.19 Explain how the description of the Cao-Singhal algorithm can be refined to cope with concurrent checkpointing runs by different initiators.

# Security

Distributed computer systems can be vulnerable to hostile attacks. An eavesdropper may secretly listen to a private message exchange, or an unauthorized intruder may steal or modify parts of a database. An information security system aims to prevent such attacks and provide confidentiality, integrity, and availability of messages and data. Confidentiality means that information is never disclosed to unauthorized entities. Integrity means that the accuracy and completeness of information are preserved at all times. Availability means that information is accessible when needed.

A wide range of standard attacks exist to try and violate these properties. Confidentiality can, for example, be threatened by a spoofing attack in which the attacker masquerades as another. A particular instance is the person-in-the-middle attack, in which the attacker secretly relays messages between two parties which believe they are communicating directly with each other. In a replay attack, a valid data transmission from the past is maliciously repeated by an adversary who intercepted the data and retransmits it. Integrity may be violated by an unauthorized intruder who manages to obtain write access in a database. Availability can be threatened by a denial-of-service attack, in which a large flood of simultaneous messages, usually sent from many sources, forces the target system to shut down.

This chapter presents some methods to defend a distributed system against certain kinds of hostile attacks. First, a few standard techniques are discussed, followed by five security protocols that exploit some of these techniques. The Kerberos authentication protocol allows one party to prove its identity to another party in an insecure environment. With the Diffie-Hellman key exchange protocol, two parties can construct a secret only known to them via a public channel. The Merkle signature lets the recipient of a piece of information establish with certainty its origin as well as its integrity. A blockchain, which underlies the Bitcoin protocol for secure financial transactions in P2P networks, exemplifies how consensus can be reached in an open environment if a significant majority of peers is trustworthy. Quantum cryptography protects channels from eavesdropping through the use of quantum mechanics.

# 19.1 Basic Techniques

This section presents some important mechanisms for building secure distributed systems. Cryptographic hash functions, which cannot be inverted by an attacker, are an essential tool for authentication. Symmetricand public-key cryptosystems serve as a backbone for secure communication. And proof-of-work requires that a simple task, such as sending an email, may be performed only after spending a huge amount of effort solving some meaningless puzzle. The purpose is to deter prospective attackers.

# Cryptographic Hash Function

A hash function (which was already encountered in section 18.1) maps elements from a large and possibly heterogeneous data domain $D$ to a usually much smaller data domain $E$ in which all elements have a fixed length. Inevitably, hash collisions may occur, meaning that two different elements of $D$ hash to the same value in $E$ . Computing the hash value of an element in $D$ is required to be easy. Originally hash functions were developed to fit elements from a vast data domain into a table of fixed size and perform fast lookups.

A cryptographic hash function $h : D \to E$ has an important additional property:

• Collision resistance: It is very hard to find different $d , d ^ { \prime } \in D$ with $h ( d ) = h ( d ^ { \prime } )$

As a consequence, cryptographic hash functions also satisfy the following property:

• Preimage resistance: Given an $e \in E$ , it is very hard to find a $d \in D$ with $h ( d ) = e$

One important application of cryptographic hash functions is that passwords for user authentication are not stored, but their hash values are stored instead. When a password is entered by a user, its hash value is compared with the corresponding value in the database. The chance that an erroneous password happens to have the same hash value as the correct one is negligible. The big advantage of storing hashed passwords is in the unfortunate circumstance of a security breach in which an intruder secretly steals the database of hashed passwords. Thanks to preimage resistance, the attacker will still have a very hard time finding an acceptable password. Actually, since passwords tend to be relatively short, hash values of what are called salted passwords are stored, meaning that some (randomly generated) piece of data is attached to a password before the hash value is computed; the salt is stored in combination with the hash value of the salted password. This defends against e.g. a dictionary attack in which hash values of large numbers of possible passwords are precomputed by the attacker. Other important applications of cryptographic hash functions will be discussed in the remainder of this chapter.

Developing collision-resistant hash functions, and checking that cryptographic hash functions used in practice possess this property, has turned out to be a huge challenge. For example, the widely employed functions SHA-1 and MD5 were in the end shown to have serious vulnerabilities and fell from grace.

The birthday attack aims to break collision resistance by exploiting the birthday paradox: after generating the hash values of approximately $\sqrt { | { \cal E } | }$ randomly selected elements in $D$ , where $| E |$ denotes the number of elements in $E$ , one can expect to have found some collision. The name of this paradox refers to the fact that as a consequence, the probability of two persons in a room sharing the same birthday increases surprisingly quickly with the total number of people in the room. A widely used cryptographic hash function like SHA256 hashes to bit strings of length 256, meaning that the birthday attack requires roughly $2 ^ { 1 2 8 }$ hash values before one can expect to find a collision, which is currently considered a safe margin.

In the Merkle tree data structure, the leaves of the tree are data blocks, while each nonleaf carries the hash value of its children. The Merkle root at the top of the tree is a fingerprint of the data blocks in the leaves. If a cryptographic hash function is employed, then the Merkle root can be used to verify the integrity of the data blocks in the leaves of the corresponding Merkle tree. Suppose a collection of large data blocks is obtained from an untrusted source in the form of a Merkle tree, and its Merkle root can also be acquired from a trusted source or from a large number of sources, of which the vast majority are honest. If the Merkle root of the tree is found to be correct, the data is uncorrupted. An advantage of the tree structure, in comparison to the linear hash list data structure, is that branches of the tree can be downloaded and verified individually.

# Symmetric-Key and Public-Key Cryptography

The field of cryptography develops techniques for secure communication, primarily through the use of encryption techniques that turn sensible data into what appears to be nonsense by means of an encryption key. An eavesdropper should be unable to make sense of the resulting encrypted data without knowing the decryption key, which turns the encrypted data back into its origin.

Traditionally cryptography was mostly based on symmetric-key encryption schemes, where the encryption and decryption keys are identical or can be turned into each other by a simple transformation. A classical simplistic example is a technique employed by Julius Caesar, who encrypted secret messages by shifting each letter three places upward in the alphabet. A vulnerability of symmetric-key cryptography is that all intended recipients of secret information need to know the decryption key and therefore can derive the encryption key. A hostile intruder may secretly manage to steal the decryption key from a trusted recipient, or such a recipient may have bad intentions and abuse the encryption key. Ideally, a symmetric key is therefore shared with only one, trusted party. Symmetric-key cryptography tends to provide secure communication between two parties that trust each other and need to build a private key together before starting their communication. Both encryption and decryption of information is performed based on this key, which should therefore be known only to the two parties involved. The Advanced Encryption Standard (AES) is a widely used method for symmetric-key cryptography.

A public-key cryptosystem is a symmetric counterpart of the signature scheme explained in section 13.4. It consists of finite (but very large) domains $\mathcal { M }$ of messages, called plaintexts, and $\mathcal { E }$ of encryptions, called cyphertexts. For each process $p$ there are functions $P _ { p } : \mathcal { M } \to \mathcal { E }$ and $S _ { p } : { \mathcal { E } }  { \mathcal { M } }$ with $S _ { p } ( P _ { p } ( m ) ) = m$ for all $m \in \mathcal { M }$ . (In particular, $P _ { p }$ is injective and $S _ { p }$ is surjective.) An entity makes its public key $P _ { p }$ for encryption openly known to everybody but keeps its private key $S _ { p }$ for decryption secret. Vital for the robustness of this approach is that although the private key is the inverse of the public key, it should be infeasible to reconstruct the private key from the public one. To send a secret message to an entity, the sender applies the public key of that entity to the message beforehand. After reception, the entity applies its private key to obtain the original message. An eavesdropper can do nothing with the encrypted message without knowing the corresponding private key.

New entities in the network create a fresh private/public key pair and publish the public key through a trusted key server. A trusted certificate authority links entities in the network to private/public key pairs and upon request dispenses public keys of entities, encrypted with the private key of the certificate authority. The recipient can decrypt such a message by using the public key of the certificate authority. This prevents an attacker from spreading bogus public keys.

The RSA cryptosystem yields a private and a public key that are each other’s inverses, with the desired property that computing the private key from the public key is hard. It exploits a basic equality from number theory. For all prime numbers $p$ and $q$ , natural numbers $m$ with $m = 1$ mod $\left( p - 1 \right) \cdot \left( q - 1 \right)$ , and integers $k$ ,

$$
k ^ { m } = k \mathrm { m o d } p { \cdot } q .
$$

Plaintexts and cyphertexts in RSA both are taken from $\mathbb { Z } / p { \cdot } q \mathbb { Z }$ , i.e., they consist of numbers modulo $p { \cdot } q$ . /To build private and public keys, very large prime numbers $p$ and $q$ are chosen, as well as a (small) positive number $e$ that is relatively prime to $\left( p - 1 \right) \cdot \left( q - 1 \right)$ , meaning that these two numbers do not have any prime factors in common. Then a positive number $d$ is determined such that $d \cdot e = 1$ mod $\left( p - 1 \right) \cdot \left( q - 1 \right)$ . The number $e$ and the product $p { \cdot } q$ are made public; the public key applied to a message $n$ produces $n ^ { e }$ mod $p { \cdot } q$ . On the other hand, the numbers $d , p$ , and $q$ are kept secret; the private key applied to a message $n$ produces $n ^ { d }$ mod $p { \cdot } q$ . Note that applying both the private and the public key to a message $n$ , irrespective of the order in which they are applied, yields $n ^ { d \cdot e } = n$ mod $p { \cdot } q$ by the preceding equation. So these keys are each other’s inverses.

Since $p$ and $q$ are very large, the public information consisting of $e$ and $p { \cdot } q$ is insufficient to efficiently compute $d$ . For this purpose, one first must find the prime factors $p$ and $q$ from their product. No efficient algorithm for prime factorization is known. The only way found so far to break RSA uses a quantum computer based on quantum mechanics. However, the quantum computers built so far have only very limited processing power and thus do not yet pose a serious threat to RSA.

Elliptic curve cryptography is an alternative method for developing a public-key cryptosystem, based on more advanced mathematical notions, particularly elliptic curves over finite fields. This technique is nowadays widely used in practice, because it requires significantly smaller keys compared to, say, RSA to reach the same level of security.

# Proof-of-Work

A proof-of-work is a puzzle that takes a considerable amount of processing power to solve, while it is easy to verify whether a proposed solution is correct. Ideally, the puzzle has many possible solutions and can only be solved by blind guessing, trying out possible solutions until a correct solution is found. A solution to such a puzzle is typically not interesting in its own right; the puzzle is only posed to dissuade attackers from performing a vast number of small tasks with bad intent, such as email spam or a denial-of-service attack. The puzzle is generally related to the task being performed. For example, to deter email spammers, for each email sent a proof-of-work could be required on the basis of the email header. If this puzzle takes a few seconds to solve, it will not trouble legitimate emailers, while spammers will have difficulty generating the required solutions on a massive scale because this requires too much time and computational power.

Another important application of proof-of-work, as we will see in the next section, is in an open network in which not all nodes can be trusted and it is easy to spawn new nodes. An attacker could create many alias nodes that are all under its control and in this way, for instance, dominate some majority vote. A defense against such a so-called Sybil attack is to require a significant proof-of-work for each vote. Then an attacker can only bully the network if it possesses a vast amount of processing power compared to the honest nodes in the network. Ideally, the percentage of correct solutions in the entire space of possible solutions of a puzzle can be adapted easily to increase the difficulty of finding a solution if puzzles are being solved at a faster rate, typically because more processing power has become available in the network.

# 19.2 Kerberos Authentication Protocol

A serious security risk in a distributed computer system is that an attacker manages to obtain secret information by impersonating as some trusted entity. Authentication, meaning the verification of the identity of a network entity, is therefore an important security measure. Authentication over a computer network by means of a password is often a bad idea, as it may be intercepted by an eavesdropper. The Kerberos authentication protocol enables an entity in an insecure network to prove its identity to another entity without sending data over the network that could be misused later by an attacker. It is named after the three-headed dog that in Greek mythology guards the gate of Hades, where souls go after death. The protocol is widely used as a default method for authentication in large computer networks.

A nonce, short for number used once, is an arbitrary number, typically randomly generated, that is included in a message exchange with the aim to achieve a secure communication. For each message exchange a new nonce must be generated. A nonce often includes a time stamp to avoid a replay attack, in which an eavesdropper uses old messages it overheard with bad intent, typically as part of a spoofing attack.

Kerberos is based on the Needham-Schroeder authentication protocol that employs symmetric-key cryptography. Each process is required to have its symmetric key registered at an authentication server, which acts as a trusted third party. Suppose a process $p$ wants to authenticate itself to another process $q$ and construct a fresh so-called session key for secure communication with $q$ based on symmetric-key cryptography. Then $p$ starts by contacting authentication server $A$ , to obtain this session key and a newly forged ticket it can show to $q$ . The plaintext message from $p$ to $A$ has the form $\left( p , q , n _ { p } \right)$ with $n _ { p }$ a fresh nonce generated at $p$ . Upon receiving this message, $A$ looks up the symmetric keys $K _ { p }$ , ,and $K _ { q }$ of $p$ and $q$ and generates a fresh (symmetric) session key $K _ { p q }$ . This key plays a central role in the authentication of $p$ to $q$ and can afterwards be used for secure communication between $p$ and $q$ . The ticket constructed by $A$ consists of the pair $( p , K _ { p q } )$ encrypted with $q$ ’s symmetric key, denoted by $( p , K _ { p q } ) ^ { K _ { q } }$ . Next, $A$ sends the message $( q , n _ { p } , K _ { p q } , ( p , K _ { p q } ) ^ { K _ { q } } ) ^ { K _ { p } }$ to $p$ , where again the superscript $K _ { p }$ refers to the fact that the message has been encrypted, this time with $p$ ’s symmetric key. Since $A$ ’s message is encrypted with $K _ { p }$ , only $p$ can decrypt it and only $A$ can have sent it, as nobody else knows $p$ ’s symmetric key. The pair $q , n _ { p }$ in $A$ ’s message demonstrates to $p$ that this message is in reply to $p$ ’s preceding request to $A$ ,and protects against a replay attack. Now $p$ has obtained the session key $K _ { p q }$ as well as the ticket. Next, $p$ sends the ticket $( p , K _ { p q } ) ^ { K _ { q } }$ to $q$ , which decrypts this message with its symmetric key to also discover the session key $K _ { p q }$ ,. In reply, $q$ generates a fresh nonce $n _ { q }$ and sends $( n _ { q } ) ^ { K _ { p q } }$ to $p$ . Finally, $p$ sends $( n _ { q } - 1 ) ^ { K _ { p q } }$ to $q$ , proving to $q$ that it is communicating with $p$ . Because owing to the parameter $p$ in the ticket, $q$ is certain that next to $q$ and $A$ , only $p$ knows $K _ { p q }$ . The transformation $n _ { q } - 1$ in this last message avoids that an attacker overhearing the message $( n _ { q } ) ^ { K _ { p q } }$ from $q$ to $p$ could simply replay it to $q$ , pretending to be $p$ . Without steps 4 and 5, a replay attack would be possible, in which an intruder intercepts the ticket sent by $p$ in step 3, and then passes it on to $q$ . In summary, the Needham-Schroeder protocol consists of the following five steps between $p , A$ , and $q$ :

$$
\begin{array} { l l } { { 1 . } } & { { p  A : \quad p , q , n _ { p } } } \\ { { 2 . } } & { { A  p : \quad ( q , n _ { p } , K _ { p q } , ( p , K _ { p q } ) ^ { K _ { q } } ) ^ { K _ { p } } } } \\ { { 3 . } } & { { p  q : \quad ( p , K _ { p q } ) ^ { K _ { q } } } } \\ { { 4 . } } & { { q  p : \quad ( n _ { q } ) ^ { K _ { p q } } } } \\ { { 5 . } } & { { p  q : \quad ( n _ { q } - 1 ) ^ { K _ { p q } } } } \end{array}
$$

In the long run, the session key $K _ { p q }$ could be compromised, if an intruder manages to break into $p$ ’s or $q$ ’s computer. A weakness of the Needham-Schroeder protocol is that this intruder, having also overheard the ticket, could then replay steps 3 and 5 of the protocol. This would trick $q$ into falsely verifying that it is communicating with $p$ . Therefore, as a protective measure it makes sense to include time stamps in the message exchange, to guarantee the freshness of messages 3 and 5 and limit the time window in which $p$ can authenticate itself.

In the Kerberos authentication protocol, which was developed for the client-server architecture, a session key and a ticket are obtained separately. The message exchange resembles two consecutive runs of the Needham-Schroeder protocol. Suppose a user wants to establish authenticate with some server. The user’s client contacts the authentication server to obtain a session key, which the client then uses to obtain a ticket at the ticket-granting server. The user at some point needs to provide her password to the client. Note that this is done locally, so without the need to send the password through the network. An advantage of separating the authentication and ticket-granting server is that a user can reuse a session key and ticket from the authentication server at the ticket-granting server for setting up sessions with different servers, without having to repeatedly employ her password. This is important from a security perspective, because providing the user’s password to her client for each separate session or (even worse) caching the password at the client poses a security risk. Tickets carry an expiration time, typically of several hours, which significantly reduces the risk that an attacker manages to reuse a stolen ticket.

A user $U$ who wants to authenticate herself to some server $s$ contacts a client machine $C$ . Then $C$ generates a fresh nonce $n$ and sends the plaintext message $\left( C , U , T , t _ { 1 } , t _ { 2 } , n \right)$ to authentication server $A$ in order to obtain a session key and a ticket with start time $t _ { 1 }$ , , , , ,and expiration time $t _ { 2 }$ . This session key and ticket are intended for establishing a secure communication with ticket-granting server $T$ . In reply, $A$ generates a fresh session key $K _ { C T }$ for secure communication between $C$ and $T$ . Furthermore, $A$ asks the key distribution center to look up the symmetric keys $K _ { U }$ and $K _ { T }$ of $U$ and $T$ , where $K _ { U }$ was generated in the past by applying some cryptographic hash function $h$ to $U$ ’s (salted) password. Then $A$ sends a message to $C$ that consists of two parts, both constructed at the key distribution center. The first part $( n , K _ { C T } ) ^ { K _ { U } }$ of this message communicates the session key to $C$ ; the nonce protects against a replay attack and confirms that the message is in reply to the earlier message from $C$ . After receiving $A$ ’s message, $C$ asks $U$ to type in her password, which it transforms to $K _ { U }$ by means of the hash function $h$ (if $U$ types in the correct password). After decrypting $( n , K _ { C T } ) ^ { K _ { U } }$ to verify the nonce $n$ and obtain the session key $K _ { C T }$ , $C$ can erase $U$ ’s password and $K _ { U }$ from ,its memory, which is important for the security of $U$ ’s password. The second part of $A$ ’s message to $C$ is the ticket $( C , T , t _ { 1 } , t _ { 2 } , K _ { C T } ) ^ { K _ { T } }$ , which can be decrypted only by $T$ . Next, $C$ asks $T$ for a ticket to establish a , , , ,secure communication with $S .$ The message from $C$ to $T$ consists of an informative plaintext part $( S , n ^ { \prime } )$ with $n ^ { \prime }$ a nonce, a part $( C , t _ { 1 } ) ^ { K _ { C T } }$ to authenticate $C$ to $T$ , and the ticket $( C , T , t _ { 1 } , t _ { 2 } , K _ { C T } ) ^ { K _ { T } }$ that $C$ ,received from $A$ . After receiving $C$ ,’s message, $T$ , , , ,decrypts the ticket to uncover the session key $K _ { C T }$ , which it then uses to decrypt the authenticator $( C , t _ { 1 } ) ^ { K _ { C T } }$ ; it authenticates $C$ because only $C$ and $T$ (and $A$ ) know $K _ { C T }$ . Time stamp $t _ { 1 }$ ,in this part of the message protects against a replay attack. Moreover, authentication must be completed within a limited amount of time, the default being five minutes. Next, $T$ generates a fresh session key $K _ { C S }$ for secure communication between $C$ and $s$ and sends it to $C$ in the form $( n ^ { \prime } , K _ { C S } ) ^ { K _ { C T } }$ . Moreover, $T$ asks the key distribution center to look up the symmetric key $K _ { S }$ of $s$ ,and appends a ticket $( C , S , t _ { 1 } , t _ { 2 } , K _ { C S } ) ^ { K _ { S } }$ to its message to $C$ , , , ,; note that this second ticket is constructed in the same way as the first ticket, but with $T$ replaced by $s$ . After receiving $T$ ’s message, $C$ decrypts $( n ^ { \prime } , K _ { C S } ) ^ { K _ { C T } }$ to verify the nonce $n ^ { \prime }$ and obtain the session key

$K _ { C S }$ . Next, $C$ sends a message to $s$ , consisting of a nonce $n ^ { \prime \prime }$ , a part $( C , t _ { 1 } ) ^ { K _ { C S } }$ to authenticate $C$ to $s$ , and the ticket that $C$ received from $T$ . After receiving $C$ ’s message, $s$ ,decrypts the ticket $( C , S , t _ { 1 } , t _ { 2 } , K _ { C S } ) ^ { K _ { S } }$ to uncover the session key $K _ { C S }$ , which it then uses to decrypt the authenticator $( C , t _ { 1 } ) ^ { K _ { C S } }$ , , ,. Finally, $s$ sends the authenticator $( n ^ { \prime \prime } ) ^ { K _ { C S } }$ to $C$ , so that $C$ can be certain it is communicating with $s$ . In summary, the Kerberos protocol consists of the following six steps between $C , A , T$ , and $s$ :

$$
\begin{array} { r l } { { 1 . } } & { { C  A : \quad C , U , T , t _ { 1 } , t _ { 2 } , n } } \\ { { 2 . } } & { { A  C : \quad ( n , K _ { C T } ) ^ { K _ { U } } , ( C , T , t _ { 1 } , t _ { 2 } , K _ { C T } ) ^ { K _ { T } } } } \\ { { 3 . } } & { { C  T : \quad S , n ^ { \prime } , ( C , t _ { 1 } ) ^ { K _ { C T } } , ( C , T , t _ { 1 } , t _ { 2 } , K _ { C T } ) ^ { K _ { T } } } } \\ { { 4 . } } & { { T  C : \quad ( n ^ { \prime } , K _ { C S } ) ^ { K _ { C T } } , ( C , S , t _ { 1 } , t _ { 2 } , K _ { C S } ) ^ { K _ { S } } } } \\ { { 5 . } } & { { C  S : \quad n ^ { \prime \prime } , ( C , t _ { 1 } ) ^ { K _ { C S } } , ( C , S , t _ { 1 } , t _ { 2 } , K _ { C S } ) ^ { K _ { S } } } } \\ { { 6 . } } & { { S  C : \quad ( n ^ { \prime \prime } ) ^ { K _ { C S } } } } \end{array}
$$

Each encrypted part in this message exchange contains a session key or is encrypted with a session key. Moreover, in the message from $A$ and from $T$ to $C$ , the part that communicates the session key is paired with a nonce. These attributes protect against replay attacks.

If $U$ wants to authenticate herself to another server $S ^ { \prime }$ before the ticket obtained from $A$ in step 2 of the Kerberos protocol expires, then $C$ can do so on $U$ ’s behalf without contacting $A$ . It repeats step 3 with $s$ and $n$ in the first part of the message to $T$ replaced by $S ^ { \prime }$ and a fresh nonce. Also steps 4, 5, and 6 are repeated with $s$ replaced by $S ^ { \prime }$ and fresh nonces. Note that these steps do not require $U$ ’s password or $K _ { U }$ .

The authentication and ticket-granting servers form one logical unit with the key distribution center, to safeguard communication of symmetric keys. In very large computer networks, having only one authentication and one ticket-granting server can become a performance bottleneck. In practice, such a network is therefore partitioned into subnetworks called realms, each with its own key distribution center and authentication/ticket-granting servers. A client authenticates herself to servers in other realms through her local key distribution center and authentication and ticket-granting server, together with a chain of trust relations between realms.

# 19.3 Diffie-Hellman Key Exchange Protocol

Let two peers, called Alice and Bob, communicate with each other over a public channel, meaning that eavesdroppers can freely listen in. Suppose Alice and Bob want to set up a secret communication using symmetric-key cryptography, by constructing a private key that is known only to them. The Diffie-Hellman key exchange protocol allows them to do this in a secure manner, in spite of the fact that all their communication can be overheard, by exploiting commutative private mappings. It is important that Alice and Bob employ some form of authentication, to make certain they are communicating with each other directly, as else the Diffie-Hellman protocol would be vulnerable to a person-in-the-middle attack.

First Alice and Bob (publicly) agree on a data domain $D$ and an element $d \in D$ that will serve as the basis for determining the private key. Selecting a different data domain for each key exchange reduces the risk that information leaked in a key exchange can be exploited by an attacker in a future key exchange. Alice and Bob both choose a private mapping, $S _ { A } : D  D$ and $S _ { B } : D  D$ , respectively. It is essential that these mappings are guaranteed to be commutative: $S _ { A } ( S _ { B } ( e ) ) = S _ { B } ( S _ { A } ( e ) )$ for all $e \in D$ .

Both Alice and Bob apply their private mapping to $d$ and send the result to their partner; Alice sends $S _ { A } ( d )$ to Bob and Bob sends $S _ { B } ( d )$ to Alice. Next, both Alice and Bob apply their private mapping to the data element they receive; Alice computes $S _ { A } ( S _ { B } ( d ) )$ and Bob computes $S _ { B } ( S _ { A } ( d ) )$ . By the commutativity property, these two data elements coincide. This result constitutes the private key of Alice and Bob.

The information leaked via the public channel is: the domain $D$ , the element $d$ , and the data elements $S _ { A } ( d )$ and $S _ { B } ( d )$ . The private mappings must be defined in such a way that this information is insufficient to readily compute the private key determined by Alice and Bob.

In the original paper that presented the Diffie-Hellman protocol, domains $D$ consist of $( \mathbb { Z } / p \mathbb { Z } ) ^ { * }$ for very large prime numbers $p$ , i.e., the numbers modulo $p$ /except the zero element, with (only) a multiplicative structure. The element $d$ is what is called a primitive root modulo $p$ , meaning that each nonzero element of the numbers modulo $p$ is a power of $d$ . It is a well-known arithmetic fact that a primitive root exists for each prime number $p$ , and a primitive root can be determined in an efficient fashion. The private mappings of Alice and Bob are power functions: $S _ { A } ( k ) = k ^ { a }$ mod $p$ and $S _ { B } ( k ) = k ^ { b }$ mod $p$ for certain very large integers $a$ and $^ b$ , which Alice and Bob keep secret. Clearly, the required commutativity property holds: $S _ { A } ( S _ { B } ( k ) ) =$ $S _ { B } ( S _ { A } ( k ) ) = k ^ { a \cdot b }$ mod $p$ for all integers $k$ . No efficient general method is known to compute a value $\ell$ if only the values $p , k$ , and $k ^ { \ell }$ modulo $p$ are known (and $p$ and $\ell$ ℓare very large numbers); this is called the discrete logarithm problem. So from the values $p , d , d ^ { a }$ mod $p$ ℓ, and $d ^ { b }$ mod $p$ , an attacker cannot effectively compute the values $a$ and $^ b$ . Hence, in spite of the publicly shared information between Alice and Bob, their private mappings remain secure and their shared private key $d ^ { a \cdot b }$ mod $p$ can be computed only by them.

Example 19.1 Let $p = 7$ . The domain $D$ consists of the nonzero numbers modulo 7, i.e., $( \mathbb { Z } / 7 \mathbb { Z } ) ^ { * } =$ $\{ 1 , 2 , 3 , 4 , 5 , 6 \}$ /. The primitive roots modulo 7 are 3 and 5. Alice and Bob publicly select the modulo 7 do, , , , ,main and the primitive root 3 as the basis for computing their private keys. For their private mappings, Alice and Bob choose $a = 2$ and $b = 3$ , respectively. (In reality, of course, much larger values must be chosen for $p , a$ , and $^ b$ , to provide a high level of security.) Since $3 ^ { 2 } = 9 = 2$ mod 7, Alice sends 2 to Bob. Likewise, since $3 ^ { 3 } = 2 7 = 6$ mod 7, Bob sends 6 to Alice. Next Alice computes $6 ^ { 2 } = 3 6 = 1$ mod 7 and Bob computes $2 ^ { 3 } = 8 = 1$ mod 7. So the private key shared between Alice and Bob is 1.

The elliptic curve Diffie-Hellman protocol is more widely used in practice than the original one based on modulo arithmetic, as it offers comparable security with much smaller keys.

# 19.4 Quantum Cryptography

The Huygens-Fresnel principle states that every point in space that is reached by a wave becomes a source of a spherical wave. This effect becomes apparent if a wave in the water encounters a wall with a small hole. At the other side of the wall, the wave continues in a semicircular shape, with the hole at its center. If there are two holes close to each other in the wall, the two resulting semicircular waves may together form a standing wave in which the two subwaves at some places amplify each other and at other places cancel each other out. Christiaan Huygens predicted in 1678 that light behaves like a wave. Thomas Young confirmed this claim in a famous double-slit experiment in 1805 showing that a light beam passing through two thin slits may on the wall behind it form the pattern of a standing wave consisting of an alternating sequence of brightly lit and dark patches. A paradox, known as wave-particle duality, is that light consists of individual elementary particles called photons that according to the double-slit experiment exhibit wave properties by themselves. On the other hand, if one starts to measure which of the two slits a photon passes through, the interference effect of the double-slit experiment disappears and light passes through the slits in a straight line, forming two bright stripes on the wall behind it.

It turns out that an elementary particle can be in a range of possible states at the same time with a certain probability distribution. This is called a superposition. Interaction with an observer causes the particle to fall back to one of these possible states. A qubit, short for quantum bit, is a binary bit that may be in superposition, basically meaning that it is undecided between 0 and 1. Such a superposition is represented by an expression

$$
\alpha _ { 0 } | 0 \rangle + \alpha _ { 1 } | 1 \rangle .
$$

In physics, $\alpha _ { 0 }$ and $\alpha _ { 1 }$ may be complex numbers (like $i$ with $i ^ { 2 } = - 1$ ), but for our purpose it suffices to restrict α αthem to real numbers, written as $a _ { 0 }$ and $a _ { 1 }$ . (Crucially, they can be negative numbers.) These values indicate what may happen when the qubit falls back from its superposition to a classical deterministic state: with probability $a _ { 0 } ^ { 2 }$ it becomes 0, and with probability $a _ { 1 } ^ { 2 }$ it becomes 1. Since these two probabilities must sum to 1, the pair $\left( a _ { 0 } , a _ { 1 } \right)$ constitutes the coordinates of a point on the unit circle in the two-dimensional plane $\mathbb { R } ^ { 2 }$ , ,which we represent as a vector $\binom { a _ { 0 } } { a _ { 1 } }$ .

![](images/3a46113b8b4186586c6cf7059b5975df770e49ea8ad89e88cd31398108025c1d.jpg)

Although the numbers $a _ { 0 }$ and $a _ { 1 }$ are associated with (nonnegative) probabilities, it is essential that these numbers themselves can be negative, because the operations on qubits that we will now explain range over the entire unit circle.

The no-cloning theorem states that it is impossible to create an identical copy of an elementary particle in an unknown superposition. The underlying idea is that to make a copy, the particle needs to be measured, which inevitably influences the state the particle is in. The no-cloning theorem is fundamental to the BB84 quantum key exchange protocol that will be explained in this section. An eavesdropper cannot make identical copies of qubits sent through a quantum channel, which can carry elementary particles in superposition, but is forced to affect the information flow through the channel while measuring qubits that are in superposition.

# Quantum Operations

Controlled quantum operations can be performed on an elementary particle that transform it from some superposition into another superposition. These are linear operations that can be expressed by $2 \times 2$ matrices.

After such a transformation, probabilities must of course still sum to 1; in other words, the linear operation must map the unit circle in two-dimensional space onto itself. Furthermore, quantum operations are always invertible. A quantum operation (restricted to $\mathbb { R } ^ { 2 }$ ) can be expressed by what is called an orthogonal matrix.

We start with some basic linear algebra. The two-dimensional plane $\mathbb { R } ^ { 2 }$ consists of vectors $\binom { a _ { 0 } } { a _ { 1 } }$ with $a _ { 0 } , a _ { 1 } \in \mathbb { R }$ , representing the point in $\mathbb { R } ^ { 2 }$ with $x$ -coordinate $a _ { 0 }$ and $y .$ -coordinate $a _ { 1 }$ 1. Addition of two vectors is defined by separately adding the $x$ -coordinates and the $y .$ -coordinates: ${ \binom { a _ { 0 } } { a _ { 1 } } } + { \binom { b _ { 0 } } { b _ { 1 } } } = { \binom { a _ { 0 } + b _ { 0 } } { a _ { 1 } + b _ { 1 } } }$ . Likewise, multiplication of a vector with a $c \in \mathbb { R }$ is defined at the level of coordinates: $c \cdot { \binom { a _ { 0 } } { a _ { 1 } } } = { \binom { c \cdot a _ { 0 } } { c \cdot a _ { 1 } } }$

A $2 \times 2$ matrix is a linear operator that maps $\mathbb { R } ^ { 2 }$ to itself. By linearity, it suffices to define such a matrix $M$ cto. A $\binom { 1 } { 0 }$ and  matr $\binom { 0 } { 1 }$ of ere $\mathbb { R } ^ { 2 }$ : the  has $M$ -imagee form eral vector , where the $\binom { a _ { 0 } } { a _ { 1 } }$ in col $\mathbb { R } ^ { 2 }$ in ned by is the $a _ { 0 } { \cdot } M \Big (  _ { 0 } ^ { 1 } \Big ) + a _ { 1 } { \cdot } M \Big (  _ { 1 } ^ { 0 } \Big )$ $2 \times 2$ $\binom { a _ { 0 } \ b _ { 0 } } { a _ { 1 } \ b _ { 1 } }$ $\binom { a _ { 0 } } { a _ { 1 } }$ $M$ 0 1-image of the first base vector and the second column $\binom { b _ { 0 } } { b _ { 1 } }$ a1  is the $M$ a1-image of the second base vector.

Example 19.2 Consider the $2 \times 2$ matrix $\binom { 1 } { 2 } - 1 )$ . It maps the first base vector $\textstyle { \binom { 1 } { 0 } }$ to the first column $\textstyle { \binom { 1 } { 2 } }$ and the second base vector $\binom { 0 } { 1 }$ to the second column $\left( \begin{array} { r } { 3 } \\ { - 1 } \end{array} \right)$ of the matrix. So, for instance, the vector $\left( \begin{array} { r } { { 2 } } \\ { { - 1 } } \end{array} \right)$ is by this matrix mapped to $2 \cdot { \binom { 1 } { 2 } } - 1 \cdot { \binom { 3 } { - 1 } } = { \binom { 2 } { 4 } } + { \binom { - 3 } { 1 } } = { \binom { - 1 } { 5 } } .$

As noted, after performing a quantum operation, the probability mass of all possible states of a superposition must still sum to 1. Therefore, quantum operations (restricted to $\mathbb { R } ^ { 2 }$ ) are associated with an orthogonal matrix, which leaves the length of a vector and the angle between a pair of vectors in $\mathbb { R } ^ { 2 }$ unchanged. In other words, for a $2 \times 2$ orthogonal matrix, the two base vectors of $\mathbb { R } ^ { 2 }$ are mapped to an orthogonal unit basis: vectors of length 1 that are orthogonal to each other, meaning that they have an angle of (plus or minus) 90 degrees. That is, a matrix $\left( { \begin{array} { l } { a _ { 0 } \ b _ { 0 } } \\ { a _ { 1 } \ b _ { 1 } } \end{array} } \right)$ is orthogonal if $a _ { 0 } ^ { 2 } + a _ { 1 } ^ { 2 } = 1$ (the image of the first base vector has length 1), $b _ { 0 } ^ { 2 } + b _ { 1 } ^ { 2 } = 1$ (the image of the second base vector has length 1), and $a _ { 0 } { \cdot } b _ { 0 } + a _ { 1 } { \cdot } b _ { 1 } = 0$ (these two images are orthogonal to each other). Clearly, the matrix of any rotation around the origin $( 0 , 0 )$ of $\mathbb { R } ^ { 2 }$ is orthogonal, and likewise for a reflection in a line through the origin. Actually, each orthogonal $2 \times 2$ matrix with coefficients in $\mathbb { R }$ is a composition of such rotations and reflections.

Let us now return to qubits. You need to make a mental leap in considering the states $| 0 \rangle$ and $| 1 \rangle$ as the base vectors of a two-dimensional space. Accordingly, a superposition $c _ { 0 } \left| 0 \right. + c _ { 1 } \left| 1 \right.$ is represented as the vector $\binom { c _ { 0 } } { c _ { 1 } }$ in tor $\mathbb { R } ^ { 2 }$ . A quantum ope the unit circle in on associated with an orthogo. That is, a quantum operation $2 \times 2$ matrix acts transforms a q to derin and $\mathbb { R } ^ { 2 }$ $\binom { a _ { 0 } \ b _ { 0 } } { a _ { 1 } \ b _ { 1 } }$ $| 0 \rangle$ $a _ { 0 } | 0 \rangle + a _ { 1 } | 1 \rangle$ $| 1 \rangle$ to $b _ { 0 } | 0 \rangle + b _ { 1 } | 1 \rangle$ . Since quantum operations are linear, a qubit in a superposition $c _ { 0 } | 0 \rangle + c _ { 1 } | 1 \rangle$ is transformed to $c _ { 0 } \cdot ( a _ { 0 } | 0 \rangle + a _ { 1 } | 1 \rangle ) + c _ { 1 } \cdot ( b _ { 0 } | 0 \rangle + b _ { 1 } | 1 \rangle ) = ( c _ { 0 } \cdot a _ { 0 } + c _ { 1 } \cdot b _ { 0 } ) | 0 \rangle + ( c _ { 0 } \cdot a _ { 1 } + c _ { 1 } \cdot b _ { 1 } ) | 1 \rangle .$

The Hadamard transform is the quantum operation defined by the orthogonal matrix $\left( { \frac { \frac { 1 } { \sqrt { 2 } } } { \frac { 1 } { \sqrt { 2 } } } } - { \frac { \frac { 1 } { \sqrt { 2 } } } { \sqrt { 2 } } } \right)$ , which is also written as $\textstyle { \frac { 1 } { \sqrt { 2 } } } { \binom { 1 } { 1 } }$ . Note that the minus sign in front of the bottom right coefficient is essential for orthogonality. The Hadamard transform brings $| 0 \rangle$ as well as $| 1 \rangle$ in a superposition where the outcomes 0 and 1 are equally likely. Because $| 0 \rangle$ is transformed into $\textstyle { \frac { 1 } { \sqrt { 2 } } } \left. 0 \right. + { \frac { \mathrm { 1 } } { \sqrt { 2 } } } \left. 1 \right.$ and $| 1 \rangle$ into ${ \scriptstyle { \frac { 1 } { \sqrt { 2 } } } } \left| 0 \right. - { \frac { 1 } { \sqrt { 2 } } } \left| 1 \right.$ .

Example 19.3 Let us apply two consecutive Hadamard transforms on a qubit that is in the (deterministic) state $| 0 \rangle$ or $| 1 \rangle$ .

If it is in state $| 0 \rangle$ , then after the first application it is in the superposition ${ \textstyle \frac { 1 } { \sqrt { 2 } } } \left. 0 \right. + { \textstyle \frac { 1 } { \sqrt { 2 } } } \left. 1 \right.$ . So the second application results in $\begin{array} { r } { \frac { 1 } { \sqrt { 2 } } \cdot ( \frac { 1 } { \sqrt { 2 } } \left| 0 \right. + \frac { 1 } { \sqrt { 2 } } \left| 1 \right. ) + \frac { 1 } { \sqrt { 2 } } \cdot ( \frac { 1 } { \sqrt { 2 } } \left| 0 \right. - \frac { 1 } { \sqrt { 2 } } \left| 1 \right. ) = \left| 0 \right. } \end{array}$ .

If it is in state $| 1 \rangle$ , then after the first application it is in the superposition ${ \scriptstyle { \frac { 1 } { \sqrt { 2 } } } } \left| 0 \right. - { \frac { 1 } { \sqrt { 2 } } } \left| 1 \right.$ . So the second application results in $\begin{array} { r } { \frac { 1 } { \sqrt { 2 } } \cdot ( \frac { 1 } { \sqrt { 2 } } \left| 0 \right. + \frac { 1 } { \sqrt { 2 } } \left| 1 \right. ) ^ { - } - \frac { 1 } { \sqrt { 2 } } \cdot ( \frac { 1 } { \sqrt { 2 } } \left| 0 \right. - \frac { 1 } { \sqrt { 2 } } \left| 1 \right. ) ^ { - } = \bar { | 1 \rangle } } \end{array}$ .

In either case, after performing the two Hadamard transforms, the qubit has returned to its original state. In other words, the Hadamard transform is its own inverse.

# BB84 Quantum Key Exchange Protocol

The fact that a qubit cannot be measured without perturbing its state can be exploited as a cryptographic tool. Different companies spread over the globe have turned quantum cryptography into a commercial product. The most famous example is the BB84 key exchange protocol, which is named after its two inventors Bennett and Brassard and the year in which it was developed. Suppose two peers, called Alice and Bob, want to construct a private key that is known only to them. The BB84 protocol allows them to do this in a secure manner by using qubits. The beauty of this key exchange protocol is that, owing to the nature of superpositions, an eavesdropper cannot avoid disturbing the information flow between Alice and Bob, which will inevitably thwart each attempt to overhear the private key. The price to pay is that an eavesdropper may cause such a serious perturbation of the information flow that the attempt by Alice and Bob to build a private key may fail. Moreover, error correction must be employed at the end, because casual eavesdroppers or quantum noise on the communication channel may have introduced few anomalies in a (successfully computed) private key.

In the BB84 key exchange protocol, Alice starts with a string of $n$ qubits out of which the private key will be constructed. Initially, each qubit is either in state $| 0 \rangle$ or in state $| 1 \rangle$ ; for each qubit, this value is chosen randomly. Alice sends each of the $n$ qubits to Bob via a public quantum channel. For each of these qubits, she randomly chooses to send the qubit either unchanged or after performing the Hadamard transform on it. Likewise, for each of the $n$ received qubits, Bob randomly chooses to measure it either in the state in which it was received or after performing the Hadamard transform on it. If neither Alice nor Bob performed the Hadamard transform on a qubit, then clearly Alice and Bob read the same value for this qubit. And if both Alice and Bob did perform the Hadamard transform on a qubit, then again they read the same value, because the Hadamard transform is its own inverse, as was shown in example 19.3. Since both of them perform their Hadamard transforms in a random fashion, it is expected that on about half of the $n$ qubits they can be certain their values agree. Alice and Bob inform each other, via a public classical (authenticated) channel, on which qubits they performed the Hadamard transform. The values of the (on average, $\frac { n } { 2 }$ ) qubits on which both Alice and Bob either did or did not perform the Hadamard transform can be used to build the private key.

The underlying idea of the protocol is that if an eavesdropper Eve on the quantum channel overhears a qubit on which Alice performed the Hadamard transform, then this may introduce an error. Since the qubit cannot be cloned, it needs to be measured, which typically forces it into a deterministic state $| 0 \rangle$ or $| 1 \rangle$ ; in view of the definition of the Hadamard transform, each of these outcomes occurs with a 50 percent chance. To obtain a substantial amount of information with regard to the private key, Eve is bound to cause a significant perturbation in the values of the qubits read by Bob. To recognize such a perturbation, Alice sends half of the private key to Bob via the public classical channel. For each of these control bits, Bob checks whether Alice’s value agrees with the value he read. If this is the case for all or almost all control bits, then (with very high probability) potential eavesdroppers have gained insufficient information for reconstructing the private key, Alice and Bob can safely build the private key from the values of the other qubits that Bob certainly measured correctly (i.e., of those qubits that were not used as control bits). If this is not the case, then Alice and Bob must start a new attempt to build a private key.

Casual eavesdroppers that measured a handful of qubits over the quantum channel and noise on the quantum channel may introduce a few flaws in the private key. Error correction is used to eliminate such errors in the private key. For instance, a simple error correction scheme is to let Alice divide the private key into pairs of bits and tell Bob the XOR-value of each pair (i.e., the sum of these two bits modulo 2). If Bob has the same XOR-value for such a pair, then Alice and Bob both keep the first bit but discard the second bit, because information about the relation between these two bits was revealed. If their values differ, then they discard both bits, because one of the two bits at Bob’s side is corrupted. The remaining bits form their private key. After error correction, Alice and Bob share the same private key, if Alice did not have the misfortune of pairing two corrupted bits.

Example 19.4 Let $n = 8$ . (In reality, of course, a much larger number must be taken, in order to provide a high level of security.) Let the random initial values of the successive qubits at Alice be 00 101100. Alice randomly decides to apply the Hadamard transform on the first, third, and eighth qubits, and Bob on the second, third, seventh, and eighth qubits. After Alice has communicated to Bob which qubits she applied the Hadamard transform on, Bob determines that he is guaranteed to have measured the correct values for the third, fourth, fifth, sixth, and eighth qubits. So these values can be used to build the private key: 1 0 1 1 0.

Suppose now that Eve measures only the third qubit. Since Alice applied the Hadamard transform on this qubit, its superposition before Eve’s measurement is $\textstyle { \frac { 1 } { \sqrt { 2 } } } \left| 0 \right. - { \frac { 1 } { \sqrt { 2 } } } \left| 1 \right.$ . Suppose that by Eve’s measurement the qubit falls back to the deterministic state 0, so that Bob computes an incorrect value for the third qubit. This anomaly is observed by Bob if the value of the third qubit is part of the control bits that Alice sends to him. Else, error correction will repair this flaw.

# 19.5 Merkle Signature Scheme

From a security perspective, it is often important to establish with certainty the origin of a piece of information as well as its integrity, meaning that its content has not been tampered with. This can be achieved with a digital signature that cannot be forged by an attacker. In section 13.4, the notion of a signature scheme was explained, based on a private key $S _ { p } : \mathcal { M } \to \mathcal { E }$ and a public key $P _ { p } : \mathcal { E }  \mathcal { M }$ for each process $p$ , with $P _ { p }$ the inverse of $S _ { p }$ , where $p$ keeps $S _ { p }$ secret and makes $P _ { p }$ public. Sender $p$ signs message $m$ with the signature $S _ { p } ( m )$ .

This signature scheme is vulnerable to what is called a key-only attack. To create a forgery with the aim of impersonating another entity $p$ , the attacker picks a random signature and applies the public key $P _ { p }$ to compute the message belonging to that signature. Then the attacker sends the computed message together with the signature. To avoid this type of attack, $p$ first applies a publicly known cryptographic hash function to the message that needs to be signed and then the private key $S _ { p }$ to the resulting hash value. The receiver applies $P _ { p }$ to the signature, applies the hash function to the message, and compares the two outcomes. The key-only attack is rendered ineffective because the attacker can only determine the hash of the corresponding message from a signature, while it is required to send the original message along with the signature. A bonus of this adapted digital signature scheme is that the hashed message is usually much shorter than the message itself, so that applying the private key to it requires less effort.

The most common methods to build private/public key pairs, based on modulo arithmetic or elliptic curves, are under threat from the development of quantum computers, because these offer efficient ways to factorize large numbers and to solve the so-called elliptic-curve discrete logarithm problem. Also the discrete logarithm problem that underlies the implementation of the Diffie-Hellman protocol explained in the previous section can be solved efficiently on quantum computers. Although current quantum computers are still in their infancy, it is becoming ever more likely that mature quantum computers will be realized in the not too distant future that can crack certain previously unsolvable mathematical problems. The dawn of quantum computers thus poses a serious threat to large parts of modern cryptography and has spurred research into post-quantum cryptography that is thought to be secure against an attack by a quantum computer.

# Lamport Signatures

The Lamport signature scheme is based on cryptographic hash functions, which so far have stood their ground against quantum computers. It is a one-time signature scheme, in the sense that a Lamport signature can be used for only a single message. The signature is determined with regard to a hash of the original message. Suppose Alice wants to send a message to Bob, the hash of which consists of $k$ bits $a _ { 1 } \cdots a _ { k }$ . Alice constructs a private/public key pair for this message, where the private key is used by Alice to build the signature of the message while the public key is used by Bob to verify this signature. To build this key pair, Alice generates $k$ (very large) random numbers $X _ { i }$ for $i = 1 , \ldots , k$ . Their concatenation $X _ { 1 } \parallel \cdots \parallel X _ { k }$ forms Alice’s private key, while her public key is $h ( h ( X _ { 1 } ) \mid \mid \cdots \mid \mid h ( X _ { k } ) )$ . . ,, for some cryptographic hash function $h$ . For $i = 1 , \ldots , k$ , let $s i g _ { i } = X _ { i }$ if $a _ { i } = 0$ and $s i g _ { i } = h ( X _ { i } )$ if $a _ { i } = 1$ . Alice signs her message with $s i g _ { 1 } \parallel \cdots \parallel s i g _ { k }$ . To verify this signature, Bob computes the hash of Alice’s message, obtains the public key associated to the message, applies $h$ to $s i g _ { i }$ if $a _ { i } = 0$ for $i = 1 , \ldots , k .$ , applies $h$ to the concatenation of the $k$ resulting strings, and checks , . . . ,whether the final result agrees with the public key. Since only Alice knows the private key, only she can generate the signature correctly. Furthermore, if an attacker would change one or more bits in the message, the signature would no longer be valid.

Example 19.5 Let the hash of Alice’s message to Bob be 101. The private key for the signature of this message is of the form $X _ { 1 } \parallel X _ { 2 } \parallel X _ { 3 }$ . The public key is $h ( h ( X _ { 1 } ) \parallel h ( X _ { 2 } ) \parallel h ( X _ { 3 } ) )$ . Alice’s signature is $h ( X _ { 1 } ) \parallel X _ { 2 } \parallel h ( X _ { 3 } )$ . Bob verifies the signature by computing the hash 101 of the message, applying $h$ to the second number in Alice’s signature, applying $h$ to the result, and comparing it to Alice’s public key.

The Lamport signature scheme has two serious disadvantages. First, to achieve a secure signature, the private key (and so the signature) must be of large size. Second, a public key can be used to sign only a single message, because a signature leaks information about the corresponding private key. These two issues will be addressed by the following two signature schemes.

# Winternitz Signatures

The idea behind the Winternitz signature scheme is to let Alice generate one random number per $\ell$ bits in the hash of her message, for some $\ell \geq 1$ . This divides the signature size roughly by $2 \ell$ , at the cost of additional computation time because series of applications of $h$ need to be performed. Again, the hash of Alice’s message to Bob consists of $k$ bits. Let $n = \lceil \frac { k } { \ell } \rceil$ . Alice generates random numbers $X _ { 1 } , \ldots , X _ { n }$ and computes $Y _ { i } = \breve { h ^ { 2 } } ^ { \ell - 1 } ( X _ { i } )$ for all $i = 1 , \ldots , n$ , where $h ^ { j } ( X )$ denotes $j$ ,.consecutive applications of $h$ ,to $X$ . The private , . . . ,key associated to the message is $X _ { 1 } \parallel \cdots \parallel X _ { n }$ , and the public key $h ( Y _ { 1 } \parallel \cdots \parallel Y _ { n } )$ . The outside application of $h$ reduces the size of the public key. The hash of Alice’s message, padded with 0’s at the left to make its length divisible by $\ell$ , consists of $n$ bit strings $b _ { 1 } \cdots b _ { n }$ , each of length $\ell$ . Every $b _ { i }$ represents a binary number in the range $0 , \ldots , 2 ^ { \ell } - 1$ ℓ (by interpreting its bits in the base-2 numeral system). Alice signs her message with $h ^ { b _ { 1 } } ( X _ { 1 } ) \parallel \cdots \parallel h ^ { b _ { n } } ( X _ { n } )$ . To verify Alice’s signature $s i g _ { 1 } \| \cdots \| s i g _ { n }$ , Bob computes the hash of Alice’s message and $s i g _ { i } ^ { \prime } = h ^ { 2 ^ { t } - 1 - b _ { i } } ( s i g _ { i } )$ for all $i = 1 , \ldots , n$ , and checks whether $h ( s i g _ { 1 } ^ { \prime } \parallel \cdots \parallel s i g _ { n } ^ { \prime } )$ equals the public key.

, . . . ,There is a trade-off between the size of the signature and computation time. Increasing $\ell$ decreases the size of the private key in a linear fashion, while increasing the number of applications of $h$ ℓin an exponential fashion. It should be noted that hash functions are generally especially designed to be easy to compute. In practice, generally the random numbers $X _ { i }$ consist of 256 bits, $h$ is SHA-256, $n = 3 2$ , and $\ell = 8$ .

Example 19.6 Let $k = 1 5$ and $\ell = 3$ , so $n = 5$ . Alice generates a private key $ X _ { 1 } \| X _ { 2 } \| X _ { 3 } \| X _ { 4 } \| X _ { 5 }$ and pubℓlishes the corresponding public key $h ( h ^ { 7 } ( X _ { 1 } ) \parallel h ^ { 7 } ( X _ { 2 } ) \parallel h ^ { 7 } ( X _ { 3 } ) \parallel h ^ { 7 } ( X _ { 4 } ) \parallel h ^ { 7 } ( X _ { 5 } ) )$ . Let 110101010010111 be the hash of Alice’s message to Bob. The five binary substrings of length three represent the numbers 6, 5, 2, 2, and 7, respectively. So Alice signs her message with $h ^ { 6 } ( X _ { 1 } ) \parallel h ^ { 5 } ( X _ { 2 } ) \parallel h ^ { 2 } ( X _ { 3 } ) \parallel h ^ { 2 } ( X _ { 4 } ) \parallel h ^ { 7 } ( X _ { 5 } )$ . To verify the signature, Bob computes the hash of the message and applies $h$ to $h ^ { 6 } ( X _ { 1 } )$ , $h ^ { 2 }$ to $h ^ { 5 } ( X _ { 2 } ) , h ^ { 5 }$ to $h ^ { 2 } ( X _ { 3 } )$ , and $h ^ { 5 }$ to $h ^ { 2 } ( X _ { 4 } )$ , and leaves $h ^ { 7 } ( X _ { 5 } )$ unchanged. Finally, he applies $h$ to the concatenation of the five resulting strings and checks that the outcome coincides with the public key.

As such, the Winternitz signature scheme is vulnerable to a replay attack. An eavesdropper Eve can reuse the public key published by Alice and exploit the hash of her message and the corresponding signature to forge a signature of another message, which Bob wrongly accepts as a genuine signature by Alice. The hash of Eve’s forged message must consist of substrings $c _ { 1 } \ldots c _ { n }$ of length $\ell$ such that $b _ { i } \leq c _ { i }$ for all $i =$ $1 , \ldots , n$ , where the bit strings $b _ { i }$ and $c _ { i }$ . . . ℓare interpreted as binary numbers. To forge a signature, Eve applies $h ^ { c _ { i } - b _ { i } }$ to the ith component $h ^ { b _ { i } } ( X _ { i } )$ of Alice’s signature, for all $i = 1 , \ldots , n$ , thus constructing the signature $h ^ { c _ { 1 } } ( X _ { 1 } ) \parallel \cdots \parallel h ^ { c _ { n } } ( X _ { n } )$ .

Example 19.7 We revisit example 19.6. Reusing the public key and exploiting the hash of Alice’s message and the corresponding signature, Eve forges a signature of another message with hash 110110010100111. The five binary substrings of length three of this hash represent the numbers 6, 6, 2, 4, and 7, respectively. With regard to Alice’s signature, Eve leaves $h ^ { 6 } ( X _ { 1 } )$ unchanged, applies $h$ to $h ^ { 5 } ( X _ { 2 } )$ , leaves $h ^ { 2 } ( X _ { 3 } )$ unchanged, applies $h ^ { 2 }$ to $h ^ { 2 } ( X _ { 4 } )$ , and leaves $h ^ { 7 } ( X _ { 5 } )$ unchanged, leading to the signature $h ^ { 6 } ( X _ { 1 } ) \parallel h ^ { 6 } ( X _ { 2 } ) \parallel h ^ { 2 } ( X _ { 3 } ) \parallel h ^ { 4 } ( X _ { 4 } ) \parallel h ^ { 7 } ( X _ { 5 } )$ . To verify the signature, Bob applies $h$ to $h ^ { 6 } ( X _ { 1 } )$ , $h$ to $h ^ { 6 } ( X _ { 2 } ) , h ^ { 5 }$ to $h ^ { 2 } ( X _ { 3 } )$ , and $h ^ { 3 }$ to $h ^ { 4 } ( X _ { 4 } )$ , and leaves $h ^ { 7 } ( X _ { 5 } )$ unchanged. Finally, he applies $h$ to the concatenation of these five strings and checks that the result coincides with the public key, thus accepting Eve’s forged signature of her message as a genuine signature by Alice.

To avoid this replay attack, Alice includes a checksum in her signature, tying it to the particular message she sends. She computes $C = ( 2 ^ { \ell } - 1 - b _ { 1 } ) + \dots + ( 2 ^ { \ell } - 1 - b _ { n } )$ , where again the $b _ { i }$ are interpreted as binary numbers. Note that the checksum of Eve’s forged message is inevitably smaller than $C$ , which implies that Eve cannot forge a signature as before. The binary representation of $C$ is split into bit strings $b _ { n + 1 } \cdots b _ { m }$ of length $\ell$ .

Again 0’s may be padded at the left to make the length divisible by $\ell$ . Alice generates additional random numbers $X _ { n + 1 } , \ldots , X _ { m }$ ℓfor her private key and extends her public key under $h$ with $h ^ { 2 ^ { \ell } - 1 } ( X _ { n + 1 } ) \parallel \cdots \parallel h ^ { 2 ^ { \ell } - 1 } ( X _ { m } )$ . , . . . ,She moreover extends her signature with $h ^ { b _ { n + 1 } } ( X _ { n + 1 } ) \parallel \cdots \parallel h ^ { \bar { b } _ { m } } ( X _ { m } )$ . Bob verifies the extended signature $s i g _ { 1 } \| \cdots \| s i g _ { n } \| s i g _ { n + 1 } \| \cdots \| s i g _ { m }$ as before, where he additionally computes the checksum $C$ , determines $b _ { n + 1 } , \ldots , b _ { m }$ , and applies $h ^ { 2 ^ { \ell } - 1 - b _ { i } }$ to $s i g _ { i }$ for $i = n + 1 , \ldots , m$ as well. Since Eve’s checksum is smaller than $C$ , , . . . , ,...,she can no longer perform the replay attack described earlier. To cope with the checksum, Eve needs to find values $c _ { i } \geq b _ { i }$ for $i = 1 , \ldots , n$ such that the checksum $( 2 ^ { \ell } - 1 - c _ { 1 } ) + \dots + ( 2 ^ { \ell } - 1 - c _ { n } )$ yields binary numbers $c _ { i } \geq b _ { i }$ for $i = n + 1 , \ldots , m$ ,, which is a difficult task.

Example 19.8 We again revisit example 19.6. Alice computes as checksum $( 7 - 6 ) + ( 7 - 5 ) + ( 7 - 2 ) + ( 7 -$ $2 ) + ( 7 - 7 ) = 1 3$ , which has the binary representation 1101. Two 0’s are padded at the left to make the length of this string divisible by 3: 001101. The binary representations of $b _ { 6 }$ and $b _ { 7 }$ are thus 001 and 101, so $b _ { 6 } = 1$ and $b _ { 7 } = 5$ . Alice generates additional random numbers $X _ { 6 }$ and $X _ { 7 }$ for her private key and extends her public key to $h ( h ^ { 7 } ( X _ { 1 } ) \parallel h ^ { 7 } ( X _ { 2 } ) \parallel h ^ { 7 } ( X _ { 3 } ) \parallel h ^ { 7 } ( X _ { 4 } ) \parallel h ^ { 7 } ( X _ { 5 } ) \parallel h ^ { 7 } ( X _ { 6 } ) \parallel h ^ { 7 } ( X _ { 7 } ) )$ . She moreover extends her signature with $h ( X _ { 6 } ) \parallel h ^ { 5 } ( X _ { 7 } )$ . To verify the signature, Bob additionally computes the checksum 13, determines that $b _ { 6 } = 1$ and $b _ { 7 } = 5$ , and applies $h ^ { 6 }$ to $h ( X _ { 6 } )$ and $h ^ { 2 }$ to $h ^ { 5 } ( X _ { 7 } )$ in Alice’s signature.

Eve’s checksum is (inevitably) smaller than the one from Alice: $( 7 - 6 ) + ( 7 - 6 ) + ( 7 - 2 ) + ( 7 - 4 ) +$ $( 7 - 7 ) = 1 0$ , which has the binary representation 1010. The binary representations of $b _ { 6 }$ and $b _ { 7 }$ for Eve are thus 001 and 010, so $b _ { 6 } = 1$ and $b _ { 7 } = 2$ . Since Eve’s value of $b _ { 7 }$ is smaller than for Alice, Eve cannot perform the replay attack based on Alice’s (extended) signature.

# Merkle Signatures

A serious bottleneck of one-time signature schemes is the overhead in key management. Exchanging public keys is a complex matter, as they have to be authenticated and it must be ensured that they have not been modified. In the Lamport and Winternitz schemes, these complications are aggravated by the fact that public keys are quite large. Furthermore, storing these public keys in a publicly accessible database can put a severe strain on memory resources. The Merkle signature scheme makes it possible to sign many messages using only a single public key, through the use of a complete binary Merkle tree of a depth $n \geq 1$ . Each public key generated in this signature scheme, which is stored at the root of the Merkle tree, can be used to sign $2 ^ { n }$ consecutive messages. Alice generates $2 ^ { n }$ private/public key pairs $( X _ { i } , Y _ { i } )$ for signing these messages, where $i = 1 , . . . , 2 ^ { n }$ ,, with a one-time signature scheme such as Winternitz. To avoid the need to store them ,. .. ,all in memory at once, they are generated using some pseudo-random number generator and a seed value, so that private/public key pairs can be generated from the seed when needed, first to compute the Merkle root, and later on when such a pair is needed to digitally sign the corresponding message. (The signature if then constructed based on this message and the private key at hand.) The values $h ( Y _ { i } )$ for $i = 1 , \ldots , 2 ^ { n }$ are assigned to the $2 ^ { n }$ consecutive leaves of the complete binary tree. Each of them in turn will be used in the signature of one of Alice’s messages, starting at the leftmost leaf. The Merkle root is used to verify the integrity of Alice’s public keys $Y _ { i }$ . For this purpose, every nonleaf in the tree contains the cryptographic hash of the concatenation of the values of its two children. To be more precise, let $H _ { j i }$ denote the hash value in the ith node at depth $j$ in the tree, for $j = 0 , \ldots , n$ and $i = 1 , \ldots , 2 ^ { j }$ . For the leaves, $H _ { n i } = h ( Y _ { i } )$ for $i = 1 , \ldots , 2 ^ { n }$ , while for the nonleaves, $H _ { j i } = h ( H _ { ( j + 1 ) ( 2 i - 1 ) } | | H _ { ( j + 1 ) ( 2 i ) } )$ , . . . ,for $j = 0 , . . . , n - 1$ and $i = 1 , \ldots , 2 ^ { j }$ , . . . ,. Only the Merkle root $H _ { 0 1 }$ at the root of the tree is made public. It is a fingerprint of the hash values in the leaves, serving as public key for all $2 ^ { n }$ messages. The applications of $h$ keep the strings relatively short and obscure the values in the tree.

When Alice sends a message to Bob, she picks an (unused) private/public key pair, associated to say the $i _ { 0 }$ th leaf. To let Bob verify the signature of the message, he must be able to (1) verify the one-time signature $s i g _ { i _ { 0 } }$ associated to the pair $( X _ { i _ { 0 } } , Y _ { i _ { 0 } } )$ and (2) corroborate the integrity of the public key $Y _ { i _ { 0 } }$ by relating $h \big ( Y _ { i _ { 0 } } \big )$ to the Merkle root $H _ { 0 1 }$ ,by means of the Merkle tree. First of all, he must be provided with the public key $Y _ { i _ { 0 } }$ and the one-time signature $s i g _ { i _ { 0 } }$ (which Alice builds from the private key $X _ { i _ { 0 } }$ ). Second, let $\nu _ { 0 } , . . . , \nu _ { n }$ be the sequence of $n + 1$ nodes in the Merkle tree on the path from the $i _ { 0 }$ th leaf to the root; so $\nu _ { 0 }$ νis the $i _ { 0 }$ . . , νth leaf, $\nu _ { n }$ is the root, and each $\nu _ { i }$ is at depth $n - i$ in the tree. For all $i = 1 , \ldots , n$ ν, to determine the value in node $\nu _ { i }$ ν, Bob needs νto know the values in both children of $\nu _ { i }$ , so in $\nu _ { i - 1 }$ , . . . ,as well as in its other child, say $\nu _ { i - 1 } ^ { \prime }$ ν. Therefore, Alice includes the values auth $0 , \ldots , a u t h _ { n - 1 }$ ν νof the nodes $\nu _ { 0 } ^ { \prime } , \ldots , \nu _ { n - 1 } ^ { \prime }$ νin her signature. In conclusion, the signature of Alice’s message is $s i g _ { i _ { 0 } } \parallel Y _ { i _ { 0 } } \parallel a u t h _ { 0 } \parallel \cdots \parallel a u t h _ { n - 1 }$ .

To verify this signature, Bob first verifies the one-time signature $s i g _ { i _ { 0 } }$ with regard to the public key $Y _ { i _ { 0 } }$ . If this signature turns out to be valid, Bob next applies $h$ to $Y _ { i _ { 0 } }$ to determine the value in the $i _ { 0 } \mathrm { t h }$ leaf $\nu _ { 0 }$ . Then he consecutively computes the values in $\nu _ { i }$ for $i = 1 , \ldots , n$ by applying $h$ νto the concatenation (in the νorder in which they occur in the Merkle tree) of $a u t h _ { i - 1 }$ , . . . ,and the value in $\nu _ { i - 1 }$ . Bob accepts the signature of Alice’s message if the value computed for the root $\nu _ { n }$ νcoincides with the public key $H _ { 0 1 }$ . Thus authenticity and integrity of the one-time public key $Y _ { i _ { 0 } }$ νare verified through the “master” public key $H _ { 0 1 }$ .

Example 19.9 Let $n = 3$ . Alice generates private/public key pairs $( X _ { i } , Y _ { i } )$ for $i = 1 , \ldots , 8$ using a one-time , ,...,signature scheme and constructs the Merkle tree of depth three below. Only the actual values $h ( Y _ { i } )$ of the leaves are given. For all nonleaves, $H _ { j i } = h ( H _ { ( j + 1 ) ( 2 i - 1 ) } | | H _ { ( j + 1 ) ( 2 i ) } )$ .

![](images/41e06f661fb416bec2258c511397324d4d2b3d147008296f8d25335062db1328.jpg)

Let Alice send a message to Bob with a signature based on the fifth leaf of the tree. This signature takes the form $s i g _ { 5 } \parallel Y _ { 5 } \parallel h ( Y _ { 6 } ) \parallel H _ { 2 4 } \parallel H _ { 1 1 }$ , where $s i g _ { 5 }$ is the one-time signature associated to $( X _ { 5 } , Y _ { 5 } )$ . The nodes ,in the Merkle tree of which the values are computed by Bob in his validation of the signature of Alice’s message are colored gray. The nodes carrying authentication values that are used in this computation and are included in the signature are drawn with a dashed circle. Bob first verifies the one-time signature $s i g _ { 5 }$ with regard to the public key $Y _ { 5 }$ . This signature turns out to be valid and Bob next applies $h$ to $Y _ { 5 }$ to determine the value in the fifth leaf. Then he consecutively computes $H _ { 2 3 } = h ( h ( Y _ { 5 } ) \parallel h ( Y _ { 6 } ) )$ , $H _ { 1 2 } = h ( H _ { 2 3 } \parallel H _ { 2 4 } )$ , and $H _ { 0 1 } = h ( H _ { 1 1 } \parallel H _ { 1 2 } )$ . Since this last value is $H _ { 0 1 }$ , Bob accepts the signature of Alice’s message.

At first sight it may seem that with the Merkle signature we have jumped from the fire into the frying pan. Instead of exchanging, authenticating, and storing a large number of public keys, it appears that the sender Alice must store the huge Merkle tree in memory. We will now concern ourselves with avoiding the need to store the entire Merkle tree at once. The idea is to let the sender of a message generate only small parts of the corresponding Merkle tree, as far as needed in the construction of a signature, and to let her remove these parts from memory when possible.

To calculate the public key $H _ { 0 1 }$ , Alice can employ what is called the treehash algorithm to traverse the nodes in the Merkle tree from the leaves toward the root. It uses the stack data structure, containing nodes of the Merkle tree paired with their values. Initially the stack is empty and a counter $c$ , keeping track which leaf is next in line to be pushed onto the stack, has the value 1. The treehash algorithm repeatedly checks whether the top two nodes on the stack are positioned at the same depth in the tree. If so, the value of their parent in the tree is computed, the top two nodes are popped from the stack (and removed from memory), and their parent is pushed onto the stack. If not, the value of the cth leaf is computed, this leaf is pushed onto the stack, and $c$ is increased by 1. The algorithm terminates when the value $H _ { 0 1 }$ at the root has been determined.

At any moment during the computation of the Merkle root, this application of the treehash algorithm stores at most $n + 1$ node/value pairs in memory. Actually, next to this, during the computation, the values $H _ { i 2 }$ for $i = n , . . . , 1$ are preserved in memory, as they will be needed in the signature of the first message.

Example 19.10 We revisit the Merkle tree from example 19.9. To compute $H _ { 0 1 }$ , Alice starts with pushing the leftmost two leaves (and their values $h ( Y _ { 1 } )$ and $h ( Y _ { 2 } ) ) ,$ ) onto the empty stack. Since they are at the same depth, she computes the value $H _ { 2 1 } = h ( h ( Y _ { 1 } ) \parallel h ( Y _ { 2 } ) )$ of their parent, pops the two leaves from the stack (but keeps $h ( Y _ { 2 } )$ in memory for the first signature), and pushes their parent onto the stack. Next, she pushes the third and fourth leaves onto the stack, computes the value $H _ { 2 2 } = h ( h ( Y _ { 3 } ) \parallel h ( Y _ { 4 } ) )$ of their parent, pops these two leaves from the stack again, and pushes their parent onto the stack. She now computes the value $H _ { 1 1 } = h \big ( H _ { 2 1 } \big | | H _ { 2 2 } \big )$ of the parent of the two nodes on the stack, pops these two nodes from the stack (remembering $H _ { 2 2 }$ for the first signature), and pushes their parent onto the stack. The computation so far is now basically mirrored in the righthand subtree to determine $H _ { 1 2 }$ . Alice pushes the fifth and sixth leaves onto the stack, computes the value $H _ { 2 3 } = h ( h ( Y _ { 5 } ) \parallel h ( Y _ { 6 } ) )$ of their parent, pops these two leaves from the stack again (and from memory), and pushes their parent onto the stack. Next, she pushes the seventh and eighth leaves onto the stack, computes the value $H _ { 2 4 } = h ( h ( Y _ { 7 } ) \parallel h ( Y _ { 8 } ) )$ of their parent, pops these two leaves from the stack again (and from memory), and pushes their parent onto the stack. She now computes the value $H _ { 1 2 } = h ( H _ { 2 3 } \parallel H _ { 2 4 } )$ of the parent of the two top nodes on the stack, pops these two nodes from the stack (and from memory), and pushes their parent onto the stack. Finally, Alice computes the value $H _ { 0 1 } = h ( H _ { 1 1 } \parallel H _ { 1 2 } )$ of the root, pops the two remaining nodes from the stack (remembering $H _ { 1 2 }$ for the first signature), and returns $H _ { 0 1 }$ as the public key.

Since Alice does not keep the entire Merkle tree in memory, the challenge that remains is to let her efficiently recompute authentication values for consecutive signatures. Authentication values at nodes that are higher in the tree are more expensive to compute, but are also reused more often: an authentication value at a depth $d \geq 1$ is used in $2 ^ { n - d }$ consecutive signatures. To shed light on the structure in reuse of authentication values, the Merkle tree from example 19.9 is redrawn, but now at each node it is depicted for which messages the hash value in this node is used as an authentication value.

![](images/9a5ab672c48b55bfd54dea3e9dac7f71a5579e5e31c71c09619481ab9640bc5b.jpg)

Alice runs multiple instances of the treehash algorithm concurrently, one for each depth $\geq 1$ to determine the next authentication value at this depth. These instances crawl up the tree from the leaves, fast enough to reach the intended depth at the moment the authentication value at this depth is needed, but slow enough to keep memory consumption under control. A careful scheduling of these concurrent treehashes, which favors upcoming authentication values that are lower in the tree because they are required sooner and require less memory, restricts memory overhead of the concurrent treehashes to at most $3 n$ values at any moment in time.

# 19.6 Blockchains

In the world of finance, a ledger is a book in which all monetary transactions of an organization are noted. In the context of computer science, this book is a data file. A public (or permissionless) blockchain is an openly accessible ledger that is stored as a decentralized distributed database. It can be used to keep track of ownership of assets. A blockchain consists of a continuously growing linked list of blocks, each containing a batch of validated transactions, as well as a link to its predecessor (except for the Genesis block at the start of the list). The blockchain is supposed to contain only legitimate financial transactions, which are temporally ordered by their places in the chain. Anybody can try to add a new block at the end of the list. The main challenge is to prevent an attacker from tampering with the blockchain or adding fraudulent transactions.

The database is distributed over a P2P network in which peers (i.e., processes) can freely join and leave (see chapter 18), and may be malicious. Some peers keep track of the entire blockchain; updates are shared among those peers. Other peers may be content with a local view that contains sufficient information to validate transactions in new blocks without keeping the entire history of the blockchain in memory. When a peer (re)joins the network, it downloads and verifies (newly added) blocks from other peers to obtain (or update) its local copy of the blockchain or its local view. In contrast to the client-server architecture, data is replicated many times, and each change to the blockchain creates communication overhead. Paradoxically, this decentralized and replicated nature of a blockchain is essential not only for its accessibility but also for its security, since there is no single target for an attacker.

The remainder of this section discusses the Bitcoin protocol for financial transactions over the Internet, which employs a blockchain to achieve secure, tamper-resistant consensus between peers without central authority or trusted third party. The possible applications of blockchains stretch beyond financial transactions, as will be discussed briefly at the end of this section. However, the Bitcoin protocol provides an insightful illustration of their potential as well as the challenges one is faced with when using blockchain technology.

The Bitcoin protocol employs cryptographic hash functions (notably SHA-256). A peer controls one or more addresses called wallets, each associated with a unique private/public key pair; the address consists of a cryptographic hash of the public key. In contrast to traditional bank accounts, reusing the same wallet for different transactions is considered an undesirable and unnecessary security risk. A transaction collects cryptocurrency called bitcoins from one set of wallets and attributes it to (and divides it over) another set of wallets. It takes as inputs the outputs of earlier transactions and protects each of its outputs with a hash of the public key belonging to the destination wallet, which ensures that the cryptocurrency attributed to this wallet can be spent only by the peer controlling this wallet. The output of a transaction can serve as input to a subsequent transaction only once, so to retain part of this cryptocurrency, the payer should in the subsequent transition attribute this part to a wallet under its own control. Otherwise the unspent bitcoins would be attributed to the miner that adds this transaction to the blockchain, which will be explained below.

Some peers hold the entire blockchain in memory, so that they can check the validity of newly added blocks. In view of the large size of the blockchain, peers can also limit themselves to what is called simplified payment verification, meaning that they only download and verify the headers of all blocks in the blockchain. This makes it possible to run a wallet from say a smartphone. Such peers need to consult peers with the entire blockchain in memory for verifying new transactions and blocks.

A transaction is broadcast to all peers in order to be included in a block that may be added to the blockchain. Upon receiving a new transaction, a peer can validate that all financial contributors to the transaction agree and that their contributions have not been spent previously. The peer then verifies the chain of ownership, either directly by using its local view or indirectly through another trusted peer. Published transactions cannot be retracted and are in principle irreversible once they have been included in the blockchain. This eliminates the risk of chargeback fraud, in which a customer claims a refund (typically for a credit card transaction) without returning the purchased goods.

A miner collects validated transactions and bundles them in a block; on average 1,700 transactions per block. To add this block at the end of the blockchain, a miner must complete a proof-of-work, which will be described later. When a miner succeeds in adding its block to the blockchain, it broadcasts the block to each peer, which accepts the block as the new head of the blockchain only after validating the proofof-work and that all transactions in the block are valid. This miner is allowed to reward itself with some newly created bitcoins, which also serves the purpose of disseminating fresh bitcoins in a decentralized fashion. Mining requires hard labor and slowly makes new cryptocurrency available, reminiscent of extracting valuable minerals from the earth. The reward for adding a block is included in the block itself as what is called a coinbase transaction, which creates coins from nothing and so has no ancestor. This reward (6.25 bitcoins since May 2020) is halved with each 210,000 blocks, which boils down to roughly once every four years. Eventually (around the year 2140) it will be set to zero, once the maximum number of 21 million bitcoins has been reached. Ownership of bitcoins is defined by sequences of digitally signed transactions originating at their creation as a mining reward in coinbase transactions. A voluntary transaction fee, which consists of the unspent bitcoins in a transaction, is paid to a miner for including the transaction in a block and adding it to the blockchain. Miners naturally tend to select pending transactions with higher fees. When all bitcoins have been mined, transaction fees will become even more important to incentivize miners. Currently the transaction fee tends to be around 0.0005 bitcoin. (The smallest unit is 0.00000001 bitcoin, called a satoshi in honor of the anonymous developer(s) who published the Bitcoin protocol under the pseudonym Satoshi Nakamoto.)

A fork in the blockchain may occur when two miners complete the proof-of-work and add a block at almost the same time. Miners will continue to append new blocks to the longest chain they are aware of, meaning the one that required the largest amount of effort to produce. As a result, one of the forks will quickly prevail, and the so-called orphan blocks in the unlucky shorter fork will be ignored. In view of the possibility of a fork, it is recommended that a transaction in a block in the blockchain is only considered definite after six more blocks have been added to the blockchain.

A dishonest miner can attempt to deliberately create a long fork of rogue blocks that starts from an older block, thus turning genuine blocks in the blockchain into orphans. This would, for instance, allow the miner to spend the same cryptocurrency twice: first in an orphan block and then in a rogue block. For this reason, mining is intentionally resource-intensive, and the proof-of-work chains a block to its predecessor in the blockchain through cryptographic means, as will be explained. As long as a significant majority of the computing power is controlled by honest miners, a fork of rogue blocks will quickly be outpaced by the fork of honest blocks. Likewise, to modify a past block, an attacker must redo the proof-of-work of that block and all its successors and then surpass the work of the honest miners. The probability of an attacker being able to catch up diminishes quickly with subsequent blocks added by honest miners.

![](images/429e062c2416b73b581e4602c06f985f168b130dd879713bfc20c369f1c8416f.jpg)

Next to the body, which consists of its transactions stored in a Merkle tree, a block also carries a header with the following components: the hash of the header of the previous block in the chain, a nonce that is allowed to carry any 32-bit value, a time stamp based on real time, and the Merkle root of its own body. The first component of the header of a block firmly chains it to the previous block in the blockchain and at the same time helps to protect the integrity of the header of the previous block. The second component is used in the proof-of-work, which will be explained below. The third component, which affirms the ordering of the blocks in the blockchain through increasing time stamps, makes manipulation of the blockchain by an attacker even more difficult. And the fourth component guarantees that the body of a block cannot be changed after it has been added to the blockchain. Depicted above is a small part of a blockchain, with the four components in the header of each block. A fork has happened, whereby the bottom block becomes an orphan block that will be disregarded by miners.

The demanding proof-of-work required from a miner who wants to add its block at the head of the blockchain is to find a nonce for the second component such that the hash of the header of this block starts with many (typically 40) zeros. This results in a guessing game where approximately one out of every $2 ^ { 4 0 }$ nonces yields a solution to this puzzle that allows the miner to add its block. The nonce starts at zero and is increased in a linear fashion until either a solution is found or it overflows, which will happen often because the nonce is small compared to the difficulty of the puzzle. In case of an overflow, an extra nonce field within the coinbase transaction of the block is incremented and the nonce in the block header is restarted at zero. Incrementing the extra nonce field entails recomputing part of the Merkle tree in the body of the block because it changes the coinbase transaction. If in the end no solution is found, then the time stamp of the block is changed and the search for an appropriate nonce value is started anew. To be more precise, the difficult puzzle concerns a double hash of the block header for increased security, although currently no attack on the Bitcoin protocol is known even in case of a single hash.

The difficulty of the puzzle is calibrated automatically based on the speed with which new blocks are being added, to keep the average at approximately once every ten minutes. This gives enough time to let information regarding a new head of the blockchain disseminate through the network, while the delay this causes for the effectuation of transactions is acceptable in practice. If more processing power becomes available so that the time between adding new blocks decreases, then the system increases the required number of leading zeros of the double hash of a header; the average work required to solve a puzzle grows exponentially with every additional leading zero bit. If, on the other hand, miners decide to quit their operations, typically because they are no longer profitable, then the required number of leading zeros is decreased. In this way, the Bitcoin protocol effectively controls the cryptocurrency supply.

Since mining is something of a gamble and requires a lot of processing power to have a serious chance of success, many miners have organized themselves into pools that share resources as well as rewards, usually under some centralized form of coordination. For the security of the Bitcoin protocol, it is essential that no pool controls a large part of the hashing power in the network. Currently the vast majority of blocks are mined by a limited number of pools. If these pools join together, the longest chain rule would no longer constitute an effective defense mechanism against adding rogue blocks. Since in the Bitcoin protocol mining rewards decrease over time, the incentive to mine may diminish, which makes the threat of a mining monopoly in the future even more imminent.

Because of proof-of-work, mining bitcoins consumes huge amounts of power, which is a terrible waste of energy. In 2021 it was reported that mining bitcoins uses roughly $0 . 5 \%$ of all electricity consumed worldwide and is still increasing fast. Alternatively, a proof-of-stake can be used to decide which new block is added at the head of the blockchain. The basic idea is that a peer’s voting power in adding a new block is proportional to the amount of cryptocurrency this peer holds. The cryptocurrency added to the system with each new block is divided among all peers in the same proportional manner, which effectively leads to a steady inflation. An important additional advantage of proof-of-stake is that it mitigates the risk of a monopoly, because an attacker needs to own a majority of the available cryptocurrency instead of the available processing power. A peer is free to vote for both branches of a fork and could maliciously try to spend the same cryptocurrency in both branches. However, such an attack only has a serious chance of success if the peer controls a large amount of cryptocurrency, in which case she actually has a strong interest in maintaining the integrity of the system. A naive implementation of proof-of-stake, however, provides little incentive to validate new blocks and a perverse incentive to stock up on cryptocurrency. Therefore, it needs to be equipped with incentives that counterbalance these factors, possibly based on some form of proof-of-work. The popular cryptocurrency Ethereum uses proof-of-work and proof-of-stake in parallel.

The application of blockchains goes beyond mere financial transactions. A blockchain can be endowed with more complex operations, in particular, instructions from a programming language. A computer program can thus be performed by the blockchain, which ensures that the execution is tamper resistant and is recorded permanently in the blockchain. This can, for instance, serve to run a smart contract that automatically verifies and enforces the terms of a binding legal agreement by cryptographic means. The program can perform a specific action, such as the transfer of cryptocurrency, taking into account the terms of the agreement, actions by the contract partners, and input data provided by trusted peers. For example, a smart contract could regulate car insurance policies, particularly the settlement in the case of an accident.

# Bibliographical notes

Public-key cryptosystems and the RSA algorithm are credited to [33] and [103], respectively. (These notions had actually already been invented some years earlier within the secret service of the United Kingdom but remained classified information until 1997.) The Needham-Schroeder authentication protocol originates from [89], the need for time stamps was noted in [32], and the Kerberos protocol as discussed here was presented in [90]. The Diffie-Hellman key exchange protocol stems from [33]. Lamport signatures date back to [69] and the Winternitz trick, described in [84], was suggested in 1979 by Robert Winternitz. Merkle trees and Merkle signatures originate from [83] and the efficient scheduling of treehashes to compute authentication values is due to [114]. Proof-of-work can be traced back to [39] and the Bitcoin protocol was proposed in [88]. The BB84 key exchange protocol stems from [13].

# 19.7 Exercises

Exercise 19.1 Let each integer $k$ be mapped to $k$ mod $n$ for some positive natural number $n$ . Argue that this hash function is neither collision-resistant nor preimage-resistant.

Exercise 19.2 Why does the birthday attack threaten collision resistance but not preimage resistance?

Exercise 19.3 Consider the RSA cryptosystem with $p = 5$ , $q = 1 3$ , and $e = 5$ .

(a) Encrypt 7.   
(b) Determine the value for $d$ .   
(c) Decrypt the value you computed in (a).

Exercise 19.4 Given a public-key cryptosystem, let Alice send a message m to Bob, encrypted with his public key. After Bob has received it and decrypted it using his private key, he sends $m$ back to Alice, encrypted with her public key. After Alice has received this reply and decrypted it using her private key, she is certain Bob received her message in good order. Explain how an eavesdropper could launch a replay attack to learn $m$ .

Exercise 19.5 Placing the ticket under $K _ { p }$ in step 2 of the Needham-Schroeder protocol is not strictly necessary, as it is openly sent in the next step. Motivate why it is placed under $K _ { p }$ in step 2.

Exercise 19.6 Suppose that in de Needham-Schroeder protocol, $q$ would defend against an attacker who stole the session key and replays steps 3 and 5 by remembering which tickets it received in steps 3 and ignoring multiple instances of the same ticket. What are drawbacks of this approach?

Exercise 19.7 [89] Specify a variant of the Needham-Schroeder protocol based on public-key (instead of symmetric-key) cryptography.

Exercise 19.8 [90] Explain how dividing a computer network into realms, each with its own key distribution center, authentication server, and ticket-granting server, can be taken into account in the Kerberos protocol.

Exercise 19.9 Let a client employ the Kerberos protocol to authenticate the same client to two different servers, within the time window in which the ticket obtained from the authentication server is still valid. Give the entire message exchange.

Exercise 19.10 Suppose that in step 2 of the Kerberos protocol, the authentication server would include the server ID $s$ in the ticket it sends to the client. (Where moreover the client includes $s$ in step 1 and omits $s$ outside the ticket in step 3.) Explain how this would seriously hamper the applicability of the Kerberos protocol.

Exercise 19.11 Kerberos 5 introduced pre-authentication, meaning that the client must authenticate itself to the authentication server at the very start of the protocol.

(a) Which kind of attacks on Kerberos 4 is prevented by pre-authentication? (b) How can this authentication be performed?

Exercise 19.12 Let Alice and Bob build a private key using the Diffie-Hellman protocol, with $p = 1 1$ and $d$ the smallest positive integer that is a primitive root modulo 11. Moreover, let $a = 5$ and $b = 3$ . Compute which key they construct.

Exercise 19.13 In the Diffie-Hellman protocol, why is it important that $d$ is a primitive root? And why is $p$ chosen to be a prime number?

Exercise 19.14 Suppose that in the Diffie-Hellman protocol, addition instead of the power function were used in the private mappings: $S _ { A } ( k ) = k + a$ mod $p$ and $S _ { B } ( k ) = k + b$ mod $p$ . (With $\mathbb { Z } / p \mathbb { Z }$ as domain.) Argue that the resulting key exchange protocol is correct but insecure.

Exercise 19.15 Suppose that in the Diffie-Hellman protocol, Alice would always choose a small value for $a$ . How could Eve then find this value quickly?

Exercise 19.16 Develop a variant of the Diffie-Hellman protocol that allows three peers to share a private key.

Exercise 19.17 Suppose that the Diffie-Hellman protocol is employed without authentication. Describe a person-in-the-middle attack.

Exercise 19.18 Show that the Hadamard transform is composed of a rotation around the origin followed by a reflection in a line through the origin in $\mathbb { R } ^ { 2 }$ .

Exercise 19.19 In the BB84 protocol, why are errors introduced by Eve for qubits on which only Alice or only Bob applied the Hadamar transform irrelevant?

Exercise 19.20 Suppose that in a run of the BB84 protocol, Eve performs the Hadamard transform on a qubit and then measures it. Why is it sensible for Eve to apply another Hadamard transform on the qubit before sending it to Bob?

Exercise 19.21 Consider the BB84 protocol with $n = 1 0$ , and let 0 1 10 0 1 0 1 00 be the random initial values of the successive qubits at Alice. She randomly decides to apply the Hadamard transform on the second, third, fourth, and eighth qubits, while Bob applies it on the first, second, fourth, seventh, eighth, and ninth qubits.

(a) Which qubits can be used for the private key shared by Alice and Bob?   
(b) Suppose Eve measures the fourth qubit and then passes it on to Bob. How can this introduce errors at both Eve and Bob?   
(c) Suppose Eve applies the Hadamard transform to the fifth qubit, measures it, applies the Hadamard transform to it again, and then passes it on to Bob. How can this introduce errors at both Eve and Bob?   
(d) Suppose Eve applies the Hadamard transform once on all ten qubits in the quantum channel, before measuring them and passing them on to Bob. What is the probability that Bob does not experience any disruptions caused by Eve? And what is this probability if Eve applies the Hadamard transform twice on all ten qubits, once before and once after measuring them?

Exercise 19.22 Assuming there is no eavesdropper or quantum noise, explain how long the private key computed in the BB84 protocol will be on average, in terms of $n$ , taking into account control bits and the simple error correction scheme.

Exercise 19.23 Consider the simple error correction scheme for the BB84 protocol.

(a) If the XORs of a pair of bits at Alice and Bob do not coincide, why do they discard both bits from the private key?   
(b) If the XORs of a pair of bits at Alice and Bob coincide, why do they discard the second bit from the private key?

(c) If Alice happened to pair two corrupted bits, how does this lead to an error in the private key?

Exercise 19.24 Explain for each of the following $2 \times 2$ matrices whether it is a possible replacement for the Hadamard transform in the BB84 protocol:

(b) (a) $\begin{array} { r l } & { \frac { 1 } { 2 } \binom { 1 } { 1 - 1 } ; } \\ & { \frac { 1 } { \sqrt { 2 } } \binom { - 1 } { 1 } ; } \\ & { \binom { 0 } { 1 0 } ; } \\ & { \binom { \cos \frac { \pi } { 4 } } { \sin \frac { \pi } { 4 } - \cos \frac { \pi } { 4 } } ; } \\ & { \phantom { \frac { 1 } { \sqrt { 2 } } } \binom { \cos \frac { \pi } { 4 } } { \sin \frac { \pi } { 8 } - \cos \frac { \pi } { 8 } } . } \end{array}$ (c) (d) (e)

Exercise 19.25 In Lamport’s signature scheme, why is it a bad idea to let Alice use only every other bit in the hash of her message for the private key, to reduce its size?

Exercise 19.26 Why does Alice determine the Lamport signature with regard to the (cryptographic) hash of her message? And why does Alice apply $h$ to $h ( X _ { 1 } ) \parallel \cdots \parallel h ( X _ { k } )$ in her public key?

Exercise 19.27 Consider the Winternitz signature scheme with $k = 1 2$ and $\ell = 4$ . Let 001101010001 be the ℓhash of Alice’s message to Bob. Explain how Alice computes the public key and signature of her message, taking into account the checksum, and how Bob verifies this signature.

Exercise 19.28 In the Winternitz signature, the 0’s padded between the checksum and the hash of the message are redundant. How can the signature scheme be adapted so that 0’s are padded only in front of the checksum?

Exercise 19.29 In the Winternitz signature, why would the checksum $b _ { 1 } + \cdots + b _ { n }$ be less effective against replay attacks than the actual checksum?

Exercise 19.30 Give two advantages of the outermost application of the cryptographic hash function $h$ in the public key of the Winternitz signature scheme.

Exercise 19.31 List the first four Merkle signatures for the Merkle tree in example 19.9. Explain how the third of these signatures is employed by Bob to verify whether public key $Y _ { 3 }$ is genuine.

Exercise 19.32 Consider a Merkle tree of depth $n = 4$ .

(a) Express $H _ { 1 2 }$ in terms of the leaf values.   
(b) Show how the value of $H _ { 1 2 }$ is determined by the treehash algorithm.

Exercise 19.33 Consider the Merkle signature scheme.

(a) Suppose an attacker manages to store the entire Merkle tree in memory. Explain why this does not seriously jeopardize the corresponding one-time signatures.   
(b) Why is it still not a good idea to publish the entire Merkle tree, relieving Alice from the duty to provide authentication values to Bob in her corresponding signatures? Give two reasons.

Exercise 19.34 Argue, by induction on $n$ , that the treehash algorithm to compute $H _ { 0 1 }$ stores at most $n + 1$ node/value pairs in memory, where $n$ is the depth of the Merkle tree.

Exercise 19.35 Describe the ways in which cryptographic hash functions play a crucial role in the Bitcoin protocol.

Exercise 19.36 Give two reasons why it is useful to include a time stamp as one of the components in the header of a block in the Bitcoin protocol.

Exercise 19.37 Suppose all bitcoin miners, except one dishonest pool, take an extended Christmas break.   
Explain how this pool can (try to) spend the same cryptocurrency twice.

# Online Scheduling

So far, we mostly ignored timing aspects. Logical clocks were used for rollback recovery, termination detection, and mutual exclusion; local clocks with bounded drift were employed to build a synchronous system in the presence of Byzantine processes; and time stamps helped to serialize distributed transactions. But these were mostly abstract representations of time. Also resource requirements were only considered at an abstract level, in the context of resource deadlocks, mutual exclusion, distributed transactions, and P2P networks. In this chapter, we will consider jobs, meaning units of work, that need to be scheduled and executed and are for this purpose divided among the processors. These jobs have time constraints and resource requirements.

One important application of real-time computing is computer graphics in video games, where it is vital to produce and analyze images in real time, and there is very little time available per image. Typically, every image is then decomposed into triangles, and special hardware is employed to generate the pixels inside each of the triangles separately. Another important application is in air traffic control to direct planes on the ground and through the air, based on information from different sources such as radars, weather stations, and pilots.

# 20.1 Jobs

The arrival time of a job is the moment in time at which it arrives at a processor, while the release time of a job is the moment in time at which it becomes available for execution. In many cases, these two times will coincide, but sometimes it can be useful to postpone the release time of a job, notably to avoid resource competition (see section 20.3). The execution time of a job at a processor is the amount of time needed to perform the job (assuming it executes alone and all resources are available).

We disregard the functional behavior of a job and focus on its deadline, meaning the time by which it must have been completed. This can be expressed as an absolute deadline, meaning a fixed moment in real time, or as a relative deadline, the maximum allowed time between arrival and completion of a job. A deadline can be hard, meaning that late completion is not allowed, or soft, meaning that late completion is allowed but comes with some penalty.

A scheduler at a processor decides the order in which jobs are performed at this processor, and which re sources they can claim. A scheduler aims to meet all hard deadlines, meet soft deadlines as much as possible, and avoid deadlocks. Of course, a job cannot be scheduled before its release time, and the total amount of time assigned to a job should equal its (maximum) execution time.

A task is a set of related jobs. Three types of tasks can be distinguished:

Periodic: Such a task is known at the start of the system; the jobs have hard deadlines. Aperiodic: Such a task is executed in response to some external event; the jobs have soft deadlines. Sporadic: Such a task is executed in response to some external event; the jobs have hard deadlines. A periodic task is defined by the following three parameters: the release time $r$ of the first periodic job; the period $p$ , which is a periodic time interval at the start of which a periodic job is released; the execution time $e$ of each periodic job.

For simplicity, we assume that the relative deadline of each periodic job equals its period. The utilization of a periodic task $( r , p , e )$ is $\frac { e } { p }$ , representing the relative amount of execution time on a processor that will be , ,consumed by this periodic task. The utilization at a processor is the sum of utilizations of its periodic tasks. Clearly, scheduling of the periodic tasks at a processor is possible only if its utilization does not exceed 1.

Example 20.1 Consider the periodic tasks $T _ { 1 } = ( 1 , 2 , 1 )$ and $T _ { 2 } = ( 0 , 3 , 1 )$ at a processor. The utilization at the processor is $\textstyle { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } = { \frac { 5 } { 6 } }$ , , , ,. The periodic jobs can be executed as follows.

![](images/7acc53623f2e41fbf8f3627e754788fcc3898ca74ef295c7310b0c69f2a18ef1.jpg)

The conflict at time 3, when periodic jobs of both $T _ { 1 }$ and $T _ { 2 }$ are released, must be resolved by some scheduler.   
In this example, $T _ { 1 }$ is given priority over $T _ { 2 }$ . Different schedulers will be discussed in the next section.

# 20.2 Schedulers

An offline scheduler determines the order in which jobs will be executed beforehand, typically with an algorithm for an NP-complete graph problem. In such schedulers, time is usually divided into regular time intervals called frames, and in each frame, a predetermined set of periodic tasks is executed. Jobs may be sliced into subjobs to accommodate the frame length. Offline scheduling is conceptually simple but cannot cope well with imprecise release and execution times, extra workload, nondeterminism, and system modifications.

Here we focus on online schedulers, where the schedule is computed at runtime. Scheduling decisions are made when jobs are released, when aperiodic or sporadic tasks arrive, when jobs are completed, or when resources are required or released. Released jobs are placed in priority queues, ordered by, for instance, release time, execution time, period of the task, deadline, or slack. The latter means the available idle time of a job until the next deadline. For example, if at time 2 a job with a deadline at time 6 still needs three time units to complete, then its slack at time 2 is $( 6 - 2 ) - 3 = 1$ .

For simplicity, we consider aperiodic and sporadic jobs instead of tasks. Such jobs are offered to processors at runtime. Sporadic jobs are only accepted at a processor if they can be completed in time, without causing the processor to miss hard deadlines of other jobs. We assume that aperiodic jobs are always accepted and are performed such that periodic and accepted sporadic jobs do not miss their deadlines. Sporadic and aperiodic jobs that need to be executed at a processor are placed in job queues. The queueing discipline of aperiodic jobs tries to minimize the penalty associated with missed soft deadlines (for example, minimize the number of missed soft deadlines, or the average amount of time by which an aperiodic job misses its deadline).

Unless stated otherwise, we assume that there is no resource competition and that a job is preemptive, meaning that it can be suspended at any time during its execution.

# Scheduling Periodic Jobs

A popular scheduler for periodic tasks is the rate-monotonic scheduler, which gives periodic jobs with a shorter period a higher priority. A strong point of this scheduler is that the static priority at the level of tasks makes its schedules relatively easy to compute and predict. The idea behind the rate-monotonic scheduler is that if a periodic job $J _ { 1 }$ has a shorter period than a periodic job $J _ { 2 }$ , then the relative deadline of $J _ { 1 }$ is shorter than the relative deadline of $J _ { 2 }$ . However, it may be the case that $J _ { 2 }$ has been released before $J _ { 1 }$ , in which case $J _ { s }$ has an earlier deadline than $J _ { 1 }$ . As a result, the rate-monotonic scheduler is not optimal, in the sense that it may cause periodic jobs to miss their deadlines even in cases where the utilization of the periodic tasks at a processor is less than 1.

Example 20.2 Consider a single processor, with periodic tasks $T _ { 1 } = ( 0 , 4 , 2 )$ and $T _ { 2 } = ( 0 , 6 , 3 )$ . Note that the utilization is $\begin{array} { r } { \frac { 2 } { 4 } + \frac { 3 } { 6 } = 1 } \end{array}$ , ,. The rate-monotonic scheduler, which gives jobs from $T _ { 1 }$ , ,a higher priority than jobs from $T _ { 2 }$ , schedules the periodic jobs as follows.

![](images/9d94cd142de30bcd1310206773141b109649847b700c919f12b7c6eda7641e84.jpg)

Note that $T _ { 2 }$ is preempted by $T _ { 1 }$ at times 4 and 8. The first periodic job of $T _ { 2 }$ misses its deadline at time 6.

The earliest deadline first scheduler gives a job a higher priority if its deadline is earlier. In the case of preemptive jobs and no competition for resources, this scheduler is optimal in the sense that if utilization at a processor does not exceed 1, then periodic jobs will be scheduled in such a way that no deadlines are missed.

Example 20.3 Consider the setting of example 20.2, a single processor with periodic tasks $T _ { 1 } = ( 0 , 4 , 2 )$ and $T _ { 2 } = ( 0 , 6 , 3 )$ . The earliest deadline first scheduler may schedule the periodic jobs as follows.

![](images/bf9fb25f3b1ddcb4c1117170c6e4a63fbcdbcf09f9b750b5ac750c292120ff95.jpg)

No deadlines are missed. Note that at time 8 it would also be possible to let $J _ { 1 }$ preempt $J _ { 2 }$ , because both jobs have their deadlines at time 12.

The least slack-time first scheduler gives a job a higher priority if it has less slack. This scheduler is also optimal: if utilization at a processor does not exceed 1, then periodic jobs will be scheduled in such a way that no deadlines are missed.

The slack of a job gives precise information on how much time can be spent on other jobs without this job missing its deadline. However, continuously keeping track of and comparing the slack of all jobs imposes computational overhead. Another drawback of the least slack-time first scheduler is that priority between jobs is dynamic in the sense that it may change over time. Continuous scheduling decisions would lead to what is called context switch overhead in the case of two jobs with the same amount of slack, because they would interrupt each other repeatedly.

In the case of nonpreemptive jobs or resource competition, it may be impossible to schedule periodic jobs in such a way that no deadlines are missed, even in cases where utilization at a processor is (much smaller than) 1. For instance, suppose there are two nonpreemptive periodic tasks $( 0 , 1 , e )$ and $( 0 , p , 2 )$ . No matter how small $e > 0$ and how large $p$ , , , ,are chosen, as soon as a job of the second periodic task is executed, a job of >the first periodic task will miss its deadline. The same holds if these periodic tasks are preemptive but both require the same resource from start to finish. Moreover, nonpreemptive jobs or resource competition can give rise to scheduling anomalies: shorter execution times may lead to violation of deadlines. This is shown in the next example.

Example 20.4 Let three nonpreemptive jobs be executed at the same processor: job $J _ { 1 }$ is released at time 0 with a deadline at time 2 and execution time 1; job $J _ { 2 }$ is released at time 1 with a deadline at time 5 and execution time 2; and job $J _ { 3 }$ is released at time 2 with a deadline at time 3 and execution time 1. The earliest deadline first and least slack-time first schedulers both schedule these three jobs as follows.

![](images/917820ec93c019d544e8fd1f99dedd6d64d17e529b78e86879fb50d2c57183c7.jpg)

Job $J _ { 3 }$ misses its deadline at time 3.

If the execution time of $J _ { 1 }$ is increased from 1 to 2, then the earliest deadline first and least slack-time first schedulers both schedule these three jobs as follows.

![](images/20c3b7719bbcd9b8bb9cf8509dfa56ede75028a80ea5d1137bda3f026f3c3660.jpg)

In this case, no deadlines are missed.

We assume that aperiodic jobs are always accepted for execution at a processor and that they are executed in such a way that periodic and accepted sporadic jobs do not miss their hard deadlines. The challenge is to execute aperiodic jobs in such a way that they adhere to their soft deadlines as much as possible.

A straightforward solution is the background server, which schedules aperiodic jobs only in idle time, when no periodic and sporadic jobs are available for execution. The drawback is that this server may needlessly let an aperiodic job miss its deadline.

Example 20.5 Let aperiodic job $A$ have execution time 1 and a deadline one time unit away, while sporadic job $s$ has execution time 1 and a deadline ten time units away. Although A could easily be scheduled before $s$ , the background server would schedule $s$ first, causing $A$ to miss its deadline.

In the slack stealing server, an aperiodic job may be executed as long as the processor has slack, meaning that it could idle without causing periodic or sporadic jobs to miss their deadlines. The drawback of this server is that the amount of slack of a processor is difficult to compute because it changes over time, and in practice one would need to take imprecise release and execution times into account.

Example 20.6 Suppose a processor is executing periodic tasks $T _ { 1 } = ( 0 , 2 , \frac { 1 } { 2 } )$ and $T _ { 2 } = ( 0 , 3 , \frac { 1 } { 2 } )$ , and that , , , ,aperiodic jobs are available for execution at this processor in the time interval [0 6]. The following graph ,depicts how, with the slack stealing server, the amount of slack of the processor changes over time.

![](images/b61387cb3f28b16833fe61aaac5db0762fa2672145e640bcb518821d79a68760.jpg)

In the time intervals $\langle 0 , 1 \frac { 1 } { 2 } \rangle$ , $\langle 2 , 2 { \scriptstyle { \frac { 1 } { 2 } } } \rangle$ , $\langle 3 , 3 \frac { 1 } { 2 } \rangle$ , and $\langle 4 , 5 \rangle$ , aperiodic jobs are executed. A periodic job from $T _ { 1 }$ is executed in $\bigl \langle 1 \frac { 1 } { 2 } , 2 \bigr \rangle$ , $\langle 3 \frac 1 2 , 4 \rangle$ ,, and $\langle 5 , 5 \frac { 1 } { 2 } \rangle$ ,and a periodic job from $T _ { 2 }$ is executed in $\langle 2 { \scriptstyle { \frac { 1 } { 2 } } } , 3 \rangle$ and $\left. 5 { \frac { 1 } { 2 } } , 6 \right.$ .

We discuss three more servers that are based on utilization. Suppose periodic tasks $T _ { k } = \left( r _ { k } , p _ { k } , e _ { k } \right)$ for $k = 1 , \ldots , n$ , ,are being executed at the processor under consideration. For simplicity, we ignore sporadic jobs.

The polling server carries two parameters, $p _ { s }$ and $e _ { s }$ . In each period of length $p _ { s }$ , the first $e _ { s }$ time units can be used to execute aperiodic jobs. The polling server works correctly if

$$
\sum _ { k = 1 } ^ { n } { \frac { e _ { k } } { p _ { k } } } + { \frac { e _ { s } } { p _ { s } } } \leq 1 .
$$

For the correctness of the polling server, it is essential that in a period $p _ { s }$ , aperiodic jobs are executed only in the first $e _ { s }$ time units; see example 20.7. A drawback of the polling server is that aperiodic jobs released just after the first $e _ { s }$ time units of a period $p _ { s }$ may be delayed needlessly.

The deferrable server is similar to the polling server but allows aperiodic jobs to be executed for $e _ { s }$ time units in the entire period $p _ { s }$ , not only at the start. The following example shows that, for the deferrable server, criterion (20.1) for the values $p _ { s }$ and $e _ { s }$ would be incorrect.

Example 20.7 Consider a processor with one periodic task $T = ( 2 , 5 , 3 \frac { 1 } { 3 } )$ , and let $p _ { s } = 3$ and $e _ { s } = 1$ . Note that criterion (20.1) is satisfied.

Let an aperiodic job $A$ with execution time 2 arrive at time 2. The deferrable server would allow $A$ to execute at the end of the first period $p _ { s }$ , from time 2 until time 3, and at the start of the second period $p _ { s }$ , from time 3 until time 4. As a result, the first periodic job, which is released at time 2, can start execution only at time 4 and until time $7 \frac { 1 } { 3 }$ . So it misses its deadline at time 7.

A drawback of the deferrable server is that it is not easy to determine optimal values for $p _ { s }$ and $e _ { s }$ .

The total bandwidth server fixes a utilization rate $\tilde { u } _ { s }$ for aperiodic jobs such that

$$
\sum _ { k = 1 } ^ { n } \frac { e _ { k } } { p _ { k } } + \tilde { u } _ { s } \leq 1 .
$$

When the queue of aperiodic jobs gets a new head, a deadline $d$ is determined for this head as follows. I, at a time $t$ either a job arrives at the empty aperiodic queue or an aperiodic job completes and the tail of the aperiodic queue is nonempty, then

$$
d \gets \operatorname* { m a x } \{ d , t \} + \frac { e } { \tilde { u } _ { s } } ,
$$

where $e$ denotes the execution time of the new head of the aperiodic queue. Initially, $d = 0$

Aperiodic jobs can now be treated in the same way as periodic jobs, by the earliest deadline first scheduler. Periodic jobs are guaranteed to meet their deadlines (in the absence of sporadic jobs), and aperiodic jobs meet the deadlines assigned to them (which may differ from their actual soft deadlines).

Example 20.8 Consider a processor with two periodic tasks $T _ { 1 } = ( 0 , 2 , 1 )$ and $T _ { 2 } = ( 0 , 3 , 1 )$ . We fix $\begin{array} { r } { \tilde { u } _ { s } = \frac { 1 } { 6 } } \end{array}$

<html><body><table><tr><td>1</td><td>JJA 2</td><td></td><td></td><td>J</td><td></td><td>AJ</td><td></td><td>J</td><td>J</td><td>A3</td><td>J</td><td>J</td><td>+</td></tr></table></body></html>

Aperiodic job $A _ { 1 }$ , released at time 1 with execution time $\frac { 1 } { 2 }$ , gets (at 1) deadline $1 + 3 = 4$ . Aperiodic job $A _ { 2 }$ , released at time 2 with execution time $\frac { 2 } { 3 }$ , gets (at $2 \textstyle { \frac { 1 } { 2 } }$ ) deadline $4 + 4 = 8$ . Aperiodic job $A _ { 3 }$ , released at time 3 with execution time $\frac { 2 } { 3 }$ , gets (at $6 { \scriptstyle { \frac { 1 } { 6 } } }$ ) deadline $8 + 4 = 1 2$

Scheduling Sporadic Jobs

We now present an acceptance test for sporadic jobs. A sporadic job can be accepted at a processor only if it can be executed before its (hard) deadline without causing the violation of deadlines of periodic and accepted sporadic jobs at this processor.

A sporadic job with deadline $d$ and execution time $e$ that is offered to a processor at time $t$ is accepted if utilization of the periodic and accepted sporadic jobs in the time interval $[ t , d ]$ is never more than $1 - { \frac { e } { d - t } }$ . If accepted, utilization in $[ t , d ]$ is increased with $\frac { e } { d - t }$ , . Periodic and accepted sporadic jobs can be scheduled ,according to the earliest deadline first scheduler.

Example 20.9 Consider a processor with one periodic task $T = ( 0 , 2 , 1 )$ . Utilization of this periodic task over the entire time domain is $\frac { 1 } { 2 }$ .

Sporadic job $S _ { 1 }$ with execution time 2 and deadline 6 is offered to the processor at time $1 . S _ { 1 }$ is accepted, and utilization in [1 6] is increased to $\textstyle { \frac { 1 } { 2 } } + { \frac { 2 } { 5 } } = { \frac { 9 } { 1 0 } }$ .   
Sporadic job $S _ { 2 }$ ,   with execution time 2 and deadline 20 is offered to the processor at time 2. $S _ { 2 }$ is rejected because utilization in the time interval [2 6] would increase beyond 1.   
Sporadic job $S _ { 3 }$ ,with execution time 1 and deadline 13 is offered to the processor at time 3. $S _ { 3 }$ is accepted, utilization in [3 6] is increased to ${ \frac { 9 } { 1 0 } } + { \frac { 1 } { 1 0 } } = 1$ , and utilization in [6 13] is increased to $\textstyle { \frac { 1 } { 2 } } + { \frac { 1 } { 1 0 } } = \frac { 3 } { 5 }$ = 35 .

![](images/3b3080024f6d1782ed27cedb81a0225ac44cea0ec1ff0621b618b9fcf5af081c.jpg)

The acceptance test may reject schedulable sporadic jobs. In particular, sporadic job $S _ { 2 }$ in the previous example is schedulable, but it is nevertheless rejected.

The total bandwidth server can be integrated with the acceptance test for sporadic jobs, for example, by making the allowed utilization rate $\tilde { u } _ { s }$ for the total bandwidth server dynamic.

# 20.3 Resource Access Control

So far, we have ignored competition for resources, such as a block of memory. In this section, we consider resource units that can be requested by a job during its execution and are allocated to jobs in a mutually exclusive fashion. When a requested resource is refused, the job is preempted.

One danger of resource sharing is that it may give rise to deadlock, when two jobs block each other because they hold different resources and these jobs require both resources. A second danger is that a highpriority job $J$ may be blocked by a sequence of low-priority jobs if $J$ requires a resource that is being held by a job with a very low priority. We give examples of these two situations.

Example 20.10 Consider jobs $J _ { 1 }$ and $J _ { 2 }$ , where $J _ { 1 }$ has a higher priority than $J _ { 2 }$ , and resources $R$ and $R ^ { \prime }$ . First, $J _ { 2 }$ is executing, and claims $R$ . Then, $J _ { 1 }$ arrives at the same processor, preempts $J _ { 2 }$ , starts executing, and claims $R ^ { \prime }$ . Next, $J _ { 1 }$ requires $R$ ; since this resource is held by $J _ { 2 } , J _ { 1 }$ is preempted and $J _ { 2 }$ continues its execution. Finally, $J _ { 2 }$ requires $R ^ { \prime }$ ; since this resource is held by $J _ { 1 } , J _ { 2 }$ is preempted. Now $J _ { 1 }$ is blocked because $J _ { 2 }$ holds $R$ , while $J _ { 2 }$ is blocked because $J _ { 1 }$ holds $R ^ { \prime }$ . So $J _ { 1 }$ and $J _ { 2 }$ are deadlocked.

Example 20.11 Consider jobs $J _ { 0 } , J _ { 1 } , \ldots , J _ { k }$ , with $J _ { 0 } > J _ { 1 } > \cdots > J _ { k }$ as priorities. A resource $R$ is required by both $J _ { 0 }$ and $J _ { k }$ .

First, $J _ { k }$ is executing and claims $R$ . Then, $J _ { k - 1 }$ arrives at the same processor, preempts $J _ { k }$ , and starts executing. Next, $J _ { k - 2 }$ arrives at the same processor, preempts $J _ { k - 1 }$ , and starts executing. This pattern is repeated, until finally $J _ { 0 }$ arrives at the same processor, preempts $J _ { 1 }$ , starts executing, and requires $R$ . Since this resource is held by $J _ { k } , J _ { 0 }$ is preempted, and $J _ { 1 }$ (which has the highest priority of the available jobs) continues its execution. When $J _ { 1 }$ is completed, $J _ { 2 }$ continues its execution; upon completion of $J _ { 2 } , \ J _ { 3 }$ continues its execution, and so on, until finally $J _ { k }$ continues its execution, completes, and releases $R$ . Only then can $J _ { 0 }$ claim $R$ and continue its execution.

<html><body><table><tr><td>Jk</td><td></td><td>Jk-1···</td><td>J1</td><td>Jo</td><td></td><td>···</td><td>Jk-1</td><td>J</td><td>J0</td><td></td></tr></table></body></html>

Priority inheritance makes blocking of a high-priority job $J$ by a sequence of low-priority jobs less likely. The idea is that when a job $J _ { 1 }$ is blocked because it requires a resource that is held by a job $J _ { 2 }$ , and $J _ { 1 }$ has a higher priority than $J _ { 2 }$ , then $J _ { 2 }$ inherits the priority of $J _ { 1 }$ as long as it is blocking the execution of $J _ { 1 }$ .

Example 20.12 We revisit example 20.11 with priority inheritance. When $J _ { 0 }$ requires $R$ , $J _ { k }$ inherits the priority of $J _ { k }$ . So instead of $J _ { 1 }$ , now $J _ { k }$ continues its execution. When $J _ { k }$ completes and releases $R$ , $J _ { 0 }$ can claim $R$ and continue its execution.

<html><body><table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>JkJk-1··JJoJkJo···Jk-1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html>

However, with priority inheritance, a deadlock can still occur. For instance, priority inheritance has no effect on the execution discussed in example 20.10. Such deadlocks can be avoided by a priority ceiling. The priority ceiling of a resource $R$ at a time $t$ is the highest priority of (known) jobs that will require $R$ at some time $\geq t$ . The priority ceiling of a processor at a time $t$ is the highest priority ceiling of resources that are in use at time $t$ . The priority ceiling of a processor has a special bottom value $\varOmega$ when no resources are in use. In Ωthe case of a priority ceiling, from the arrival of a job at a processor, this job is not released until its priority is higher than the priority ceiling of the processor.

The idea behind a priority ceiling is that a job $J$ is released only if all the resources it will require during its execution are not in use, because otherwise, upon the arrival of $J$ , the priority ceiling of the processor increases to the priority of $J$ if this priority ceiling is not beyond this level already. Of course, this approach works properly only if all the resources a job will require during its execution are always known beforehand. If priorities of jobs do not change over time (as is the case for the earliest deadline first scheduler but not for the least slack-time first scheduler), then deadlocks like the one in example 20.10 cannot occur.

Example 20.13 We revisit example 20.10 with a priority ceiling. When $J _ { 1 }$ arrives at the processor, the priority ceiling is increased to the priority of $J _ { 1 }$ , because $J _ { 1 }$ will require $R$ , and this resource is in use by $J _ { 2 }$ . So $J _ { 1 }$ is not yet released. When $J _ { 2 }$ completes and releases $R$ , the priority ceiling goes down to $\varOmega$ , so that $J _ { 1 }$ is released and starts executing.

A priority ceiling makes it less likely that a high-priority job is blocked by a series of lower-priority jobs.

Example 20.14 We revisit example 20.11 with a priority ceiling, under the assumption that the future arrival of $J _ { 0 }$ is known from the start. Since $J _ { 0 }$ will require $R$ , and $J _ { k }$ holds $R$ , the priority ceiling becomes the priority of $J _ { 0 }$ . Therefore, $J _ { k - 1 }$ is not released upon its arrival, and $J _ { k }$ continues its execution. When $J _ { k }$ completes and releases $R$ , the priority ceiling drops to $\varOmega$ , so jobs are released. When $J _ { 0 }$ arrives, it can claim $R$ and start executing straightaway.

<html><body><table><tr><td>Jk</td><td></td><td>Jk-2···</td><td></td><td>J1</td><td>Jo</td><td>J1</td><td>···</td><td>Jk-2</td><td>Jk-1</td><td></td></tr></table></body></html>

The priority ceiling has no effect on jobs that have been released. For instance, if in example 20.11 the arrival of $J _ { 0 }$ is known only upon its arrival, a priority ceiling does not help. Therefore, priority inheritance tends to be imposed on top of a priority ceiling.

The priority ceiling can be extended to a setting with multiple units of the same resource type. Then the definition of a priority ceiling is adapted as follows. The priority ceiling of a resource $R$ with $k$ free units at a time $t$ is the highest priority level of known jobs that require more than $k$ units of $R$ at some time $\geq t$ .

# Bibliographical notes

The slack stealing server originates from [73], the deferrable server from [113], and the total bandwidth server in [111]. Priority inheritance was introduced in [106], and the priority ceiling comes from [99].

# 20.4 Exercises

In these exercises, all jobs are assumed to be preemptive.

Exercise 20.1 [75] Consider a system with two processors. Suppose jobs $J _ { 1 } , J _ { 2 }$ , and $J _ { 3 }$ are released at time 0, with execution times 1, 1, and 2 and deadlines at times 1, 2, and 3, respectively.

(a) Let jobs $J _ { 4 }$ and $J _ { 5 }$ be released at time 2, both with execution time 1 and deadline 3. (b) Let job $J _ { 4 }$ be released at time 1, with execution time 2 and deadline 3. (There is no $J _ { 5 }$ .)

In both cases, give a schedule such that all deadlines are met.

Exercise 20.2 [75] Which of the following collections of periodic tasks are schedulable on one processor by the earliest deadline first scheduler? And which ones are schedulable by the rate-monotonic scheduler?

(a) (0 8 4), (0 10 2), (0 12 3).   
, , , , , ,(b) (0 8 4), (0 12 4), (0 20 4).   
, , , , , ,(c) (0 8 3), (0 9 3), (0 15 3).

Exercise 20.3 Consider a processor with one periodic task $( 0 , 5 , 3 { \frac { 1 } { 3 } } )$ and the earliest deadline first scheduler.

(a) Given a polling server with $p _ { s } = 3$ , what is the maximum value for $e _ { s }$ ?

(b) Given a deferrable server with $p _ { s } = 3$ , what is the maximum value for $e _ { s }$ ?   
(c) Given a total bandwidth server, what is the maximum utilization rate $\tilde { u } _ { s }$ ?   
(d) Suppose aperiodic jobs $A _ { 1 } , A _ { 2 }$ , and $A _ { 3 }$ arrive at times 3, 5, and 13, with execution times 1, 2, and 1, respectively. Explain how these aperiodic jobs are executed in the case of the deferrable server (with $e _ { s }$ maximal) and the total bandwidth server (with $\tilde { u } _ { s }$ maximal).

Exercise 20.4 Suppose that the total bandwidth server is adapted as follows. When at time $t$ an aperiodic job (with execution time $e$ ) arrives at the aperiodic queue while it is empty, $\begin{array} { r } { d \gets t + \frac { e } { \tilde { u } _ { s } } } \end{array}$ . Give an example to show that then, with the earliest deadline first scheduler, periodic jobs may miss their deadlines.

Exercise 20.5 Consider a processor with one periodic task (0 3 1). Suppose sporadic jobs $S _ { 1 }$ $\mathbf { \Phi } _ { 1 } , S _ { 2 } , S _ { 3 }$ , and $S _ { 4 }$ , ,arrive at times 0, 1, 3, and 6, with execution times 1, 3, 1, and 2, and with deadlines at times 1, 12, 7, and 14, respectively. Explain which of these jobs pass the acceptance test.

Exercise 20.6 Give an example where the acceptance test for sporadic jobs rejects a sporadic job at a time $t$ , while it accepts this same job at a time $t ^ { \prime } > t$ .

Exercise 20.7 Suggest an adaptation of the acceptance test for sporadic jobs that accepts more sporadic jobs (without computing slack). Give an example of a sporadic job that is accepted by your test but not by the original test. Does your test accept all schedulable sporadic jobs?

Exercise 20.8 Jobs $J _ { 1 }$ and $J _ { 2 }$ arrive at times 1 and 0, with execution times 1 and 2, respectively. Let $J _ { 1 }$ and $J _ { 2 }$ use resource $R$ for their entire executions, and $J _ { 2 }$ use resource $R ^ { \prime }$ for the last time unit of its execution.

(a) Job $J _ { 3 }$ arrives at time 1, with execution time 100. Let $J _ { 1 } > J _ { 3 } > J _ { 2 }$ . Explain how $J _ { 1 } , J _ { 2 }$ , and $J _ { 3 }$ are executed with and without priority inheritance.   
(b) Job $J _ { 4 }$ arrives at time 1, with execution time 2. Let $J _ { 4 }$ use resource $R ^ { \prime }$ for its entire execution and use resource $R$ for the last time unit of its execution. Let $J _ { 1 } > J _ { 4 } > J _ { 2 }$ . Explain how $J _ { 1 } , J _ { 2 }$ , and $J _ { 4 }$ are executed with and without priority inheritance.

Exercise 20.9 Let preemptive jobs $J _ { 1 } , J _ { 2 }$ , and $J _ { 3 }$ arrive at times 2, 1, and 0, respectively, with execution time 2. Let the priorities be $J _ { 1 } > J _ { 2 } > J _ { 3 }$ . Let $J _ { 1 }$ and $J _ { 3 }$ use resource $R$ for their entire executions. The jobs are > >executed using a priority ceiling.

(a) Explain how the three jobs are executed if the arrival of $J _ { 1 }$ is known from the start. (b) Explain how the three jobs are executed if the arrival of $J _ { 1 }$ is not known before time 2. Consider the cases with and without priority inheritance.

Exercise 20.10 Give an example to show that with a priority ceiling a job can still be blocked by a sequence of lower-priority jobs, even if there is priority inheritance and the arrivals of all jobs are known from the start.

Exercise 20.11 Give an example to show that a deadlock can occur if a priority ceiling is applied in combination with the least slack-time first scheduler. (The resources a job requires during its execution are assumed to be known beforehand.)

# Appendix: Pseudocode Descriptions

Pseudocode descriptions are presented for a considerable number of distributed algorithms discussed in the main body of this book. Several algorithms are excluded here either because their pseudocode descriptions are trivial or very similar to another algorithm that is included or because the main body contains a description that resembles the pseudocode.

Each piece of pseudocode is presented for a process $p$ or $p _ { i }$ ; its local variables are subscripted with $p$ or $i$ , respectively. We use Neighborsp to denote the set of neighbors of process $p$ in the network and use Processes for the set of processes in the network.

Each pseudocode description starts with a variable declaration section. Let bool, nat, int, and real denote the data type of Booleans, natural numbers, integers, and reals, with default initial values false for the first data type and 0 for the latter three. The operations $\wedge , \vee$ , and $\neg$ on Booleans denote conjunction, disjunction, and negation, respectively. The data type dist, representing distance, consists of the natural numbers extended with infinity $\infty$ , where $\infty + d = d + \infty = \infty$ for all distance values $d$ , and $d < \infty$ for all $d \neq \infty$ ; its default initial value is $\infty$ .

The data type of processes in the network, proc, has default initial value $\perp$ (i.e., undefined). The data types mess-queue and proc-queue represent FIFO queues of basic messages and processes, respectively. Likewise, mess-set, proc-set, proc-nat-set, proc-real-nat-set, and proc-dist-set represent sets of basic messages; processes; pairs of a process and a natural number; triples of a process, a natural number, and a real value; and pairs of a process and a distance value, respectively. Variables containing queues or sets have as default initial value $\varnothing$ ; that is, empty. There are three operations on queues: head produces the head and tail the tail of the queue (on the empty queue, these operations are undefined), while append $( \varrho , e )$ appends element $e$ at the end of queue $Q$ .

We recall that assignment of a new value to a variable is written as $\gets$ . Equality between two data elements, $d _ { 1 } = d _ { 2 }$ (or between two sets, $S _ { 1 } = S _ { 2 }$ ), represents a Boolean value, which is true if and only if the two elements (or sets) are equal. We also recall that the network topology is supposed to be strongly connected. In the pseudocode, it is assumed that the network size $N$ is greater than one.

A process is supposed to interrupt the execution of a procedure call (under a boxed text, such as “If $p$ receives [...]”) only if it needs to wait for an incoming message, or in the case of a while $^ b$ do statement end while construct, or when it enters its critical section.

# A.1 Chandy-Lamport Snapshot Algorithm

The Boolean variable recorded ${ \bf \chi } _ { p } ^ { \prime }$ in the following pseudocode is set (to true) when $p$ takes a local snapshot of its state. For each incoming channel $c$ of $p$ , the Boolean variable marker $_ p [ c ]$ is set when a marker message arrives at $p$ through $c$ , and the queue state $_ p [ c ]$ keeps track of the basic messages that arrive through channel $c$ after $p$ has taken its local snapshot and before a marker message arrives through $c$ .

bool recorded $_ p$ , marker $_ p [ c ]$ for all incoming channels $c$ of $p$ ;   
mess-queue state $_ p [ c ]$ for all incoming channels $c$ of $p$ ;

If $p$ wants to initiate a snapshot perform procedure TakeSnapshotp;

If $p$ receives a basic message $m$ through an incoming channel $c _ { 0 }$ if recorded $_ p = t r u e$ and markerp[c0] $=$ false then state ${ \bf \dot { \boldsymbol } p } [ c _ { 0 } ] \gets \boldsymbol { a p p e n d } ( s t a t e _ { p } [ c _ { 0 } ] , m )$ ;

end if

If $p$ receives $\langle \mathbf { m a r k e r } \rangle$ through an incoming channel $c _ { 0 }$

perform procedure TakeSnapshotp;   
marke $r _ { p } [ c _ { 0 } ] \gets t r u e$ ;   
if marke $r _ { p } [ c ] =$ true for all incoming channels $c$ of $p$ then terminate;   
end if

Procedure TakeSnapshotp

if recorded ${ \bf \Pi } _ { p } = { \bf \Pi } _ { \cdot }$ false then recorded $\mathbf { \omega } _ { p } \gets t r u e$ ; send $\langle \mathbf { m a r k e r } \rangle$ into each outgoing channel of $p$ ; take a local snapshot of the state of $p$ ;   
end if

# A.2 Lai-Yang Snapshot Algorithm

The variable recorded $\boldsymbol { \mathsf { \Pi } } _ { p }$ is set when $p$ takes a local snapshot of its state. The set $S t a t e _ { p } [ q p ]$ keeps track of the basic messages that arrived postsnapshot at $p$ through its incoming channel $q p$ and that were sent presnapshot by $q$ . The variable counter $\dot { \mathbf { \eta } } _ { q } [ q p ]$ at $q$ counts how many basic messages $q$ sent presnapshot into its outgoing channel $q p$ , while the variable counter $\dot { p } [ q p ]$ at $p$ keeps track how many basic messages $p$ will receive postsnapshot through its incoming channel $q p$ that were sent presnapshot by $q$ . Right before taking its local snapshot, $q$ sends the control message $\langle \mathrm { p r e s n a p } , c o u n t e r _ { q } [ q p ] + 1 \rangle$ to $p$ (the $+ 1$ is present because the control message itself is also counted), and $p$ adds the value within this message to the value of its variable counte $r _ { p } [ q p ]$ . Finally, $p$ terminates when it has received a control message $\left. \mathbf { p r e s n a p } , k \right.$ and $k - 1$ basic messages with the tag false through each incoming channel $q p$ .

bool recorded $\boldsymbol { \mathsf { \Pi } } _ { p }$ ;   
nat counter $_ p [ c ]$ for all channels $c$ of $p$ ;   
mess-set State $_ p [ c ]$ for all incoming channels $c$ of $p$ ;

If $p$ wants to initiate a snapshot perform procedure TakeSnapshotp;

If $p$ sends a basic message $m$ into an outgoing channel $c _ { 0 }$ send $\langle m , r e c o r d e d _ { p } \rangle$ into $c _ { 0 }$ ; ,if recorded ${ \bf \Pi } _ { p } =$ false then $c o u n t e r _ { p } [ c _ { 0 } ] \gets c o u n t e r _ { p } [ c _ { 0 } ] + 1$

end if

If $p$ receives $\langle m , b \rangle$ through an incoming channel $c _ { 0 }$

if $b = t r u e$ then perform procedure TakeSnapshot $_ p$ ;   
else if recorded ${ \bf \Pi } _ { p } =$ false then counte $\mathbf { \dot { \rho } } _ { p } [ c _ { 0 } ] \gets c o u n t e r _ { p } [ c _ { 0 } ] - 1$ ;   
else $S t a t e _ { p } [ c _ { 0 } ] \gets S t a t e _ { p } [ c _ { 0 } ] \cup \{ m \}$ ; if $| S t a t e _ { p } [ c ] | + 1 = c o u n t e r _ { p } [ c ]$ for all incoming channels $c$ of $p$ then terminate; end if   
end if

If $p$ receives $\langle \mathbf { p r e s n a p } , \ell \rangle$ through an incoming channel $c _ { 0 }$

count $e r _ { p } [ c _ { 0 } ] \gets c o u n t e r _ { p } [ c _ { 0 } ] + \ell$ ;   
ℓperform procedure TakeSnapshotp;   
if $| S t a t e _ { p } [ c ] | + 1 = c o u n t e r _ { p } [ c ]$ for all incoming channels $c$ of $p$ then terminate;   
end if

$$
\boxed { \mathrm { P r o c e d u r e ~ } T a k e S n a p s h o t _ { p } }
$$

if recorded ${ \bf \Pi } _ { p } =$ false then recorded $\mathbf { \omega } _ { p } \gets t r u e$ ; send ⟨presnap $c o u n t e r _ { p } [ c ] + 1 \rangle$ into each outgoing channel $c$ ; ,take a local snapshot of the state of $p$ ;   
end if

# A.3 Cidon’s Depth-First Search Algorithm

The variable $p a r e n t _ { p }$ contains the parent of $p$ in the spanning tree rooted at the initiator (or $\perp$ if $p$ has no parent); $i n f o _ { p }$ is set when $p$ sends the token for the first time, and token $_ p [ q ]$ is set when $p$ is certain that

neighbor $q$ will receive or has received the token. In the variable forward $_ p$ , the neighbor is stored to which $p$ forwarded the token last.

<html><body><table><tr><td>bool infop,tokenp[r] for all r ∈Neighborsp; proc parentp,forwardp;</td></tr><tr><td>If p is the initiator</td></tr><tr><td>perform procedure ForwardTokenp;</td></tr><tr><td>If p receives (info) from a neighbor q</td></tr><tr><td>if forwardp ≠ q then tokenp[q← true;</td></tr><tr><td>else perform procedure ForwardTokenp;</td></tr><tr><td>end if If p receives (token) from a neighbor q</td></tr><tr><td>if forwardp =⊥ then parentp ←q；tokenp[q]← true; perform procedure ForwardTokenp;</td></tr><tr><td>else if forwardp = q then perform procedure ForwardTokenp; else tokenp[q] ← true;</td></tr><tr><td>end if Procedure ForwardTokenp</td></tr><tr><td>if {r ∈Neighborsp|tokenp[r]=false}≠O then choose a q from this set,and send (token) to q; forwardp ← q;tokenp[q] ← true; if infop =false then</td></tr><tr><td>send (info)to each r ∈ Neighborsp\{q,parentp}; infop ←true; end if</td></tr><tr><td>else if parentp ≠⊥then send (token) to parent p; else decide;</td></tr></table></body></html>

# A.4 Tree Algorithm

The variable $p a r e n t _ { p }$ contains the parent of $p$ in the spanning tree. The variable received ${ \bf \Pi } _ { p } ^ { \prime } [ q ]$ is set when $p$ receives a wave message from neighbor $q$ . Messages are included to inform all processes of the decision.

bool received $_ p [ r ]$ for all $r \in N e i g h b o r s _ { p }$ ;   
proc parentp;   
Initialization of p   
perform procedure SendWavep;   
If $p$ receives ⟨wave⟩ from a neighbor q   
received $p [ q ] \gets t r u e$ ;   
perform procedure SendWavep;   
Procedure SendWavep   
if $| \{ r \in N e i g h b o r s _ { p } \mid r e c e i \nu e d _ { p } [ r ] = f a l s e \} | = 1$ then send ⟨wave⟩ to the only $q \in N e i g h b o r s _ { p }$ with received ${ \dot { \mathbf { \eta } } } _ { p } [ q ] = { \dot { \mathbf { \eta } } } _ { \mathbf { \eta } }$ false; $p a r e n t _ { p } \gets q$ ;   
else if $| \{ r ^ { * } $ en decide; send $\left. \mathrm { i n f } \mathbf { 0 } \right.$ to each $r \in N e i g h b o r s _ { p } \setminus \{ p a r e n t _ { p } \} ;$ ;   
end if   
If $p$ receives $\left. \mathbf { i n f 6 } \right.$ from parentp   
send $\left. \mathbf { i n f 6 } \right.$ to each $r \in N e i g h b o r s _ { p } \setminus \{ p a r e n t _ { p } \} ;$

# A.5 Echo Algorithm

The variable parentp contains the parent of $p$ in the spanning tree rooted at the initiator. The variable received $\dot { p }$ counts how many wave messages have arrived at $p$ .

<html><body><table><tr><td>nat receivedp; proc parent p;</td></tr><tr><td>If p is the initiator</td></tr><tr><td>send (wave) to each r E Neighborsp;</td></tr><tr><td>If p receives (wave) from a neighbor q</td></tr><tr><td>receivedp ←receivedp+1; if parent p =⊥and p is a noninitiator then</td></tr><tr><td>parentp ←q; if |Neighborsp| &gt;1 then</td></tr><tr><td>send (wave) to each r ∈ Neighborsp\{q};</td></tr><tr><td>else send (wave) to q;</td></tr><tr><td>end if else if receivedp = |Neighborsp| then</td></tr></table></body></html>

if parent $_ p \neq \perp$ then send ⟨wave⟩ to parentp; else decide; end if end if

# A.6 Shavit-Francez Termination Detection Algorithm

The variable parentp contains the parent of $p$ in a tree in the forest, and $c c _ { p }$ keeps track of (or better, estimates from above) the number of children of $p$ in its tree. The variable active $\dot { p }$ is set when $p$ becomes active, and it is reset when $p$ becomes passive.

bool activep;   
nat $c c _ { p }$ ;   
proc parentp;

<html><body><table><tr><td>If p is an initiator</td></tr><tr><td>activep ← true;</td></tr><tr><td>If p sends a basic message</td></tr><tr><td>cCp ←cCp+1; If p receives a basic message from a neighbor q</td></tr><tr><td>if activep =false and ccp = O then activep ←true;parentp ←q; else send (ack) to q;</td></tr><tr><td>end if If p receives (ack)</td></tr><tr><td>cCp ←cCp-1;</td></tr><tr><td>perform procedure LeaveTree p; If p becomes passive</td></tr><tr><td>activep ←false;</td></tr><tr><td>perform procedure LeaveTree p; Procedure LeaveTree p if activep = false and ccp = O then</td></tr></table></body></html>

start a wave, tagged with $p$ ; end if end if

If $p$ receives a wave message

if $a c t i \nu e _ { p } = .$ false and $c c _ { p } = 0$ then act according to the wave algorithm; in the case of a decide event, call Announce;   
end if

# A.7 Rana’s Termination Detection Algorithm

The variable active $\dot { p }$ is set when $p$ becomes active, and it is reset when $p$ becomes passive. The variable clockp represents the clock value at $p$ , and unackp keeps track of the number of unacknowledged basic messages sent by $p$ .

bool activep;

<html><body><table><tr><td>boolactivep; nat clockp, unackp;</td></tr><tr><td>If p is an initiator activep ← true;</td></tr><tr><td>If p sends a basic message</td></tr><tr><td>unackp ←unackp +1;</td></tr><tr><td>If p receives a basic message from a neighbor q</td></tr><tr><td>activep ← true; send (ack,clockp) to q;</td></tr><tr><td>If p receives (ack,t) clockp ←max{clockp,t +1}；unackp ←unackp -1;</td></tr><tr><td>if activep =false and unackp = O then start a wave, tagged with p and clockp; end if</td></tr><tr><td>If p becomes passive activep ←false;</td></tr><tr><td>if unackp = O then start a wave, tagged with p and clockp; end if</td></tr><tr><td>If p receives a wave message tagged with q and t if activep = false and unackp = Oand clockp ≤t then</td></tr></table></body></html>

act according to the wave algorithm, for the wave tagged with $q$ and $t$

in the case of a decide event, call Announce; end if $c l o c k _ { p } \gets \operatorname* { m a x } \{ c l o c k _ { p } , t \} ;$

# A.8 Safra’s Termination Detection Algorithm

The variable activep is set when $p$ becomes active, and it is reset when $p$ becomes passive. The variable $b l a c k _ { p }$ is set when $p$ receives a basic message, and it is reset when $p$ forwards the token. Moreover, the initiator of the control algorithm at the start sets this variable to make sure it sends out the token when it becomes passive for the first time. As long as $p$ is holding the token, $t o k e n _ { p }$ is set. When $p$ sends or receives a basic message, mess-counter $\dot { \boldsymbol { p } }$ is increased or decreased by 1, respectively. The variable token-counte $\dot { \mathbf { \zeta } } _ { p }$ is used to store the counter value of the token. For simplicity, we assume that the initiator of the control algorithm is also an initiator of the basic algorithm.

bool activep, tokenp, blackp;   
int mess-counte $r _ { p }$ , token-counte $\boldsymbol { r } _ { p }$ ;

<html><body><table><tr><td>If p is the initiator of the control algorithm</td><td></td></tr><tr><td>tokenp ← true;blackp ←true;</td><td></td></tr><tr><td>If p is an initiator of the basic algorithm</td><td></td></tr><tr><td>activep ←true;</td><td></td></tr><tr><td>If p sends a basic message</td><td></td></tr><tr><td>mess-counterp ←mess-counterp +1;</td><td></td></tr><tr><td> If p receives a basic message</td><td></td></tr><tr><td></td><td>activep ←true；blackp ←true；mess-counterp ←mess-counterp -1;</td></tr><tr><td>If p becomes passive activep ←false;</td><td></td></tr><tr><td>perform procedure TreatTokenp;</td><td></td></tr><tr><td>If p receives (token,b,k)</td><td>tokenp ←true；blackp ←blackp Vb;token-counterp ←k;</td></tr><tr><td>perform procedure TreatTokenp;</td><td></td></tr><tr><td>Procedure TreatTokenp</td><td></td></tr><tr><td>if activep = false and tokenp = true then token-counterp ← token-counterp +mess-counterp if p is a noninitiator then</td><td></td></tr></table></body></html>

else if $b l a c k _ { p } = t r u e$ or token-counter $_ p > 0$ then send ⟨token false $0 \rangle$ >on a round trip through the network; token $_ { p } \gets$ false; $b l a c k _ { P } $ false; else call Announce; end if end if

# A.9 Weight-Throwing Termination Detection Algorithm

The variable $a c t i v e _ { p }$ is set when $p$ becomes active, and it is reset when $p$ becomes passive. The variable weightp contains the weight at $p$ , and total contains the total amount of weight in the network. The constant minimum, a real value between 0 and $\frac { 1 } { 2 }$ , represents the minimum allowed weight at a process. In the case of underflow, a noninitiator informs the initiator that it has added one extra unit of weight to the system, and it waits for an acknowledgment from the initiator. For simplicity, we assume that there is a bidirectional channel between the initiator and every other process in the network.

bool activep;   
real weight p, total only at the initiator;

If $p$ is the initiator

$$
a c t i \nu e _ { p } \gets t r u e ; \quad w e i g h t _ { p } \gets 1 ; \quad t o t a l \gets 1 ;
$$

If $p$ sends a basic message $m$ to a neighbor q

if $\frac { 1 } { 2 } \cdot w e i g h t _ { p } <$ minimum then if $p$ <is a noninitiator then send ⟨more-weight⟩ to the initiator to ask for extra weight; wait for an acknowledgment from the initiator to arrive; else $t o t a l \gets t o t a l + 1 $ end if $w e i g h t _ { p } \gets w e i g h t _ { p } + 1 ;$   
end if   
send $\begin{array} { r } { \langle m , \frac { 1 } { 2 } { \cdot } w e i g h t _ { p } \rangle } \end{array}$ to $q$ ;   
$w e i g h t _ { p } \gets \frac { 1 } { 2 } { \cdot } w e i g h t _ { p }$ ;   
If $p$ receives a basic message $\langle m , w \rangle$   
$a c t i \nu e _ { p } \gets t r u e ; \quad w e i g h t _ { p } \gets w e i g h t _ { p } + w ;$   
If $p$ becomes passive   
$a c t i v e _ { p } \gets f a l s e .$ ;   
if $p$ is a noninitiator then send ⟨return-weight $w e i g h t _ { p } \rangle$ to the initiator;

$w e i g h t _ { p } \gets 0$ ; else if tota $\mathbf { \Psi } ^ { \prime } = w e i g h t _ { p }$ then call Announce; end if

If initiator $p$ receives ⟨more-weight⟩ from a process q

$t o t a l \gets t o t a l + 1$ ;   
send an acknowledgment to $q$ ;

If initiator $p$ receives ⟨return-weight w⟩

$w e i g h t _ { p } \gets w e i g h t _ { p } + w$ ;   
if activ ${ \bf \dot { p } = }$ false and t $o t a l = w e i g h t _ { p }$ then call Announce;   
end if

# A.10 Chandy-Misra Routing Algorithm

The variable $p a r e n t _ { p }$ contains the parent of $p$ in the spanning tree rooted at the initiator, and $d i s t _ { p }$ is the distance value of $p$ toward the initiator.

dist ${ d i s t } _ { p }$ ;   
proc parentp;

If $p$ is the initiator

$d i s t _ { p } \gets 0$ ;   
send $\langle \mathbf { d i s t } , 0 \rangle$ to each $r \in N e i g h b o r s _ { p }$ ;

If $p$ receives $\langle \mathbf { d i s t } , d \rangle$ from a neighbor q

if $d + w e i g h t ( p q ) < d i s t _ { p }$ then $d i s t _ { p } \gets d + w e i g h t ( p q )$ ; $p a r e n t _ { p } \gets q$ ; send $\langle \mathbf { d i s t } , d i s t _ { p } \rangle$ to each $r \in N e i g \dot { h } b o r s _ { p } \setminus \{ q \}$ ;   
end if

# A.11 Merlin-Segall Routing Algorithm

The variable $p a r e n t _ { p }$ contains the parent of $p$ in the spanning tree rooted at the initiator, and $d i s t _ { p }$ is the distance value of $p$ toward the initiator. In new-parentp, the process is stored that sent the message to $p$ on which the current value of $d i s t _ { p }$ is based; at the end of a round, the value of new-parentp is passed on to parentp. In counte $\boldsymbol { r } _ { p }$ , $p$ keeps track of how many messages it has received in the current round.

nat counterp;   
dist distp;

proc parentp, new-parentp;

If $p$ is the initiator

$d i s t _ { p } \gets 0$ ;   
initiate a wave that determines a spanning tree of the network, captured by values of parentr for all r ∈ Processes, with   
$p$ as root;   
wait until this wave has terminated;   
for $k = 1$ to $N - 1$ do send $\langle \mathbf { d i s t } , 0 \rangle$ to each $r \in N e i g h b o r s _ { p }$ ; ,while counter $\dot { \boldsymbol { p } } < | N e i g h b o r s _ { p } |$ do <wait for a message $\langle \mathbf { d i s t } , d \rangle$ to arrive; counte $r _ { p } \gets c o u n t e r _ { p } + 1$ ; end while counte $r _ { p } \gets 0$ ;   
end for

If $p$ is a noninitiator

take part in the wave, and provide paren $\dot { p }$ with the resulting parent value;

for $k = 1$ to $N - 1$ do while counter $\dot { \boldsymbol { p } } < | N e i g h b o r s _ { p } |$ do <wait for a message $\langle \mathbf { d i s t } , \dot { d } \rangle$ from a $q \in N e i g h b o r s _ { p }$ ; counte $r _ { p } \gets c o u n t e r _ { p } + 1$ ; if $d + w e i g h t ( p q ) < d i s t _ { p }$ then $d i s t _ { p } \gets d + w e i g h t ( p q ) ; \quad n e w - p a r e n t _ { p } \gets q ;$ end if if $q = p a r e n t _ { p }$ then send $\langle \mathbf { d i s } \dot { \mathbf { t } } , d i s t _ { p } \rangle$ to each $r \in N e i g h b o r s _ { p } \setminus \{ p a r e n t _ { p } \}$ ; end if end while send $\langle \mathbf { d i s t } , d i s t _ { p } \rangle$ to parentp; $p a r e n t _ { p } \gets n e w – p a r e n t _ { p }$ ; $c o u n t e r _ { p } \gets 0$ ;   
end for

# A.12 Toueg’s Routing Algorithm

The variable $p a r e n t _ { p } [ q ]$ contains the parent of $p$ in the spanning tree rooted at process $q$ , and $d i s t _ { p } [ q ]$ is the distance value of $p$ toward destination $q$ . In round $\boldsymbol { \mathsf { \Pi } } _ { p }$ , $p$ keeps track of its round number. The distance values of the pivot in round $k$ are stored in $D i s t a n c e s _ { p } [ k ]$ . Each process that sends a request to $p$ for the distance values of the pivot in the current or a future round $k$ is stored in Forward ${ \bf \Phi } _ { p } [ k ]$ . We assume that $p$ only treats incoming requests when it is idle, to avoid having a request stored in Forward ${ \bf \Phi } _ { p } [ k ]$ after $p$ forwarded the distance values of the pivot in round $k$ . The pivot in round $k$ is denoted by pivot $\cdot ( k )$ . We include the optimization that a process, upon receiving distance values from the pivot, first checks which of its distance values are improved and then forwards only those elements of the set that attained an improved distance value.

nat round $p$ ;   
dist $d i s t _ { p } [ r ]$ for all r ∈ Processes;   
proc paren $_ p [ r ]$ for all r ∈ Processes;   
proc-set Forward $_ p [ k ]$ for all $k \in \{ 0 , . . . , N - 1 \}$ ;   
proc-dist-set Distance ${ \mathrm { \Delta } } _ { p } [ k ]$ for all $k \in \left\{ 0 , . . . , N - 1 \right\}$ ;

Initialization of p

$d i s t _ { p } [ p ] \gets 0$ ; parentp[r] ← r and $d i s t _ { p } [ r ] \gets w e i g h t ( p r )$ for all $r \in N e i g h b o r s _ { p }$ perform procedure Requestp;

Procedure Requestp

if $p = p i \nu o t ( r o u n d _ { p } )$ then send ⟨dist-set $\{ ( r , d i s t _ { p } [ r ] ) | r \in P r o c e s s e s \mathrm { a n d } d i s t _ { p } [ r ] < \infty \} $ to each $q \in F o r w a r d _ { p } [ r o u n d _ { p } ]$ ; perform procedure NextRound $\dot { p }$ ;   
else if parent $_ p [ p i \nu o t ( r o u n d _ { p } ) ] \ne \perp$ then send ⟨request round $_ p \rangle$ to parent $_ p [ p i \nu o t ( r o u n d _ { p } ) ]$ ;   
else perform procedure NextRound $_ p$ ;   
end if

If $p$ receives $\langle \mathbf { r e q u e s t } , k \rangle$ from a neighbor $q$

if $k < r o u n d _ { p }$ then <send ⟨dist-set Distances $_ p [ k ] \rangle$ to $q$ ;   
else ${ \mathit { F o r w a r d } } _ { \mathit { p } } [ k ] \gets { \mathit { F o r w a r d } } _ { \mathit { p } } [ k ] \cup \{ q \} ;$ ;   
end if

If $p$ receives ⟨dist-set Distances⟩ from parentp[pivot(roundp)]

for each s ∈ Processes do if there is a pair $( s , d )$ in Distances then if $d + d i s t _ { p } [ p i \nu o t ( r o u n d _ { p } ) ] < d i s t _ { p } [ s ]$ then paren $t _ { p } [ s ] \gets p a r e n t _ { p } [ p i \nu o t ( r o u n d _ { p } ) ]$ ; $d i s t _ { p } [ s ] \gets d + d i s t _ { p } [ p i \nu o t ( r o u n d _ { p } ) ] \mathrm { , }$ ; else remove entry $( s , d )$ from Distances; end if end if   
end for   
send $\langle \mathbf { d i s t - s e t } , D i s t a n c e s \rangle$ to each r ∈ Forward $_ p$ [roundp];   
D $i s t a n c e s _ { p } [ r o u n d _ { p } ] \gets D i s t a n c e s ;$   
perform procedure NextRound $_ p$ ;

Procedure NextRoundp if round $_ { p } < N - 1$ then

$r o u n d _ { p } \gets r o u n d _ { p } + 1$ ; perform procedure Requestp; else terminate; end if

# A.13 Frederickson’s Breadth-First Search Algorithm

The variable $p a r e n t _ { p }$ contains the parent of $p$ in the spanning tree rooted at the initiator, and $d i s t _ { p }$ is the distance value of $p$ toward the initiator. In $d i s t _ { p } [ r ]$ , $p$ stores the best-known distance value of neighbor $r$ . After $p$ has sent forward or explore messages, it uses $A c k _ { p }$ to keep track of the neighbors that should still send a (positive or negative) reply. In Reported $\mathbf { \Delta } _ { p } ^ { \prime }$ , $p$ keeps track of the neighbors to which it must send a forward message in the next round. The initiator maintains the round number in counter. During each round, $\ell$ levels are explored. For uniformity, messages $\langle \mathbf { r e v e r s e } , b \rangle$ are always supplied with the distance value of ℓthe sender.

nat counter only at the initiator;   
dist ${ d i s t } _ { p }$ , $d i s t _ { p } [ r ]$ for all $r \in N e i g h b o r s _ { p }$ ;   
proc paren $\dot { p }$ ;   
proc-set $A c k _ { p }$ , Reported $\dot { p }$ ;

If $p$ is the initiator

send $\left. \mathbf { e x p l o r e } , 1 \right.$ to each r ∈ Neighborsp;   
,distp ← 0; Ackp ← Neighborsp; counter ← 1;

If $p$ receives $\left. \mathbf { e x p l o r e } , k \right.$ from a neighbor q

$d i s t _ { p } [ q ] \gets \operatorname* { m i n } \{ d i s t _ { p } [ q ] , k - 1 \}$ ;   
if $k < d i s t _ { p }$ then $p a r e n t _ { p } \gets q ; \quad d i s t _ { p } \gets k ; \quad R e p o r t e d _ { p } \gets 0 ;$ ; if $k$ mod $\ell \neq 0$ then send ⟨explore $k + 1 \rangle$ to each $r \in N e i g h b o r s _ { p } \setminus \{ q \}$ ; $A c k _ { p } \gets \{ r \in N e i g h b o r s _ { p } | d i s t _ { p } [ r ] > k + 1 \}$ ; if $A c k _ { p } = 0$ then send ⟨reverse $k , f a l s e )$ to $q$ ; end if else send ⟨reverse $k , t r u e \rangle$ to $q$ ; end if   
else if $k > d i s t _ { p }$ or $k$ mod $\ell \neq 0$ then if $k \leq d i s t _ { p } + 2$ and $q \in A c k _ { p }$ then $A c k _ { p }  A c k _ { p } \backslash \{ q \}$ ; perform procedure ReceivedA $c k _ { p }$ ; else if $k = d i s t _ { p }$ then

$R e p o r t e d _ { p } \gets R e p o r t e d _ { p } \setminus \{ q \} ;$ end if else send ⟨reverse k false⟩ to $q$ ; end if

If $p$ receives $\langle \mathbf { r e v e r s e } , k , b \rangle$ from a neighbor $q$

$d i s t _ { p } [ q ] \gets \operatorname* { m i n } \{ d i s t _ { p } [ q ] , k \}$ ;   
if $k = d i s t _ { p } + 1$ then if $b = t r u e$ and $d i s t _ { p } [ q ] = k$ then Reported $\mathbf { \chi } _ { p } \gets R e p o r t e d _ { p } \cup \{ q \}$ ; end if if $q \in A c k _ { p }$ then $A c k _ { p } \gets A c k _ { p } \setminus \{ q \} ;$ ; perform procedure ReceivedAckp; end if   
end if

Procedure ReceivedAckp

if $A c k _ { p } = \emptyset$ then if parent $_ p \neq \perp$ then send ⟨reverse $d i s t _ { p } , R e p o r t e d _ { p } \neq \emptyset \rangle$ to parentp; else if Reported $\iota _ { p } \neq \emptyset$ ,then send ⟨forward $\ell$ ·counter⟩ to each r ∈ Reported $\ v { p }$ ; $A c k _ { p } \gets R e p o r t e d _ { p }$ ; Reported ${ \boldsymbol { \mathbf { \mathit { \Sigma } } } } _ { p } \gets { \boldsymbol { \mathbf { \emptyset } } }$ ; counter $ c o u n t e r + 1$ ; else terminate; end if   
end if

If $p$ receives ⟨forward k⟩ from a neighbor q

if $q = p a r e n t _ { p }$ then if $k < d e p t h _ { p }$ then <send ⟨forward $k \rangle$ to each r ∈ Reportedp; $A c k _ { p } \gets R e p o r t e d _ { p }$ ; Reported ${ \boldsymbol { \mathbf { \mathit { \Sigma } } } } _ { p } \gets { \boldsymbol { \mathbf { \emptyset } } }$ ; else $A c k _ { p } \gets \{ r \in N e i g h b o r s _ { p } \ : | \ : d i s t _ { p } [ r ] = \infty \} ;$ if $A c k _ { p } \neq \emptyset$ then send $\scriptstyle \left. \mathbf { e x p l o r e } , k + 1 \right.$ to each $r \in A c k _ { p }$ ; else send ⟨reverse $k , f a l s e )$ to $q$ ; end if end if   
end if

# A.14 Dolev-Klawe-Rodeh Election Algorithm

Initially, activep is set if $p$ is an initiator, and it is reset when $p$ becomes passive. If $p$ terminates as the leader, it sets leade ${ \bf \dot { \boldsymbol { p } } }$ . In election- $i d _ { p }$ , $p$ stores the $\mathrm { I D }$ it assumes for the current election round. In neighb-idp[0] and neighb- $\cdot i d _ { p }$ [1], $p$ stores the process IDs of its two nearest active predecessors in the directed ring in the current election round. A total order $<$ is assumed on process IDs. For simplicity, we abstract away from received messages for future election rounds.

bool activep, leade $r _ { p }$ ;   
proc election- $i d _ { p }$ , neighb- $i d _ { p } [ b ]$ for bits $^ b$ ; If $p$ is an initiator   
$a c t i \nu e _ { p } \gets t r u e$ ; election- $i d _ { p } \gets p$ ; send $\langle \mathbf { i d } , p , 0 \rangle$ ;

If p receives $\langle \mathbf { i d } , q , b \rangle$

if $a c t i v e _ { p } = t r u e$ then if $b = 0$ then send $\langle \mathbf { i d } , q , 1 \rangle$ ; end if neighb- $\cdot i d _ { p } [ b ]  q$ ; if neighb- $\cdot { i d _ { p } } [ 1 - b ] \neq \perp$ then perform procedure Compare $I D s _ { p }$ ; end if   
else send $\langle \mathbf { i d } , q , b \rangle$ ;   
end if

Procedure CompareIDsp

i $\mathbf { f } \operatorname* { m a x } \{ e l e c t i o n - i d _ { p } , n e i g h b - i d _ { p } [ 1 ] \} < n e i g h b - i d _ { p } [ 0 ] \mathbf { t } \mathbf { t }$ en election- $\cdot i d _ { p } \gets n e i g h b - i d _ { p } [ 0 ]$ ; send $\langle \mathbf { i d } , e l e c t i o n \mathbf { - } i d _ { p } , 0 \rangle$ ; for $b = 0$ and $b = 1$ ,do neighb- $\cdot i d _ { p } [ b ]  \bot$ ; end for   
else if $\operatorname* { m a x } \{ e l e c t i o n - i d _ { p } , n e i g h b - i d _ { p } [ 1 ] \} > n e i g h b - i d _ { p } [ 0 ]$ then active $_ p $ false;   
else leade $r _ { p } \gets t r u e$ ;   
end if

# A.15 Gallager-Humblet-Spira Minimum Spanning Tree Algorithm

The variable $p a r e n t _ { p }$ contains $p$ ’s parent toward the core edge of $p$ ’s fragment. The name and level of $p$ ’s fragment are stored in $n a m e _ { p }$ and leve $\boldsymbol { \mathbf { \ell } } _ { p }$ . Initially, state $_ p$ has the value find; for simplicity, the state sleep and the corresponding wake-up phase are omitted. The channel states, $s t a t e _ { p } [ q ]$ for each $q \in N e i g h b o r s _ { p }$ , initially are basic. While looking for a lowest-weight outgoing edge, $p$ stores the optimal intermediate result in best-weigh ${ \bf \Pi } _ { p } ^ { \dagger }$ . If the optimal result was reported through the basic or branch edge $p q$ , then best-edgep has the value $q$ . While $p$ is testing whether basic edge $p q$ is outgoing, test-edgep has the value $q$ . In counte $\boldsymbol { r } _ { p }$ , $p$ keeps track of how many branch edges have reported their minimum values; it starts at 1 to account for the fact that $p$ ’s parent in general does not report a value (except for the core nodes). In parent-reportp, a core node $p$ can keep the value reported by its parent; if there is no report yet, its value is 0, while the value $\infty$ means that $p$ ’s parent has reported no outgoing edges at its side. In Connectsp and $T e s t s _ { p }$ , $p$ stores incoming connect and test messages to which a reply is being delayed until the level of $p$ ’s fragment is high enough.

<html><body><table><tr><td>{find,found} statep; {basic,branch,rejected} statep[r] forallr ENeighborsp; real name p; nat levelp,counterp; dist best-weightp, parent-report p; proc parentp,test-edgep, best-edgep; proc-nat-set Connectsp;</td></tr><tr><td>proc-real-nat-set Tests p; Initialization of p</td></tr><tr><td>determine the lowest-weight channel pq; statep ←found;statep[q] ←branch;counterp ←1；parent-reportp ←0;</td></tr><tr><td>send (connect,O) to q; If p receives connect,l) from a neighbor q if l &lt;levelp then</td></tr><tr><td>send (initiate,namep,levelp,statep) to q; statep[q]←branch; elseif statep[q]=branch then send (initiate,weight(pq),levelp +1,find) to q; else</td></tr><tr><td>Connectsp = Connectsp U{(q,l)}; end if If p receives (initiate,fn,l,st) from a neighbor q</td></tr></table></body></html>

<html><body><table><tr><td>send (initiate,fn,l,st) to eachr∈Neighborsp\{q} with statep[r]=branch;</td></tr><tr><td>for each (q1,fn1,l1) ∈ Testsp do</td></tr><tr><td>if l1≤levelp then</td></tr><tr><td>perform procedure ReplyTestp(q1);</td></tr><tr><td>Testsp ←Testsp\{(qi,fn,1)};</td></tr><tr><td>end if</td></tr><tr><td>end for if st = find then</td></tr><tr><td>perform procedure FindMinimalOutgoingp;</td></tr><tr><td>end if</td></tr><tr><td>Procedure FindMinimalOutgoing p</td></tr><tr><td>if {pr|r∈Neighborsp and statep(pr)=basic}≠O then</td></tr><tr><td>send (test,namep,levelp}into the lowest-weight channel pq in this collection;</td></tr><tr><td>test-edgep ←q; else</td></tr><tr><td>test-edgep ←⊥;</td></tr><tr><td> if counterp =|{r ∈Neighborsp|statep[r]=branch}| then</td></tr><tr><td>perform procedure SendReportp end if</td></tr><tr><td>end if</td></tr><tr><td>If p receives (test,fn,l) from a neighbor q</td></tr><tr><td>if l ≤ levelp then</td></tr><tr><td>perform procedure ReplyTest p(q);</td></tr><tr><td>else</td></tr><tr><td>Testsp = Testsp U{(q,fn,l)};</td></tr><tr><td>end if</td></tr><tr><td>Procedure ReplyTestp(q)</td></tr><tr><td>if namep ≠ fn then</td></tr><tr><td> send (accept) to q;</td></tr><tr><td>else</td></tr><tr><td>statep[pq] ←rejected;</td></tr><tr><td>if test-edgep q then</td></tr><tr><td> send (reject) to q;</td></tr><tr><td>else</td></tr><tr><td> perform procedure FindMinimalOutgoing p;</td></tr><tr><td>end if</td></tr><tr><td>end if</td></tr><tr><td>If p receives (reject) from a neighbor q</td></tr><tr><td></td></tr><tr><td>statep[q] ←rejected;</td></tr><tr><td></td></tr><tr><td>perform procedure FindMinimalOutgoing p;</td></tr></table></body></html>

test- $e d g e _ { p } \gets \perp$ ;   
if weig $h t ( p q ) < b e s t – w e i g h t _ { p }$ then best-edg ${ \boldsymbol { p } } _ { p } \gets { \boldsymbol { q } }$ ; best-weigh $t _ { p } \gets w e i g h t ( p q )$ ;   
end if   
if counte $r _ { p } = | \{ r \in N e i g h b o r s _ { p } \mid s t a t e _ { p } [ r ] = b r a n c h \} |$ then perform procedure SendReportp

# end if

$$
\boxed { \mathrm { P r o c e d u r e \thinspace } S e n d R e p o r t _ { p } }
$$

$s t a t e _ { p } \gets f o u n d ;$ ;   
send $\langle \mathbf { r e p o r t } , b e s t \mathbf { - } w e i g h t _ { p } \rangle$ to parentp;   
,if parent-report $_ p > 0$ and best-weightp parent-reportp then >perform procedure ChangeRoo $_ p$ ;

# end if

If $p$ receives $\left. \mathbf { r e p o r t } , \lambda \right.$ from a neighbor $q$

if $q \neq p a r e n t _ { p }$ then counte $r _ { p } \gets c o u n t e r _ { p } + 1$ ; if $\lambda <$ best-weightp then <best-edg $e _ { p } \gets q$ ; best-weightp ← ; end if if counte $\dot { \boldsymbol { \mathbf { \rho } } } _ { p } = | \{ r \in N e i g h b o r s _ { p } \mid s t a t e _ { p } [ r ] = b r a n c h \} |$ and test-edg ${ \bf \Xi } _ { p } ^ { \circ } = \perp$ then perform procedure SendReportp end if   
else if state $_ p =$ find then parent-repor $t _ { p } \gets \lambda$ ;   
else if best-weigh ${ \bf \Phi } _ { p } < \lambda$ then < λperform procedure ChangeRoo $_ p$ ; else if $\lambda = \infty$ then λterminate; end if   
end if

Procedure ChangeRootp

if s $t a t e _ { p } [ b e s t - e d g e _ { p } ] = b$ ranch then send ⟨changeroot⟩ to best-edg $\boldsymbol { \mathscr { e } } _ { p }$ ;   
else $s t a t e _ { p } [ b e s t - e d g e _ { p } ]  b r a n c h ;$ ; send $\langle \mathbf c \mathbf { o n n e c t } , l e \nu e l _ { p } \rangle$ to best-edgep; if $( b e s t - e d g e _ { p } , l e \nu e l _ { p } ) \in C o n n e c t s _ { p }$ then ,send ⟨initiate best-weight $_ p , l e \nu e l _ { p } + 1 , f i n d \rangle$ to best-edgep; Connects $\dot { \mathbf { \eta } } _ { p } \gets C o n n e c t s _ { p } \setminus \{ ( b e s t - e d g e _ { p } , l e \nu e l _ { p } ) \}$ ; end if   
end if

# A.16 IEEE 1394 Election Algorithm

The variable $p a r e n t _ { p }$ contains the parent of $p$ in the spanning tree. The variable received $_ p [ q ]$ is set when $p$ receives a parent request from a neighbor $q$ to which $p$ has not sent a parent request. If $p$ gets into root contention and chooses to start a timer, it sets waitin $g _ { p }$ . If $p$ terminates as the leader, it sets leade $\boldsymbol { r } _ { p }$ .

bool leade $r _ { p }$ , waitin $g _ { p }$ , received $_ p [ r ]$ for all $r \in N e i g h b o r s _ { p }$ proc parentp;

Initialization of $p$ perform procedure SendRequestp;

Procedure SendRequestp

if $| \{ r \in N e i g h b o r s _ { p } \mid r e c e i \nu e d _ { p } [ r ] = f a l s e \} | = 1$ then send ⟨parent-req⟩ to the only $q \in N e i g h b o r s _ { p }$ with received $ \flat [ q ] =$ false; $p a r e n t _ { p } \gets q$ ;   
end if

If $p$ receives ⟨parent-req⟩ from a neighbor q

if $q \neq p a r e n t _ { p }$ then received $\dot { I _ { p } } [ q ] \gets t r u e$ ; send $\langle \mathbf { a c k } \rangle$ to $q$ ; perform procedure SendRequestp;   
else if waitin $\begin{array} { r } { g _ { p } = . } \end{array}$ false then perform procedure RootContention $p$ ;   
else le $u d e r _ { p } \gets t r u e ;$ ;   
end if

If $p$ receives ⟨ack⟩ from parentp

terminate;

Procedure RootContentionp either send ⟨parent-req⟩ to $q$ and waitin ${ \bf \Phi } _ { p } \gets f a l s e$ , or start a timer and waiti $\begin{array} { r } { \iota g _ { p } \gets t r u e } \end{array}$ ;

If a timeout occurs at $p$ perform procedure RootContention $p$

# A.17 Awerbuch’s Synchronizer

The variable parent $\dot { p }$ is the parent of $p$ in the spanning tree within its cluster, $C h i l d r e n _ { p }$ contains the children of $p$ in this spanning tree, and Designated $\dot { p }$ contains the processes $q$ for which there is a designated channel pq. Note that these three values are fixed after the initialization phase. In 1st-counte $\boldsymbol { r } _ { p }$ and 2nd-counte $\boldsymbol { r } _ { p }$ , $p$ keeps track of how many messages still need to be received in the first and second phases of this synchronizer, respectively.

nat 1st-counter $\dot { \boldsymbol { p } }$ , 2nd-counterp;   
proc paren $_ p$ ;   
proc-set Children $p$ , Designatedp;

Initialization

The network is divided into clusters, and within each cluster a spanning tree is built. Between each pair of distinct clusters that are connected by a channel, one of these connecting channels is labeled as designated. Furthermore, a wake-up phase makes sure that each process starts its first pulse, meaning that it performs the procedure NewPulse.

$$
\boxed { \mathrm { P r o c e d u r e } N e w P u l s e _ { p } }
$$

send $k \geq 0$ basic messages;   
1st-counte $\dot { \mathbf { \rho } } _ { p } \gets k + | C h i l d r e n _ { p } |$ ; $2 n d - c o u n t e r _ { p } \gets | C h i l d r e n _ { p } | + | D e s i g n a t e d _ { p } | ;$   
perform procedure FirstReportp;

If $p$ receives a basic message from a neighbor $q$

send $\langle \mathbf { a c k } \rangle$ to $q$

If $p$ receives $\langle \mathbf { a c k } \rangle$ or ⟨safe⟩

1st-counte $r _ { p } \gets I s t - c o u n t e r _ { p } - 1 ;$ ;   
perform procedure FirstReportp;

Procedure FirstReportp

if 1st-counte $r _ { p } = 0$ then if parent $_ p \neq \perp$ then send ⟨safe⟩ to parentp; else perform procedure SendNex $\dot { \boldsymbol { p } }$ ; end if   
end if

$$
\boxed { \mathrm { P r o c e d u r e } S e n d N e x t _ { p } }
$$

send $\langle \bf n e x t \rangle$ to each $q \in C h i l d r e n _ { p }$ ;   
send ⟨cluster-safe⟩ to each $r \in$ Designated $_ p$ ;   
perform procedure SecondReportp;

If p receives ⟨next⟩ perform procedure SendNextp;

If p receives ⟨cluster-safe⟩   
2nd-counter $_ p $ 2nd-counterp − 1;   
perform procedure SecondReportp;   
Procedure SecondReportp   
if 2nd-counte $\dot { \boldsymbol { p } } = 0$ then if parent $_ p \neq \perp$ then send ⟨cluster-safe⟩ to parentp; else perform procedure SendClusterNext $p$ ; end if   
end if   
Procedure SendClusterNextp   
send ⟨cluster-next⟩ to each $q \in C h i l d r e n _ { p }$ ;   
perform procedure NewPulsep;   
If p receives ⟨cluster-next⟩   
perform procedure SendClusterNex $\dot { p }$ ;

# A.18 Ricart-Agrawala Mutual Exclusion Algorithm

We use the lexicographical order on pairs $( t , i )$ with $t$ a time stamp and $i$ a process index. The variable clocki represents the clock value at $p _ { i }$ ,; it starts at 1. In req-stam $p _ { i }$ , $p _ { i }$ stores the time stamp of its current request; if there is none, $r e q { - } s t a m p _ { i } = 0$ . The number of permissions that $p _ { i }$ has received for its current request is maintained in counteri. In Pendin $g _ { i }$ , $p _ { i }$ keeps track of the processes it has received a request from but to which it has not yet sent permission. The Carvalho-Roucairol optimization is taken into account. In Requestsi, $p _ { i }$ keeps track of the processes to which it must send (or has sent) its next (or current) request.

<html><body><table><tr><td>nat clocki,req-stampi,counteri; proc-set Pendingi,Requestsi;</td></tr><tr><td>Initialization of pi Requests; ←Neighborsi；clocki ←1;</td></tr><tr><td>If pi wants to enter its critical section</td></tr><tr><td>if Requests; ≠O then</td></tr><tr><td>send (request,clocki,i) to each q E Requestsi; req-stampi ←clocki；counteri ←0;</td></tr><tr><td>else</td></tr></table></body></html>

# end if

If $p _ { i }$ receives ⟨permission⟩

$c o u n t e r _ { i } \gets c o u n t e r _ { i } + 1$ ;   
if counte $\dot { \boldsymbol { \mathbf { \rho } } } _ { i } = | R e q u e s t s _ { i } |$ then perform procedure CriticalSection $p$ ;   
end if

Procedure CriticalSectionp

enter critical section;   
exit critical section;   
send ⟨permission⟩ to each $q \in P e n d i n g _ { i }$ ;   
$r e q { - } s t a m p _ { i } \gets 0$ ; Requestsi ← Pendingi; $P e n d i n g _ { i } \gets \emptyset$ ;

If $p _ { i }$ receives $\langle \mathbf { r e q u e s t } , t , j \rangle$ from a p j

$c l o c k _ { i } \gets \operatorname* { m a x } \{ c l o c k _ { i } , t + 1 \}$ ;   
if req- $s t a m p _ { i } = 0$ or $( t , j ) < ( r e q \ – s t a m p _ { i } , i )$ then ,send ⟨permission⟩ to $p _ { j }$ ; if $p _ { j }$ ∈ Requestsi then /Requ $s t s _ { i } \gets R e q u e s t s _ { i } \cup \{ p _ { j } \} $ ; if req-stamp $_ i > 0$ then >send ⟨request req-stampi $i \rangle$ to $p _ { j }$ ; end if end if   
else $P e n d i n g _ { i }  P e n d i n g _ { i } \cup \{ p _ { j } \} ;$   
end if

# A.19 Raymond’s Mutual Exclusion Algorithm

The variable parentp contains the parent of $p$ in the spanning tree. The queue pendin $g _ { p }$ contains the children of $p$ in the tree that have asked for the token and possibly $p$ itself.

proc parentp;   
proc-queue pendingp;

If $p$ is the initiator

Initiate a wave that determines a spanning tree of the network, captured by values of parentr for all $r \in$ Processes, with $p$ as root;

If $p$ wants to enter its critical section if paren $_ p \neq \perp$ then pendin $g _ { p } \gets a p p e n d ( p e n d i n g _ { p } , p )$ ; if head $( \dot { p } e n d i n g _ { p } ) = p$ then

send ⟨request⟩ to paren $p$ ; end if else perform procedure CriticalSection $p$ ; end if

If $p$ receives $\langle \mathbf { r e q u e s t } \rangle$ from a neighbor $q$

p $n d i n g _ { p }  a p p e n d ( p e n d i n g _ { p } , q )$ ;   
if head $( \bar { p } e n d i n g _ { p } ) = q$ then if $p a r e n t _ { p } \neq \pm$ then send ⟨request⟩ to parentp; else if $p$ is not in its critical section then perform procedure SendToken $p$ ; end if   
end if

If $p$ receives ⟨token⟩

if $h e a d ( p e n d i n g _ { p } ) \neq p$ then perform procedure SendToken $p$ ;   
else $p a r e n t _ { p } \gets \bot ; \quad p e n d i n g _ { p } \gets t a i l ( p e n d i n g _ { p } ) ;$ perform procedure CriticalSection $p$ ;   
end if

$$
\boxed { \mathrm { P r o c e d u r e } S e n d T o k e n _ { p } }
$$

$p a r e n t _ { p } \gets h e a d ( p e n d i n g _ { p } ) ; \quad p e n d i n g _ { p } \gets t a i l ( p e n d i n g _ { p } ) ;$   
send $\mathbf { \langle t o k e n \rangle }$ to parent p;   
if pending ${ \bf \Phi } _ { p } \neq \emptyset$ then send ⟨request⟩ to parentp;   
end if

Procedure CriticalSectionp

enter critical section;   
exit critical section;   
if pending ${ \bf \Phi } _ { p } \neq \emptyset$ then perform procedure SendToken $p$ ;   
end if

# A.20 Agrawal–El Abbadi Mutual Exclusion Algorithm

The variable requestsp contains a queue of processes from which $p$ must still obtain permission to enter its critical section. The set Permission $s _ { p }$ contains the processes from which $p$ has received permission during its current attempt to become privileged. The queue pendin $g _ { p }$ contains the processes from which $p$ has received a request; it has only sent permission to the head of this queue. (We recall that $p$ may have to ask permission from itself.) We assume that $N = 2 ^ { k } - 1$ for some $k > 1$ , so that the binary tree has depth $k - 1$ . The constant >root denotes the root node of the binary tree, and for any nonleaf $q$ in the tree, left-child $( q )$ and right-child $( q )$ denote its children at the left and right, respectively. Processes may crash, and they are provided with a complete and strongly accurate failure detector. When $p$ detects that another process has crashed, it puts the corresponding process ID in the set Crashed $\boldsymbol { \mathbf { \rho } } _ { p }$ .

<html><body><table><tr><td>proc-queue requestsp, pending p; proc-set Permissionsp, Crashed p;</td></tr><tr><td> If p wants to enter its critical section</td></tr><tr><td>requestsp←append(0,root); perform procedure SendRequest p;</td></tr><tr><td></td></tr><tr><td>Procedure SendRequest p if head(requestsp)$ Crashedp then</td></tr><tr><td>send (request) to head(requestsp);</td></tr><tr><td>else perform procedure HeadRequestsCrashed p;</td></tr><tr><td>end if</td></tr><tr><td>Procedure HeadRequestsCrashed p if head(requestsp) is not a leaf of the binary tree then</td></tr><tr><td>requestsp ←append(append(tail(requestsp),left-child(head(requestsp))), right-child(head(requestsp));</td></tr><tr><td>perform procedure SendRequest p; else</td></tr><tr><td>Permissionsp←0;</td></tr><tr><td>start a new attempt to enter the critical section; end if</td></tr><tr><td> If p receives (request) from a process q</td></tr><tr><td>pendingp ← append(pendingp,q); if head(pendingp) = q then</td></tr><tr><td>perform procedure SendPermissionp; end if</td></tr><tr><td>Procedure SendPermissionp</td></tr><tr><td>if pendingp ≠ 0 then</td></tr><tr><td>if head(pendingp)  Crashedp then send (permission) to head(pendingp);</td></tr><tr><td>else</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>pendingp ← tail(pendingp);</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>perform procedure SendPermissionp;</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>end if</td></tr></table></body></html>

# If $p$ receives ⟨permission⟩ from process q

<html><body><table><tr><td>Permissionsp ←Permissionsp U{q}；requestsp ←tail(requestsp); if q is not a leaf of the binary tree then either requestsp ←append(requestsp,left-child(q)) or requestsp ←append(requestsp,right-child(q)); end if</td></tr><tr><td>if requestsp ≠ O then perform procedure SendRequest p;</td></tr><tr><td>else</td></tr><tr><td>enter critical section;</td></tr><tr><td>exit critical section;</td></tr><tr><td>send (released) to each r EPermissionsp;</td></tr><tr><td>Permissionsp ←@; end if</td></tr><tr><td></td></tr><tr><td>If p receives (released)</td></tr><tr><td>pendingp ←tail(pendingp); perform procedure SendPermissionp;</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>If p detects that a process q has crashed</td></tr><tr><td>Crashedp ←Crashedp U{q}; if head(requestsp) = q then</td></tr><tr><td>perform procedure HeadRequestsCrashed p;</td></tr><tr><td>end if if head(pendingp)= q then pendingp ←tail(pendingp);</td></tr></table></body></html>

# A.21 MCS Queue Lock

Since processes can use the same element for each lock access, we take the liberty of representing the queue of waiting processes by using process IDs instead of elements. The atomic multi-writer register wait $\dot { p }$ is true as long as $p$ must wait to get the lock. The atomic multi-writer register $s u c c _ { p }$ points to the successor of $p$ in the queue of waiting processes. The atomic single-reader/single-writer register $p r e d _ { p }$ points to the predecessor of $p$ in the queue of waiting processes. When a process arrives at this queue, it assigns its process $\mathrm { I D }$ to the multi-writer register last. The operation last get-and-set $( p )$ assigns the value $p$ to last and returns the .previous value of last, all in one atomic step. And last compare-and-set $( p , \perp )$ in one atomic operation reads the value of last and either assigns the value $\perp$ . ,to last, if its current value is $p$ , or leaves the value of last unchanged otherwise. In the first case, this operation returns true, while in the second case it returns false.

bool wait $\dot { p }$ ;   
proc last, $s u c c _ { p } , p r e d _ { p }$ ;

If $p$ wants to enter its critical section

$p r e d _ { p } \gets$ last get-and-set(p);   
if pred $l _ { p } \neq \perp$ then wa $i t _ { p } \gets t r u e$ ; $s u c c _ { p r e d _ { p } } \gets p$ ; while wait $_ p =$ true do $\{ \}$ ; end while   
end if   
enter critical section;   
exit critical section;   
if $s u c c _ { p } \neq \bot$ then $w a i t _ { s u c c _ { p } } \gets f a l s e ;$ ;   
else if last compare-and-set $( p , \bot )$ returns false then while $s u c c _ { p } = \perp$ do $\{ \}$ ; end while $w a i t _ { s u c c _ { p } } \gets f a l s e ;$   
end if

# A.22 CLH Queue Lock with Timeouts

The data type pointer consists of pointers to an element, with null as default initial value. If $p$ wants to enter its critical section, it creates an element $\epsilon$ containing a pointer pred . Let element $\epsilon ^ { \prime }$ denote the nearest nonabandoned predecessor of $\epsilon$ ϵin the queue. The pointer $p r e d _ { p }$ ϵpoints to $\epsilon ^ { \prime }$ ϵ. In pred-pred $l _ { p }$ , $p$ repeatedly stores the value of $p r e d _ { \epsilon ^ { \prime } }$ . If $p$ ϵ ϵ decides to abandon its attempt to get the lock and has a successor in the queue, ϵthen it lets pred point to $\epsilon ^ { \prime }$ . The multi-writer register last points to the last element in the queue.

pointer last, pred $p$ , pred-predp, pred for all elements $\epsilon$ ;

If $p$ wants to enter its critical section

create an element $\epsilon$ ;   
predp ← last get-and-set $( \epsilon )$ ;   
if $p r e d _ { p } = \mathtt { n u l 1 }$ then perform procedure CriticalSection $_ p ( \epsilon )$ ;   
else while no timeout occurs do pred-pred $_ p  p r e d _ { p r e d _ { p } }$ ; if pred-pred $l _ { p } =$ released then perform procedure CriticalSection $_ p ( \epsilon )$ ; else if pred- $r e d _ { p } \ne \mathtt { n u l 1 }$ then $p r e d _ { p } \gets p r e d  – p r e d _ { p }$ ; end if end while   
if last compare-and-s $e t ( \epsilon , p r e d _ { p } )$ returns false then $p r e d _ { \epsilon } \gets p r e d _ { p }$ ;   
end if   
abandon the attempt to take the lock;

# end if

$$
\boxed { \mathrm { P r o c e d u r e } C r i t i c a l S e c t i o n _ { p } ( \epsilon ) }
$$

enter critical section;   
exit critical section;   
if last compare-and- $\mathsf { \iota } e t ( \epsilon , \mathtt { n u l 1 } )$ returns false then $p r e d _ { \epsilon } \gets$ released;   
end if   
terminate;

# A.23 Afek-Kutten-Yung Spanning Tree Algorithm

Self-stabilizing algorithms are always defined in a shared-memory framework. Therefore, the messagepassing description of the Afek-Kutten-Yung spanning tree algorithm in section 17.3 is here cast in shared variables. We recall that a variable can be initialized with any value in its domain.

The variable $r o o t _ { p }$ is the root of the spanning tree according to $p$ $p , p a r e n t _ { p }$ represents the parent of $p$ in the spanning tree, and $d i s t _ { p }$ is the distance value of $p$ toward the root. The variables $r e q _ { p } , f r o m _ { p }$ , $t o _ { p }$ , and directionp deal with join requests and corresponding grant messages. The process ID of the process that originally issued the request is stored in $r e q _ { p }$ , the neighbor from which $p$ received the request is stored in $f r o m _ { p }$ , the neighbor to which $p$ forwarded the request is stored in $t o _ { p }$ , and whether a request is being forwarded to the root of the fragment or a grant message is being forwarded to the process that originally issued the request is remembered in direction $_ p$ . The Boolean variable $t o g g l e _ { p }$ makes sure that $p$ performs an event only when all its neighbors have copied the current values of $p$ ’s local variables; $t o g g l e _ { q } ( p )$ represents the copy at neighbor $q$ of the value of $t o g g l e _ { p }$ . It is assumed that a process copies the values of all local variables of a neighbor in one atomic step.

We use the following abbreviations. AmRoo $\dot { p }$ states that $p$ considers itself the root:

$$
p a r e n t _ { p } = \perp \ \wedge \ r o o t _ { p } = p \ \wedge \ d i s t _ { p } = 0 .
$$

$N o t R o o t _ { p }$ states that $p$ does not consider itself the root and that the values of $p$ ’s local variables are in line with those of its parent:

$$
p a r e n t _ { p } \in N e i g h b o r s _ { p } \land r o o t _ { p } > p \land r o o t _ { p } = r o o t _ { p a r e n t _ { p } } \land d i s t _ { p } = d i s t _ { p a r e n t _ { p } } + 1 .
$$

MaxRootp states that no neighbor of $p$ has a root value greater than $r o o t _ { p }$ :

$$
r o o t _ { p } \geq r o o t _ { r } { \mathrm { ~ f o r ~ a l l ~ } } r \in N e i g h b o r s _ { p } .
$$

The network is stable, with the process with the largest ID as root, if at each process $p$ either AmRootp or NotRoot $\dot { p }$ holds, as well as MaxRootp.

In the following pseudocode, $p$ repeatedly copies the values of the local variables of its neighbors, checks whether all its neighbors have copied the current values of $p$ ’s local variables, and, if so, tries to perform one of several possible events. First of all, if $N o t R o o t _ { p } \land M a x R o o t _ { p }$ does not hold and $p$ does not yet consider itself the root, then $p$ makes itself the root. The second kind of event arises if $M a x R o o t _ { p }$ does not hold (and so, since $p$ skipped the first case, $A m R o o t _ { p }$ does hold). Then $p$ asks a neighbor with a maximum root value to become its parent, if $p$ is not already making such a request to a neighbor $q$ , expressed by (the negation of) the predicate $A s k i n g _ { p } ( q )$ :

$$
o o t _ { q } \ge r o o t _ { r } \mathrm { ~ f o r ~ a l l ~ } r \in N e i g h b o r s _ { p } \ \wedge \ r e q _ { p } = f r o m _ { p } = p \ \wedge \ t o _ { p } = q \ \wedge \ d i r e c t i o n _ { p } = q \ .
$$

Or such a request by $p$ may be granted by a neighbor $q$ , expressed by the predicate Granted ${ \bf \Phi } _ { p } ^ { \prime } ( q )$ :

$$
r e q _ { q } = r e q _ { p } \wedge f r o m _ { q } = p \wedge d i r e c t i o n _ { q } = \mathrm { g r a n t } \wedge d i r e c t i o n _ { p } = \mathrm { a s k } ,
$$

where we take $q$ to be $t o _ { p }$ . It is, moreover, required that $p$ issued a request to $t o _ { p }$ , expressed by the predicate Requestor $\dot { p }$ :

$$
t o _ { p } \in N e i g h b o r s _ { p } \ \wedge \ r o o t _ { t o _ { p } } > p \ \wedge \ r e q _ { p } = f r o m _ { p } = p .
$$

In this case, $t o _ { p }$ becomes $p$ ’s parent. The third kind of event arises when $p$ is not yet handling a request from a neighbor $q$ , expressed by (the negation of) the predicate Handlin ${ \bf \Xi } _ { p } ^ { \prime } ( q )$ :

$$
r e q _ { q } = r e q _ { p } \wedge f r o m _ { p } = q \wedge t o _ { q } = p \wedge t o _ { p } = p a r e n t _ { p } \wedge d i r e c t i o n _ { q } = \mathsf { a s k . }
$$

Here $q$ should be either a root that issued a join request to $p$ or a child of $p$ in the spanning tree, expressed by the predicate Request $\dot { \mathbf { \rho } } _ { p } ( q )$ :

$$
( A m R o o t _ { q } \wedge r e q _ { q } = f r o m _ { q } = q \wedge t o _ { q } = p ) \vee ( p a r e n t _ { q } = p \wedge r e q _ { q } \not \in \{ q , \perp \} ) .
$$

If the four variables that capture requests are not all undefined, expressed by (the negation of) the predicate NotHandlingp,

$$
r e q _ { p } = \perp \ \wedge f r o m _ { p } = \perp \ \wedge \ t o _ { p } = \perp \ \wedge \ d i r e c t i o n _ { p } = \perp ,
$$

then $p$ sets the values of these four variables to $\perp$ . Otherwise, $p$ forwards a request, but only if $f r o m _ { p a r e n t _ { p } } \neq p$ (allowing parentp to first reset its join request variables). The fourth kind of event is a root $p$ that is handling a request of a neighbor setting direction ${ \bf \ell } _ { p }$ to grant. Finally, the fifth kind of event is a nonroot $p$ that finds that its request has been granted by its parent setting direction $_ p$ to grant. Note that for the third, fourth, and fifth kinds of event, $A m R o o t _ { p } \lor N o t R o o t _ { p }$ (because $p$ skipped the first case) and $M a x R o o t _ { p }$ (because $p$ skipped the second case). And for the fourth and fifth kinds of event, Reques $t _ { p } ( q ) \land H a n d l i n g _ { p } ( q )$ for some $q \in N e i g h b o r s _ { p }$ (because $p$ skipped the third case).

bool togglep, $t o g g l e _ { p } ( r )$ for all $r \in N e i g h b o r s _ { p }$ ;   
dist ${ d i s t } _ { p }$ ;   
proc parentp, $r o o t _ { p }$ $, r e q _ { p } , f r o m _ { p } , t o _ { p }$ ;   
{ask grant ⊥} directionp;

while true do

copy the values of variables of all neighbors into a local copy; if $t o g g l e _ { r } ( p ) = t o g g l e _ { p }$ for all $r \in N e i g h b o r s _ { p }$ then if $\lnot ( N o t R o o t _ { p } \land M a x R o o t _ { p } ) \land \lnot A m R o o t _ { p }$ then $p a r e n t _ { p } \gets \bot ; \quad r o o t _ { p } \gets p ; \quad d i s t _ { p } \gets 0 ;$ ; else if $\lnot M a x R o o t _ { p }$ then if $\neg A s k i n g _ { p } ( r )$ for all $r \in N e i g h b o r s _ { p }$ then $r e q _ { p } \gets p ; \quad f r o m _ { p } \gets p ; \quad d i r e c t i o n _ { p } \gets \mathsf { a s k } ;$ $t o _ { p } \gets q$ for a $q \in N e i g h b o r s _ { p }$ with $r o o t _ { q }$ as large as possible; else if Requestorp ∧ Granted $_ p ( t o _ { p } )$ then $\begin{array} { r l r } & { } & { p a r e n t _ { p }  t \dot { o _ { p } } ; ~ r o o t _ { p }  r o o t _ { t o _ { p } } ~ d i s t _ { p }  d i s t _ { t o _ { p } } + 1 ; } \\ & { } & { r e q _ { p }  \perp ; ~ f r o m _ { p }  \perp ; ~ t o _ { p }  \perp ; ~ d i r e c t i o n _ { p }  \perp ; } \end{array}$ end if else if $\lnot ( R e q u e s t _ { p } ( r ) \land H a n d l i n g _ { p } ( r ) )$ for all $r \in N e i g h b o r s _ { p }$ then if ¬NotHandli $\boldsymbol { \it g } _ { p }$ then els $\begin{array} { l } { { r e q _ { p } \gets \bot ; \quad ^ { \prime } f r o m _ { p } \gets \bot ; \quad t o _ { p } \gets \bot ; \quad d i r e c t i o n _ { p } \gets \bot ; } } \\ { { \mathbf e \ \mathbf i f f r o m _ { p a r e n t _ { p } } \neq p \land R e q u e s t _ { p } ( q ) \ \mathrm { f o r ~ s o m e \ } q \in N e i g h b o r s _ { p } \ \mathbf t h e \mathbf n } } \\ { { r e q _ { p } \gets r e q _ { q } ; \quad f r o m _ { p } \gets q ; \quad t o _ { p } \gets p a r e n t _ { p } ; \quad d i r e c t i o n _ { p } \gets z } } \end{array}$ 1 ask; end if else if AmRootp ∧ direction $_ p =$ ask then directio $\iota _ { p } \gets \mathtt { g r a n t }$ ; else if paren ${ \bf \Pi } _ { p } ^ { \prime } \in N e i g h b o r s _ { p } \wedge G r a n t e d _ { p } ( p a r e n t _ { p } )$ then directio $\iota _ { p } \gets \mathtt { g r a n t }$ ; end if $t o g g l e _ { p }  \neg t o g g l e _ { p }$ ; end if end while

# References

1. Y. AFEK, S. KUTTEN, M. YUNG (1997), The local detection paradigm and its applications to self-stabilization, Theoretical Computer Science, 186, pp. 199–229.   
2. D. AGRAWAL, A. EL ABBADI (1991), An efficient and fault-tolerant solution for distributed mutual exclusion, ACM Transactions on Computer Systems, 9, pp. 1–20.   
3. T. E. ANDERSON (1990), The performance of spin lock alternatives for shared-memory multiprocessors, IEEE Transactions on Parallel and Distributed Systems, 1, pp. 6–16.   
4. D. ANGLUIN (1980), Local and global properties in networks of processors, in (R. E. Miller, S. Ginsburg, W. A. Burkhard, R. J. Lipton, eds.) Proceedings of the 12th Symposium on Theory of Computing, pp. 82–93, ACM.   
5. G. ANTONOIU, P. K. SRIMANI (1998), A self-stabilizing distributed algorithm for minimal spanning tree problem in a symmetric graph, Computers & Mathematics with Applications, 35, pp. 15–23.   
6. A. ARORA, M. G. GOUDA (1994), Distributed reset, IEEE Transactions on Computers, 43, pp. 1026–1038.   
7. H. ATTIYA, A. BAR-NOY, D. DOLEV (1991), Sharing memory robustly in message-passing systems, Journal of the ACM, 42, pp. 124–142.   
8. B. AWERBUCH (1985), Complexity of network synchronization, Journal of the ACM, 32, pp. 804–823.   
9. B. AWERBUCH (1985), A new distributed depth-first-search algorithm, Information Processing Letters, 20, pp. 147–   
150.   
10. R. BAKHSHI, J. ENDRULLIS, W. J. FOKKINK, J. PANG (2011), Fast leader election in anonymous rings with bounded expected delay, Information Processing Letters, 111, pp. 864–870.   
11. R. BAKHSHI, W. J. FOKKINK, J. PANG, J. C. VAN DE POL (2008), Leader election in anonymous rings: Franklin goes probabilistic, in (G. Ausiello, J. Karhumaki, G. Mauri, C.-H. L. Ong, eds.) Proceedings of the 5th IFIP Con- ¨ ference on Theoretical Computer Science, pp. 57–72, Springer.   
12. M. BEN-ARI (1984), Algorithms for on-the-fly garbage collection, ACM Transactions on Programming Languages and Systems, 6, pp. 333–344.   
13. C. H. BENNETT, G. BRASSARD (1984), Quantum cryptography: Public key distribution and coin tossing, in Proceedings of the Conference on Computers, Systems and Signal Processing, pp. 175–179, IEEE.   
14. P. A. BERNSTEIN, D. W. SHIPMAN, J. B. ROTHNIE JR. (1980), Concurrency control in a system for distributed databases (SDD-1), ACM Transactions on Database Systems, 5, pp. 18–51.   
15. D. I. BEVAN (1987), Distributed garbage collection using reference counting, in (J. W. de Bakker, A. J. Nijman, P. C. Treleaven, eds.) Proceedings of the 1st Conference on Parallel Architectures and Languages Europe, vol. 259 of Lecture Notes in Computer Science, pp. 176–187, Springer.   
16. G. BRACHA, S. TOUEG (1985), Asynchronous consensus and broadcast protocols, Journal of the ACM, 32, pp. 824–840.   
17. G. BRACHA, S. TOUEG (1987), Distributed deadlock detection, Distributed Computing, 2, pp. 127–138.   
18. J. E. BURNS, N. A. LYNCH (1993), Bounds on shared memory for mutual exclusion, Information and Computation, 107, pp. 171–184.   
19. G. CAO, M. SINGHAL (2001), Mutable checkpoints: A new checkpointing approach for mobile computing systems, IEEE Transactions on Parallel and Distributed Systems, 12, pp. 157–172.   
20. O. S. F. CARVALHO, G. ROUCAIROL (1983), On mutual exclusion in computer networks, Communications of the ACM, 26, pp. 146–147.   
21. J. CHALOPIN, E. GODARD, Y. METIVIER ´ , G. TEL (2007), About the termination detection in the asynchronous message passing model, in (J. van Leeuwen, G. F. Italiano, W. van der Hoek, C. Meinel, H. Sack, F. Plasil, eds.) Proceedings of the 33rd Conference on Current Trends in Theory and Practice of Computer Science, vol. 4362 of Lecture Notes in Computer Science, pp. 200–211, Springer.   
22. T. D. CHANDRA, S. TOUEG (1996), Unreliable failure detectors for reliable distributed systems, Journal of the ACM, 43, pp. 225–267.   
23. K. M. CHANDY, L. LAMPORT (1985), Distributed snapshots: Determining global states of distributed systems, ACM Transactions on Computer Systems, 3, pp. 63–75.   
24. K. M. CHANDY, J. MISRA (1982), Distributed computation on graphs: Shortest path algorithms, Communications of the ACM, 25, pp. 833–837.   
25. E. J. H. CHANG (1982), Echo algorithms: Depth parallel operations on general graphs, IEEE Transactions on Software Engineering, 8, pp. 391–401.   
26. E. J. H. CHANG, R. ROBERTS (1979), An improved algorithm for decentralized extrema-finding in circular configurations of processes, Communications of the ACM, 22, pp. 281–283.   
27. Y.-I. CHANG, M. SINGHAL, M. T. LIU (1990), A fault tolerant algorithm for distributed mutual exclusion, Proceedings of the 9th Symposium on Reliable Distributed Systems, pp. 146–154, IEEE.   
28. T.-Y. CHEUNG (1983), Graph traversal techniques and the maximum flow problem in distributed computation, IEEE Transactions on Software Engineering, 9, pp. 504–512.   
29. C.-T. CHOU, I. CIDON, I. S. GOPAL, S. ZAKS (1990), Synchronizing asynchronous bounded delay networks, IEEE Transactions on Communications, 38, pp. 144–147.   
30. I. CIDON (1988), Yet another distributed depth-first-search algorithm, Information Processing Letters, 26, pp. 301– 305.   
31. T. S. CRAIG (1993), Building FIFO and priority-queueing spin locks from atomic swap, Technical Report TR 93-02-02, University of Washington.   
32. D. E. DENNING, G. M. SACCO (1981), Timestamps in key distribution protocols, Communications of the ACM, 24, pp. 533–536.   
33. B. W. DIFFIE, M. E. HELLMAN (1976), New directions in cryptography, IEEE Transactions on Information Theory, 22, pp. 644–654.   
34. E. W. DIJKSTRA (1974), Self-stabilizing systems in spite of distributed control, Communications of the ACM, 17, pp. 643–644.   
35. E. W. DIJKSTRA (1987), Shmuel Safra’s version of termination detection, vol. 998 of EWD manuscripts, The University of Texas at Austin.   
36. E. W. DIJKSTRA, C. S. SCHOLTEN (1980), Termination detection for diffusing computations, Information Processing Letters, 11, pp. 1–4.   
37. D. DOLEV, M. M. KLAWE, M. RODEH (1982), An $O ( n \log { n } )$ unidirectional distributed algorithm for extrema finding in a circle, Journal of Algorithms, 3, pp. 245–260.   
38. D. DOLEV, H. R. STRONG (1983), Authenticated algorithms for Byzantine agreement, SIAM Journal on Computing, 12, pp. 656–666.   
39. C. DWORK, M. NAOR (1992), Pricing via processing or combatting junk mail, in (E. F. Brickell, ed.) Proceedings of the 12th Cryptology Conference, vol. 740 of Lecture Notes in Computer Science, pp. 139-–147, Springer.   
40. K. P. ESWARAN, J. N. GRAY, R. A. LORIE, I. L. TRAIGER (1976), The notions of consistency and predicate locks in a database system, Communications of the ACM, 19, pp. 624–633.   
41. C. J. FIDGE (1988), Timestamps in message-passing systems that preserve the partial ordering, in (K. Raymond, ed.) Proceedings of the 11th Australian Computer Science Conference, pp. 56–66.   
42. M. J. FISCHER, N. A. LYNCH, M. PATERSON (1985), Impossibility of distributed consensus with one faulty process, Journal of the ACM, 32, pp. 374–382.   
43. W. J. FOKKINK, J.-H. HOEPMAN, J. PANG (2005), A note on $K$ -state self-stabilization in a ring with $K = N$ , Nordic Journal of Computing, 12, pp. 18–26.   
44. W. J. FOKKINK, J. PANG (2006), Variations on Itai-Rodeh leader election for anonymous rings and their analysis in PRISM, Journal of Universal Computer Science, 12, pp. 981–1006.   
45. W. J. FOKKINK, G. SAMSOM (2019), Variations of the Itai-Rodeh algorithm for computing anonymous ring size, in (M. S. Alvim, K. Chatzikokolakis, C. Olarte, F. Valencia, eds.) The Art of Modelling Computational Systems – A Journey from Logic and Concurrency to Security and Privacy, vol. 11760 of Lecture Notes in Computer Science, pp. 3–13, Springer.   
46. W. R. FRANKLIN (1982), On an improved algorithm for decentralized extrema-finding in circular configurations of processes, Communications of the ACM, 25, pp. 336–337.   
47. G. N. FREDERICKSON (1985), A single source shortest path algorithm for a planar distributed network, in (K. Mehlhorn, ed.) Proceedings of the 2nd Symposium on Theoretical Aspects of Computer Science, vol. 182 of Lecture Notes in Computer Science, pp. 143–150, Springer.   
48. E. GAFNI, D. P. BERTSEKAS (1981), Distributed algorithms for generating loop-free routes in networks with frequently changing topology, IEEE Transactions on Communications, 29, pp. 11–18.   
49. R. G. GALLAGER, P. A. HUMBLET, P. M. SPIRA (1983), A distributed algorithm for minimum-weight spanning trees, ACM Transactions on Programming Languages and Systems, 5, pp. 66–77.   
50. J. N. GRAY (1978), Notes on data base operating systems, in (M. J. Flynn, J. Gray, A. K. Jones, K. Lagally, H. Opderbeck, G. J. Popek, B. Randell, J. H. Saltzer, H.-R. Wiehle, eds.) Operating Systems, An Advanced Course, vol. 60 of Lecture Notes in Computer Science, pp. 393–481, Springer.   
51. T. HARDER ¨ , A. REUTER (1983), Principles of transaction-oriented database recovery, ACM Computing Surveys, 15, pp. 287-–317.   
52. D. HENSGEN, R. A. FINKEL, U. MANBER (1988), Two algorithms for barrier synchronization, International Journal of Parallel Programming, 17, pp. 1–17.   
53. M. HERLIHY (1991), Wait-free synchronization, ACM Transactions on Programming Languages and Systems, 13, pp. 124–149.   
54. M. HERLIHY, J. E. B. MOSS (1993), Transactional memory: Architectural support for lock-free data structures, in (A. J. Smith, ed.) Proceedings of the 20th Symposium on Computer Architecture, pp. 289–300, ACM.   
55. M. HERLIHY, N. SHAVIT (2008), The Art of Multiprocessor Programming, Morgan Kaufmann.   
56. D. S. HIRSCHBERG, J. B. SINCLAIR (1980), Decentralized extrema-finding in circular configurations of processors, Communications of the ACM, 23, pp. 627–628.   
57. S.-T. HUANG (1989), Detecting termination of distributed computations by external agents, in Proceedings of the 9th International Conference on Distributed Computing Systems, pp. 79–84, IEEE.   
58. IEEE COMPUTER SOCIETY (1996), IEEE standard for a high performance serial bus, Technical Report Std. 1394- 1995, IEEE.   
59. A. ITAI, M. RODEH (1990), Symmetry breaking in distributed networks, Information and Computation, 88, pp. 60– 87.   
60. V. JACOBSON (1988), Congestion avoidance and control, in (V. G. Cerf, ed.) Proceedings of the 3rd Symposium on Communications Architectures and Protocols, pp. 314–329, ACM.   
61. G. KARLOS, W. J. FOKKINK, P. FUCHS (2021), Fault-tolerant termination detection with Safra’s algorithm, in (K. Echihabi, R. Meyer, eds.) Proceedings of the 9th Conference on Networked Systems, vol. 12754 of Lecture Notes in Computer Science, pp. 71–87, Springer.   
62. J. L. KIM, T. PARK (1993), An efficient protocol for checkpointing recovery in distributed systems, IEEE Transactions on Parallel and Distributed Systems, 4, pp. 955–960.   
63. C. P. KRUSKAL, L. RUDOLPH, M. SNIR (1988), Efficient synchronization on multiprocessors with shared memory, ACM Transactions on Programming Languages and Systems, 10, pp. 579–601.   
64. H. T. KUNG, J. T. ROBINSON (1981), On optimistic methods for concurrency control, ACM Transactions on Databases, 6, pp. 213–226.   
65. T. H. LAI, T. H. YANG (1987), On distributed snapshots, Information Processing Letters, 25, pp. 153–158.   
66. K. B. LAKSHMANAN, N. MEENAKSHI, K. THULASIRAMAN (1987), A time-optimal message-efficient distributed algorithm for depth-first search, Information Processing Letters, 25, pp. 103–109   
67. L. LAMPORT (1974), A new solution of Dijkstra’s concurrent programming problem, Communications of the ACM, 17, pp. 453–455.   
68. L. LAMPORT (1978), Time, clocks, and the ordering of events in a distributed system, Communications of the ACM, 21, pp. 558–565.   
69. L. LAMPORT (1979), Constructing digital signatures from a one way function, Technical Report CSL-98, Computer Science Laboratory, SRI International.   
70. L. LAMPORT (1987), A fast mutual exclusion algorithm, ACM Transactions on Computer Systems, 5, pp. 1–11.   
71. L. LAMPORT, R. E. SHOSTAK, M. C. PEASE (1982), The Byzantine generals problem, ACM Transactions on Programming Languages and Systems, 4, pp. 382–401.   
72. B. W. LAMPSON (1981), Atomic transactions, in (B. W. Lampson, M. Paul, H.-J. Siegert, eds.) Distributed Systems–Architecture and Implementation, An Advanced Course, vol. 105 of Lecture Notes in Computer Science, pp. 246–265, Springer.   
73. J. P. LEHOCZKY, S. RAMOS-THUEL (1992), An optimal algorithm for scheduling soft-aperiodic tasks in fixedpriority preemptive systems, in Proceedings of the 13th Real-Time Systems Symposium, pp. 110–123, IEEE.   
74. H. LIEBERMAN, C. HEWITT (1983), A real-time garbage collector based on the lifetimes of objects, Communications of the ACM, 26, pp. 419–429.   
75. J. W. LIU (2000), Real-Time Systems, Prentice-Hall.   
76. P. S. MAGNUSSON, A. LANDIN, E. HAGERSTEN (1994), Queue locks on cache coherent multiprocessors, in (H. J. Siegel, ed.) Proceedings of the 8th Symposium on Parallel Processing, pp. 165–171, IEEE.   
77. S. R. MAHANEY, F. B. SCHNEIDER (1985), Inexact agreement: Accuracy, precision, and graceful degradation, in (M. A. Malcolm, H. R. Strong, eds.) Proceedings of the 4th Symposium on Principles of Distributed Computing, pp. 237–249, ACM.   
78. F. MATTERN (1989), Global quiescence detection based on credit distribution and recovery, Information Processing Letters, 30, pp. 195–200.   
79. F. MATTERN (1989), Virtual time and global states of distributed systems, in (M. Corsnard, ed.) Proceedings of the Workshop on Parallel and Distributed Algorithms, pp. 215–226, North-Holland/Elsevier.   
80. J. M. MCQUILLAN (1974), Adaptive Routing for Distributed Computer Networks, PhD thesis, Harvard University.   
81. J. M. MCQUILLAN, I. RICHER, E. C. ROSEN (1980), The new routing algorithm for ARPANET, IEEE Transactions on Communications, 28, pp. 711–719.   
82. J. M. MELLOR-CRUMMEY, M. L. SCOTT (1991), Algorithms for scalable synchronization on shared-memory multiprocessors, ACM Transactions on Computer Systems, 9, pp. 21–65.   
83. R. C. MERKLE (1979), Secrecy, Authentication, and Public Key Systems, PhD thesis, Stanford University.   
84. R. C. MERKLE (1989), A certified digital signature, in (G. Brassard, ed.) Proceedings of the 9th Cryptology Conference, vol. 435 of Lecture Notes in Computer Science, pp. 218–238, Springer.   
85. P. M. MERLIN, P. J. SCHWEITZER (1980), Deadlock avoidance in store-and-forward networks I: Store-andforward deadlock, IEEE Transactions on Communications, 28, pp. 345–354.   
86. P. M. MERLIN, A. SEGALL (1979), A failsafe distributed routing protocol, IEEE Transactions on Communications, 27, pp. 1280–1287.   
87. S. MUSAEV, W. J. FOKKINK (2022), A note on the message complexity of Cidon’s algorithm, A Journey from Process Algebra via Timed Automata to Model Learning, vol. 13560 of Lecture Notes in Computer Science, pp. 467–471, Springer.   
88. SATOSHI NAKAMOTO (2008), Bitcoin: A peer-to-peer electronic cash system, Cryptography mailing list at metzdowd.com.   
89. R. M. NEEDHAM, M. D. SCHROEDER (1978), Using encryption for authentication in large networks of computers, Communications of the ACM, 21, pp. 993–999.   
90. B. C. NEUMAN, T. TS’O (1994), Kerberos: An authentication service for computer networks, IEEE Communications Magazine, 32, pp. 33–38.   
91. J. K. PACHL, E. KORACH, D. ROTEM (1984), Lower bounds for distributed maximum-finding algorithms, Journal of the ACM, 31, pp. 905–918.   
92. M. C. PEASE, R. E. SHOSTAK, L. LAMPORT (1980), Reaching agreement in the presence of faults, Journal of the ACM, 27, pp. 228–234.   
93. C. E. PERKINS, E. M. BELDING-ROYER, S. R. DAS (1980), Ad hoc On-demand Distance Vector (AODV) routing, RFC 3561, Network Working Group.   
94. G. L. PETERSON (1981), Myths about the mutual exclusion problem, Information Processing Letters, 12, pp. 115– 116.   
95. G. L. PETERSON (1982), An $O ( n \log { n } )$ unidirectional algorithm for the circular extrema problem, ACM Transactions on Programming Languages and Systems, 4, pp. 758–762.   
96. G. L. PETERSON, M. J. FISCHER (1977), Economical solutions for the critical section problem in a distributed system, in (J. E. Hopcroft, E. P. Friedman, M. A. Harrison, eds.) Proceedings of the 9th Symposium on Theory of Computing, pp. 91–97, ACM.   
97. S. L. PETERSON, P. KEARNS (1993), Rollback based on vector time, in Proceedings of the 12th Symposium on Reliable Distributed Systems, pp. 68–77, IEEE.   
98. J. M. PIQUER (1991), Indirect reference counting: A distributed garbage collection algorithm, in (E. H. L. Aarts, J. van Leeuwen, M. Rem, eds.) Proceedings of the 3rd Conference on Parallel Architectures and Languages Europe, vol. 505 of Lecture Notes in Computer Science, pp. 150–165, Springer.   
99. R. RAJKUMAR, L. SHA, J. P. LEHOCZKY (1988), Real-time synchronization protocols for multiprocessors, in Proceedings of the 9th Real-Time Systems Symposium, pp. 259–269, IEEE.   
100. S. P. RANA (1983), A distributed solution of the distributed termination problem, Information Processing Letters, 17, pp. 43–46.   
101. K. RAYMOND (1989), A tree-based algorithm for distributed mutual exclusion, ACM Transactions on Computer Systems, 7, pp. 61–77.   
102. G. RICART, A. K. AGRAWALA (1981), An optimal algorithm for mutual exclusion in computer networks, Communications of the ACM, 24, pp. 9–17.   
103. R. L. RIVEST, A. SHAMIR, L. M. ADLEMAN (1978), A method for obtaining digital signatures and public-key cryptosystems, Communications of the ACM, 21, pp. 120–126.   
104. M. L. SCOTT, W. N. SCHERER III (2001), Scalable queue-based spin locks with timeout, in (M. T. Heath, A. Lumsdaine, eds.) Proceedings of the 8th Symposium on Principles and Practice of Parallel Programming, pp. 44–52, ACM.   
105. A. SEGALL (1983), Distributed network protocols, IEEE Transactions on Information Theory, 29, pp. 23–34.   
106. L. SHA, R. RAJKUMAR, J. P. LEHOCZKY (1990), Priority inheritance protocols: An approach to real-time synchronization, IEEE Transactions on Computers, 39, pp. 1175–1185.   
107. N. SHAVIT, N. FRANCEZ (1986), A new approach to detection of locally indicative stability, in (L. Kott, ed.) Proceedings of the 13th Colloquium on Automata, Languages and Programming, vol. 226 of Lecture Notes in Computer Science, pp. 344–358, Springer.   
108. N. SHAVIT, D. TOUITOU (1997), Software transactional memory, Distributed Computing, 10, pp. 99–116.   
109. D. SKEEN (1981), Nonblocking commit protocols, in (Y. E. Lien, ed.) Proceedings of the SIGMOD Conference on Management of Data, pp. 133–142, ACM.   
110. J. L. A. VAN DE SNEPSCHEUT (1987), “Algorithms for on-the-fly garbage collection” revisited, Information Processing Letters, 24, pp. 211–216.   
111. M. SPURI, G. C. BUTTAZZO (1996), Scheduling aperiodic tasks in dynamic priority systems, Real-Time Systems, 10, pp. 179–210.   
112. I. STOICA, R. MORRIS, D. LIBEN-NOWELL, D. R. KARGER, M. F. KAASHOEK, F. DABEK, H. BALAKRISHNAN (2003), Chord: A scalable peer-to-peer lookup protocol for Internet applications, IEEE/ACM Transactions on Networking, 11, pp. 17–32.   
113. J. K. STROSNIDER, J. P. LEHOCZKY, L. SHA (1995), The deferrable server algorithm for enhanced aperiodic responsiveness in hard real-time environments, IEEE Transactions on Computers, 44, pp. 73–91.   
114. M. SZYDLO (2004), Merkle tree traversal in log space and time, in (C. Cachin, J. Camenisch, eds.) Proceedings of the 23rd Conference on the Theory and Applications of Cryptographic Techniques, vol. 3027 of Lecture Notes in Computer Science, pp. 541–554, Springer.   
115. G. TARRY (1895), Le probleme des labyrinthes \` , Nouvelles Annales de Mathematiques, 14, pp. 187–190. ´   
116. G. TEL (1994), Network orientation, International Journal of Foundations of Computer Science, 5, pp. 23–57.   
117. G. TEL (2000), Introduction to Distributed Algorithms, 2nd edition, Cambridge University Press.   
118. G. TEL, F. MATTERN (1993), The derivation of distributed termination detection algorithms from garbage collection schemes, ACM Transactions on Programming Languages and Systems, 15, pp. 1–35.   
119. G. TEL, R. B. TAN, J. VAN LEEUWEN (1988) The derivation of graph marking algorithms from distributed termination detection protocols, Science of Computer Programming, 10, pp. 107–137.   
120. S. TOUEG (1980), An all-pairs shortest-path distributed algorithm, Technical Report RC-8397, IBM Thomas J. Watson Research Center.   
121. Y.-C. TSENG (1995), Detecting termination by weight-throwing in a faulty distributed system, Journal of Parallel and Distributed Computing, 25, pp. 7–15.   
122. Y. H. TSIN (2002), Some remarks on distributed depth-first-search, Information Processing Letters, 82, pp. 173– 178.   
123. S. VASUDEVAN, J. F. KUROSE, D. F. TOWSLEY (2004), Design and analysis of a leader election algorithm for mobile ad hoc networks, Proceedings of the 12th Conference on Network Protocols, pp. 350–360, IEEE.   
124. S. C. VESTAL (1987), Garbage Collection: An Exercise in Distributed, Fault-Tolerant Programming, PhD thesis, University of Washington.   
125. J. E. WALTER, J. L. WELCH, N. H. VAIDYA (2001), A mutual exclusion algorithm for ad hoc mobile networks, Wireless Networks, 7, pp. 585–600.   
126. P. WATSON, I. WATSON (1987), An efficient garbage collection scheme for parallel computer architectures, in (J. W. de Bakker, A. J. Nijman, P. C. Treleaven, eds.) Proceedings of the 1st Conference on Parallel Architectures and Languages Europe, vol. 259 of Lecture Notes in Computer Science, pp. 432–443, Springer.   
127. P.-C. YEW, N.-F. TZENG, D. H. LAWRIE (1987), Distributing hot-spot addressing in large-scale multiprocessors, IEEE Transactions on Computers, 36, pp. 388–395.

0-potent, 112   
1-potent, 112

$\alpha$ synchronizer, 104   
αabort, 171   
absolute deadline, 235   
ACID properties, 171   
active process, 41   
active route, 197   
acyclic network, 5   
acyclic orientation, 71   
acyclic orientation cover, 71   
acyclic orientation cover controller, 71   
Advanced Encryption Standard, 211   
Afek-Kutten-Yung spanning tree algorithm, 189, 271   
Agrawal–El Abbadi mutual exclusion algorithm, 144, 267   
agreement, 111   
algorithm, 1 basic, 10 centralized, 7 control, 10 decentralized, 7 distributed, 6 Las Vegas, 92 Monte Carlo, 92 probabilistic, 92 self-stabilizing, 183   
Anderson’s lock, 153   
anonymous network, 91 echo algorithm with extinction, 95

Itai-Rodeh election algorithm, 93 Itai-Rodeh ring size algorithm, 97 resuscitation election algorithm, 108 AODV routing protocol, 197 aperiodic job, 236 aperiodic task, 236 application layer, 194 Arora-Gouda spanning tree algorithm, 186 arrival time, 235 assertion, 7 asymmetric relation, 3 asynchronous communication, 5 atomic register, 12 atomic step, 6 atomicity, 171 attack, 209 birthday, 210 denial-of-service, 209 dictionary, 210 key-only, 220 person-in-the-middle, 209 replay, 209, 213 spoofing, 209 Sybil, 212 authentication, 213 Kerberos protocol, 213 Lamport-Shostak-Pease algorithm, 134 Needham-Schroeder protocol, 213 authentication server, 213 authenticator, 214

availability, 209   
Awerbuch’s depth-first search algorithm, 26   
Awerbuch’s synchronizer, 103, 264

$\beta$ synchronizer, 104   
βbackground server, 239   
backward validation, 175   
bakery mutual exclusion algorithm, 149   
barrier, 161 combining tree, 162 dissemination, 167 sense-reversing, 161 tournament, 165   
basic algorithm, 10   
basic message, 10   
BB84 key exchange protocol, 219   
bidirectional channel, 5   
binary consensus, 112   
binary number, 222   
binary relation, 3   
binary tree, 144 complete, 144   
birthday attack, 210   
bitcoin, 227   
Bitcoin protocol, 226   
bivalent configuration, 112   
block, 226 orphan, 228   
blockchain, 226   
blocked node, 31   
Boolean, 3   
Border Gateway Protocol, 73   
border router, 73   
bounded delay network, 106   
bounded expected delay network, 108   
Bracha-Toueg Byzantine consensus algorithm, 126   
Bracha-Toueg crash consensus algorithm, 113   
Bracha-Toueg deadlock detection algorithm, 34   
breadth-first search, 61 Frederickson’s algorithm, 67, 257   
breadth-first search tree, 61   
bus, 10   
Byzantine broadcast, 131 Lamport-Shostak-Pease algorithm, 132 Lamport-Shostak-Pease authentication algorithm, 1   
Byzantine clock synchronization

Lamport–Melliar-Smith synchronizer, 137 Mahaney-Schneider synchronizer, 130 Byzantine consensus, 125 Bracha-Toueg algorithm, 126 Byzantine failure, 125

synchronizer, 104   
γcache, 10   
cache coherence protocol, 11 MSI protocol, 11   
cache line, 10, 154   
cache miss, 10   
Cao-Singhal checkpointing algorithm, 203   
Carvalho-Roucairol optimization, 140   
cascading aborts, 175   
causal order, 8   
centralized algorithm, 7   
certificate authority, 211   
Chandra-Toueg crash consensus algorithm, 117   
Chandy-Lamport snapshot algorithm, 16, 246   
Chandy-Misra routing algorithm, 59, 254   
Chang-Roberts election algorithm, 77   
channel, 5 bidirectional, 5 FIFO, 5 public, 215 quantum, 217 unidirectional, 5 weighted, 59   
channel state, 15   
checkpoint mutable, 203 permanent, 205 tentative, 205   
checkpointing, 18 Cao-Singhal algorithm, 203 coordinated, 203 Peterson-Kearns algorithm, 19 uncoordinated, 19   
checksum, 222   
child node, 6   
Chord protocol, 194   
Cidon’s depth-first search algorithm, 26, 247   
CLH lock, 154   
CLH lock with timeouts, 156, 270   
client-server architecture, 171   
clock, 5, 106 local, 106 logical, 8   
cohort, 176   
coinbase transaction, 227   
collision resistance, 210   
combining tree barrier, 162   
commit, 171   
communication, 5 asynchronous, 5 synchronous, 6   
communication deadlock, 31   
communication protocol, 5   
commutativity, 215   
compare-and-set, 11   
complete binary tree, 144   
complete failure detector, 115   
complete network, 5   
completion phase, 176   
computation, 8   
concurrent event, 8   
confidentiality, 209   
configuration, 6 bivalent, 112 critical, 120 initial, 6 reachable, 6 symmetric, 91 terminal, 6   
congestion window, 73   
consensus, 111 binary, 112 Byzantine, 125 crash, 111 $k$ -Byzantine, 125 $k$ -crash, 112   
consistency, 171   
consistent snapshot, 15   
control algorithm, 10   
control message, 10   
controller, 70 acyclic orientation cover, 71 destination, 70 hops-so-far, 70   
coordinated checkpointing, 203   
coordinator, 116, 176   
core edge, 84   
core node, 84   
correct process, 111, 125   
crash consensus, 111 Bracha-Toueg algorithm, 113 Chandra-Toueg algorithm, 117 rotating coordinator algorithm, 116   
crash failure, 18, 111   
crashed process, 111   
critical configuration, 120   
critical section, 139   
cryptocurrency, 227   
cryptographic hash function, 210   
cryptography, 211 post-quantum, 221 public-key, 211 quantum, 219 symmetric-key, 211   
cyclic garbage, 53   
cyphertext, 134, 211   
database, 171   
database transaction, 31   
deadline, 235 absolute, 235 hard, 235 relative, 235   
deadlock, 31 communication, 31 resource, 31 store-and-forward, 70   
deadlock detection Bracha-Toueg algorithm, 34   
decentralized algorithm, 7   
decide event, 23   
decryption key, 211   
deferrable server, 240   
denial-of-service attack, 209   
dependence, 131   
depth, 66   
depth-first search, 25 Awerbuch’s algorithm, 26 Cidon’s algorithm, 26, 247   
depth-first search tree, 25   
dequeue, 141   
descendant, 6   
destination controller, 70   
dictionary attack, 210   
Diffie-Hellman key exchange protocol, 215   
digital signature, 134, 220   
Dijkstra-Scholten termination detection algorithm, 42   
Dijkstra’s token ring, 183   
directed network, 5   
dirty read, 174   
discrete logarithm problem, 216   
dissemination barrier, 167   
distance-vector routing, 72   
distributed algorithm, 6   
distributed database, 171   
distributed system, 5   
distributed transaction, 171   
Dolev-Klawe-Rodeh election algorithm, 79, 259   
Dolev-Strong optimization, 135   
doorway, 149   
durability, 171   
earliest deadline first scheduler, 237   
eavesdropper, 209   
echo algorithm, 28, 249   
echo algorithm with extinction, 82, 95   
edge, 5 core, 84 frond, 6 outgoing, 84 tree, 6   
election, 77 Chang-Roberts algorithm, 77 Dolev-Klawe-Rodeh algorithm, 79, 259 echo algorithm with extinction, 82, 95 Franklin’s algorithm, 78 IEEE 1394 election algorithm, 99, 263 Itai-Rodeh algorithm, 93 resuscitation algorithm, 108 tree algorithm, 81 Vasudevan-Kurose-Towsley algorithm, 200   
elliptic curve, 212   
encryption key, 211   
enqueue, 141   
event, 6 concurrent, 8 decide, 23 postsnapshot, 15

presnapshot, 15 receive, 6 send, 6 eventually strongly accurate failure detector, 115 eventually weakly accurate failure detector, 117 execution, 6 fair, 7 execution time, 235 exponential back-off, 152

failure Byzantine, 125 crash, 111   
failure detector, 18, 115 complete, 115 eventually strongly accurate, 115 eventually weakly accurate, 117 strongly accurate, 115 weakly accurate, 116   
failure detector history, 115   
failure pattern, 115   
fair execution, 7   
fair message scheduling, 114   
false root, 186   
false sharing, 154   
fault-tolerant weight-throwing termination detection algorithm, 47   
field, 10 sense, 161 status, 178 time-to-live, 72   
FIFO channel, 5   
FIFO queue, 141   
finger table, 195   
first-come, first-served, 149   
Fischer’s mutual exclusion algorithm, 151   
flat transaction, 172   
flooding, 72, 194   
fork, 228   
fragment, 84   
Franklin’s election algorithm, 78   
Frederickson’s breadth-first search algorithm, 67, 257   
frond edge, 6

Gallager-Humblet-Spira minimum spanning tree algorithm, 83, 260

garbage, 53 cyclic, 53   
garbage collection, 53 generational, 57 mark-compact, 57 mark-copy, 57 reference counting, 53 indirect, 54 weighted, 55 tracing, 57   
general, 131   
generational garbage collection, 57   
get-and-increment, 11   
get-and-set, 11   
gossip protocol, 194   
graph, 5 sink, 144 wait-for, 31   
growing phase, 173   
Hadamard transform, 218   
hard deadline, 235   
hardware transactional memory, 178   
hash collision, 194, 210   
hash function, 194, 210 cryptographic, 210   
hash table, 194 distributed, 194   
head, 141   
heartbeat message, 18   
hop count, 93   
hops-so-far controller, 70

ID, 5   
IEEE 1394 election algorithm, 99, 263   
inconsistent retrievals, 172   
indirect reference counting, 54   
initial configuration, 6   
initiator, 7   
integrity, 209   
invalid route, 200   
invalidate, 11   
invariant, 7   
inverse, 134   
irreflexive relation, 8   
isolation, 171   
Itai-Rodeh election algorithm, 93   
Itai-Rodeh ring size algorithm, 97

job, 235 aperiodic, 236 periodic, 236 preemptive, 237 sporadic, 236   
$k$ -Byzantine broadcast, 131   
$k$ -Byzantine clock synchronization, 130   
$k$ -Byzantine consensus, 125   
$k$ -crash consensus, 112   
Kerberos authentication protocol, 213   
key, 134 decryption, 211 encryption, 211 private, 134, 211 public, 134, 211 session, 213   
key distribution center, 214   
key exchange, 215 BB84 protocol, 219 Diffie-Hellman protocol, 215   
key server, 211   
key-only attack, 220   
Lai-Yang snapshot algorithm, 17, 246   
Lamport signature, 221   
Lamport’s logical clock, 8   
Lamport–Melliar-Smith Byzantine clock synchronization algorithm, 137   
Lamport-Shostak-Pease authentication algorithm, 134 Dolev-Strong optimization, 135   
Lamport-Shostak-Pease broadcast algorithm, 132   
Las Vegas algorithm, 92   
leaf, 6   
least slack-time first scheduler, 238   
ledger, 226   
lexicographical order, 3   
lieutenant, 131   
link-state packet, 72   
link-state routing algorithm, 72   
livelock, 146   
livelock-freeness, 12   
liveness property, 7   
local clock, 106   
local snapshot, 15   
local variable, 6   
lock, 12 queue, 153 read, 173 test-and-set, 152 test-and-test-and-set, 152 write, 173   
lock-freeness, 12   
lockstep, 103   
logical clock, 8 Lamport’s, 8 vector, 9   
lost message, 15   
lost update, 172   
Mahaney-Schneider Byzantine clock synchronization algorithm, 130   
main memory, 10   
MANET, 193   
mark-compact garbage collection, 57   
mark-copy garbage collection, 57   
matrix, 218 orthogonal, 218   
MCS lock, 155, 269   
memory barrier, 10   
Merkle signature, 223   
Merkle tree, 211   
Merlin-Segall routing algorithm, 61, 254   
message, 5 basic, 10 control, 10 heartbeat, 18 lost, 15 orphan, 15 RERR, 199 RREP, 197 RREQ, 197 valid, 134   
message passing, 5   
miner, 227   
minimum spanning tree, 83 Gallager-Humblet-Spira algorithm, 83, 260

minimum-hop path, 61   
mobile ad hoc network, 193

modulo arithmetic, 5   
Monte Carlo algorithm, 92   
MSI protocol, 11   
multi-reader register, 10   
multi-writer register, 10   
multiset, 132   
mutual exclusion, 139 Agrawal–El Abbadi algorithm, 144, 267 bakery algorithm, 149 Dijkstra’s token ring, 183 Fischer’s algorithm, 151 Peterson’s algorithm, 146 Raymond’s algorithm, 141, 266 Ricart-Agrawala algorithm, 140, 265 test-and-set lock, 152 test-and-test-and-set lock, 152 Walter-Welch-Vaidya algorithm, 201   
Needham-Schroeder authentication protocol, 213   
nested transaction, 171   
network, 5 acyclic, 5 anonymous, 91 bounded delay, 106 bounded expected delay, 108 complete, 5 directed, 5 mobile ad hoc, 193 overlay, 194 P2P, 193 strongly connected, 5 undirected, 5 unweighted, 61 weighted, 59   
network latency, 18   
no-cloning theorem, 217   
node, 5 blocked, 31 child, 6 core, 84 parent, 6   
nonblocking, 12   
nonce, 213   
$N$ -out-of- $M$ request, 31   
null, 155, 270   
NUMA architecture, 156   
pop, 225   
post-quantum cryptography, 22   
postsnapshot event, 15   
precision, 106   
preemptive job, 237   
preimage resistance, 210   
premature write, 173   
presnapshot event, 15   
priority ceiling, 242   
priority inheritance, 242   
private key, 134, 211   
privileged process, 139   
probabilistic algorithm, 92   
process, 5 active, 41 correct, 111, 125 crashed, 111 passive, 41 privileged, 139 safe, 103   
process ID, 5   
processor, 10   
progress property, 12   
proof-of-stake, 229   
proof-of-work, 212   
property liveness, 7 progress, 12 safety, 7   
protocol, 5   
pseudocode, 245   
public channel, 215   
public key, 134, 211   
public-key cryptography, 211   
pulse, 103   
push, 225   
quantum channel, 217   
quantum computer, 212   
quantum cryptography, 219   
quantum operation, 217   
qubit, 217   
queue, 141   
queue lock, 153 Anderson’s lock, 153 CLH lock, 154

object   
root, 53   
object owner, 54   
offline scheduler, 236   
one-time signature scheme, 221   
online scheduler, 236   
optimistic concurrency control, 175   
order, 3   
lexicographical, 3   
partial, 3   
total, 3   
orphan block, 228   
orphan message, 15   
orthogonal matrix, 218   
OSPF Protocol, 73   
outgoing edge, 84   
out-of-order execution, 12   
overflow, 5   
overlay network, 194   
P2P network, 193   
structured, 194   
unstructured, 194   
padding, 154   
parent node, 6   
parent-child relation, 24   
partial order, 3   
passive process, 41   
password, 210   
salted, 210   
path, 5   
minimum-hop, 61   
Paxos, 112   
peer, 193   
peer-to-peer network, 193   
period, 236   
periodic job, 236   
periodic task, 236   
person-in-the-middle attack, 209   
Peterson-Kearns checkpointing algorithm, 19   
Peterson’s mutual exclusion algorithm, 146   
pivot, 64   
plaintext, 134, 211   
pointer, 53, 154   
null, 155   
polling server, 239

CLH lock with timeouts, 156, 270 MCS lock, 155, 269 quorum, 144

priority ceiling, 242 priority inheritance, 242 resource deadlock, 31 resuscitation election algorithm, 108 Ricart-Agrawala mutual exclusion algorithm, 140, 265 Carvalho-Roucairol optimization, 140 ring size Itai-Rodeh algorithm, 97 ring traversal algorithm, 23 RIP protocol, 73 rollback recovery, 18 root, 6 false, 186 root object, 53 rotating coordinator crash consensus algorithm, 116 route, 59 active, 197 invalid, 200 routing, 59 AODV protocol, 197 Chandy-Misra algorithm, 59, 254 distance-vector algorithm, 72 link-state algorithm, 72 Merlin-Segall algorithm, 61, 254 Toueg’s algorithm, 64, 255 routing table, 59 RREP message, 197 RREQ message, 197 RSA cryptosystem, 212 safe process, 103 safety property, 7 Safra’s termination detection algorithm, 45, 252 scheduler, 235 earliest deadline first, 237 least slack-time first, 238 offline, 236 online, 236 rate-monotonic, 237 Selective Acknowledgement, 73 self-stabilization, 183 Afek-Kutten-Yung spanning tree algorithm, 189, 271 Arora-Gouda spanning tree algorithm, 186 Dijkstra’s token ring, 183 send event, 6 sense field, 161

$\rho$ -bounded drift, 106   
ρrace condition, 1   
Raft, 112   
Rana’s termination detection algorithm, 43, 251   
rate-monotonic scheduler, 237   
Raymond’s mutual exclusion algorithm, 141, 266   
reachable configuration, 6   
read, 6   
read lock, 173   
read-modify-write operation, 11 commuting, 121 compare-and-set, 11 get-and-increment, 11 get-and-set, 11 overwriting, 121 test-and-set, 11   
real-time computing, 235   
realm, 215   
receive event, 6   
reference, 53   
reference counting, 53 indirect, 54 weighted, 55   
register, 10 atomic, 12 multi-reader, 10 multi-writer, 10 single-reader, 10 single-writer, 10   
relation asymmetric, 3 binary, 3 causal order, 8 irreflexive, 8 parent-child, 24 transition, 6 transitive, 3   
relative deadline, 235   
release time, 235   
replay attack, 209, 213   
RERR message, 199   
resource access control, 241   
sense-reversing barrier, 161   
serializable, 172   
server authentication, 213 background, 239 deferrable, 240 key, 211 polling, 239 slack stealing, 239 ticket-granting, 214 total bandwidth, 240   
session key, 213   
set, 3   
SHA-256, 210   
shared memory, 10   
shared variable, 10   
Shavit-Francez termination detection algorithm, 43, 250   
shrinking phase, 173   
signature scheme, 134, 220 Lamport, 221 Merkle, 223 one-time, 221 Winternitz, 221   
single-reader register, 10   
single-writer register, 10   
sink graph, 144   
sink tree, 6   
slack, 236   
slack stealing server, 239   
smart contract, 230   
snapshot, 15 Chandy-Lamport algorithm, 16, 246 consistent, 15 Lai-Yang algorithm, 17, 246 local, 15   
software transactional memory, 178   
spanning tree, 6 Afek-Kutten-Yung algorithm, 189, 271 Arora-Gouda algorithm, 186 minimum, 83   
spin lock, 150   
spinning, 139   
spoofing attack, 209   
sporadic job, 236   
sporadic task, 236   
stabilization procedure, 196   
stable storage, 18   
stack, 225   
starvation-freeness, 12, 139   
state, 6 channel, 15   
status field, 178   
store-and-forward deadlock, 70   
strongly accurate failure detector, 115   
strongly connected network, 5   
successor list, 196   
superposition, 217   
Sybil attack, 212   
symmetric configuration, 91   
symmetric-key cryptography, 211   
synchronization conflict, 172   
synchronizer, 103 , 104 αAwerbuch’s, 103, 264 , 104 β, 104   
γsynchronous communication, 6   
synchronous system, 103   
tail, 141   
Tarry’s traversal algorithm, 24   
task, 236 aperiodic, 236 periodic, 236 sporadic, 236   
terminal configuration, 6   
termination, 41, 111   
termination detection, 41 Dijkstra-Scholten algorithm, 42 fault-tolerant weight-throwing algorithm, 47 Rana’s algorithm, 43, 251 Safra’s algorithm, 45, 252 Shavit-Francez algorithm, 43, 250 weight-throwing algorithm, 46, 253   
test-and-set, 11   
test-and-set lock, 152   
test-and-test-and-set lock, 152   
thread, 10   
three-phase commit protocol, 177   
thundering herd problem, 152   
ticket-granting server, 214   
time stamp ordering, 174   
time-to-live field, 72   
token, 23   
total bandwidth server, 240   
total order, 3   
Toueg’s routing algorithm, 64, 255   
tournament barrier, 165   
tournament tree, 147   
tracing garbage collection, 57   
transaction, 31, 171 distributed, 171 flat, 172 nested, 171   
transactional bit, 178   
transactional line, 178   
transactional memory, 178 hardware, 178 software, 178   
transition, 6   
transition relation, 6   
transition system, 6   
transitive relation, 3   
Transmission Control Protocol, 73   
traversal, 23 breadth-first search algorithm, 61 depth-first search algorithm, 25 ring algorithm, 23 Tarry’s algorithm, 24   
tree binary, 144 complete, 144 breadth-first search, 61 depth-first search, 25 sink, 6 spanning, 6 minimum, 83 tournament, 147   
tree algorithm, 27, 248   
tree edge, 6   
tree election algorithm, 81   
treehash algorithm, 225   
trusted third party, 213   
two-phase commit protocol, 176

two-phase locking, 173   
uncoordinated checkpointing, 19   
underflow, 47   
undirected network, 5   
unidirectional channel, 5   
unweighted network, 61   
update phase, 175   
utilization, 236

valid message, 134   
validation phase, 175   
validity, 111, 125   
variable, 6 local, 6 shared, 10   
Vasudevan-Kurose-Towsley election algorithm, 200   
vector clock, 9   
voting phase, 176

wait-for graph, 31   
wait-freeness, 12   
wallet, 227   
Walter-Welch-Vaidya mutual exclusion algorithm, 201   
wave, 23   
echo algorithm, 28, 249   
tree algorithm, 27, 248   
weakly accurate failure detector, 116   
weighted channel, 59   
weighted network, 59   
weighted reference counting, 55   
weight-throwing termination detection algorithm, 46, 253   
fault-tolerant, 47   
Winternitz signature, 221   
working phase, 175   
write, 6   
write lock, 173

XOR, 220

Z n Z, 5   
$( \mathbb { Z } / p \mathbb { Z } ) ^ { * }$ , 216