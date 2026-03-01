
# Securing Accounts – CS50 Cybersecurity

## 1. Core Idea

Authentication is the process of knowing whether someone is truly who they claim to be before granting access.

sometimes security is overlooked in a software or program not because of lack of technical expertise but because of user behaviour and usability

## 2. Key Concepts

### Authentication vs Authorization
- Authentication: Are you who you say you are?
- Authorization: What are you allowed to access?

### Password Storage
- Passwords are often stored in structured datasets.
- Attackers can use dictionary attacks by trying common words.

### Dictionary Attack
An attacker uses a predefined list of likely passwords to attempt access.

### Brute Force Attack
An attacker systematically tries all possible combinations using code.
Example: nested loops iterating through digits and ASCII letters constants(

### NIST(National Institute of standards and technology)
it is an organisation in USA that recommends guidelines and policy related to cybersecurity practices fo governments, companies and critical infrasstructure

### 2-Factor authentication
its a way of verification and authentication of identity using only two factors such as a password and something which we have such as codes generated in authenticator apps on our device 

### Multifactor-Authentication
it is a secure way of verification and authentication of identity using more than two factors, such as passwords,SMS,OTP,codes on authenticator app,biometric like fingerprint

### keylogger
keylogger is a programm that tracks keystroke or in other words it can track what we type on our device

usage:-attackers can use this kind of software/programm to send our typing habits or what we type on keyboards to remote servers via internet

### Sim swapping attack
sim swapping is a technique that involves convincing the mobile carrier to transfer the victim's phone number to another sim and gaining access to their bank account,social media, email. an attacker succeeds generally because of gathering opensource information about the victim

### Social Engineering
it is a technique of exploiting human psychology into giving sensitive and confidential information

### Phishing
phishing is a method of tricking people into revealing sensitive information via fake and deceptive apps and websites that often mimics original ones realistically. common security hygienes include proper checking of links and URL

### Machine in the Middle Attack
also called man in the middle attack (MITM) is a type of cyberattack where a device or software is set by an attacker that sits in between the app/application and the user.

### Credential stuffing
it is a type of cyberattack where the attacker has access to a list consisting of a number of usernames and passwords downloaded from the Internet after a breach is occured

### Single-Sign-On (SSO)
a single-sign-on is a simple authentication mechanism where one platform account is enough to register for other separate independent platform account ,it requires you to have only one account from a verified and widely used platform such as Google sign on we usually see.

### Password Manager
a password manager is like a egg basket having a bunch of eggs togather. A password manager contains all the account's password we created and requires only one strong password for itself(password manager) for the sake of security

### Passkeys
a passkey is a Cryptographic way of authentication that use a public/private key where user's device use a private cryptographic key to sign a server's challenge and the server verifies it using the public key that matches

## 3. Technical Observation

A practical demonstration is implemented in `code/crack.py`.

The script simulates a brute force / dictionary-style password attempt by iterating through possible combinations programmatically.

This demonstrates:

- Weak passwords is easier to brute force 
- short passwords are mathematically vulnerable

## 4. Human as a attack vector

If passwords become too complex:
- Users may reuse passwords.
- Users may note them down somewhere in written form which can be stolen
- Users may abandon the system.

Security must balance strength and usability.

## 5. Deeper Reflection

The biggest vulnerability may not be the system/Technology — but human behavior.

Improving security often requires improving user habits, not just writing better code.
