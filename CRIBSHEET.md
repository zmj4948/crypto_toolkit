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
    > "Split up" the key s. t. you have Kpub and Kpr                      
- Disadvantage: 
    > computationally very intensive (1000 times slower that sym algorithms)                      
- Hybrid systems are used in practice: key exchange is done with asymmetric, and everything else is done with symmetric
- Based on a "one-way function", where computing the inverse of the function is computationally infeasible
- Three main families of mathematically hard problems: Integer Factorization (RSA), Discrete Logarithm (Diffie-hellman, ElGamal, DSA), Elliptic Curves (ECDH, ECDSA)                    
##RSA
**Topic 7, Week 11, CH 7, pg 173**
- Mainly used for transport of symmetric keys or Digital signatures

**Definition**
Given the public key (n,e) = Kpub and the private key d = kpr, we write 

    y = eKpub(x) = x^e mod n
    x = dkpr(y) = y^d mod n 
Algorithm for key generation:
1. Choose two large primes _p, q_ 
2. Compute _n = p * q_
3. Compute _phi(n) = (p-1) * (q-1)_
4. Select the public exponent _e exists {1, 2, ..., phi(n)-1}_ s. t. gcd _(e, phi(n)) = 1_
5. Compute the private key _d_ s. t. _d * e = 1 mod phi(n)_
6. Return _kpub = (n, e), kpr = d_

Notes on algorithm: 
- step 1 is non-trivial
- selecting e using gcd means that e will have an inverse. 
- step 5 can be done with EEA
- leaking _d, p, q, phi(n)_ can be FATAL to the system

Implementation aspects
- Conceptually simple due to only one arithmetic operation (modular exponentiation)
- slow due to very long numbers
- Square and Multiply algorithm allows for fast exponentiation 

##CRT
##Primality Testing (Carmichael, Fermat, Miller-Rabin)
##DHKE
##ElGamal
##Hashing
##Number Theory (Euler, Fermat, last n digits, Group theory, primitive elements)
