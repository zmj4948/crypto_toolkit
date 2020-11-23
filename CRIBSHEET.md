# Crypto Crib Sheet for Exam 03
##Public-Key Cryptography
**Topic 6, Week 10**                      
- Also known as Asymmetric Ciphers                      
- Two Properties of Symmetric : 
    > 1) the same secrete key K is used for encryption decryption
    > 2) decryption are very similar operations.                          
- Short comings of Symmetric: 
    > 1) Alice or Bob can cheat because they have similar keys
    > 2) Key distribution problem (the secret key must be transported securely)
    > 3) number of keys (in a network, each user will need to store n-1 keys, and there will be n* (n-1) / 2 keys needed in total)
- Principal of Asymmetric
    > "Split up" the key s. t. you have Kpub and Kpr                      
- Disadvantage: 
    > computationally very intensive (1000 times slower that sym algorithms)                      
- Hybrid systems are used in practice: key exchange is done with asymmetric, and everything else is done with symmetric
- Based on a "one-way function", where computing the inverse of the function is computationally infeasible
- Three main families of mathematically hard problems: Integer Factorization (RSA), Discrete Logarithm (Diffie-hellman, ElGamal, DSA), Elliptic Curves (ECDH, ECDSA)                    
##RSA
**Topic 7, Week 11**
- CRT
- Primality Testing (Carmichael, Fermat, Miller-Rabin)
- DHKE
- ElGamal
- Hashing
- Number Theory (Euler, Fermat, last n digits, Group theory, primitive elements)