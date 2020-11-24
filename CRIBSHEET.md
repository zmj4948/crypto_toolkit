# Crypto Crib Sheet for Exam 03
##Public-Key Cryptography
**Topic 6, Week 10, CH 6, pg 149**                      
- Also known as Asymmetric Ciphers                      
- Two Properties of Symmetric : 
    > - the same secrete key K is used for encryption decryption
    > - decryption are very similar operations.                          
- Short comings of Symmetric: 
    > - Alice or Bob can cheat because they have similar keys
    > - Key distribution problem (the secret key must be transported securely)
    > - number of keys (in a network, each user will need to store n-1 keys, and there will be n* (n-1) / 2 keys needed in total)
- Principal of Asymmetric
    > "Split up" the key s. t. you have K<sub>pub</sub> and K<sub>pr</sub>                      
- Disadvantage: 
    > computationally very intensive (1000 times slower that sym algorithms)                      
- Hybrid systems are used in practice: key exchange is done with asymmetric, and everything else is done with symmetric
- Based on a "one-way function", where computing the inverse of the function is computationally infeasible
- Three main families of mathematically hard problems: Integer Factorization (RSA), Discrete Logarithm (Diffie-hellman, ElGamal, DSA), Elliptic Curves (ECDH, ECDSA)                    

##RSA
**Topic 7, Week 11, CH 7, pg 173**
#### RSA Basics
Mainly used for transport of symmetric keys or Digital signatures

**Definition**
Given the public key (n,e) = K<sub>pub</sub> and the private key d = k<sub>pr</sub>, we write 
> y = eK<sub>pub</sub>(x) = x<sup>e</sup> mod n  
> x = dK<sub>pr</sub>(y) = y<sup>e</sup> mod n 

Algorithm for key generation:
1. Choose two large primes _p, q_ 
2. Compute _n = p * q_
3. Compute _phi(n) = (p-1) * (q-1)_
4. Select the public exponent _e exists {1, 2, ..., phi(n)-1}_ s. t. gcd _(e, phi(n)) = 1_
5. Compute the private key _d_ s. t. _d * e = 1 mod phi(n)_
6. Return _K<sub>pub</sub> = (n, e), k<sub>pr</sub> = d_

Notes on algorithm: 
- step 1 is non-trivial
- selecting e using gcd means that e will have an inverse. 
- step 5 can be done with EEA
- leaking _d, p, q, phi(n)_ can be FATAL to the system

Implementation aspects
- Conceptually simple due to only one arithmetic operation (modular exponentiation)
- slow due to very long numbers
- Square and Multiply algorithm allows for fast exponentiation 

 The following techniques are used to speed up RSA
 - Short public exponent _e_
 - CRT (Chinese remainder Theorem)
 - Using Pre-computed values 
 
 Using a short public exponent _e_
 - does not weaken RSA
 - improves speed rapidly

| Public Key value _e_ | _e_ as binary string |  # SQ + #Mul |
| ----------- | ----------- |----------- |
| 2<sup>1</sup> + 1 = 3 | (11)<sub>e</sub> | 1 + 1 = 2 | 
| 2<sup>4</sup> + 1 = 17 | (1 0001)<sub>e</sub> | 4 + 1 = 5 | 
| 2<sup>16</sup> + 1 = 65,537 | (1 0000 0000 0000 0001)<sub>e</sub> | 16 + 1 = 17 |  

Choosing a small private key _d_ results in security weaknesses!
- _d_ must have at least 0.3 * _t_ bits, where _t_ is the bit length of the modulus n  

####Chinese Remainder Theorem
**Topic 7, Week 11, CH 7, pg 184**  
Has three distinct steps
1) transformation of operand into the CRT domain
2) Modular exponentiation in the CRT domain
3) Inverse transformation back to the problem domain  

These steps are equivalent to one modular exponentiation in the problem domain  
  
Faster due to less operations, pre-computed basis vector, and constant time transition  
CRT is **4 times faster** than straightforward exponentiation 

To generator _p_ and _q_, generate random integers and test for primality 
###Primality Testing
**Topic 7, Week 11, CH 7, pg 188**  
Used to test whether _p_ and _q_ are prime.  
Typical primality tests are probabilistic, meaning that they are not 100% accurate, but have high enough probability 
####Fermat
Basic idea: Fermat's Little Theorem holds for all primes so if it doesn't hold for candidate p̃, then it cannot be prime  
>Algorithm  
Input: prime candidate p̃, security parameter s  
>Output: "p̃ is composite" or "p̃ is likely prime"  
>
    for i = 1 to s   
        Choose random a ∈ {2, 3, . . . p̃ -2}  
        If a<sup>p̃-1</sup> ≠ 1 mod p̃ then`
            Return “p̃ is composite”  
 
####Carmichael numbers
- Specifically problematic for Fermat's test  
- A Carmichael number is also known as pseudoprime that satisfies Fermat's Little Theorem  
- Given a Carmichael number C, the following expression holds for _all_ integers a for which gcd(a,C) = 1:  
    > a<sup>C-1</sup> = 1 mod C  
####Miller-Rabin
Based on following theorem:  
    
    Given the decomposition of an odd prime candidate p̃
        p̃-1 = 2<sup>u</sup>r   
    where r is odd. If we can find an integer a such that  
        a<sup>r</sup> ≠ 1 mod p and a^(r2^(j))  ≠ p̃-1 mod p̃
    for all j = {0, 1, ..., u-1}, then p̃ is composite. Otherwise, it is probably a prime 
    
This turns into an efficient primality test
    
    Input #1: n > 3, an odd integer to be tested for primality
    Input #2: k, the number of rounds of testing to perform
    Output: “composite” if n is found to be composite, “probably prime” otherwise  
    
    write n as 2r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
    WitnessLoop: repeat k times:
        pick a random integer a in the range [2, n − 2]
        x ← ad mod n
        if x = 1 or x = n − 1 then
            continue WitnessLoop
        repeat r − 1 times:
            x ← x2 mod n
            if x = n − 1 then
                continue WitnessLoop
        return “composite”
    return “probably prime”     

##DHKE
**Topic 8, Week 12, CH 8, pg 206**  
- Proposed in 1976 by Diffie and Hellman
- used in SSH, TLS, IPSec
- Key exchange **ONLY**, **not** used for encryption
- never used on it's own, must authenticate to counteract the "Man in the middle" attack  

Diffie-Hellman Setup
> 1. Choose large prime _p_
> 2. Choose an integer α ∈ {2, 3, ..., _p_-2}
> 3. Publish _p_ and α

Key Exchange  
	![DHKE overview](crib_sheet_photos/DHKE.JPG)

Alice computes: _B<sup>a</sup>_ = _(α<sup>b</sup>)<sup>a</sup>_ = _α<sup>ab</sup>_ mod _p_ 
Bob computes: _A<sup>b</sup>_ = _(α<sup>a</sup>)<sup>b</sup>_ = _α<sup>ab</sup>_ mod _p_ 

Based on the Discrete Log Problem ( found in number theory)

##ElGamal
**Topic 8b, Week 12, CH 8, pg 227**
- Proposed by ElGamal
- used for encryption and is an extension of DHKE
- security is based on the intractability of the Discrete Log Problem  

Principal of ElGamal Encryption
Key Exchange  
	![ElGamal overview](crib_sheet_photos/ElGamal.JPG)

ElGamal: Set-up
- Large (1024+ bits) prime p and primitive element α are generated
- Both parties perform DHKE to obtain a shared key K<sub>M</sub> (M for masking)
- New idea:  
    - Alice uses this key as a multiplication mask to encrypt _x_
    - Bob uses the multiplicative inverse of the shared key (K<sub>M</sub>) to decrypt _y_  

ElGamal in practice
- Protocol is rearranges the sequence of operations so that Alice only has to send one message to Bob (instead of two)
- Scheme is probabilistic since Alice picks a new i every time
Key Exchange  
	![ElGamal practice](crib_sheet_photos/ElGamal_Practice.JPG)
    
##Hashing
**Topic 9, Week 13, CH 11, pg 293**
##Number Theory (Euler, Fermat, last n digits, Group theory, primitive elements)
###Discrete Log problem
Find integer x to satisfy the following: 
> _α<sup>x</sup>_ = β mod _p_